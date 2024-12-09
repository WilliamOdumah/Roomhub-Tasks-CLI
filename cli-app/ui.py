from tasks import fetch_tasks, create_task, toggle_completion, user_has_room, BASE_URL
import requests

class TaskCLI:
    def __init__(self, email):
        self.email = email
        self.room_name = None
        self.tasks = {"pending": [], "completed": []}  # Store tasks locally

    def check_user_room(self):
        """Ensure the user has a room before allowing task access."""
        has_room, room_name = user_has_room(self.email)
        if not has_room:
            print(
                f"You don't have a room associated with this email, so you can't use task features. "
                f"Use the test email 'odumahw@myumanitoba.ca' to test this feature with an existing room."
            )
            return False
        self.room_name = room_name
        print(f"Welcome! Your room name is '{self.room_name}'. You can now manage tasks.")
        return True

    def main_menu(self):
        """Display the main menu."""
        if not self.check_user_room():
            return  # Exit if the user doesn't have a room

        while True:
            print("\n--- Task Manager CLI ---")
            print("1. View Tasks")
            print("2. Create Task")
            print("3. Mark Task as Completed")
            print("4. Exit")
            choice = input("Enter your choice: ")
            try:
                if choice == "1":
                    self.view_tasks()
                elif choice == "2":
                    self.create_task_ui()
                elif choice == "3":
                    self.mark_task_completed_ui()
                elif choice == "4":
                    print("Exiting Task Manager CLI. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except RuntimeError as e:
                print(e)

    def view_tasks(self):
        """Fetch and display tasks."""
        self.tasks = fetch_tasks(self.email)
        print("\nPending Tasks:")
        if self.tasks["pending"]:
            for i, task in enumerate(self.tasks["pending"], start=1):
                print(f"{i}. {task['task_description']} (Due: {task['due_date']})")
        else:
            print("No pending tasks.")

        print("\nCompleted Tasks:")
        if self.tasks["completed"]:
            for i, task in enumerate(self.tasks["completed"], start=1):
                print(f"{i}. {task['task_description']}")
        else:
            print("No completed tasks.")

    def mark_task_completed_ui(self):
        """Mark a task as completed."""
        if not self.tasks["pending"]:
            print("\nNo pending tasks to complete.")
            return

        print("\nPending Tasks:")
        for i, task in enumerate(self.tasks["pending"], start=1):
            print(f"{i}. {task['task_description']} (Due: {task['due_date']})")

        try:
            choice = int(input("\nSelect a task number to mark as completed: "))
            if 1 <= choice <= len(self.tasks["pending"]):
                task = self.tasks["pending"][choice - 1]
                toggle_completion(self.email, task["task_id"])
                print(f"Task '{task['task_description']}' marked as completed.")
            else:
                print("Invalid task number. Please try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid task number.")

    # def create_task_ui(self):
    #     """Create a new task."""
    #     print("\n--- Create New Task ---")
    #     task_name = input("Task Name: ")
    #     assignee = input("Assignee Email: ")
    #     due_date = input("Due Date (YYYY-MM-DD): ")
    #     create_task(self.email, task_name, assignee, due_date)
    #     print(f"Task '{task_name}' assigned to {assignee}.")
        
    def create_task_ui(self):
        """Create a new task."""
        print("\n--- Create New Task ---")
        try:
            # Fetch roommates
            response = requests.get(f"{BASE_URL}/user/{self.email}/get-user-roommates")
            if response.status_code == 200 and response.json().get("all_roommates"):
                all_roommates = response.json()["all_roommates"]
                roommates = [roommate[0] for roommate in all_roommates]  # Extract roommate emails

                # Display list of roommates
                print("\nAvailable Roommates:")
                for email in roommates:
                    print(f"- {email}")

                # Get task details
                task_name = input("\nTask Name: ")
                assignee = input("Enter the email of the assignee: ").strip()
                due_date = input("Due Date (YYYY-MM-DD): ")

                if assignee in roommates:
                    # Create the task
                    create_task(self.email, task_name, assignee, due_date)
                    print(f"Task '{task_name}' assigned to {assignee}.")
                else:
                    print(f"Error: The provided email '{assignee}' is not in your room.")
                    print("Here are the emails of users you can assign tasks to:")
                    for email in roommates:
                        print(f"- {email}")
            else:
                print("You don't have any roommates in your room.")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching roommates: {e}")
        except RuntimeError as e:
            if "403" in str(e):
                print("Error: Cannot assign a task. Assignee is not in the room or does not exist.")
            else:
                print(e)
        except ValueError:
            print("Invalid input. Please enter the details again.")



if __name__ == "__main__":
    email = input("Enter your email: ")
    cli = TaskCLI(email)
    cli.main_menu()
