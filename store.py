import products


class Store:
    def __init__(self, products):
        self.products = products


    def get_products(self):
        """Return the product list"""
        return self.products


    def set_products(self, products):
        """Set product list"""
        self.products = products


    def add_product(self, product):
        """
        Add a product to the product list.
        Set the new list.
        """
        products = self.get_products()
        products.append(product)
        self.set_products(products)


    def remove_product(self, product):
        """
        Remove a product from the product list.
        Set the new list.
        """
        products = self.get_products()
        try:
            products.remove(product)
        except ValueError:
            print(f'Product "{product}" is not in list.')
        
        self.set_products(products)


    def get_total_quantity(self):
        """Return how many items are in the store in total."""
        products = self.get_products()
        quantity = 0
        for product in products:
            quantity += product.get_quantity()
        return quantity


    def get_all_products(self):
        """Return all products in the store that are active."""
        products = self.get_products()
        active_products = []
        for product in products:
            if product.is_active():
                active_products.append(product)
        return active_products    


    def order(self, shopping_list):
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        """
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
    

def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

    best_buy = Store(product_list)
    availible_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(availible_products[0], 1), (availible_products[1], 2)]))


if __name__ == "__main__":
        main()