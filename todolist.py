def add_tasks():
    name = input("Enter the task name: ")
    f = open("task.txt","+a")
    f.write(name + "\n")
    f.close


def view_tasks():
    f = open("task.txt","r")
    data = f.read()
    print(data)
    f.close()



def delete_task():
    f=open("task.txt","r")
    data=input("Enter the task u want to delete:")
    val = f.read()
    newlist = val.split("\n") #remove \n while reading
    newlist.remove(data)
    f.close()

    f=open("task.txt","w")
    for i in newlist:
        f.write(i + "\n")   # each task goes on a new line
    f.close()


choose = {
    "1" : add_tasks,
    "2" : view_tasks,
    "3" : delete_task,
    "4" : "exit"
}

print("This is a To-Do List")
a = input("Choose what you want to perform : \n 1. Add Task  2. View Tasks  3. Delete Task  4. Exit     ")
for i in range(100):
    if "4" not in a:
        choose[a]()
        a = input("Choose what you want to perform : \n 1. Add Task  2. View Tasks  3. Delete Task  4. Exit     ")
    else:
        print("Exit Sucessfully")
        break
