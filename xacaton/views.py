from utils import read_db, validate_id, write_to_db
        
database = read_db("db.json")

def retrieve(u_id):
        validate_id(database.keys(), u_id)
        mark = database[u_id]["mark"]
        model = database[u_id]["model"]
        year = database[u_id]["year"]
        vol_eng = database[u_id]["vol_eng"]
        color = database[u_id]["color"]
        type_ = database[u_id]["type"]
        probeg = database[u_id]["probeg"]
        price = database[u_id]["price"]
        print(f"""
        ==========={u_id}============
        mark: {mark}
        year: {year}
        model: {model}
        vol_eng: {vol_eng}
        color: {color}
        type: {type_}
        probeg: {probeg}
        price: {price}
        ==========================
        """)

def listing():
        for i in database:
            b = retrieve(i)
        return b
def create():
        from utils import generate_id
        from models import Cars
        Cars(str(input("Введите марку: ")), str(input("Введите модель: ")), int(input("Введите год выпуска: ")), round(float(input("Введите обьем двигателя: ")),1), str(input("Укажите цвет: ")), input("Укажите тип кузова\n*седан\n*универсал.купе\n*хэтчбэк\n*минивен\n*внедорожник\n*пикап\n====================\n "), int(input("Введите пробег: ")), round(float(input("Введите цену: ")),2))
        id_ = generate_id(database.keys())
        for o in Cars.objects:

            database[id_] = {
                "mark": o.mark,
                "model": o.model,
                "year": o.year,
                "vol_eng": o.vol_eng,
                "color": o.color,
                "type": o.type_,
                "probeg": o.probeg,
                "price": o.cost
            }
        print("мы добавили вашу машину в БД")
        write_to_db("db.json", database)
        print(f'ваш персональный id: {id_}')


def delete(u_id):
        validate_id(database.keys(), u_id)
        mark = database[u_id]["mark"]
        del database[u_id]
        print(f"{mark} был успешно удален")
        write_to_db("db.json", database)


def update(u_id):
        validate_id(database.keys(), u_id)
        retrieve(u_id)
        # принимаем новые данные
        mark = str(input("Введите марку: "))
        model = str(input("Введите модель: "))
        year = int(input("Введите год выпуска: "))
        vol_eng = round(float(input("Введите обьем двигателя: ")),1)
        color = str(input("Укажите цвет: "))
        type_ = str(input("Укажите тип кузова\n*седан\n*универсал.купе\n*хэтчбэк\n*минивен\n*внедорожник\n*пикап\n====================\n"))
        probeg = int(input("Введите пробег: "))
        price = round(float(input("Введите цену: ")),2)

        # изменяем в бд
        database[u_id]["mark"] = mark
        database[u_id]["model"] = model
        database[u_id]["year"] = year
        database[u_id]["vol_eng"] = vol_eng
        database[u_id]["color"] = color
        database[u_id]["type"] = type_
        database[u_id]["probeg"] = probeg
        database[u_id]["price"] = price
        write_to_db("db.json", database)