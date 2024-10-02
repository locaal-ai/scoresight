import datetime
from os import path

from text_detection_target import TextDetectionTargetWithResult
from sc_logging import logger


def save_text_files(results, out_folder, append_method_index):
    for targetWithResult in results:
        if targetWithResult.result is None:
            continue
        if (
            "skip_empty" in targetWithResult.settings
            and targetWithResult.settings["skip_empty"]
            and len(targetWithResult.result) == 0
        ):
            continue
        if (
            targetWithResult.result_state
            != TextDetectionTargetWithResult.ResultState.Success
        ):
            continue

        output_file_path = path.abspath(
            path.join(
                out_folder,
                f"{targetWithResult.name}.txt",
            )
        )
        append_method = "w"
        if append_method_index == 1 or append_method_index == 2:
            append_method = "a"

        # check if the file exists, if it does, append the result to the file
        try:
            with open(output_file_path, append_method) as f:
                f.write(f"{targetWithResult.result}")
                if append_method == "a":
                    f.write("\n")
        except Exception as e:
            logger.error(f"Error writing to file: {e}")


def save_csv(results, out_folder, append_method_index, first_csv_append):
    if not out_folder:
        return

    # add timestamp as first column
    result_concat_for_aggreagate = f"{datetime.datetime.now().isoformat()},"
    header = "Timestamp,"
    for targetWithResult in results:
        header += f"{targetWithResult.name},"
        if (
            targetWithResult.result_state
            != TextDetectionTargetWithResult.ResultState.Success
        ):
            result_concat_for_aggreagate += ","
        else:
            result_concat_for_aggreagate += (
                f"{targetWithResult.result}," if targetWithResult.result else ","
            )

    aggregate_output_file_path = path.abspath(path.join(out_folder, "results.csv"))
    append_method = "w"
    if append_method_index == 0 or append_method_index == 2:
        append_method = "a"

    try:
        with open(aggregate_output_file_path, append_method) as f:
            # if this is the first-time-appending or truncating, add the header
            if first_csv_append or append_method == "w":
                f.write(header + "\n")
                first_csv_append = False
            f.write(result_concat_for_aggreagate + "\n")
    except Exception as e:
        logger.error(f"Error writing to aggregate file: {e}")


def save_xml(results, out_folder):
    if not out_folder:
        return

    aggregate_output_file_path = path.abspath(path.join(out_folder, "results.xml"))

    try:
        with open(aggregate_output_file_path, "w") as f:
            # add xml preamble
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')

            f.write("<data>")
            for targetWithResult in results:
                # serialize dictionary to xml
                dictionary = targetWithResult.to_dict()
                f.write("<result>")
                for key in dictionary:
                    f.write(f"<{key}>{dictionary[key]}</{key}>")
                f.write("</result>")
            f.write("</data>")
    except Exception as e:
        logger.error(f"Error writing to xml file: {e}")
