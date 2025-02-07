print("MENU\n1.Addition\n2.Difference\n3.Division\n4.Produt")
choice=int(input("enter choice 1-4"))
x=int(input("enter a number"))
y=int(input("enter a number"))
if choice==1:
    print("Addition:",x+y)
elif choice==2:
    print("Difference:",x-y)
elif choice==3:
    print("Division:",x/y)
elif choice==4:
    print("Product:",x*y)
else:
    print("Invalid choice")
