
studentlist = ["Hardik","Naman","Aryan","Aniket"]
print("Chosse what you want")
print("1.View list")
print("2.Add element from list")
print("3.Remove element from list")
chosse=int(input(""))

if chosse==1:
    print(studentlist)

elif chosse==2:
    print("The list is:", studentlist)
    num=int(input("Enter the number of elemnt you want to add"))
    for i in range(num):
        element=input(f"enter element {i+1}:")
        studentlist.append(element)

    print("List is:", studentlist)

elif chosse==3:
    print("The list is:", studentlist)
    print("type the elment you want to remove")
    element=input("")
    studentlist.remove(element)
    print("The new list is:", studentlist)

else :
    print("You wrong operation")
    


    
