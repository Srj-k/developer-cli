from services.task_service import add_task_service, view_task_service, remove_task_service, edit_task_service, sort_task_service
from utils.custom_print import success, error, warning
from utils.table import print_table, print_detail
from utils.helper import format_datetime

def add_task(args):
    try:
        task_id = add_task_service(
            name=args.task_name, 
            description=args.task_description, 
            priority=args.priority, 
            status=args.status
        )

        success(f"Task '{args.task_name}' added successfully with ID {task_id}")
    
    except ValueError as e:
        error(f"Error: {e}")
    except IOError:
        error("Failed to save task")

    except Exception:
        error("Unexpected error while creating task")


def view_task(args):
    try:
        data = view_task_service(args.task_id)

    except ValueError:
        error("Data file is corrupted. Please reset.")
        return
    
    except IOError:
        error("Unable to read task file.")
        return
    
    if data is None:
        error(f"No task found with id {args.task_id}")
        return

    if len(data) == 0:
        warning("No tasks found")
        return

    if args.task_id is not None:
        task = data[0]

        task_dict = {
            "Id" : task.id,
            "Name" : task.name,
            "Description" : task.description,
            "Priority" : task.priority,
            "Status" : task.status,
            "Created at" : format_datetime(task.created_at)
        }

        print_detail("Task info", task_dict)
        return

    rows = []
    header = ["Id", "Name", "Priority", "Status", "Created at"]
    
    for task in data:
        rows.append([
            task.id, 
            task.name, 
            task.priority, 
            task.status, 
            format_datetime(task.created_at)
        ])

    print_table("Tasks", header, rows)


def remove_task(args):
    try:
        result = remove_task_service(args.id)

    except ValueError:
        error("Data file is corrupted.")
        return

    except IOError:
        error("Failed to update task file.")
        return

    if result:
        success(f"Task with id {args.id} removed successfully")
    else:
        error(f"No task found with id {args.id}")


def edit_task(args):
    try:
        result = edit_task_service(
            args.id,
            args.name,
            args.description,
            args.priority,
            args.status
        )
        if result is None:
            error(f"No task found with id {args.id}")
        else:
            success(f"Task with id {args.id} updated successfully")
    
    except ValueError as e:
        error(f"{e}")

    except IOError:
        error("Failed to read/write task file")

    except Exception as e:
        error(f"Unexpected error: {e}")


def sort_task(args):
    try:
        tasks = sort_task_service(args.sort_by)

        if not tasks:
            warning("No tasks found")
            return

        rows = []
        header = ["Id", "Name", "Priority", "Status", "Created at"]

        for task in tasks:
            rows.append([
                task.id,
                task.name,
                task.priority,
                task.status,
                format_datetime(task.created_at)
            ])

        print_table("Sorted Tasks", header, rows)

    except ValueError as e:
        error(str(e))

    except Exception as e:
        error(f"Unexpected error: {e}")