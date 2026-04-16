class Animal:
    #Base class for all animals in the zoo
    def __init__(self, name, age=10, health_level=50, happiness_level=40):
        self.name = name 
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level
    
    def display_info(self):
        animal_type = self.__class__.__name__
        print(f"Type: {animal_type:10} | Name: {self.name:10} | Health: {self.health_level:3} | Happiness: {self.happiness_level}")
        return self
    
    def feed(self):
        #General feeding method for all animals
        self.health_level += 10
        self.happiness_level += 10
        return self 

#---------------------------------------
class Lion(Animal):
    def __init__(self, name, age=14, health_level=50, happiness_level=40, mane_color="Brown", is_king=True):
        # Passing attributes to the Parent (Animal) class correctly
        super().__init__(name, age, health_level, happiness_level)
        self.mane_color = mane_color 
        self.is_king = is_king

    # ---(Total Overriding) ---
    def feed(self):
        #Overriding feed method => # This completely IGNORES the parent's feed() method.
        # It replaces the logic entirely
        self.health_level += 20
        self.happiness_level += 5
        return self
    
    # ---(Extending with super) ---
    def feed(self):
        super().feed()   # This RUNS the parent's logic FIRST (adds +10 health, +10 happiness).
        # Then, it ADDS these extra points on top of what the parent did.
        self.health_level += 20  
        self.happiness_level += 5  
        return self
    
#---------------------------------------
class Tiger(Animal):
    def __init__(self, name, age=12, health_level=50, happiness_level=40, stripe_pattern="bold"):
        super().__init__(name, age, health_level, happiness_level)
        self.stripe_pattern = stripe_pattern

    def feed(self):
        #Overriding feed method (Total Overriding)
        self.health_level += 30
        self.happiness_level += 10
        return self

#---------------------------------------
class Monkey(Animal):
    def __init__(self, name, age=5, health_level=50, happiness_level=40, tail_length=100, climbing_speed="fast"):
        super().__init__(name, age, health_level, happiness_level)
        self.tail_length = tail_length
        self.climbing_speed = climbing_speed

    def climb(self):
        print(f"The Monkey {self.name} is climbing a tree!")

#---------------------------------------
class Bear(Animal):
    def __init__(self, name, fur_type="Thick", weight=500):
        # Bear uses default Animal values for age, health, and happiness
        super().__init__(name)
        self.fur_type = fur_type
        self.weight = weight

#---------------------------------------
class Zoo: 
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, animal):
        #Adds any Animal object to the zoo (Demonstrates Polymorphism)
        self.animals.append(animal)  
        return self

    def print_all_info(self):
        print("\n" + "="*30, self.name.upper(), "="*30)
        for animal in self.animals:
            animal.display_info()
    
# --- Testing Section ---
zoo1 = Zoo("John's Zoo")

# Adding animals with specific custom stats
zoo1.add_animal(Lion("Nala", health_level=500, is_king=False))
zoo1.add_animal(Lion("Simba"))
zoo1.add_animal(Tiger("Rajah" ,200, 60, stripe_pattern="striped").feed())
zoo1.add_animal(Tiger("Shere Khan"))
zoo1.add_animal(Bear("Banda"))

# Displaying the final zoo report
zoo1.print_all_info()