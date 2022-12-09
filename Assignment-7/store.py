from qrcode import make

products = []
def read_from_database():
    file = open("database.txt", "r")
    for line in file:
        result = line.split(",")
        my_dict = {
            "code" :result[0],
            "name": result[1],
            "price": result[2],
            "count": result[3]
        }
        products.append(my_dict)
    file.close()

def remove_new_line():
    for product in products:
        if type(product["count"]) == str and '\n' in product["count"]:
            product["count"] = product["count"].strip("\n")

def write_to_database():
    remove_new_line()
    file = open("database.txt", "w")
    for product in products:
        file.write(f"{product['code']},{product['name']},{product['price']},{product['count']}\n")
    file.close()

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

def add():
    code = int(input("enter code: "))
    name = input("enter name: ")
    price = int(input("enter price: "))
    count = int(input("enter count: "))
    new_product = {
        "code": code,
        "name": name,
        "price": price,
        "count": count
    }
    products.append(new_product)

def edit():
    product = find_product(code=input("Enter the product code: "))
    if product:
        feild = input("Which field do you want to edit? enter name, Price or Count: ")
        for obj in products:
            if obj["code"] == product["code"]:
                obj[feild] = input("Please enter the new value for this field: ")
        print("Product was update successfuly!")
    else:
        print("product not found.")

def remove():
    code = input("Enter the product code: ")
    for index, product in enumerate(products):
        if product["code"] == code:
            del products[index]
            print("The product has been successfully removed!")
            break
    else:
        print("Product not found!")

def search():
    user_input = input("type your keyword: ")
    product = find_product(user_input, user_input)
    print("code\t\tname\t\tprice", '\n', product["code"], "\t\t", product["name"], "\t\t", product["price"]) if product else print("Not Found")

def show_list():
    print("code\t\tname\t\tprice")
    for product in products:
        print(product["code"], "\t\t", product["name"], "\t\t", product["price"])

def buy():
    cart = []
    while True:
        user_input = input("Enter the product code for buying a product and enter 0 for back to menu: ")
        if user_input == "0":
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
    product = find_product(input("Enter the product code: "))
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
        write_to_database()
        exit(0)
    else:
        print("invalid input")
