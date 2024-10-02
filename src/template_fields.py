from text_detection_target import TextDetectionTargetWithResult


def evaluate_template_field(
    results: list[TextDetectionTargetWithResult],
    template_field: TextDetectionTargetWithResult,
):
    template = template_field.settings["templatefield_text"]
    if not template:
        return None
    if not results or len(results) == 0:
        return ""

    # replace the template field with the results by name
    for result in results:
        template = template.replace("{{" + result.name + "}}", result.result)

    return template
