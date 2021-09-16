# Task Manager

*Definition:*
a Program that allows the user to create, store and track tasks.

## Goal

The goal of this capstone project is to make use of all the skills we have aquired during the first level
of the sofware enginering bootcamp.

## Use

**The program will run as admin and give the user several option.
When choosing an option from the menu the user will be asked for further information.**

* Register new user - Only admin will have the ability to add a new user.
  * New user     - **Input** a new username. **The program then checks if this username already exists.**
  * New password - **Input** a new password.
  * Verify       - **Input** the above password. **If the passwords do not match the user will be asked to enter them again.**
  
  *The new user will then be added to a text file containing all created users.*

* Add task          - Adding and storing as new task.
  * Task user   - **Input** the username of the person assigned to the task.
  * Title       - **Input** the title of the task.
  * Description - **Input** the description of the task.
  * Due date    - **Input** the due date of the task.
  
  *The task will then be added to a text file.*

* View all          - View all stored tasks.
  * Here the program reads from the text file containing all the tasks and prints them out in an easy to read manner for the user to understand.

* View my           - View all tasks assigned to logged in user.
  * Task - **Input** the number of the task you would like to edit.
    * Edit      - The user has the option to edit the task.
    * Complete  - The user has the option to mark the task as complete.

* Generate report   - Generates a report with all information concerning various aspects of all stored tasks.
  * The program reads from the text files containing the users and the tasks.
  * Certain information is gathered and written to two new text files namely.
  
    * Task overview  
      * Number of completed tasks.
      * Number of uncompleted tasks.
      * Percentage of tasks completed.
      * Percentage of tasks uncompleted.
    * User overview  
      * The amount of tasks for the current logged in user.
      * Percentage of tasks for the current logged in user.
      * Percentage of completed tasks for logged in user.
      * Percentage of uncompleted task for logged in user.

* View stats        - Only admin will have the ability to view the statistics of the tasks.
  * Task ammount  - Displays the total ammount of tasks.
  * User amount   - Displays the total amount of users.

* Exit              - Stops running the program.
