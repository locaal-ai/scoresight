import requests

from text_detection_target import TextDetectionTargetWithResult
from sc_logging import logger


class VMixAPI:
    def __init__(self, host, port, input_number, field_mapping):
        self.host = host
        self.port = port
        self.input_number = input_number
        self.field_mapping = field_mapping
        self.running = False

    def set_field_mapping(self, field_mapping):
        self.field_mapping = field_mapping

    def update_vmix(self, detection: list[TextDetectionTargetWithResult]):
        if not self.running:
            return

        if not self.field_mapping:
            logger.debug("Field mapping is not set")
            return

        # Prepare the data to send
        data = {}
        for target in detection:
            if target.result_state == TextDetectionTargetWithResult.ResultState.Success:
                if target.name in self.field_mapping:
                    data[self.field_mapping[target.name]] = target.result

        if not data:
            logger.debug("No data to send")
            return

        for key, value in data.items():
            # Prepare the URL
            url = (
                f"http://{self.host}:{self.port}/api/?Input={self.input_number}&"
                + f"Function=SetText&SelectedName={key}&Value={value}"
            )
            try:
                # Send the request
                response = requests.post(url, data=data)

                # Check the response
                if response.status_code != 200:
                    logger.error(
                        f"Failed to send data, status code: {response.status_code}"
                    )
            except requests.exceptions.RequestException as e:
                logger.error(f"Failed to send data to {url}: {e}")
