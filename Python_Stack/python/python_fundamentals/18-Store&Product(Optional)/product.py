class Product:
    # Class variable — shared across all instances, increments with each new product
    id_counter = 1

    def __init__(self, name, price, category):
        self.id = Product.id_counter  # assign unique id
        Product.id_counter += 1       # increment for next product
        self.name = name
        self.price = price
        self.category = category

    def print_info(self):
        print(f"ID: {self.id} | Name: {self.name} | Category: {self.category} | Price: ${self.price:.2f}")

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price * (percent_change / 100)
        else:
            self.price -= self.price * (percent_change / 100)