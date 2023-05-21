import os
def getBaseTmxPth():
    # Get the path to the 'maps' folder relative to the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    maps_folder = os.path.join(script_dir, 'maps')
 

    return maps_folder