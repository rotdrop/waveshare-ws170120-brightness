# WaveShare WS170120 Brightness

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Intro](#intro)
- [Installation](#installation)
    - [pip](#pip)
    - [pipx](#pipx)
    - [Manually](#manually)
- [Usage](#usage)
    - [Python Module](#python-module)
    - [Standalone Script](#standalone-script)

<!-- markdown-toc end -->

## Intro

A simple python pip module and script in order to control the
backlight of a WaveShare WS170120 touchscreen. The tools provided by
Waveshare are binary only and are only able to set the brightness in
steps of 10%, while the hardware supports steps of 1%.

The project has been generated from some simple USB capturing. The
protocol is easy enough, see [USB-Protocol](reverse-engineering/USB-Protocol.md)

## Installation

### pip

`pip install waveshare-ws170120-brightness`

or

```
git clone https://github.com/rotdrop/waveshare-ws170120-brightness.git
pip install ./waveshare-ws170120-brightness
```

### pipx

This generates an isolated virtual environment and installes the bundled script `waveshare-ws170120-brightness`.

`pipx install waveshare-ws170120-brightness`

or

```
git clone https://github.com/rotdrop/waveshare-ws170120-brightness.git
pipx install ./waveshare-ws170120-brightness
```

### Manually

Clone the repository, install the requirements (see [requirements.txt](./requirements.txt)). The python script is located in [__init__.py](waveshare_ws170120_brightness/__init__.py).

## Usage

### Python Module

```
from waveshare_ws170120_brightness import WaveshareWS170120
...
backlightController = WaveshareWS170120(verbosity=1)
backlichtController.setBrightness(percentage=47)
```

The class constructor as well as the `setBrightness()` method will raise exceptions if something goes wrong.

- the constructor will raise a `FileNotFoundError` if the hidraw device for the touchscreen could not be found
- the `setBrightness()` method may raise an `IOError` if writing to the hidraw device gave unexpected results

In addition, the called system services may raise their own errors. These are not caught in the program code.

### Standalone Script

The corresponding executable just has the same name as the package, `waveshare-ws170120-brightness`. Please run
```
waveshare-ws170120-brightness -h
```
for usage information. Currently, this generates the output
```
usage: waveshare-ws170120-brightness [-h] -b PERCENTAGE [-v]

Set the brightness of an attached Waveshare WS170120 touch-screen

options:
  -h, --help            show this help message and exit
  -b PERCENTAGE, --brightness PERCENTAGE
                        set the brightness value to the given percentage.
  -v, --verbose
```
However, that may change ...


