from shop.models import Category, Product
from shop.views import product_detail, product_list,product_create,product_delete,product_update
cat = Category('Phones')
Category("space watch")
Category("Dyson")
Category("Food")
obj1 = Product("iphone", 234, "...", 3,cat)
obj2 = Product("lenove", 12, "...", 3,cat)
obj3 = Product("samsung", 199, "...", 3,cat)

from pprint import pprint
# pprint(product_create())
pprint(product_list()) 
id = input("Введите продукт для изменения: ")
pprint(product_update(id))
pprint(product_list()) 