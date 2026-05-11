import products
import store

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)


def get_all_products(my_store):
    """Return list of all active products in the store."""
    return my_store.get_all_products()


def print_all_products(my_store):
    """Print a list of all active products in the store."""
    products_to_print = get_all_products(my_store)
    for i, product in enumerate(products_to_print, start=1):
        print(f"{i}.", end=" ")
        product.show()


def get_total_quantity(my_store):
    """Print the combined quantity of all active products."""
    print(f"Total of {my_store.get_total_quantity()} items in store.")


def order(my_store):
    """Make an order and print the total price."""
    shopping_list = []

    while True:
        print_all_products(my_store)

        index_of_product = input("Choose product number (or q to finish): ")

        if index_of_product == "q":
            break

        try:
            index_of_product = int(index_of_product) - 1
            products_in_store = my_store.get_all_products()
            product_to_order = products_in_store[index_of_product]

            quantity_to_order = int(input("How many: "))

            shopping_list.append((product_to_order, quantity_to_order))

        except (ValueError, IndexError):
            print("Invalid input, try again.")

    total_price = my_store.order(shopping_list)
    print(f"Total order price: {total_price}")


def start(my_store):
    """Return the main menu as a dict."""
    command_dict = {
        "1": lambda *args: print_all_products(my_store),
        "2": lambda *args: get_total_quantity(my_store),
        "3": lambda *args: order(my_store),
        }
    return command_dict


def print_commands():
    """Print a list of the available commands in a formatted manner."""
    menu = ["",
    "********** Store Manager **********",
    "",
    "Menu:",
    "1. List all products in store",
    "2. Show total amount in store",
    "3. Make an order",
    "4. Quit",
    ""
    ]
    for line in menu:
        print(line)


def get_command(menu):
    """Prompt the user for a command."""
    while True:
        command = input("Command>    ")

        if command == "4":
            print("Program closed.")
            break

        if command:
            if command not in menu:
                print("Invalid command. Try again.")
                continue

            else:
                menu[command]()
                print_commands()

        print()


def main():
    menu = start(best_buy)
    print_commands()
    get_command(menu)


if __name__ == "__main__":
        main()
