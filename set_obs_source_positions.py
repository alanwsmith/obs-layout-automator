import obspython as obs

def position_sources(props, prop):
    source_name = "Test Source"
    current_scene = obs.obs_frontend_get_current_scene()
    scene = obs.obs_scene_from_source(current_scene)
    source = obs.obs_get_source_by_name(source_name)
    scene_item = obs.obs_scene_find_source(scene, source_name)
    if scene_item:
        pos = obs.vec2()
        pos.x = 50
        pos.y = 50
        obs.obs_sceneitem_set_pos(scene_item, pos)
    obs.obs_scene_release(scene)
    obs.obs_source_release(source)

def script_description():
    return "Position Sources In Scenes"

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(
        props, "button", "Position Sources", position_sources 
    )
    return props





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

