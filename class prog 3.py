class Card:
    def __init__(self, imageURL,price,rating,description,deliverywithin,comments,brandname):
        self.image = imageURL
        self.price = price
        self.rating = rating
        self.description = description
        self.deliverywithin = deliverywithin
        self.comments = comments
        self.brandname = brandname

phone1 = Card("dfdkddj.jpg",10000,5,"good quality", "7 days"," nice","apple")
print(phone1.image)
print(phone1.rating)
print(phone1.price)


output:
dfdkddj.jpg
5
10000
