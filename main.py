import argparse
from commands.config import set_config, get_config, remove_config, reset_config, view_config
from commands.organise import organise
from commands.rename import rename
from commands.task import add_task, remove_task, edit_task, view_task, sort_task
from commands.search import search
from commands.shortcut import add_shortcut, remove_shortcut, view_shortcut, run_shortcut

parser = argparse.ArgumentParser(description="Developer Productivity CLI", usage="devcli <command> [options]")

subparsers = parser.add_subparsers(title="Commands", metavar="<command>")


organise_parser = subparsers.add_parser("organize",help="organize files", description="organize files")
organise_parser.set_defaults(func=organise)

rename_parser = subparsers.add_parser("rename",help="rename files", description="rename files")
rename_parser.set_defaults(func=rename)



#Task Parser
task_parser = subparsers.add_parser("task",help="manage tasks", description="Manage tasks from the command line", usage="devcli task <command> [options]")
task_actions_parser = task_parser.add_subparsers(title="Commands", metavar="<command>")

task_add_parser = task_actions_parser.add_parser("add", help="add a new task") # Add task
task_add_parser.set_defaults(func=add_task)

task_view_parser = task_actions_parser.add_parser("view", help="view tasks") # View task
task_view_parser.set_defaults(func=view_task)

task_remove_parser = task_actions_parser.add_parser("remove", help="remove a task") # Remove task
task_remove_parser.set_defaults(func=remove_task)

task_edit_parser = task_actions_parser.add_parser("edit", help="edit a task") # Edit task
task_edit_parser.set_defaults(func=edit_task)

task_sort_parser = task_actions_parser.add_parser("sort", help="sort tasks") # Sort task
task_sort_parser.set_defaults(func=sort_task)



#Search Parser
search_parser = subparsers.add_parser("search")
search_parser.set_defaults(func=search)



#Config Parser
config_parser = subparsers.add_parser("config", help="manage config", description="Manage CLI configuration and defaults", usage="devcli config <command> [options]")
config_actions_parser = config_parser.add_subparsers(title="Commands", metavar="<command>")

config_set_parser = config_actions_parser.add_parser("set", help="set a configuration value") # Set config
config_set_parser.set_defaults(func=set_config)

config_get_parser = config_actions_parser.add_parser("get", help="get a configuration value") # Get config
config_get_parser.set_defaults(func=get_config)

config_remove_parser = config_actions_parser.add_parser("remove", help="remove a configuration") # Remove config
config_remove_parser.set_defaults(func=remove_config)

config_reset_parser = config_actions_parser.add_parser("reset", help="reset configuration") # Reset config
config_reset_parser.set_defaults(func=reset_config)

config_view_parser = config_actions_parser.add_parser("view", help="view all configurations") # View config
config_view_parser.set_defaults(func=view_config)



#Shortcut parser
shortcut_parser = subparsers.add_parser("shortcut", help="manage shortcuts", description="Create and run command shortcuts", usage="devcli shortcut <command> [options]")
shortcut_actions_parser = shortcut_parser.add_subparsers(title="Commands", metavar="<command>")

shortcut_add_parser = shortcut_actions_parser.add_parser("add", help="add a shortcut") # Add shortcut
shortcut_add_parser.set_defaults(func=add_shortcut)

shortcut_remove_parser = shortcut_actions_parser.add_parser("remove", help="remove a shortcut") # Remove shortcut
shortcut_remove_parser.set_defaults(func=remove_shortcut)

shortcut_view_parser = shortcut_actions_parser.add_parser("view", help="view shortcuts") # View shortcut
shortcut_view_parser.set_defaults(func=view_shortcut)

shortcut_run_parser = shortcut_actions_parser.add_parser("run", help="run a shortcut") # Run shortcut
shortcut_run_parser.set_defaults(func=run_shortcut)



args = parser.parse_args()


if hasattr(args,"func"):
    args.func()
else :
    parser.print_help()