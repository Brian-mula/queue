queue=[]

def enqueue():
    element=input('Enter item to add to queuue: ')
    queue.append(element)
    print('Item aaded succesfully')

def deque():
    if not queue:
        print('The queue is empty')
    else:
        e=queue.pop(0)
        print('Deleted item from q',e)

def display():
    print(queue)

while True:
    print('Select the operation: 1. enqueue, 2. dequeue, 3. display, 4. quit')
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        deque()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print('enter the correct choice')