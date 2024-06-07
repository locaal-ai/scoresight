# ScoreSight - Real-time OCR For Scoreboards, Apps, Games and more

[![GitHub](https://img.shields.io/github/license/occ-ai/scoresight)](https://github.com/occ-ai/scoresight/blob/main/LICENSE)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/occ-ai/scoresight/build.yaml)](https://github.com/occ-ai/scoresight/actions/workflows/build.yaml)
[![Total downloads](https://img.shields.io/github/downloads/occ-ai/scoresight/total)](https://github.com/occ-ai/scoresight/releases)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/occ-ai/scoresight)](https://github.com/occ-ai/scoresight/releases)
[![Discord](https://img.shields.io/discord/1200229425141252116)](https://discord.gg/8pG2tC923N)

ScoreSight is an OCR (Optical Character Recognition) application designed to extract text from real-time updating streams like scoreboards, applications, videos and games.
It is written in Python and utilizes the following technologies:

- Qt6: A cross-platform GUI toolkit for creating graphical user interfaces.
- OpenCV: A computer vision library for image and video processing.
- Tesseract OCR: An open-source OCR engine for recognizing text from images.

It is the best **free** real-time OCR tool on planet Earth for scoreboards and games.

If you'd like to donate to help support the project, you can do so on [GitHub](https://github.com/sponsors/royshil) or [Patreon](https://www.patreon.com/RoyShilkrot).

## Features

- Works on Windows, Mac and Linux (the only scoreboard OCR tool that does it)
- Input/Capture: USB, NDI, Screen Capture, URL / RTSP, Video Files, etc.
- Perspective correction
- Image processing and binarization techniques, local, global etc.
- Output to text files (.txt, .csv, .xml)
- HTTP output via local server: HTML, JSON, XML and CSV endpoints
- Import & Export configuration profiles
- Integrations: OBS (websocket), vMix (API), NewBlue FX Titler (API)
- Up to 30 updates/s
- Unlimited detection boxes
- Camera bump and drift correction with stabilization algorithm
- Unlimited devices or open instances on the same device
- Custom detection boxes

Price: FREE.

## Usage

Very short video tutorials:

<div>
<a href="https://youtu.be/wMNolI0w0tE" target="_blank"><img src="./image-16.png" width="30%"/></a>
<a href="https://youtu.be/ACY4-yT3x84" target="_blank"><img src="./image-17.png" width="30%"/></a>
<a href="https://youtu.be/yowoYzBWrps" target="_blank"><img src="./image-18.png" width="30%"/></a>
<a href="https://youtu.be/ptR-Yh5FSPg" target="_blank"><img src="./image-19.png" width="30%"/></a>
</div>

Additional guides:

- [How to use the internal HTTP server](http_server.md)
- [How to connect to vMix](vmix.md)

## Installation

See the [releases](https://github.com/occ-ai/scoresight/releases) page for downloadable executables and installers.

See the [Install Guide](../INSTALL.md) for help with installation.
