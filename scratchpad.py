import obspython as obs

from pprint import pprint

# Details on transform stuff here:
# https://obsproject.com/docs/reference-scenes.html#c.obs_transform_info

def do_something(props, prop):
    # source_name = "Test Source"
    current_scene = obs.obs_frontend_get_current_scene()
    scene = obs.obs_scene_from_source(current_scene)
    scene_item = obs.obs_scene_find_source(scene, "Test Source")
    if scene_item:
        info = obs.obs_transform_info()
        obs.obs_sceneitem_get_info(scene_item, info)
        print(f"Position X: {info.pos.x}")
        print(f"Position Y: {info.pos.y}")
        print(f"Rotation: {info.rot}")
        print(f"Alignment: {info.alignment}")
        print(f"Scale X: {info.scale.x}")
        print(f"Scale Y: {info.scale.y}")
    obs.obs_scene_release(scene)

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(
        props, "button", "Run Test", do_something 
    )
    return props
