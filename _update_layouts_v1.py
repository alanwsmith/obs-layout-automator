import obspython as obs
from os.path import getmtime, join, isfile
from yaml import load, SafeLoader

config_path = join(
    "D:", "obs-position-sources-script", "config.yaml"
)

global update_time
mod_time = 0


class Updater():
    def update(self, item, data):
        self.item = item
        self.set_position(data['px'], data['py'])

    def set_position(self, x, y):
        pos = obs.vec2()
        pos.x = x
        pos.y = y
        obs.obs_sceneitem_set_pos(self.item, pos)

    def apply_crop(self):
        obs.obs_sceneitem_set_crop(self.item, self.crop)

    def crop_left(self, value):
        self.crop.left = value
        self.apply_crop()

    def crop_right(self, value):
        self.crop.right = value
        self.apply_crop()

    def crop_top(self, value):
        self.crop.top = value
        self.apply_crop()

    def crop_bottom(self, value):
        self.crop.bottom = value
        self.apply_crop()


def update_layouts():
    print("Making update")
    with open(config_path) as _yaml:
        config = load(_yaml, SafeLoader)
    
    scenes = obs.obs_frontend_get_scenes()
    for scene_source in scenes:
        scene_name = obs.obs_source_get_name(scene_source)
        scene_scene = obs.obs_scene_from_source(scene_source)

        if scene_name in config['scenes']:
            for item in obs.obs_scene_enum_items(scene_scene):
                item_source = obs.obs_sceneitem_get_source(item)
                sourceitem_name = obs.obs_source_get_name(item_source)
                if sourceitem_name in config['scenes'][scene_name]:
                    u = Updater()
                    u.update(item, config['scenes'][scene_name][sourceitem_name])
                    #print(f"{scene_name} - {sourceitem_name}")

    #print(config)



def check_file():
    global mod_time
    if isfile(config_path) == True:
        compare_time = getmtime(config_path)
        if mod_time != compare_time:
            mod_time = compare_time
            update_layouts()
    else:
        print(f"ERROR: no config at {config_path}")

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



