#In Python, when defining methods inside a class, first parameter is always self. 
# It is not a keyword, but a naming convention that plays a key role in Python’s object-oriented programming. 
# The self parameter represents instance of the class itself, allowing you to access and modify its attributes and methods.

class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Set instance attribute
        self.model = model  # Set instance attribute

    def display(self):
        return self.brand, self.model

# Create an instance of Car
car1 = Car("Toyota", "Corolla")

# Call the display method
print(car1.display())


########################################################################
class gfg:
    def __init__(self, topic):
        self._topic = topic  # Store parameter value in instance variable

    def topic(self):
        print("Topic:", self._topic)  # Access the renamed variable

# Creating an instance of gfg
ins = gfg("Python")

# Calling the topic method
ins.topic()