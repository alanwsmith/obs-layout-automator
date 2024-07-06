#!/usr/bin/env python3

from string import Template

skeleton = """scenes:
  "Main":
    "MainWindow":
      width: $MAIN_WIDTH
      position_x: $LEFT_PAD
      position_y: $TOP_PAD
      rotation: 90
      crop_top: $MAIN_CROP_TOP
      crop_bottom: $MAIN_CROP_BOTTOM
      crop_left: 0
      crop_right: 0

    "InfoCharlie":
      width: $MAIN_WIDTH
      position_x: $LEFT_PAD
      position_y: $CHARLIE_Y_POSITION
      rotation: 90
      crop_top: 3464
      crop_bottom: 0
      crop_left: 0
      crop_right: 0

    "InfoAlfa":
      width: $SIDE_WIDTH
      position_x: $SIDE_START
      position_y: 590
      rotation: 90
      crop_top: 2538
      crop_bottom: 282
      crop_left: 0
      crop_right: 1490

    "InfoBravo":
      width: $SIDE_WIDTH
      position_x: $SIDE_START
      position_y: $CHARLIE_Y_POSITION
      rotation: 90
      crop_top: 2538
      crop_bottom: 1156
      crop_left: 722
      crop_right: 768

    "FaceCam":
      width: $SIDE_WIDTH
      position_x: $SIDE_START
      position_y: $TOP_PAD
      rotation: 0
      crop_top: 0 
      crop_bottom: 0
      crop_left: 0
      crop_right: 0

"""

data = {
    "MAIN_WIDTH": 2900,
    "MAIN_CROP_TOP": 1086,
    "MAIN_CROP_BOTTOM": 1584,
    "CHARLIE_Y_POSITION": 1628,
    "LEFT_PAD": 16,
    "RIGHT_PAD": 16,
    "TOP_PAD": 28,
    "SIDE_PAD": 32
}

data["SIDE_START"] = data["MAIN_WIDTH"] + data["SIDE_PAD"]
data["SIDE_WIDTH"] = 3860 - data["MAIN_WIDTH"] - data["SIDE_PAD"] - data["RIGHT_PAD"] - data["LEFT_PAD"]

template = Template(skeleton)

output = template.substitute(data)

with open("config.yaml", "w") as _out:
    _out.write(output)

print("Done")
