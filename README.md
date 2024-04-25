# ScoreSight - OCR Scoreboard Application

This is an OCR (Optical Character Recognition) application designed to read scoreboards.
It is written in Python and utilizes the following technologies:

- Qt6: A cross-platform GUI toolkit for creating graphical user interfaces.
- OpenCV: A computer vision library for image and video processing.
- Tesseract OCR: An open-source OCR engine for recognizing text from images.

## Features

- Extracts text from scoreboards using image processing techniques.
- Provides a user-friendly interface for interacting with the application.
- Supports multiple platforms thanks to PyInstaller packaging.

## Usage

Videos and tutorials will be provided shortly.

## Installation

See the releases page for downloadable executables and installers.

### Prerequisites

- Python 3.11
- git

### Procedure

1. Clone the repository:

  ```shell
  git clone https://github.com/occ-ai/scoresight.git
  ```

2. Install the required dependencies:

  ```shell
  pip install -r requirements.txt
  ```

For Mac and Windows there are further dependencies in `requirements-mac.txt` and `requirements-win.txt`

3. Create a `.env` file. See the contents of the file in the `.github/worksflows/build.yaml` file

### Windows

There are some extra steps for installation on Windows:
 - Download and install https://visualstudio.microsoft.com/visual-cpp-build-tools/ C++ Build Tools
 - Build the win32DeviceEnum pyd by `$ cd win32DeviceEnum && python.exe setup.py build_ext --inplace`

## Usage

1. Launch the application:

  ```shell
  python main.py
  ```

2. Follow the on-screen instructions to load an image of the scoreboard and extract the text.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request.

## License

This project is released under the MIT license.

## Contact

If you have any questions or suggestions, feel free to leave an issue on the repository.
You may also email [support@scoresight.live](mailto:support@scoresight.live).

## Business Inquiries

If you wish to contract the development team to productionize ScoreSight for your business need,
please contact [info@scoresight.live](mailto:info@scoresight.live).
