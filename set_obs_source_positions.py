import obspython as obs
import os.path
import yaml 

from pprint import pprint

config_path = os.path.join("d:", "obs-position-sources-script", "config.yaml")

class SceneItem():
    def __init__(self, name):
        self.name = name 
        self.prep()
    
    def cleanup(self):
        obs.obs_scene_release(self.scene_obj)
        obs.obs_source_release(self.source)

    def prep(self):
        # TODO: Throw an error if the thing doesn't exist
        self.source = obs.obs_get_source_by_name(self.name)
        self.scene_ref = obs.obs_frontend_get_current_scene()
        self.scene_obj = obs.obs_scene_from_source(self.scene_ref)
        self.item = obs.obs_scene_find_source(self.scene_obj, self.name)
        self.crop = obs.obs_sceneitem_crop()
        self.info = obs.obs_transform_info()
        obs.obs_sceneitem_get_crop(self.item, self.crop)
        obs.obs_sceneitem_get_info(self.item, self.info)

    def width(self):
        return obs.obs_source_get_width(self.source)

    def set_width(self, value):
        scale_value = value / self.width() 
        scale = obs.vec2()
        scale.x = scale_value
        scale.y = scale_value
        obs.obs_sceneitem_set_scale(self.item, scale)

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

    def rotate(self, value):
        obs.obs_sceneitem_set_rot(self.item, value)

def update_source_positions(props, prop):
    si = SceneItem(name="Video Capture Device")
    si.rotate(90)
    si.set_width(900)
    si.crop_left(0)
    si.cleanup()


def script_description():
    return "Position Sources In Scenes"

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(
        props, "button", "Update Source Positions", update_source_positions 
    )
    return props






# class Source(): 
#     def __init__(self):
#         self.name = None
#     def source(self):
#         return obs.obs_get_source_by_name(self.name)
#     def width(self):
#         return obs.obs_source_get_width(self.source())
#     def height(self):
#         return obs.obs_source_get_height(self.source())



#def position_sources(props, prop):
#    with open(config_path, "rb") as _config:
#        config = yaml.safe_load(_config)
#    current_scene = obs.obs_frontend_get_current_scene()
#    scene = obs.obs_scene_from_source(current_scene)
#    for settings in config["scenes"]:
#        s = Source()
#        s.name = settings["name"]
#        print(s.width())
#        print(s.height())
#        # print(s.source())
#        # print("Getting Info")
#        # source_name = settings["name"]
#        # source = obs.obs_get_source_by_name(source_name)
#        # source_width = obs.obs_source_get_width(source)
#        # source_height = obs.obs_source_get_height(source)
#        # print(source_width)
#        #scene_item = obs.obs_scene_find_source(scene, "Video Capture Device")


    

    #     current_scene = obs.obs_frontend_get_current_scene()
    #     scene = obs.obs_scene_from_source(current_scene)
    #     source = obs.obs_get_source_by_name(source_name)
    #     scene_item = obs.obs_scene_find_source(scene, source_name)
    #     if scene_item:
    #         pos = obs.vec2()
    #         pos.x = settings["px"]
    #         pos.y = settings["py"] 
    #         pprint(obs.obs_sceneitem_get_info())
    #         # pprint(scene_item.obs_transform_info.pos)
    #         # obs.obs_get_source_properties
    #         # obs.obs_sceneitem_set_pos(scene_item, pos)
    #     obs.obs_scene_release(scene)
    #     obs.obs_source_release(source)




# class Example:
#     pass 

    # def __init__(self):
    #     pos = obs.vec2()
    #     self.location = pos

    # def create_text_source(self):
    #     current_scene = obs.obs_frontend_get_current_scene()
    #     scene = obs.obs_scene_from_source(current_scene)
    #     settings = obs.obs_data_create()
    #     obs.obs_data_set_string(
    #         settings, "text", "The quick brown fox jumps over the lazy dog"
    #     )
    #     source = obs.obs_source_create_private("text_gdiplus", "test_py", settings)
    #     obs.obs_scene_add(scene, source)
    #     obs.obs_scene_release(scene)
    #     obs.obs_data_release(settings)
    #     obs.obs_source_release(source)

    # def move_text_source(self):
    #     current_scene = obs.obs_frontend_get_current_scene()
    #     source = obs.obs_get_source_by_name("test_py")
    #     scene = obs.obs_scene_from_source(current_scene)
    #     scene_item = obs.obs_scene_find_source(scene, "test_py")
    #     if scene_item:
    #         dx, dy = 10, 10
    #         print("old values", self.location.x)
    #         obs.obs_sceneitem_get_pos(
    #             scene_item, self.location
    #         )  # update to last position if its changed from OBS
    #         self.location.x += dx
    #         self.location.y += dy
    #         print("new values", self.location.x)
    #         obs.obs_sceneitem_set_pos(scene_item, self.location)
    #     obs.obs_scene_release(scene)
    #     obs.obs_source_release(source)


# eg = Example()  # class created ,obs part starts


# def add_pressed(props, prop):
#     eg.create_text_source()


# def move_pressed(props, prop):
#     eg.move_text_source()


# def script_description():
#     return "add text source to current scene"


# def script_properties():  # ui
#     props = obs.obs_properties_create()
#     obs.obs_properties_add_button(props, "button", "Add text source", add_pressed)
#     obs.obs_properties_add_button(
#         props, "button2", "Move source +10 pixels", move_pressed
#     )
#     return props

# def script_properties():  # ui
#     props = S.obs_properties_create()
#     p = S.obs_properties_add_list(
#         props,
#         "source",
#         "Select source",
#         S.OBS_COMBO_TYPE_EDITABLE,
#         S.OBS_COMBO_FORMAT_STRING,
#     )
#     sources = S.obs_enum_sources()
#     if sources is not None:
#         for source in sources:
#             source_id = S.obs_source_get_unversioned_id(source)
#             name = S.obs_source_get_name(source)
#             S.obs_property_list_add_string(p, name, name)
#         S.source_list_release(sources)
#     S.obs_properties_add_button(
#         props, "button", "Print source settings and filter names", button_pressed
#     )
#     return props

