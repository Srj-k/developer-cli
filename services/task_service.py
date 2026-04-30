import config.paths as file_path
from storage.file_handler import load_json, save_json
from models.task_model import Task
from utils.helper import get_current_timestamp
from datetime import datetime


# Add task function
def add_task_service(name, description, priority, status):

    tasks = []
    data = load_json(file_path.TASK_FILE)
    created_at = get_current_timestamp()
    
    # Convert dict to objects
    for task in data:
        try:
            task_obj = Task.from_dict(task)
            tasks.append(task_obj)
        except Exception:
            continue 

    # Generate ID
    task_id = generate_next_id(tasks)

    new_task = Task(task_id, name, description, priority, status, created_at)
    tasks.append(new_task)
        
    tasks_dict = [task.to_dict() for task in tasks]

    save_json(tasks_dict, file_path.TASK_FILE)

    return task_id


# View task function
def view_task_service(task_id):
    data = load_json(file_path.TASK_FILE)
    tasks = []
    # convert task into objects
    for task in data:
        try:
            task_obj = Task.from_dict(task)
            tasks.append(task_obj)
        except Exception:
            continue 

    if task_id != None:
        for task in tasks:
            if task.id == task_id:
                return [task] # task with given id 

        return None # invalid id
    else:
        return sort_tasks(tasks, "created_at")
    

# Remove task function 
def remove_task_service(task_id):
    data = load_json(file_path.TASK_FILE)

    if task_id is None:
        return None

    filtered_tasks = []

    for task in data:
        try:
            if int(task.get("id")) != task_id:
                filtered_tasks.append(task)
        except (ValueError, TypeError, AttributeError):
            continue

    if len(data) == len(filtered_tasks):
        return None

    save_json(filtered_tasks, file_path.TASK_FILE)
    return True


# Edit task details
def edit_task_service(id, name=None, description=None, priority=None, status=None):
    
    if all(v is None for v in [name, description, priority, status]):
        raise ValueError("No fileds to update")
    
    
    data = load_json(file_path.TASK_FILE)
    tasks = []

    # convert task into objects
    for task in data:
        try:
            task_obj = Task.from_dict(task)
            tasks.append(task_obj)
        except Exception:
            continue 
    
    found = False
    for task in tasks:
        if task.id == id:
            found = True

            if name is not None: 
                task.set_name(name)
            if description is not None: 
                task.set_description(description)
            if priority is not None: 
                task.set_priority(priority)
            if status is not None: 
                task.set_status(status)

    if not found:
        return None
    
    task_dicts = [task.to_dict() for task in tasks]

    save_json(task_dicts,file_path.TASK_FILE)
    return True


# Sort task function
def sort_task_service(field):
    data = load_json(file_path.TASK_FILE)
    tasks = []

    # Convert dict → Task objects
    for task in data:
        try:
            task_obj = Task.from_dict(task)
            tasks.append(task_obj)
        except Exception:
            continue

    # Sort tasks
    sorted_tasks = sort_tasks(tasks, field)

    return sorted_tasks


# Generate next id for adding task
def generate_next_id(data):
    max_id = 0

    for task in data:
        try:
            task_id = int(task.id)            
            max_id = max(task_id, max_id)
        except (ValueError, TypeError):
            continue

    return max_id + 1


# Sorting function

def sort_tasks(tasks, field):
    VALID_FIELDS = ["name", "status", "created_at", "priority"]

    if field not in VALID_FIELDS:
        raise ValueError(f"Invalid sort field '{field}'")

    # Priority custom order
    if field == "priority":
        priority_order = {"H": 1, "M": 2, "L": 3}
        return sorted(tasks, key=lambda task: priority_order.get(task.priority, 99))

    # Datetime sorting
    elif field == "created_at":
        return sorted(
            tasks,
            key=lambda task: datetime.fromisoformat(task.created_at),
            reverse=True
        )

    # Default sorting (name, description, status)
    else:
        return sorted(tasks, key=lambda task: getattr(task, field).lower())
