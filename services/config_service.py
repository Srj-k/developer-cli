from validators.config_validators import validate_config
from storage.file_handler import load_json, save_json
from config import settings
from utils.confirm import confirm_action

def set_config_service(feature, config_key, value):
    validated_value = validate_config(feature, config_key, value)

    if validated_value is None:
        return None
    
    configs = load_json(settings.CONFIG_FILE,default={})

    if feature in configs:
        configs[feature][config_key] = validated_value
    else:
        configs[feature] = {}
        configs[feature][config_key] = value

    save_json(configs,settings.CONFIG_FILE)

    return True

def view_config_service():

    configs = load_json(settings.CONFIG_FILE, default={})

    return configs

def get_config_service(feature, config_key):
    configs = load_json(settings.CONFIG_FILE, default={})

    if configs:
        try:
            result = configs[feature][config_key]
            return {"feature" : feature, "config_key" : config_key, "value" : result}
        except KeyError:
            return None

    return None

def remove_config_service(feature, config_key):

    configs = load_json(settings.CONFIG_FILE, default={})

    if configs:
        try:
            del configs[feature][config_key]
            save_json(configs,settings.CONFIG_FILE)
            return True
        except KeyError:
            raise KeyError("No such key exists")

    return None

def reset_config_service(feature, force):
    if confirm_action(force):
        configs = load_json(settings.CONFIG_FILE, default={})

        if configs:
            try:
                del configs[feature]
                return True
            except KeyError:
                raise KeyError("This feature is not set yet")
            
    return None        
