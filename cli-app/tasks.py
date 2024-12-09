import requests

BASE_URL = "https://7hm4udd9s2.execute-api.ca-central-1.amazonaws.com/dev"

def fetch_tasks(email):
    """Fetch pending and completed tasks."""
    try:
        pending = requests.get(f"{BASE_URL}/room/get-pending-tasks", params={"frm": email}).json().get("pending_tasks", [])
        completed = requests.get(f"{BASE_URL}/room/get-completed-tasks", params={"frm": email}).json().get("completed_tasks", [])
        return {"pending": pending, "completed": completed}
    except Exception as e:
        raise RuntimeError(f"Error fetching tasks: {e}")
    
def user_has_room(email):
    """
    Check if the user is associated with a room.

    Args:
        email (str): The user's email address.

    Returns:
        (bool, str): A tuple indicating whether the user has a room and the room name.
    """
    try:
        response = requests.get(f"{BASE_URL}/user/{email}/get-room")
        if response.status_code == 200 and response.json().get("room_name") != "NA":
            return True, response.json()["room_name"]
        return False, None
    except Exception as e:
        raise RuntimeError(f"Error checking room association: {e}")

def create_task(email, task_name, assignee, due_date):
    """Create a new task."""
    try:
        response = requests.post(
            f"{BASE_URL}/task/create-task",
            json={"tn": task_name, "frm": email, "to": assignee, "date": due_date},
        )
        response.raise_for_status()
    except Exception as e:
        raise RuntimeError(f"Error creating task: {e}")
    

def toggle_completion(email, task_id):
    """Mark a task as completed."""
    try:
        response = requests.patch(
            f"{BASE_URL}/task/mark-completed",
            json={"id": task_id, "frm": email},
        )
        response.raise_for_status()
    except Exception as e:
        raise RuntimeError(f"Error marking task as completed: {e}")
