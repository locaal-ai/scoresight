import requests
from text_detection_target import TextDetectionTargetWithResult
from sc_logging import logger
from storage import subscribe_to_data, fetch_data


class UNOAPI:
    def __init__(self, endpoint, field_mapping):
        self.endpoint = endpoint
        self.field_mapping = field_mapping
        self.running = False
        self.update_same = fetch_data("scoresight.json", "uno_send_same", False)
        subscribe_to_data("scoresight.json", "uno_send_same", self.set_update_same)

    def set_update_same(self, update_same):
        self.update_same = update_same

    def set_field_mapping(self, field_mapping):
        logger.debug(f"Setting UNO field mapping: {field_mapping}")
        self.field_mapping = field_mapping

    def update_uno(self, detection: list[TextDetectionTargetWithResult]):
        if not self.running:
            return

        if not self.field_mapping:
            logger.debug("Field mapping is not set")
            return

        look_in = [TextDetectionTargetWithResult.ResultState.Success]
        if self.update_same:
            look_in.append(TextDetectionTargetWithResult.ResultState.SameNoChange)

        for target in detection:
            if target.result_state in look_in and target.name in self.field_mapping:
                uno_command = self.field_mapping[target.name]
                self.send_uno_command(uno_command, target.result)

    def send_uno_command(self, command, value):
        payload = {"command": command, "value": value}

        try:
            response = requests.put(self.endpoint, json=payload)
            if response.status_code != 200:
                logger.error(
                    f"Failed to send data to UNO API, status code: {response.status_code}"
                )
            else:
                logger.debug(f"Successfully sent {command}: {value} to UNO API")

            # Check rate limit headers
            self.check_rate_limits(response.headers)

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to send data to UNO API: {e}")

    def check_rate_limits(self, headers):
        rate_limit_headers = [
            "X-Singular-Ratelimit-Burst-Calls",
            "X-Singular-Ratelimit-Daily-Calls",
            "X-Singular-Ratelimit-Burst-Data",
            "X-Singular-Ratelimit-Daily-Data",
        ]

        for header in rate_limit_headers:
            if header in headers:
                limit_info = headers[header]
                logger.debug(f"Rate limit info for {header}: {limit_info}")

                # You can add more sophisticated rate limit handling here if needed
                # For example, pause requests if limits are close to being reached

    def start(self):
        self.running = True

    def stop(self):
        self.running = False
