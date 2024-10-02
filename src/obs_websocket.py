import json
from os import path
import obsws_python as obs
from sc_logging import logger


def open_obs_websocket(server_info):
    # Open a websocket connection to OBS
    try:
        cl = obs.ReqClient(
            host=server_info["ip"],
            port=server_info["port"],
            password=server_info["password"],
            timeout=10,
        )
        resp = cl.get_version()
        logger.info(f"OBS Version: {resp.obs_version}")
        return cl
    except Exception as e:
        logger.warn(f"Error: {e}")
        return None


def get_all_sources(obs_client: obs.ReqClient):
    # Get all the sources from OBS
    try:
        # get all scenes
        resp = obs_client.get_scene_list()
        scenes = resp.scenes
        # get all sources from all scenes
        sources = []
        for scene in scenes:
            resp = obs_client.get_scene_item_list(scene["sceneName"])
            # add the sources with their scene name
            for source in resp.scene_items:
                source["sceneName"] = scene["sceneName"]
                sources.append(source)
        return sources
    except Exception as e:
        logger.exception("Error: unable to get all sources")
        return None


def get_source_by_name(obs_client: obs.ReqClient, source_name):
    # Get a source from OBS by name
    try:
        # get all scenes
        resp = obs_client.get_scene_list()
        scenes = resp.scenes
        # get all sources from all scenes
        sources = []
        for scene in scenes:
            resp = obs_client.get_scene_item_list(scene["sceneName"])
            # add the sources with their scene name
            for source in resp.scene_items:
                source["sceneName"] = scene["sceneName"]
                sources.append(source)
        # find the source by name
        for source in sources:
            if source["sourceName"] == source_name:
                return source
        return None
    except Exception as e:
        logger.exception("Error: unable to get source by name")
        return None


def get_source_screenshot(obs_client: obs.ReqClient, source_name, width, height):
    # Get a screenshot of a source from OBS
    try:
        resp = obs_client.get_source_screenshot(
            source_name, img_format="png", width=width, height=height, quality=100
        )
        return resp.image_data
    except Exception as e:
        logger.exception("Error: unable to get source screenshot")
        return None


def update_text_source(obs_client: obs.ReqClient, source_name, text) -> None:
    # Update a text source in OBS using SetInputSettings
    try:
        # get the source
        obs_client.set_input_settings(source_name, {"text": text}, True)
    except Exception as e:
        logger.exception("Error: unable to update text source")


def clear_or_create_new_scene(obs_client: obs.ReqClient, scene_name) -> bool:
    # Create a new scene in OBS or clear an existing one
    try:
        # check if the scene exists
        resp = obs_client.get_scene_list()
    except Exception as e:
        logger.exception("Error: unable to get scene list")
        return False
    scenes = resp.scenes
    scene_exists = False
    for scene in scenes:
        if scene["sceneName"] == scene_name:
            scene_exists = True
            break
    # if the scene doesnt exist, create it
    if not scene_exists:
        # create a new scene
        try:
            obs_client.create_scene(scene_name)
            return True
        except Exception as e:
            logger.exception(f"Cannot create scene. Error: {e}")
            return False

    try:
        # if the scene is currently selected in OBS, switch to another scene
        resp = obs_client.get_current_program_scene()
        if resp.current_program_scene_name == scene_name:
            # get the first scene that is not the current scene
            for scene in scenes:
                if scene["sceneName"] != scene_name:
                    obs_client.set_current_program_scene(scene["sceneName"])
                    break
    except Exception as e:
        logger.exception("Cannot change OBS program scene")

    try:
        resp = obs_client.get_current_preview_scene()
        if resp.current_preview_scene_name == scene_name:
            # get the first scene that is not the current scene
            for scene in scenes:
                if scene["sceneName"] != scene_name:
                    obs_client.set_current_preview_scene(scene["sceneName"])
                    break
    except Exception as e:
        logger.exception("Cannot change OBS preview scene")

    # remove all scene items
    try:
        resp = obs_client.get_scene_item_list(scene_name)
        for scene_item in resp.scene_items:
            obs_client.remove_scene_item(scene_name, scene_item["sceneItemId"])
            obs_client.remove_input(scene_item["sourceName"])
    except Exception as e:
        logger.exception("Error: unable to remove scene item")

    return True


def create_obs_scene_from_export(obs_client, scene_name):
    logger.info("creating OBS scene")
    # create a new scene in OBS
    clear_or_create_new_scene(obs_client, scene_name)

    # load the scene from obs_data/test.json
    obs_data_path = path.abspath(
        path.join(
            path.dirname(__file__), "..", "obs_data/Scoresight_OBS_scene_collection.json"
        )
    )
    logger.debug(f"loading scene from '{obs_data_path}'")
    with open(obs_data_path, "r") as f:
        scene = json.load(f)

    # find scene source with items
    scene_source = [
        source
        for source in scene["sources"]
        if source["uuid"] == "6656641a-06b4-41e5-8a06-0de8a25e38be"
    ][0]
    sources_settings = scene["sources"]

    for source in scene_source["settings"]["items"]:
        # if the source is a scene, skip it
        logger.debug(f"creating source {source['name']}")
        # find source settings in sources_settings by the uuid
        source_settings = [
            settings
            for settings in sources_settings
            if settings["uuid"] == source["source_uuid"]
        ]
        if len(source_settings) == 0:
            logger.debug(f"source {source['name']} has no settings, possibly a group")
            continue
        source_settings = source_settings[0]
        # merge settings with source['settings']
        source_settings_to_set = {**source_settings["settings"], **source}
        if "file" in source_settings_to_set:
            # get the base name of the image path
            base_name = path.basename(source_settings_to_set["file"])
            # get the absolute path to the image
            abs_path = path.abspath(
                path.join(
                    path.dirname(__file__),
                    f"obs_data/Scoreboard parts/{base_name}",
                )
            )
            source_settings_to_set["file"] = abs_path

        try:
            # create a new source in OBS
            obs_client.create_input(
                sceneName=scene_name,
                inputName=source["name"],
                inputKind=source_settings["versioned_id"],
                inputSettings=source_settings_to_set,
                sceneItemEnabled=source_settings_to_set["visible"],
            )
            # set the SetSceneItemTransform
            if "pos" in source_settings_to_set:
                # get the scene item id with GetSceneItemId
                scene_item_id = obs_client.get_scene_item_id(
                    scene_name, source["name"]
                ).scene_item_id

                transform_to_set = {
                    "alignment": source_settings_to_set["align"],
                    "cropBottom": source_settings_to_set["crop_bottom"],
                    "cropLeft": source_settings_to_set["crop_left"],
                    "cropRight": source_settings_to_set["crop_right"],
                    "cropTop": source_settings_to_set["crop_top"],
                    "positionX": source_settings_to_set["pos"]["x"],
                    "positionY": source_settings_to_set["pos"]["y"],
                    "scaleX": source_settings_to_set["scale"]["x"],
                    "scaleY": source_settings_to_set["scale"]["y"],
                }

                obs_client.set_scene_item_transform(
                    scene_name, scene_item_id, transform_to_set
                )
            # set the filters
            if "filters" in source_settings:
                for filter in source_settings["filters"]:
                    logger.debug(
                        f"creating filter {filter['name']} for source {source_settings['name']}"
                    )
                    # if the filter has "image_path" in the settings, adjust the path to the obs_data folder
                    if "image_path" in filter["settings"]:
                        # get the base name of the image path
                        base_name = path.basename(filter["settings"]["image_path"])
                        # get the absolute path to the image
                        abs_path = path.abspath(
                            path.join(
                                path.dirname(__file__),
                                f"obs_data/Scoreboard parts/{base_name}",
                            )
                        )
                        filter["settings"]["image_path"] = abs_path
                    obs_client.create_source_filter(
                        source["name"],
                        filter["name"],
                        filter["versioned_id"],
                        filter["settings"],
                    )
        except Exception as e:
            logger.exception(f"Unable to create input and filters. Error: {e}")

    logger.info("finished creating sources")
