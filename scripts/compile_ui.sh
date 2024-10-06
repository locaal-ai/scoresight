#!/bin/bash

# Directory containing the .ui files
UI_DIR="$(dirname "$0")/../src"
# Directory to output the compiled .py files
OUTPUT_DIR=$UI_DIR

# Ensure the output directory exists
mkdir -p "$OUTPUT_DIR"

# Compile each .ui file in the UI_DIR
for ui_file in "$UI_DIR"/*.ui; do
    # Get the base name of the file (without extension)
    base_name=$(basename "$ui_file" .ui)
    echo "Compiling $ui_file to $OUTPUT_DIR/ui_${base_name}.py"
    # Compile the .ui file to a .py file
    pyside6-uic "$ui_file" -o "$OUTPUT_DIR/ui_${base_name}.py"
done

echo "UI files compiled successfully."
