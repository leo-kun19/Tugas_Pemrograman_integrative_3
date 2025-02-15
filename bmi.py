class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
    
    def BMI_Value(self):
        return self.weight / (self.height ** 2)
    
    def __eq__(self, other):
        if isinstance(other, BMI):
            return self.weight == other.weight and self.height == other.height
        return False
