l=[]
y="yes"
while y=="yes":
    print("MENU\n 1.to add element\n 2.to delete element\n 3.to display the list")
    x=int(input("enter your choice"))
    if x==1:
        num=int(input("enter the num to be added"))
        l.append(num)
        print("sucessfully added")
    elif x==2:
        if len(l)==0:
            print("list is empty")
        else:
            x=int(input("enter no. to be deleted"))
            l.remove(x)
            print("sucessfully deleted")
    elif x==3:
        print(l)
    else:
        print("invalid choice. TRY AGAIN")
    y=input("want to continue? type yes")
