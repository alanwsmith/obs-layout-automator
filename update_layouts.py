import obspython as obs
from os.path import getmtime, join, isfile

config_path = join(
    "D:", "obs-position-sources-script", "config.yaml"
)

global update_time
mod_time = 0

def update_layouts():
    print("Making update")

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



