queue=[ ]

while True:
    element= input("Enter your element : ")
    queue.append(element)
    choice= input("do you want to stop? press yes for stop otherwise press any key: ")
    if choice == "yes":
        break
print(queue)

remove = input("Do you want to pop. if yes press yes or any key")
if remove == "yes":
    delete=int(input("Enter which index you want to pop :"))
    queue.pop(delete)

print(queue)
