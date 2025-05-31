import json

class Product:
    def __init__(self, Id, Ten, Gia, SoLuong, Rate, Loai, ThongTin, HinhAnh):
        self.Id = Id
        self.Ten = Ten
        self.Gia = Gia
        self.SoLuong = SoLuong
        self.Rate = Rate
        self.Loai = Loai
        self.ThongTin = ThongTin
        self.HinhAnh = HinhAnh
    
    def to_dict(self):
        return {
            "Id": self.Id,
            "Ten": self.Ten,
            "Gia": self.Gia,
            "SoLuong": self.SoLuong,
            "Rate": self.Rate,
            "Loai": self.Loai,
            "ThongTin": self.ThongTin,
            "HinhAnh": self.HinhAnh
        }

class ProductManager:
    def __init__(self):
        self.products = []
    def load_products(self):
        with open("product/products.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            for item in data:
                product = Product(item["Id"], item["Ten"], item["Gia"], item["SoLuong"], item["Rate"], item["Loai"], item["ThongTin"], item['HinhAnh'])
                self.products.append(product)
    

    def ThemProduct(self, product):
        self.products.append(product)
    
    def GhiFileJson(self):
        data = [product.to_dict() for product in self.products]
        with open("product/products.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
