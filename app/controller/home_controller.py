from flask import Blueprint, render_template
from app.model.category import Category
from app.model.product import Product
from app.controller.category_controller import categories
home_bp = Blueprint('home', __name__)

products = [
    Product(1, "Raquete de Beach Tennis Mormai", 1200.00, 1, "Raquete de beach tennis, carbono 3k, peso 350g, balance médio.", [
        "https://mormaiishop.vtexassets.com/arquivos/ids/4215621/31312314_VELHO-PRETO_1.jpg?v=638234010102430000"
    ]),
    Product(2, "Raquete de Beach Tennis Dropshot", 1500.00, 1, "Raquete de beach tennis, carbono 12k, peso 330g, balance médio.", [
        "https://cdn.dooca.store/2621/products/raquete-de-beach-tennis-drop-shot-x-drive-10-bt-1.jpg?v=1706121517"

    ]),
    Product(3, "Blusa Dropshot", 80.00, 2, "Blusa leve utilizada para a prática esportiva de beach tennis.", [
        "https://www.lojadebeachtennis.com.br/media/catalog/product/cache/6075802978a491002ad8135921ca75cd/i/m/img_2485.jpeg",

    ]),
    Product(4, "Raqueteira Mormai", 899.99, 3, "Raqueteira mormai amarela e preta.", [
        "https://images.tcdn.com.br/img/img_prod/589314/raqueteira_de_beach_tennis_mormaii_pro_samantha_barijan_6471_3_f6caeb2a24cdda9dde0dff0cc7f3fefe_20240515180849.jpg"
    ]),
    Product(5, "Manguito Dropshot esquerdo", 49.00, 3, "Manguito de compressão rosa, marca dropshot.", [
        "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcRIDCYnMpkUJrE4uWxYPsdCXzG5LYlmW0xn0Mi33pkXzHQ_4mg2fe7MAoSv1GIzI-5OUgJHc9uLDtARmRYarKXlQZd6Ku-Qrown_Cs-iQaG2u5XFjXmBN2Z1ys"

    ]),
    Product(6, "Viseira Track field holográfica", 189.99, 2, "Viseira track field holográfica, utilizada no dia a dia.", [
        "data:image/jpeg;base64,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"
    ])
]

@home_bp.route('/')
def home():
    return render_template('index.html', categories=categories, products=Product.all_products)
