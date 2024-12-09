# Task Manager CLI

This is a command-line interface (CLI) application for managing tasks. The application is designed to replicate a key feature from our main project in a desktop CLI format. The feature implemented here is **task management**, including creating tasks, viewing tasks, and marking tasks as completed.

---

## Features
- View pending and completed tasks.
- Create a new task and assign it to a roommate.
- Mark pending tasks as completed.
- Error handling for invalid inputs and user permissions.

The CLI interacts with the remote backend API to perform these operations, touching all 3 tiers of the application:
1. **UI:** This CLI acts as the user interface.
2. **Logic:** Task creation, retrieval, and updates are handled via API calls.
3. **Database:** The backend API communicates with the database to store and retrieve task data.

---

## Setup and Requirements

### **Prerequisites**
- Python installed on your system.
- Internet access to connect to the backend API.

### **Steps to Run**
1. **Navigate into the folder**
   ```bash
   cd cli-app
   ```
   
2. **Run the CLI**
   ```bash
   python ui.py
   ```

3. **Provide an Email**
    - When prompted, enter the email: odumahw@myumanitoba.ca to access task management features.
    - This email is associated with an existing room in the system. You won't be able to create tasks or use features if you provide an email without a room.

## Link to Re-implemented Feature  

The original feature that has been re-implemented in this CLI can be found in the repository at the following link:  

[Task Management Feature in the Main Roomhub Repository](https://github.com/WilliamOdumah/RoomHub/blob/main/Frontend/src/pages/ManageTasksPage.js)


## API Integration

The CLI interacts with the backend API for all operations. The following endpoints are used:


### Fetch Tasks
- **Pending Tasks**: `/room/get-pending-tasks`
- **Completed Tasks**: `/room/get-completed-tasks`

### Create Task
- **Endpoint**: `/task/create-task`

### Mark Task as Completed
- **Endpoint**: `/task/mark-completed`

### Check Room Status
- **Endpoint**: `/user/{email}/get-room`

### Get Roommates
- **Endpoint**: `/user/{email}/get-user-roommates`



## Reflection

### Why did using distributed/n-tier make this straightforward to add the interface?

The backend API's clear separation of concerns allowed the CLI to focus solely on the user interface without dealing with business logic or database operations. This separation enabled quick and efficient integration.

### Did this code base actually adhere to n-tier?

Yes, the code adheres to n-tier principles. The backend exposed endpoints for all necessary operations, and no direct database operations were performed in the CLI.

### Was the documentation in the project accurate and understandable?

The API documentation was sufficient to understand how to use the endpoints. It included clear details on expected inputs and outputs, making it straightforward to integrate.

### Did you have to change code outside of the UI layer?

No changes were made outside the UI layer. The CLI relied entirely on the backend API to handle business logic and data storage.

___

### UNIVERSITY OF MANITOBA  
**Faculty of Science**  
**Department of Computer Science**  

## Honesty Declaration for Individual Work  

I, the undersigned, declare that the attached assignment is wholly the product of my own work, and that no part of it has been:  
- copied by manual or electronic means from any work produced by any other person(s), present or past, including tutors or tutoring services,  
- based on laboratory work that I did not complete due to unexcused absence(s),  
- produced by several students working together as a team (this includes one person who provides any portion of an assignment to another student or students),  
- copied from any other source including textbooks and websites, or  
- modified to contain falsified data, except as directly authorized by the Instructor.  

I understand that penalties for submitting work which is not wholly my own, or distributing my work to other students, is considered an act of **Academic Dishonesty** and is subject to penalty as described by the University of Manitoba's Student Discipline Bylaw*.  

---

### Please PRINT all information:  

**Course**: COMP4350  
**Section**: A01  
**Last Name, First Name**: Odumah, William  
**Student Number**:  7905401
**UM Email**:  odumahw@myumanitoba.ca
**Date**:  2024/12/08

---

Penalties that may apply, as provided for under the University of Manitoba's **Student Discipline By-Law**, range from a grade of zero for the assignment, failure in the course to expulsion from the University. The Student Discipline By-Law may be accessed at:  
[University of Manitoba - Student Discipline By-Law](http://umanitoba.ca/admin/governance/governing_documents/students/868.htm)
