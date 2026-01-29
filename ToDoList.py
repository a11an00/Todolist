task_list = []
def show_tasks():
  if len(task_list)==0:
    print("no tasks available")
  else:
    for task in task_list:
      print(task)

def add_task():
  user_input=input("enter task: ")
  new_task={ "description": user_input, "completed": False }
  task_list.append(new_task)
  print("task added successfully")

def complete_task():
    show_tasks()
    task_number=int(input("enter task number to complete: "))-1
    if task_number>0 and task_number<len(task_list):
        task_list[task_number]["completed"]=True
        print("task marked as completed")
    elif task_number==0 :
        task_list[task_number]["completed"]=True
        print("task marked as completed")
    else:
        print("invalid task number")

def remove_task():
    show_tasks()
    task_number=int(input("enter task number to remove: "))-1
    if (task_number>0 and task_number<len(task_list)):
        task_list.pop(task_number)
        print("task removed successfully")
    elif task_number==0 and len(task_list)==1:
        task_list.pop(task_number)
        print("task removed successfully")
    else:
        print("invalid task number")
        
def main_menu():
  while True:
     print("--------MAIN MENU--------")
     print("choose one option:")
    
     print("1. Show Tasks")
     print("2. Add Task")
     print("3. Complete Task")
     print("4. Remove Task")
     print("5. Exit")
     user_choice=int(input("enter your choice: "))
     if user_choice==1:
        show_tasks()
     elif user_choice==2:
        add_task()
     elif user_choice==3:
        complete_task()
     elif user_choice==4:
        remove_task()
     elif user_choice==5:
        print("closing the program")
        break
     else:
        print("invalid choice, please try again")
if __name__=="__main__":
    main_menu()
    
