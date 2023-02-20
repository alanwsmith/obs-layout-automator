import obspython as obs
import os.path
import yaml 

# from pprint import pprint

config_path = os.path.join("d:", "obs-position-sources-script", "config.yaml")

class SceneItem():
    def __init__(self, name):
        self.name = name 
        self.prep()

    def cleanup(self):
        obs.obs_scene_release(self.scene_obj)
        obs.obs_source_release(self.source)

    def scale(self):
        total_width_crop = self.params['crop_left'] + self.params['crop_right']
        width_plus_crop = self.params['width'] + total_width_crop
        width_minus_crop = self.params['width'] - total_width_crop
        width_base = self.params['width']

        # print(total_width_crop / width_plus_crop)
        # print(total_width_crop / width_minus_crop)
        # print(width_plus_crop / total_width_crop)
        # print(width_minus_crop / total_width_crop)

        # print(width_minus_crop / width_plus_crop)
        # print(width_plus_crop / width_minus_crop)

        r1 = self.width() - total_width_crop
        r2 = self.params['width'] / r1
        # print(r1)
        # print(r2)
        scale = r2




        # step1 = self.params['width'] + self.params['crop_left'] + self.params['crop_right']
        # # print(step1)
        # step2 = step1 / self.width()  
        # # print(step2)

        # z1 = self.width() / step1
        # # print(f"z1 {z1}")


        # w1 = self.params['width'] / total_width_crop
        # w2 = total_width_crop / self.params['width']
        # w3 = total_width_crop / (self.params['width'] + total_width_crop)
        # w4 = (self.params['width'] + total_width_crop) / total_width_crop
        # w5 = self.params['width'] / (total_width_crop + self.params['width'])

        # print(f"w1 {w1}")
        # print(f"w2 {w2}")
        # print(f"w3 {w3}")
        # print(f"w4 {w4}")
        # print(f"w5 {w5}")



        # x_1 = self.height() / step1
        # print(x_1)
        # x_2 = x_1 + self.params['width']
        # print(x_2)


        # step2 = step1 / self.width()
        # scale = x_2
        # scale = step2 



        # height = int(self.height() * scale)

        # value = {
        #         "width": kwargs['width'],
        #         "height": height,
        #         "scale": scale
        #         }

        if self.params["rotation"] == 90:
            step0 = self.width() + self.params["crop_left"] + self.params["crop_right"]
            step1 =  step0 / self.height()
            scale = step1

            # step2 = step1 * kwargs["width"]
            # new_value = kwargs["source_x"] / kwargs["source_y"] * kwargs["width"]
            # value = {
            #     "height": kwargs['width'],
            #     "width": int(step2) ,
            #     "scale": step1
            # }
        return scale  

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



        # if self.params['rotation'] == 90:
        #     self.params['crop_top'] = kwargs['crop_right']
        #     self.params['crop_bottom'] = kwargs['crop_left']
        #     self.params['crop_left'] = kwargs['crop_top']
        #     self.params['crop_right'] = kwargs['crop_bottom']
        #     thing = self.params['width'] / self.width()
        #     target_height = self.height() * thing
        #     print(target_height)
        #     self.params['width'] = target_height


        # self.do_calculations()
        self.set_width()
        self.crop_top()
        self.crop_bottom()
        self.crop_left()
        self.crop_right()
        self.set_rotation()
        self.set_position()

        # print(self.params)

        # print("Updates Complete - ")

    # def do_calculations(self):
        # print("Doing calculations")
        # self.params['width'] = self.params['width'] + self.params['crop_left']  + self.params['crop_right']
        # width_multiplier = self.params['width']  / (self.params['width'] - self.params['crop_left'] - self.params['crop_right'])

        # if self.params['rotation'] == 90:
        #     width_multiplier = self.params['width']  / (self.params['width'] - self.params['crop_top'] - self.params['crop_bottom'])

        # self.params['width'] = self.params['width'] * width_multiplier


    def width(self):
        return obs.obs_source_get_width(self.source)

    def height(self):
        return obs.obs_source_get_height(self.source)

    def set_width(self):
        # scale_value = self.params['width'] / self.width() 
        # scale_value = self.params['width'] / self.height() 
        # if self.params['rotation'] == 90:
        #     scale_value =  self.params['width'] / target_height
        # print(self.width())
        scale_vec = obs.vec2()
        # scale.x = scale_value
        # scale.y = scale_value
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


def update_source_positions(props, prop):
    si = SceneItem(name="Video Capture Device")
    si.update(
            rotation = 0,
            width = 1020,
            crop_left = 0,
            crop_right = 0,
            crop_top = 0,
            crop_bottom = 0,
            position_x = 0,
            position_y = 0,
    )
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

