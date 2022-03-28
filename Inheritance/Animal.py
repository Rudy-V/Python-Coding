# This is the base class
class Animal (object):
    '''
    This is the base class for the Animal class
    '''
    def __init__(self, numteeth, spots, weight):
        self.numteeth = numteeth
        self.spots = spots
        self.weight = weight

# This class inherits from the Animal base class
class Lion (Animal):
    '''
    This inherits functions and variables from the Animal class
    '''
    def __init__(self, numteeth, spots, weight):
        super().__init__(numteeth, spots, weight)
        self.lion_type = "Lion Type"

    # This function calculates the type of lion
    def calc_lion_type(self):
        if self.weight <= 80:
            self.lion_type = "Cub"
        elif self.weight <= 120:
            self.lion_type = "Female"
        else:
            self.lion_type = "Male"

    # This function prints out the type of lion
    def print_lion_type(self):
        self.calc_lion_type()
        print(f"This is lion is a {self.lion_type}")

class Cheetah (Animal):
    '''
    This inherits functions and variables from the Animal Class
    '''
    def __init__(self, numteeth, spots, weight):
        super().__init__(numteeth, spots, weight)
        self.cheetah_park_array = ["Oudtshoorn","Somerset West","Albertinia", "Parys", "Bloemfontein"]

    def print_cheetah(self):
        print(f"This cheetah has {self.numteeth} teeth, spots and weighs {self.weight}KG.")
        print("Towns and cities where you can see cheetahs:")
        for i in self.cheetah_park_array:
            print(i)
        

# This creates a Lion object and assigns values to it
a = Lion(66, False, 180)
a.print_lion_type()

# This creates a Cheetah object
b = Cheetah(42, True, 75)
b.print_cheetah()
