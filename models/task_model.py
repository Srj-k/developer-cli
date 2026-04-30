
class Task:
    VALID_PRIORITIES = ["H", "M", "L"]
    VALID_STATUSES = ["Pending", "Ongoing", "Completed"]

    
    def __init__(self, id:int|None, name:str, description:str, priority:str, status:str, created_at):
        
        #Normalize data
        priority = priority.upper()
        status = status.capitalize()

        # Validate name
        if not name or not name.strip():
            raise ValueError("Task name cannot be empty")
        
        # Validate description
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty")
        
        # Validate priority
        if priority not in self.VALID_PRIORITIES:
            raise ValueError(f"Invalid priority '{priority}'. Use H, M, or L")

        # Validate status
        if status not in self.VALID_STATUSES:
            raise ValueError(f"Invalid status '{status}'. Use Pending, Ongoing, or Completed")
        
        self.id = id
        self.name = name.strip()
        self.description = description.strip()
        self.priority = priority
        self.status = status
        self.created_at = created_at


    def set_name(self, name:str):
        if not name or not name.strip():
            raise ValueError("Task name cannot be empty")
        else:
            self.name = name.strip()


    def set_description(self, description:str):
        description = description.strip()
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty")
        else:
            self.description = description.strip()


    def set_priority(self, priority:str):
        priority = priority.upper()
        if priority not in self.VALID_PRIORITIES:
            raise ValueError(f"Invalid priority '{priority}'. Use H, M, or L")
        else:
            self.priority = priority


    def set_status(self, status:str):
        status = status.capitalize()
         # Validate status
        if status not in self.VALID_STATUSES:
            raise ValueError(f"Invalid status '{status}'. Use Pending, Ongoing, or Completed")
        else:
            self.status = status


    #convert object to dict
    def to_dict(self):
        return {
            "id" : self.id,
            "name" : self.name, 
            "description" : self.description, 
            "priority" : self.priority, 
            "status" : self.status,
            "created_at" : self.created_at
        }


    #convert dict to object
    @classmethod
    def from_dict(cls, task_dict):
        try:
            id = task_dict["id"]
            name = task_dict["name"]
            description = task_dict["description"]
            priority = task_dict["priority"]
            status = task_dict["status"]
            created_at = task_dict["created_at"]
            return cls(id, name, description, priority, status, created_at)
        except KeyError as e:
            raise ValueError(f"Missing field: {e}")
        except Exception as e:
            raise ValueError(f"Invalid task data: {e}")