from project2 import *
from product import *
class order:
    print("existing user or new user")
    g=int(input())
    obj=Abc()
    if g==1:
        username=input("enter username:")
        password=input("enter password:")
        phoneno=int(input("enter phoneno:"))
        pincode=int(input("enter pincode:"))
        obj.registration(username,password,phoneno,pincode)
        print("registeration successful")
    elif g==2:
        username=input("enter user name:")
        password=input("enter password:")
        if obj.login(username,password):
            print("login successful")
            print("products are: electronic ,clothes,books")           
            h=input()
            obj1=Efg()
            if h=="electronic":
                print("products in electronics are 1.laptop 2.mobile")
                s=input(" choose laptop or mobile")
                if s=="laptop":
                    quan=10
                    print("laptop quantity is",quan)
                    obj1.Product(h,s,quan)
                else:
                    quan=15
                    print("mobile quantity is",quan)
                    obj1.Product(h,s,quan)
            elif h=="clothes":
                print("clothes are 1.pant 2.shirt")
                s=input("choose pant or shirt")
                if s=="pant":
                    quan=20
                    print("pants are",quan)
                    obj1.Product(h,s,quan)
                else:
                    quan=25
                    print("shirts are",quan)
                    obj1.Product(h,s,quan)
            elif h=="books":
                print("books are 1.schand 2.cengage")
                s=input("choose 1.schand 2.cengage")
                if s=="schand":
                    quan=20
                    print("schand qunatity is",quan)
                    obj1.Product(h,s,quan)
                else:
                    quan=30
                    print("cengage quantity is",quan)
                    obj1.Product(h,s,quan)
            
            else:
                print("enter valid product")
    else:
        print("wrong details try again")
