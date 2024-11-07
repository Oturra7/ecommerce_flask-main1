class Product:
    all_products = [] 

    def __init__(self, id, name, price, category_id, description, images):
        self.id = id
        self.name = name
        self.price = price
        self.category_id = category_id
        self.description = description
        self.images = images  

        
        Product.all_products.append(self)
