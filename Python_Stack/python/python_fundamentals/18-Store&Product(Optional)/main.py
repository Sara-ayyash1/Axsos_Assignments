from product import Product
from store import Store

if __name__ == "__main__":

    # Create a store
    my_store = Store("Sara's Store")

    # Create products
    p1 = Product("Laptop",    1200, "Electronics")
    p2 = Product("T-Shirt",   25,   "Clothing")
    p3 = Product("Headphones",150,  "Electronics")
    p4 = Product("Jeans",     60,   "Clothing")

    # Add products to store
    my_store.add_product(p1)
    my_store.add_product(p2)
    my_store.add_product(p3)
    my_store.add_product(p4)

    print("\n--- All Products ---")
    for product in my_store.products:
        product.print_info()

    my_store.sell_product(1) 

    print("\n--- After selling ---")
    for product in my_store.products:
        product.print_info()

    print("\n--- Apply 10% inflation ---")
    my_store.inflation(10)
    for product in my_store.products:
        product.print_info()

    print("\n--- 50% clearance on Clothing ---")
    my_store.set_clearance("Clothing", 50)
    for product in my_store.products:
        product.print_info()