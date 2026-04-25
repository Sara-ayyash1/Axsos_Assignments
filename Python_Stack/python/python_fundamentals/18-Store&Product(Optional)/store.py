class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)

    def sell_product(self, id):
        # find the product with the matching id
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
                print(f"Sold: ", end="")
                product.print_info()
                return
        print(f"Product with id {id} not found!")

    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, is_increased=True)

    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, is_increased=False)

              
  