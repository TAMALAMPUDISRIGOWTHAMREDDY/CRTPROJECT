import csv
class Abc:
    def registration(self,username,password,phoneno,pincode):
        self.username=username
        self.password=password
        self.phoneno=phoneno
        self.pincode=pincode
        with open("registerdetails.csv","a",newline="")as file:
            a=csv.writer(file)
            a.writerow([username,password,phoneno,pincode])
    def login(self,username,password):
        with open("registerdetails.csv","r",newline="")as file:
            read=csv.DictReader(file)
            for row in read:
                if row['username']==username and row['password']==password:
                    return True
                False


