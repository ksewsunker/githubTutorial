class Animal:
 
    def __init__(self,name, numteeth, spots, colour, sound):
        self.name = name
        self.numteeth = numteeth
        self.spots = spots
        self.colour = colour
        self.weight = weight
        self.sound = sound

class Lion(Animal):
    weight = 0

    def __init__(self, name, numteeth, spots, colour, sound, weight):
        super ().__init__(name, numteeth, spots, colour, sound)

    def get_weight(self, weight):
        for item in weight:
            self.item.append(weight)
        
    
    def get_LionType (self, weight):
    
        if int(weight) <= 80:
            return ("Cub")
        elif int(weight) <= 120:
            return ("Female")
        elif int(weight) >= 120:
            return ("Male")

    def get_description(self):
        return self.get_LionType(weight) + self.numteeth + self.spots + self.colour + self.sound

    
weight = input("What is the weight of the Lion?: ")
l = Lion('Lion ', ' lion' ' has 50 teeth', ' ,no spots', ' is brown in colour', ' and roars.' , weight)
print(l.get_LionType(weight))
print(l.get_description())



class Cheetah(Animal):
    age = [5, 12, 7]
    
    def __init__(self, name, numteeth, spots, colour, sound, age):
        super ().__init__(name, numteeth, spots, colour, sound)
        self.age = age           
    
    def get_CheetahAge (self):
        return self.age
       
    def get_description(self):
        return str(self.age) + self.numteeth + self.spots + self.colour + self.sound
    
age = [5, 12, 7]
c = Cheetah('Cheetah ', ' Cheetah' ' has 77 teeth', ' , spots', ' is brown and black in colour', ' and purrs.', (age))
print("Cheetah Ages: ")
print(c.get_CheetahAge())
print(c.get_description())
