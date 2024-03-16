import csv
class Efg:
    def Product(self,h,s,quan):
        self.electronic=h
        self.clothes=s
        self.books=quan
        with open("products.csv","a",newline="")as file:
            c=csv.writer(file)
            c.writerow([self.electronic,self.clothes,self.books])
            