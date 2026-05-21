import re
import argparse
from utils.custom_print import error

def validate_key(key):
    cleaned_key = key.lower().strip()
    expr = r'^[a-z]+\.[a-z_]+$'

    if not re.match(expr, cleaned_key):
        raise argparse.ArgumentTypeError (
            error(f"'{key}' is invalid. Key must be in 'feature.key' format.")
        )
    
    return cleaned_key

def validate_feature(feature):
    cleaned_feature = feature.lower().strip()

    if cleaned_feature in ["organize", "rename", "task", "search"]:
        return cleaned_feature
    else:
        raise argparse.ArgumentTypeError (
            error(f"'{feature}' is an invalid feature.")
        )

def validate_status(value):
    if value.title() in ["Pending", "Ongoing", "Completed"]:
        return value.title()
    return None

def validate_priority(value):
    if value.upper() in ["H", "M", "L"]:
        return value.upper()
    return None

def validate_boolean(value):
    if value.title() in ["True", "1"]:
        return True
    elif value.title() in ["False", "0"]:
        return False
    return None

def validate_positive_int(value):
    try:
        converted_value = int(value)
        if converted_value > 0: 
            return converted_value
        return None
    except ValueError:
        return None
    
def validate_task_fields(value):
    if value.lower() in ["name","status","created at","priority"]:
        return value.lower()
    return None

def validate_extension(value):
    cleaned_value = value.strip().lower().removeprefix(".")
    ext_expression = r'^[a-z0-9]+(\.[a-z0-9]+)*$'
    x = re.match(ext_expression,cleaned_value)
    if x:
        return cleaned_value
    
    return None

VALID_CONFIGS = {
        "organize" : {
            "by_type" : validate_boolean,
            "by_extension" : validate_boolean,
            "force" : validate_boolean
        },
        "rename" : {
            "auto_number" : validate_boolean,
            "uppercase" : validate_boolean,
            "force" : validate_boolean
        },
        "task" : {
            "priority" : validate_priority,
            "status" : validate_status,
            "by" : validate_task_fields,
            "desc" : validate_boolean
        },
        "search" : {
            "ext" : validate_extension,
            "min_size" : validate_positive_int,
            "max_size" : validate_positive_int,
            "priority" : validate_priority,
            "status" : validate_status,
            "recursive" : validate_boolean,
            "limit" : validate_positive_int
        }
}

def validate_config(feature, property, value):

    if feature in VALID_CONFIGS:
        pair = VALID_CONFIGS[feature]

        if property in pair:
            validation_function = pair[property]
            validated_value = validation_function(value)
            if validated_value is not None:
                return validated_value
    
        return None



