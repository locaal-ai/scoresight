import requests
import datetime
import os
from dotenv import load_dotenv
from io import StringIO
from resource_path import resource_path
from sc_logging import logger
from storage import fetch_data, store_data
from os import path
from PySide6.QtWidgets import QDialog
from PySide6.QtUiTools import QUiLoader


def fetch_release_info(update_check_url):
    logger.info("Checking for updates...")
    # Fetch the release info file from the cloud
    try:
        response = requests.get(update_check_url, timeout=5)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch release info file from the cloud: {e}")
        return None


def get_latest_release_version(release_info: str):
    # Parse the release info file and extract the latest release version
    # the file is a dotenv so use load_dotenv to parse it
    release_info_stream = StringIO(release_info)
    load_dotenv(stream=release_info_stream)
    latest_release_version = os.getenv("LATEST_RELEASE_TAG")
    latest_release_date = os.getenv("LATEST_RELEASE_DATE")
    return latest_release_version, latest_release_date


def compare_release_dates(current_release_date, latest_release_date):
    # Compare the release dates
    # they were formatted with unix `date -u +"%Y-%m-%dT%H:%M:%SZ"`
    # so we need to convert them to datetime objects
    current_date = datetime.datetime.strptime(
        current_release_date, "%Y-%m-%dT%H:%M:%SZ"
    )
    latest_date = datetime.datetime.strptime(latest_release_date, "%Y-%m-%dT%H:%M:%SZ")
    if current_date < latest_date:
        return "Newer"
    elif current_date > latest_date:
        return "Older"
    else:
        return "Same"


def check_for_updates(override_settings: bool) -> bool:
    return False

    # if not override_settings:
    #     # check in storage if update checks are enabled
    #     check_for_updates_disabled = fetch_data(
    #         "scoresight.json", "disable_update_checks"
    #     )
    #     if check_for_updates_disabled is not None and check_for_updates_disabled:
    #         logger.info("Update checks are disabled.")
    #         return False

    # # Read the current release version from the .env file
    # load_dotenv(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env")))
    # current_release_version = os.getenv("LOCAL_RELEASE_TAG")
    # current_release_date = os.getenv("LOCAL_RELEASE_DATE")

    # if not current_release_version or not current_release_date:
    #     logger.warn("Failed to read the current release version from the .env file.")
    #     if override_settings:
    #         check_for_updates_dialog(False, True)
    #     return False

    # # Fetch the release info file from the cloud
    # release_info = fetch_release_info(os.getenv("UPDATE_CHECK_URL"))

    # if release_info:
    #     # Get the latest release version and release date
    #     latest_release_version, latest_release_date = get_latest_release_version(
    #         release_info
    #     )

    #     # Compare the release dates
    #     comparison_result = compare_release_dates(
    #         current_release_date, latest_release_date
    #     )

    #     logger.info(f"Current release version: {current_release_version}")
    #     logger.info(f"Latest release version: {latest_release_version}")
    #     logger.info(f"Comparison result: {comparison_result}")

    #     if comparison_result == "Newer":
    #         check_for_updates_dialog(True, False)
    #         return True
    # else:
    #     if override_settings:
    #         check_for_updates_dialog(False, True)
    #     logger.warn("Failed to fetch release info file from the cloud.")
    #     return False

    # if override_settings:
    #     check_for_updates_dialog(False, False)

    # return False


def check_for_updates_dialog(new_version_available: bool, error: bool = False):
    # popup a qdialog with the update info
    update_dialog = QDialog()
    loader = QUiLoader()
    ui = loader.load(resource_path("update_available.ui"))
    update_dialog.setLayout(ui.layout())
    update_dialog.setWindowTitle("ScoreSight Update Available")
    update_dialog.checkBox_disableUpdateChecks.toggled.connect(
        lambda value: store_data("scoresight.json", "disable_update_checks", value)
    )
    # update the checkbox state
    disable_checks = fetch_data("scoresight.json", "disable_update_checks")
    update_dialog.checkBox_disableUpdateChecks.setChecked(
        disable_checks if disable_checks is not None else False
    )
    update_dialog.label_newVersion.setVisible(new_version_available and not error)
    update_dialog.label_noNewVersion.setVisible(not new_version_available and not error)
    update_dialog.label_error.setVisible(error)

    # adjust the height to match the height of the content
    update_dialog.setFixedSize(update_dialog.width(), update_dialog.height())

    update_dialog.exec()
