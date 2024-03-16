class carshowroom:
    def __init__(self):
        print("//WELCOME TO SA MOTORS//")
    def company(self):
        print("Avaliable companies:")
        print("1.Toyota")
        print("2.Mahindra")
        print("3.Mercedes")
        self.cn=input("Enter company name:")
        if isinstance(self.cn, str):
            self.cn = self.cn.lower()
            # print(self.cn)
        if(self.cn=="toyota" or self.cn=="1"):
            self.cn="toyota"
            print()
            print("Welcome to Toyota Family")
            return o.model()
        elif(self.cn=="mahindra" or self.cn=="2"):
            print()
            print("Welcome to Mahindra Family")
            self.cn="mahindra"
            return o.model()
        elif(self.cn=="mercedes" or self.cn=="3"):
            self.cn="mercedes"
            print()
            print("Welcome to Mercedes Family")
            return o.model()
        else:
            print()
            print("Invalid choice plz enter again")
            return o.company()
    def model(self):
        if(self.cn=="toyota"):
            print("The avaliable models in Toyota are:""\n""1.Corolla""\n""2.highlander""\n""3.Prius")
            print("If you want to change company enter 'back' ")
            self.m=input("Enter model of your choice:")
            if isinstance(self.m,str):
                self.m=self.m.lower()
            if(self.m=="corolla" or self.m=="1"):
                self.m="corolla"
                print("You have selected:",self.m)
                return o.varient()
            elif(self.m=="highlander" or self.m=="2"):
                self.m='highlander' 
                print("You have selected:",self.m)
                return o.varient()
            elif(self.m=="prius" or self.m=="3"): 
                self.m="prius"
                print("You have selected:",self.m)
                return o.varient()
            elif(self.m=="back"):
                return o.company()
            else:
                print()
                print("Wrong selection plz Select again")
                return o.model()
        if(self.cn=="mahindra"):
            print("The avaliable models in Mahindra are:""\n""1.Thar""\n""2.Scorpio""\n""3.XUV5oo")
            print("If you want to change company enter 'back' ")
            self.m=input("select model of your choice:")
            if isinstance(self.m,str):
                self.m=self.m.lower()
            if(self.m=="thar" or self.m=="1"):
                self.m="thar"
                print("You have selected ",self.m)
                return o.varient()
            elif(self.m=="scorpio" or self.m=="2"): 
                self.m="scorpio"
                print("You have selected:",self.m)
                return o.varient()
            elif(self.m=="xuv5oo" or self.m=="3"):
                self.m="xuv500" 
                print("You have selected:",self.m)
                return o.varient()
            elif(self.m=="back"):
                return o.company()
            else:
                print()
                print("Wrong selection plz Select again")
                return o.model()
        if(self.cn=="mercedes"):
            print("The avaliable models in Mercedes are:""\n""1.A-Class""\n""2.C-class""\n""3.S-class")
            print("If you want to change company enter 'back' ")
            self.m=input("Enter model of your choice:")
            if isinstance(self.m,str):
                self.m=self.m.lower()
            if(self.m=="a-class" or self.m=="1"):
                self.m="A-class"
                print("You have selected:",self.m)
                return o.varient()
            elif(self.m=="c-class" or self.m=="2"): 
                self.m="C-class"
                print("You have selected:",self.m)
                return o.varient()
            elif(self.m=="s-class" or self.m=="3"): 
                self.m="S-class"
                print("You have selected:",self.m)
                return o.varient()
            elif(self.m=="back"):
                return o.company()
            else:
                print()
                print("Wrong selection plz Select again")
                return o.model()
    def varient(self):
        print()
        print("for",self.cn,self.m,"two varients avaliable :""\n""1.petrol""\n""2.diesel")
        print("If you want to change model enter 'back' ")
        self.v=input("enter varient:")
        if isinstance(self.v, str):
            self.v = self.v.lower()
        if(self.v=="1" or self.v=="petrol"):
            self.v="petrol"
            if(self.cn=="toyota" and self.m=="corolla" ):
                self.showroomprice=1664000
                return o.display()
            elif(self.cn=="toyota" and self.m=="highlander"):
                self.showroomprice=3039708
                return o.display()
            elif(self.cn=="toyota" and self.m=="prius"):
                self.showroomprice=4012000
                return o.display()
            elif(self.cn=="mahindra" and self.m=="thar"):
                self.showroomprice=1198000
                return o.display()
            elif(self.cn=="mahindra" and self.m=="scorpio"):
                self.showroomprice=1258590
                return o.display()
            elif(self.cn=="mahindra"and self.m=="xuv500"):
                self.showroomprice=2332349
                return o.display()
            elif(self.cn=="mercedes" and self.m=="C-class"):
                self.showroomprice=2938411
                return o.display()
            elif(self.cn=="mercedes" and self.m=="A-class"):
                self.showroomprice=5903254
                return o.display()
            elif(self.cn=="mercedes" and self.m=="S-class"):
                self.showroomprice=6104896
                return o.display()
        elif(self.v=="2" or self.v=="diesel"):
            self.v="diesel"
            if(self.cn=="toyota" and self.m=="corolla" ):
                self.showroomprice=1772000
                return o.display()
            elif(self.cn=="toyota" and self.m=="highlander"):
                self.showroomprice=3948295
                return o.display()
            elif(self.cn=="toyota" and self.m=="prius"):
                self.showroomprice=4467000
                return o.display()
            elif(self.cn=="mahindra" and self.m=="thar"):
                self.showroomprice=1400858
                return o.display()
            elif(self.cn=="mahindra" and self.m=="scorpio"):
                self.showroomprice=2105349
                return o.display()
            elif(self.cn=="mahindra"and self.m=="xuv500"):
                self.showroomprice=2325349
                return o.display()
            elif(self.cn=="mercedes" and self.m=="C-class"):
                self.showroomprice=3201896
                return o.display()
            elif(self.cn=="mercedes" and self.m=="A-class"):
                self.showroomprice=6214789
                return o.display()
            elif(self.cn=="mercedes" and self.m=="S-class"):
                self.showroomprice=6845621
                return o.display()
        elif(self.v=="back"):
                return o.model()
        else:
            print()
            print("wrong choice enter varient again")
            return o.varient()
    def display(self):
        print("The ex-showroom price of",self.cn,self.m,self.v,"varient is",self.showroomprice)
        self.onroadprice=self.showroomprice+2*0.18*self.showroomprice+0.15*self.showroomprice
        print("The onroad price of",self.cn,self.m,self.v,"varient is",self.onroadprice)
o=carshowroom()
o.company()