#
# test_string = "         "
# print(len(test_string))
# test_string.strip()
# print("A" + test_string + "A")

import restaurant

product = restaurant.Product("coffee", 2.5)
print(product.__class__.__name__)
print(product.name)
print(product.price)
beverage = restaurant.Beverage("coffee", 2.5, 50)
print(beverage.__class__.__name__)
print(beverage.__class__.__bases__[0].__name__)
print(beverage.name)
print(beverage.price)
print(beverage.milliliters)
soup = restaurant.Soup("fish soup", 9.90, 230)
print(soup.__class__.__name__)
print(soup.__class__.__bases__[0].__name__)
print(soup.name)
print(soup.price)
print(soup.grams)
