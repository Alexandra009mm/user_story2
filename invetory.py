circle = "yes"
inventary = []
total = 0

#==============================================================================================
def add_product():
    keep_register = "yes"

    print("\n--- ADD PRODUCT ---")

    while keep_register == "yes":
        print("------")

        # VALIDACIÓN NOMBRE
        valid_name = "no"
        while valid_name == "no":
            product_name = input("Enter the product name: ").lower()
            if product_name == "":
                print("Error: this field must be filled")
            else:
                valid_name = "yes"

        print("------")

        # VALIDACIÓN PRECIO
        valid_price = "no"
        while valid_price == "no":
            try:
                price = float(input("Enter the price: "))
                if price <= 0:
                    print("Enter a valid price. Try again.")
                else:
                    valid_price = "yes"
            except ValueError:
                print("Error: invalid price. Try again")

        print("------")

        # VALIDACIÓN CANTIDAD
        valid_quantity = "no"
        while valid_quantity == "no":
            try:
                p_quantity = int(input("Enter the quantity: "))
                if p_quantity < 0:
                    print("Enter a valid quantity. Try again")
                else:
                    valid_quantity = "yes"
            except ValueError:
                print("Error: invalid quantity. Try again")

        print("\nProduct successfully added!\n")

        produ = {
            "product name": product_name,
            "price": price,
            "quantity": p_quantity
        }

        inventary.append(produ)

        keep_register = input("Do you want to add another product? yes/no: ").lower()


#==============================================================================================
def show_inventory():
    print("\n--- INVENTORY ---")

    if len(inventary) == 0:
        print("The inventory is empty")
    else:
        print("------")
        for i in inventary:
            print("Product name |", i["product name"])
            print("Price        |", i["price"])
            print("Quantity     |", i["quantity"])
            print("------")


#==============================================================================================
def show_total():
    print("\n--- TOTAL INVENTORY VALUE ---")

    total = 0
    for i in inventary:
        total += i["price"] * i["quantity"]

    print(f">>> Total value: {total}")


#==============================================================================================
def show_total_products():
    print("\n--- TOTAL PRODUCTS ---")

    total_products = 0
    for i in inventary:
        total_products += i["quantity"]

    print(f">>> Total products: {total_products}")


#==============================================================================================
keep_register = True

print("\n--- INVENTARY SYSTEM ---")

while keep_register:
    print("\n------ MAIN MENU ------")
    print("1. Add product")
    print("2. Show inventory")
    print("3. Statistics")
    print("4. Exit")
    print("------")

    try:
        ask = int(input("Enter an option: "))
    except (ValueError, TypeError):
        print("Error: invalid option. Try again")
        continue

    if ask == 1:
        print("\nYou chose option 1 =>")
        add_product()

    elif ask == 2:
        print("\nYou chose option 2 =>")
        show_inventory()

    elif ask == 3:
        print("\n--- STATISTICS MENU ---")
        print("1. Show inventory total")
        print("2. Show total products")
        print("------")

        try:
            question = int(input("Select an option: "))
        except (ValueError, TypeError):
            print("Error: invalid option. Try again")
            continue

        if question == 1:
            show_total()

        elif question == 2:
            show_total_products()

        else:
            print("Invalid option")

    elif ask == 4:
        print("\nThank you for using the system :)")
        keep_register = False

    else:
        print("ERROR! Enter a correct value. Try again.")