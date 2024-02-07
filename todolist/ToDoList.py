import sys
import os
import json

class OutOfBoundError(Exception):
    def __init__(self):
        self.message = "Index is out bounds."
        super().__init__(self.message)
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class JsonHandler:
    def __init__(self, filename):
        self.filename = filename

    def saveJson(self, parameter_list):
        tasks = {}
        tasks["tasks"] = parameter_list
        json_text = json.dumps(tasks, indent=4)
        with open(self.filename, "w") as file:
            file.write(json_text)

    def loadJson(self):
        with open(self.filename, "r") as file:
            json_text = json.load(file)
        return json_text
    
        

class TodoList:
    def __init__(self):
        self.head = None
        self.jsonhandler = JsonHandler(r"E:\Aditya\development\Programming\python_work\Internship Projects\todolist\todolist.json")
        self.cvtJsonToList()

    def cvtJsonToList(self):
        text = self.jsonhandler.loadJson()
        tasks_list = text['tasks']
        for index, task in enumerate(tasks_list):
            if index==0:
                self.insertAtBegin(task)
            else:
                self.insertAtEnd(task)

    def saveListToJson(self):
        current_node = self.head
        task_list = []
        while(current_node!=None):
            task_list.append(current_node.data)
            current_node = current_node.next
        self.jsonhandler.saveJson(task_list)

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if index == position:
            self.insertAtBegin(data)
        else:
            while (current_node != None and position+1 != index):
                position += 1
                current_node = current_node.next
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                # print("IndexOutOfBounds")
                raise OutOfBoundError()

    def insertAtEnd(self, data):
        new_node = Node(data)
        current_node = self.head
        while (current_node.next != None):
            current_node = current_node.next
        current_node.next = new_node
        new_node.next = None

    def deleteAtIndex(self, index):
        current_node = self.head
        previous_node = current_node
        pos = 1
        while(current_node!=None and pos!=index):
            previous_node = current_node
            current_node = current_node.next
            pos += 1
        if current_node!=None:
            previous_node.next = current_node.next
        else:
            raise OutOfBoundError()

    def showCheckList(self):
        current_node = self.head
        pos = 1
        stack = []
        while(current_node!=None):
            if current_node.data[0] == 'u':
                print(str(pos)+" ☐  "+current_node.data[1:])
                pos += 1
            elif current_node.data[0] == 'c':
                stack.append(str(" ☑  "+current_node.data[1:]))
            current_node = current_node.next
        for item in stack:
            print(str(pos)+item)
            pos += 1
        print("\n")

    def checkTodoTask(self, index):
        current_node = self.head
        pos = 1
        while(current_node!=None and pos!=index):
            current_node = current_node.next
            pos += 1
        if current_node!=None:
            current_node.data = "c" + current_node.data[1:]
        else:
            raise OutOfBoundError()

    def clearTerminal(self):
        os.system('cls')

    def displayHeader(self):
        text = """
        -----------------------------------------------------------------
        |                           Todo List                           |
        -----------------------------------------------------------------
                                    """
        print(text)

    def displayOptions(self):
        self.displayHeader()
        text = """
                            1. View todo tasks
                            2. Add another todo task
                            3. Check a todo task
                            4. Delete a todo task
                            5. Save and Quit
                            6. Quit the program
                                    """
        print(text)



    def main(self):
        space = "                        "
        self.displayOptions()
        try:
            choice = int(input(space+">>> "))
            # self.clearTerminal()
            if choice==1:
                self.showCheckList()
            elif choice==2:
                print(space+">>> "+"Enter the task you want to add")
                task = str(input(space+">>> "))
                task = "u" + task
                self.insertAtBegin(task)
            elif choice==3:
                print(space+">>> "+"Enter index of task you want to check")
                index = int(input(space+">>> "))          
                self.checkTodoTask(index)
            elif choice==4:
                print(space+">>> "+"Enter index of task you want to delete")
                index = int(input(space+">>> "))
                self.deleteAtIndex(index+1)
            elif choice==5:
                self.saveListToJson()
                sys.exit()
            elif choice==6:
                sys.exit()
            else:
                print("Invalid choice entered")
        except Exception as e:
            # print(e)
            print("Invalid choice entered")

    def run(self):
        while True:
            self.main()


if __name__ == "__main__":
    todolist = TodoList() 
    todolist.run()
