import obspython as obs
from os.path import getmtime, join, isfile

config_path = join(
    "D:", 
    "obs-position-sources-script",
    "config.yaml"
)

global update_time
mod_time = 0

def check_file():
    global mod_time
    print("Checking file")
    if isfile(config_path) == False:
        print(f"- File does not exist: {file_path}")
    else:
        compare_time = getmtime(config_path)
        if mod_time != compare_time:
            mod_time = compare_time
            print(f"- File Changed: {mod_time}")
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



