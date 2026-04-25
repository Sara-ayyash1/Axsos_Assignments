local_val = "magical unicorns"

def square(x):
    return x * x

# A class representing a User with a name attribute
class User:
    # Constructor — runs automatically when a User object is created
    def __init__(self, name):
        self.name = name  #

    def say_hello(self):
        return "hello"


# __name__ == "__main__" is True only when this file is run directly
# If this file is imported by another file, __name__ will be the file's name instead
if __name__ == "__main__":
    print(square(5))          
    user = User("Anna")        
    print(user.name)           
    print(user.say_hello())    
    print("the file is being executed directly")
else:
    # This runs when the file is imported, not executed directly
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)