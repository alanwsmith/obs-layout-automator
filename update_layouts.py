import obspython as obs
from os.path import getmtime, join, isfile
from yaml import load, SafeLoader

config_path = join(
    "D:", "obs-layout-automator", "config.yaml"
)

global update_time
mod_time = 0

class SceneItem():
    def __init__(self, source, item):
        self.item = item
        self.source = source
        self.prep()

    def cleanup(self):
        obs.obs_scene_release(self.scene_obj)
        obs.obs_source_release(self.source)

    def scale(self):
        total_width_crop = self.params['crop_left'] + self.params['crop_right']
        r1 = self.width() - total_width_crop
        r2 = self.params['width'] / r1
        scale = r2
        if self.params["rotation"] == 90:
            total_height_crop = self.params['crop_bottom'] + self.params['crop_top']
            t1 = self.height() - total_height_crop
            t2 = self.params['width'] / t1 
            scale = t2
        return scale  

    def prep(self):
        self.crop = obs.obs_sceneitem_crop()
        self.info = obs.obs_transform_info()
        obs.obs_sceneitem_get_crop(self.item, self.crop)
        obs.obs_sceneitem_get_info(self.item, self.info)

    def update(self, **kwargs):
        self.params = {
                "rotation": 0,
                "width": self.width(),
                "crop_top": 0,
                "crop_bottom": 0,
                "crop_left": 0,
                "crop_right": 0,
                "position_x": 0,
                "position_y": 0,
            }
        for key in kwargs.keys():
            self.params[key] = kwargs[key]
        if self.params['rotation'] == 90:
            self.params['crop_top'] = kwargs['crop_right']
            self.params['crop_bottom'] = kwargs['crop_left']
            self.params['crop_left'] = kwargs['crop_top']
            self.params['crop_right'] = kwargs['crop_bottom']

        self.set_width()
        self.crop_top()
        self.crop_bottom()
        self.crop_left()
        self.crop_right()
        self.set_rotation()
        self.set_position()


    def width(self):
        return obs.obs_source_get_width(self.source)

    def height(self):
        return obs.obs_source_get_height(self.source)

    def set_width(self):
        scale_vec = obs.vec2()
        scale_vec.x = self.scale()
        scale_vec.y = self.scale()
        obs.obs_sceneitem_set_scale(self.item, scale_vec)

    def apply_crop(self):
        obs.obs_sceneitem_set_crop(self.item, self.crop)

    def crop_left(self):
        self.crop.left = self.params['crop_left'] 
        self.apply_crop()

    def crop_right(self):
        self.crop.right = self.params['crop_right'] 
        self.apply_crop()

    def crop_top(self):
        self.crop.top = self.params['crop_top']
        self.apply_crop()

    def crop_bottom(self):
        self.crop.bottom = self.params['crop_bottom'] 
        self.apply_crop()

    def set_rotation(self):
        obs.obs_sceneitem_set_rot(self.item, self.params['rotation'])

    def set_position(self):
        if self.params['rotation'] == 90:
            obs.obs_sceneitem_set_alignment(self.item, 9)
        else: 
            obs.obs_sceneitem_set_alignment(self.item, 5)
        pos = obs.vec2()
        pos.x = self.params['position_x']
        pos.y = self.params['position_y']
        obs.obs_sceneitem_set_pos(self.item, pos)


def update_layouts():
    print("Making update v2")
    with open(config_path) as _yaml:
        config = load(_yaml, SafeLoader)

    print(config)
    
    scenes = obs.obs_frontend_get_scenes()
    for scene_source in scenes:
        scene_name = obs.obs_source_get_name(scene_source)
        scene_scene = obs.obs_scene_from_source(scene_source)

        if scene_name in config['scenes']:
            for item in obs.obs_scene_enum_items(scene_scene):
                item_source = obs.obs_sceneitem_get_source(item)
                sourceitem_name = obs.obs_source_get_name(item_source)
                if sourceitem_name in config['scenes'][scene_name]:
                    si = SceneItem(scene_source, item)
                    value = config['scenes'][scene_name][sourceitem_name]
                    si.update(
                            rotation = value['rotation'],
                            width = value['width'],
                            crop_left = value['crop_left'],
                            crop_right = value['crop_right'],
                            crop_top = value['crop_top'],
                            crop_bottom = value['crop_bottom'],
                            position_x = value['position_x'],
                            position_y = value['position_y'],
                        )


def check_file():
    global mod_time
    if isfile(config_path) == True:
        compare_time = getmtime(config_path)
        if mod_time != compare_time:
            mod_time = compare_time
            update_layouts()
    else:
        print(f"ERROR: no config at {config_path}")

# NOTE: Instead of using the timer, you can 
# use a frame tick that's somewhere in the
# OBS docs. 
obs.timer_add(check_file, 1000)


def script_description():
    return """This is my personal script
for setting up OBS layouts. It watches for
config file updates and makes changes 
accordingly. It runs automatically
as long as it's loaded. Click the trash 
can icon to unload it (which also stops it). 

The path to the config file is currently hard
coded. Update the source to point it where
you need
"""



