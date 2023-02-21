from sqlite3 import connect
from qrcode import make

products = []
connection = connect("store.db")
cursor = connection.cursor()
def read_from_database():
    global products
    products = []
    cursor.execute("SELECT * FROM Products")
    rsesult = cursor.fetchall()
    for product in rsesult:
        my_dict = {
            "code" :product[0],
            "name": product[1],
            "price": product[2],
            "count": product[3]
        }
        products.append(my_dict)

def find_product(code=0, name=0):
    for product in products:
        if product['code'] == code or product["name"] == name:
            return product
    else:
        return False

def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show List")
    print("6- Buy")
    print("7- Create QRcode for a product")
    print("8- Exit")

def add_to_database(name, price, count):
    cursor.execute(f"INSERT INTO Products(name, price, count) VALUES('{name}', '{price}', '{count}')")
    connection.commit()

def add():
    name = input("enter name: ")
    while True:
        try:
            price = float(input("enter price: "))
            break
        except:
            print("please enter a float number.")
    while True:
        try:
            count = int(input("enter count: "))
            break
        except:
            print("Please enter an integer.")
    add_to_database(name, price, count)
    read_from_database()
    print("new product successfully added.")

def update_database(code, field, new_value):
    try:
        code = int(code)
    except:
        pass
    cursor.execute(f'''UPDATE Products
    SET '{field}' = '{new_value}'
    WHERE code = '{code}' OR name = '{code}' ''')
    connection.commit()

def edit():
    code = input("Enter the product code: ")
    try:
        product = find_product(code=int(code), name=code)
    except:
        product = find_product(code=code, name=code)
    if product:
        feild = input("Which field do you want to edit? enter name, Price or Count: ")
        for obj in products:
            if obj["code"] == product["code"]:
                obj[feild] = input("Please enter the new value for this field: ")
                update_database(code, feild, obj[feild])
        print("Product was update successfuly!")
    else:
        print("product not found.")

def remove_from_database(code):
    cursor.execute(f"DELETE FROM Products WHERE code = '{code}' ")
    connection.commit()

def remove():
    while True:
        try:
            code = int(input("Enter the product code: "))
            break
        except:
            print("Pleses enter an integer.")
    for index, product in enumerate(products):
        if product["code"] == code:
            del products[index]
            remove_from_database(code)
            print("The product has been successfully removed!")
            break
    else:
        print("Product not found!")

def search():
    user_input = input("type your keyword: ")
    try:
        product = find_product(int(user_input), user_input)
    except:
        product = find_product(user_input, user_input)
    print("code\t\tname\t\tprice", '\n', product["code"], "\t\t", product["name"], "\t\t", product["price"]) if product else print("Not Found")

def show_list():
    print("code\t\tname\t\tprice")
    print("----------------------------------------")
    for product in products:
        print(product["code"], "\t\t", product["name"], "\t\t", product["price"])

def buy():
    cart = []
    while True:
        while True:
            try:      
                user_input = int(input("Enter the product code for buying a product and enter 0 for back to menu: "))
                break
            except:
                print("Please enter an integer.")
        if user_input == 0:
            total_price = 0
            print("name\t\tcount\t\tprice")
            for product in cart:
                total_price += int(product["price"])
                print(f"{product['name']}\t\t{product['count']}\t\t{product['price']}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Total Price:", total_price)
            break
        product = find_product(code=user_input)
        if product:
            count = int(input("How many of this product do you want? "))
            if int(product["count"]) >= count:
                for obj in products:
                    if product["code"] == obj["code"]:
                        obj["count"] = int(obj["count"]) - count
                        update_database(user_input, "count", obj["count"])
                        cart.append({
                            "name": obj["name"],
                            "count": count,
                            "price": int(obj["price"])*count
                            })
                        break
            else:
                print("Insufficient inventory")
        else:
            print("Product not found.")

def make_qr_code():
    while True:
        try:
            code = int(input("Enter the product code: "))
            break
        except:
            print("Please enter an integer.")
    product = find_product(code=code)
    if product:
        img = make(product)
        img.save(f"{product['code']}.png")
        print("Qr code generated successfuly.")
    else:
        print("product not found!")

print("welcome to store")
print("Loading...")
read_from_database()
print("Data loaded.")
while True:
    print("------------------------------------------")
    show_menu()
    choice = int(input("enter your choice: "))
    print("------------------------------------------")
    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        show_list()
    elif choice == 6:
        buy()
    elif choice == 7:
        make_qr_code()
    elif choice == 8:
        exit(0)
    else:
        print("invalid input")
