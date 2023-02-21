# OBS Position Sources Script

TODO: reanme this to something like

OBS Layout Automator


## Overview

This is the python script I use to make it
easier to position sources in OBS scenes
by doing it programmatically.

The goal of this is not to do everything,
just to make positioning things work
via a config.

## Goals

- TOML file for configuration
- Configure all scenes and sources from
  a single file
- Adjust position, sizing, and crops

## Python Install

Python needs to be installed. Then,
for my Windows machine I went to:

```
OBS -> Tools -> Scripts -> Python Settings
```

From there, I browsed for the folder that holds
Python. For me, that was:

```
C:/Users/alan/AppData/Local/Programs/Python/Pypthon310
```

TODO: Point to article on 3.6-3.10 working but not
3.11. Since 3.6 is deprecated, I installed 3.10

## Installing yaml

I had to install a toml module. I did this from the
command line with:

```
python -m pip install pyyaml
```

NOTE: that's `pyyaml` and not `yaml`

## Loading The Script

TKTKTK - TONOTE: As soon as you load the script the interface
shows up.

## Config File

TKTKTKTK

## References

- Credit to [this cheatsheet](https://github.com/Jwolter0/OBS-Studio-Python-Scripting-Cheatsheet-obspython-Examples-of-API)
  for getting me started in general
- And [this script](https://github.com/Jwolter0/OBS-Studio-Python-Scripting-Cheatsheet-obspython-Examples-of-API/blob/master/src/move_source_.py)
  specifically
- https://toml.io/en/

---

Notes:

https://obsproject.com/docs/reference-scenes.html#c.obs_scene_t

---

void obs_sceneitem_set_alignment(obs_sceneitem_t *item, uint32_t alignment)
uint32_t obs_sceneitem_get_alignment(const obs_sceneitem_t *item)

void obs_sceneitem_set_scale(obs_sceneitem_t *item, const struct vec2 *scale)
void obs_sceneitem_get_scale(const obs_sceneitem_t *item, struct vec2 *scale)

void obs_sceneitem_set_rot(obs_sceneitem_t *item, float rot_deg)
float obs_sceneitem_get_rot(const obs_sceneitem_t *item)
Sets/gets the rotation of a scene item.

void obs_sceneitem_set_pos(obs_sceneitem_t *item, const struct vec2 *pos)
void obs_sceneitem_get_pos(const obs_sceneitem_t *item, struct vec2 *pos)
Sets/gets the position of a scene item.

void obs_sceneitem_set_crop(obs_sceneitem_t *item, const struct obs_sceneitem_crop *crop)
void obs_sceneitem_get_crop(const obs_sceneitem_t *item, struct obs_sceneitem_crop *crop)

void obs_sceneitem_set_bounds_alignment(obs_sceneitem_t *item, uint32_t alignment)
uint32_t obs_sceneitem_get_bounds_alignment(const obs_sceneitem_t *item)

void obs_sceneitem_set_bounds(obs_sceneitem_t *item, const struct vec2 *bounds)
void obs_sceneitem_get_bounds(const obs_sceneitem_t *item, struct vec2 *bounds)

void obs_sceneitem_set_info(obs_sceneitem_t *item, const struct obs_transform_info *info)
void obs_sceneitem_get_info(const obs_sceneitem_t *item, struct obs_transform_info *info)
