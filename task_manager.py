# defining a function to view all the current users tasks.

def view_mine(person):
    task_file1 = open("tasks.txt", "r+")
    task_num = 0
    task_num2 = 0

    # Using a for loop to read through the text file.

    for i in task_file1:
        user1, task, desc, due, comp = i.split(", ")

        # Using an if statement to print all the current users tasks

        if person == user1:
            task_num += 1
            print(f"""
Task number:        :   {task_num}            
User responsible    :   {user1}
Task category       :   {task}
Task information    :   {desc}
Time of completion  :   {due}
Task completion     :   {comp}
        """)
    task_file1.seek(0)

    # Asking user to select a specific task using a for loop,

    specific_task = int(input("Please select a specific task by entering its task number: "))
    for i in task_file1:
        user1, task, desc, due, comp = i.split(", ")

        # Using an if statement to print that users specific task.

        if person == user1:
            task_num2 += 1
            if specific_task == task_num2:
                print(f"""
Task number:        :   {task_num2}            
User responsible    :   {user1}
Task category       :   {task}
Task information    :   {desc}
Time of completion  :   {due}
Task completion     :   {comp}
                        """)

    user_choice = input("""
To mark current task as complete enter c:
TO edit current task enter e: 
: """)
    task_file1.close()

    if user_choice == "c":

        new_file = open("tasks.txt", "r")
        new_string = ""
        count = 0

        for i in new_file:
            user3, user_task, title_task, due_task, comp_task = i.strip().split(", ")
            if person == user3:
                count += 1

            if specific_task != count:
                new_string = new_string + f"{user3}, {user_task}, {title_task}, {due_task}, {comp_task}\n"

            elif specific_task == count:
                new_string = new_string + f"{user3}, {user_task}, {title_task}, {due_task}, Yes\n"

        new_file.seek(0)
        new_file.close()

        new_file = open("tasks.txt", "w")
        new_file.write(new_string)
        new_file.seek(0)
        new_file.close()

    elif user_choice == "e":
        user_choice_edit = input("""
Please select one of the following.
To edit user assigned to this task  - u
To edit the due date of this task   - d
        """)

        if user_choice_edit == "u":

            replace_user = input("Please enter the new user: ")
            new_file = open("tasks.txt", "r")
            new_string = ""
            count = 0

            for i in new_file:
                user3, user_task, title_task, due_task, comp_task = i.strip().split(", ")
                if person == user3:
                    count += 1

                if specific_task != count:
                    new_string = new_string + f"{user3}, {user_task}, {title_task}, {due_task}, {comp_task}\n"

                elif specific_task == count:
                    new_string = new_string + f"{replace_user}, {user_task}, {title_task}, {due_task}, {comp_task}\n"

            new_file.seek(0)
            new_file.close()

            new_file = open("tasks.txt", "w")
            new_file.write(new_string)
            new_file.seek(0)
            new_file.close()

        elif user_choice_edit == "d":

            replace_date = input("Please enter the new due date: ")
            new_file = open("tasks.txt", "r")
            new_string = ""
            count = 0

            for i in new_file:
                user3, user_task, title_task, due_task, comp_task = i.strip().split(", ")
                if person == user3:
                    count += 1

                if specific_task != count:
                    new_string = new_string + f"{user3}, {user_task}, {title_task}, {due_task}, {comp_task}\n"

                elif specific_task == count:
                    new_string = new_string + f"{user3}, {user_task}, {title_task}, {replace_date}, {comp_task}\n"

            new_file.seek(0)
            new_file.close()

            new_file = open("tasks.txt", "w")
            new_file.write(new_string)
            new_file.seek(0)
            new_file.close()


# Defining a function to view all tasks.

def view_all():
    task_file1 = open("tasks.txt", "r+")

    # Using a for loop to print out all the tasks.

    for i in task_file1:
        user1, task, desc, due, comp = i.split(", ")
        print(f"""
User responsible    :   {user1}
Task category       :   {task}
Task information    :   {desc}
Time of completion  :   {due}
Task completion     :   {comp}
        """)
    task_file1.seek(0)  # Returning to the start of the text file.
    task_file1.close()  # Closing the text file.


# Defining a function to add a new task to text file.

def add_task():
    task_file1 = open("tasks.txt", "a+")

# Asking the user for input.

    task_user = input("Please enter username who is assigned to this task: ")
    task_title = input("Please enter the title of this task: ")
    task_des = input("Please describe the task: ")
    task_due = input("Please enter the due date for this task: ")
    task_comp = "No"

    # Writing that input to the appropriate text file.

    task_file1.write(f"{task_user}, {task_title}, {task_des}, {task_due}, {task_comp}\n")
    task_file1.seek(0)
    task_file1.close()


# Defining a function to register a new user.

def reg_user():
    new_user = ""
    pass_check = False
    user_check = False
    text1 = open("user.txt", "r+")
    text2 = open("user.txt", "a+")

    # Using a while loop to se if the user already exists.

    while not user_check:
        new_user = input("Please enter a new username: ")
        for i in text1:
            a, b = i.strip().split(", ")
            if new_user != a:
                user_check = True

            elif new_user == a:
                user_check = False
                print("This user already exists. Try entering a different username.")
        text1.seek(0)
    text1.close()

    # Using a while loop to verify the new user password.

    while not pass_check:
        new_pass = input("Please enter your new password: ")
        verify_pass = input("Please verify your new password: ")
        if new_pass == verify_pass:
            pass_check = True
            text2.write(f"\n{new_user}, {new_pass}")    # Adding new user if both while loop are broken.
            text2.seek(0)
            text2.close()

        elif new_pass != verify_pass:
            pass_check = False
            print("Your passwords dit not match, please re-enter details.")


user_file = open("user.txt", "r+")
user_loop = False
user = ""

# Using a while loop to see if user exists and login the user in.

while not user_loop:
    user = input("Please enter your username: ")
    password = input("Please enter your password: ")

    for line in user_file:
        line = line.strip()
        line_user, line_pass = line.split(", ")

        if user == line_user and password == line_pass:
            user_loop = True

        elif user == line_user and password != line_pass:
            user_loop = False
            print("Incorrect password, please re-enter you details.")

        elif user != line_user and password == line_pass:
            user_loop = False
            print("Incorrect username, please re-enter your details.")

    user_file.seek(0)

user_file.close()

# Using a while loop to check which menu the user should use.

main_loop = False
while not main_loop:

    if user == "admin":
        main_menu = input(f"""
Please select one of the following options:
r   -   register user
a   -   add task
va  -   view all tasks
vm  -   view my tasks
gr  -   generate reports
vs  -   view stats
e   -   exit
        """)

    else:
        main_menu = input(f"""
Please select one of the following options:
r   -   register user
a   -   add task
va  -   view all tasks
vm  -   view my tasks
e   -   exit
        """)

    # Using if and elif statements to call functions based on user input.

    if main_menu == "r" and user == "admin":
        main_loop = True
        reg_user()

    elif main_menu == "r" and user != "admin":
        print("Only admin has permission to add a new user: ")
        main_loop = False

    elif main_menu == "a":
        main_loop = True
        add_task()

    elif main_menu == "va":
        view_all()

    elif main_menu == "vm":
        view_mine(user)

    # Using an elif statement to generate 2 reports to text files.

    elif main_menu == "gr":

        # Defining variables to use.

        user_amount = 0
        user_task_completed = 0
        user_task_uncompleted = 0
        user_task_amount = 0
        task_amount = 0
        com_tasks = 0
        uncompleted_tasks = 0

        # Opening 2 text files in read and opening 2 text files in write.

        task_over = open("task_overview.txt", "w")
        task_file = open("tasks.txt", "r")
        user_over = open("user_overview.txt", "w")
        user_file = open("user.txt", "r")

        # Using a for loop and statements to change the value of the defined variables if conditions are met.

        for line in task_file:
            user2, task1, desc1, due1, comp1 = line.strip().split(", ")
            task_amount += 1
            if comp1 == "No":
                uncompleted_tasks += 1

            elif user2 == user:
                user_task_amount += 1

            elif user == user2 and comp1 == "No":
                user_task_uncompleted += 1

            elif user == user2 and comp1 != "No":
                user_task_completed += 1

            elif comp1 == "Yes":
                com_tasks += 1

        for line in user_file:
            c, d = line.strip().split(", ")
            user_amount += 1

        # Writing the information gathered from my variables to my 2 new text files.

        task_over.write(f"""Number of tasks             -   {task_amount}
        Number of completed tasks   -   {com_tasks}
        Number of uncompleted tasks -   {uncompleted_tasks}
        % of tasks completed        -   {(com_tasks * 100) / task_amount}
        % of tasks uncompleted      -   {(uncompleted_tasks * 100) / task_amount}       
                """)

        user_over.write(f"""Number of users                 -   {user_amount}
        Current user task amount        -   {user_task_amount}
        % Current user tasks            -   {(user_task_amount * 100) / task_amount}
        % Current user task uncompleted -   {(user_task_uncompleted * 100) / user_task_amount}
        % Current user task completed   -   {(user_task_completed * 100) / user_task_amount}
        """)

        # Seeking 0 and closing all the files I have been using

        task_file.seek(0)
        task_file.close()
        user_file.seek(0)
        user_file.close()
        task_over.seek(0)
        task_over.close()
        user_over.seek(0)
        user_over.close()

    # With the elif statement the programs gives the user statistical data.

    elif main_menu == "vs":
        user_file = open("user.txt", "r+")
        user_taskFile = open("tasks.txt", "r+")
        task_count = 0
        user_count = 0

        # While using for loop the program counts the amount of users and tasks.

        for line in user_file:
            user_count += 1

        for line in user_taskFile:
            task_count += 1

        print(f"""
    Task amount :   {task_count} 
    User amount :   {user_count}
    """)

        # Returning all file index to 0 and closing all text files.

        user_taskFile.seek(0)
        user_file.seek(0)
        user_file.close()
        user_taskFile.close()
