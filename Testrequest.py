import requests
from product.CProduct import ProductManager, Product

url = 'https://dummyjson.com/products'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print("Lỗi khi gọi API:", response.status_code)

products = data.get("products", [])
if products:
    print(products[0])
else:
    print("Không có sản phẩm nào.")

p = ProductManager()

for item in products:
    product = Product(item['id'], item['title'], item['price'], item['stock'], item['rating'], item['category'], item['description'], item['images'])
    p.ThemProduct(product)


p.GhiFileJson()