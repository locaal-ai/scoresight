import requests
import json
import csv
import io
from functools import partial
import xml.etree.ElementTree as ET
from urllib.parse import urlparse
import threading

from sc_logging import logger
from text_detection_target import TextDetectionTargetWithResult
from storage import fetch_data, subscribe_to_data

out_api_url = fetch_data("scoresight.json", "out_api_url", None)
out_api_encoding = fetch_data("scoresight.json", "out_api_encoding", "JSON")


def is_valid_url_urllib(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def setup_out_api_url(url):
    global out_api_url
    out_api_url = url


def setup_out_api_encoding(encoding):
    global out_api_encoding
    out_api_encoding = encoding


subscribe_to_data("scoresight.json", "out_api_url", setup_out_api_url)
subscribe_to_data("scoresight.json", "out_api_encoding", setup_out_api_encoding)


def update_out_api(data: list[TextDetectionTargetWithResult]):
    if out_api_url is None or out_api_encoding is None:
        logger.error(f"Output API not set up: {out_api_url}, {out_api_encoding}")
        return

    # validate the URL
    if not is_valid_url_urllib(out_api_url):
        logger.error(f"Invalid URL: {out_api_url}")
        return

    logger.debug(f"Sending data to output API: {out_api_url}")

    def send_data():
        try:
            if out_api_encoding == "JSON":
                response = send_json(data)
            elif out_api_encoding == "XML":
                response = send_xml(data)
            elif out_api_encoding == "CSV":
                response = send_csv(data)
            else:
                logger.error("Invalid encoding: %s", out_api_encoding)
                return

            if response.status_code != 200:
                logger.error(
                    f"Error sending data to output API: {out_api_url}, {response.status_code}"
                )
        except Exception as e:
            logger.error(f"Error sending data to output API: {out_api_url}, {e}")

    thread = threading.Thread(target=send_data)
    thread.start()


def send_json(data: list[TextDetectionTargetWithResult]):
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        out_api_url,
        headers=headers,
        data=json.dumps([result.to_dict() for result in data]),
    )
    return response


def send_xml(data: list[TextDetectionTargetWithResult]):
    headers = {"Content-Type": "application/xml"}
    root = ET.Element("root")
    for targetWithResult in data:
        resultEl = ET.SubElement(root, "result")
        resultEl.set("name", targetWithResult.name)
        resultEl.set("result", targetWithResult.result)
        resultEl.set("result_state", targetWithResult.result_state.name)
        resultEl.set("x", str(targetWithResult.x()))
        resultEl.set("y", str(targetWithResult.y()))
        resultEl.set("width", str(targetWithResult.width()))
        resultEl.set("height", str(targetWithResult.height()))
    xml_data = ET.tostring(root, encoding="utf-8")
    response = requests.post(out_api_url, headers=headers, data=xml_data)
    return response


def send_csv(data: list[TextDetectionTargetWithResult]):
    headers = {"Content-Type": "text/csv"}
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Name", "Text", "State", "X", "Y", "Width", "Height"])
    for result in data:
        writer.writerow(
            [
                result.name,
                result.result,
                result.result_state.name,
                result.x(),
                result.y(),
                result.width(),
                result.height(),
            ]
        )
    response = requests.post(out_api_url, headers=headers, data=output.getvalue())
    return response
