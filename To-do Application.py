#Build a command line interface that welcomes users and displays a menu with options to add, view, delete tasks, or quit application
#Tasks should be stored in a python list
#Core Features
#Add Tasks
#View Tasks
#Delete Tasks
#Quit the Application

def int_input (prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a number")

def view_tasks (task_list):
   if not task_list:
    print ("List is empty")
    print ("------------------")
   else:
        print("Your to-do list")
        print ("-----------------")        
        for item in task_list:
            print (f"{item}")
        print ("------------------")
   
        

def add_tasks (task_list):
    item = input("Enter the task you want to add. ")
    task_list.append(item)
    print (f"{item} add to the To-Do List.")
    

def del_tasks(task_list):
    if not task_list:
        print ("Your task list is empty.") 
        return
   
    item = input("Enter the task you want to add. ")
    if item in task_list:
        task_list.remove(item)
        print (f"{item} has been removed. ")
    else:
        print("Invalid item.")
        

def main():
    task_list = []
    
    print (f"Welcome to the To-Do Application. ")
    print ("------------------------------------")

    while True:
            print (f"1. Add Tasks")
            print (f"2. View Tasks")
            print (f"3. Delete Tasks")
            print (f"4. Quit the application")
            num = int_input ("Select the number from the menu \n ")


            if num == 1:
                add_tasks (task_list)
    
            elif num == 2:
                view_tasks (task_list)
            
            elif num == 3:
                del_tasks (task_list)
            
            elif num == 4:
                print("Goodbye")
                break
            
            else:
                print ("Invalid input")
            
main()



