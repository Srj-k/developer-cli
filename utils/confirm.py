from .custom_print import warning, info, error


YES_OPTIONS = ["y", "yes", "1"]
NO_OPTIONS = ["n", "no", "0"]
QUIT_OPTIONS = ["q", "quit"]


def validate_options(value):
    cleaned_value = value.strip().lower()

    if cleaned_value in YES_OPTIONS:
        return True

    if cleaned_value in NO_OPTIONS:
        return False

    if cleaned_value in QUIT_OPTIONS:
        return None

    return "invalid"


def confirm_action(force=False):
    if force:
        return True

    warning("Are you sure you want to perform this action? [Y/N]")
    info("Enter Q to quit")

    while True:
        confirm_flag = input("> ").strip().lower()

        result = validate_options(confirm_flag)

        if result is True:
            return True

        if result is False:
            return False

        if result is None:
            return False

        error("Invalid choice. Please enter Y/N or Q to quit.")