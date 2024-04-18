class Card:
    def __init__(self, imageURL,price,rating,description,deliverywithin,comments,brandname):
        self.image = imageURL
        self.price = price
        self.rating = rating
        self.description = description
        self.deliverywithin = deliverywithin
        self.comments = comments
        self.brandname = brandname

    def printbasicdetails(self):   #this is member function
        print("brand name is:",self.brandname)
        print("product rate is:",self.price)
        print("product rating is:",self.rating)

    def printalldetails(self):
        print("brand name is:",self.brandname)
        print("product rate is:",self.price)
        print("product rating is:",self.rating)

    def calculategst(self):
        print("calculating GST")
        

phone1 = Card("dfdkddj.jpg",100000,5,"good quality", "7 days"," nice","apple")
phone1.printalldetails()
phone1.printbasicdetails()
laptop = Card("dhygu.jpg",120000,4.9,"best quality","5 days","okk","dell")
laptop.printalldetails()
laptop.printbasicdetails()
