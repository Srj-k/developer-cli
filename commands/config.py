from services.config_service import *
from utils.custom_print import error, success, warning
from utils.table import print_table, print_detail

def set_config(args):
    try:
        feature, config_key = args.key.split(".")
        res = set_config_service(feature=feature, config_key=config_key, value=args.value)

        if res:
            success("Config created successfully")
        elif res is None:
            error("Invalid value or key.")
        
    except ValueError as e:
        error(f"Error: {e}")
    except IOError as e:
        error(f"Failed to save config. {e}")
    except:
        error("Unexpected error while creating config")
    

def get_config(args):
    try:
        feature, config_key = args.key.split(".")
        data = get_config_service(feature, config_key)
        if data is None:
            error("Config key is not found.")
            return
        print_detail("Config Detail", data)

    except KeyError:
        error("No such key exists")
        return
    
    except IOError as e:
        error(f"{e}")
        return
    

def remove_config(args):
    try:
        feature, config_key = args.key.split(".")
        res = remove_config_service(feature, config_key)
    except KeyError as e:
        error(f"{e}")
        return
    
    if res:
        success("Config removed successfully..")
    else:
        error("Failed to remove config")

def view_configs(args):
    try:
        data = view_config_service() 
    except ValueError as e:
        error(f"Error: {e}")
        return
    except IOError as e:
        error("Failed to fetch config")
        return
    except Exception:
        error("Unexpected error while fetching config")
        return

    rows = []
    headers = ["Feature", "Config", "Value"]

    if not data:
        warning("No configs found")
        return

    for feature in data:
        for key, value in data[feature].items():
            rows.append([feature, key, value])

    print_table("Configs", headers, rows)

def reset_config(args):
    force = args.force
    feature = args.feature

    try:
        if reset_config_service(feature, force):
            success("Config reset successful")

    except KeyError as e:
        error(e)


