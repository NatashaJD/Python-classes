import string
class RealNumber:
    def __init__(self, value) -> None:
        self.value = value
        self.convert ()
        
    def __float__ (self):
        return self.value
    def convert (self):
        for i in string.ascii_lowercase:
            if i in self.value:
                self.value = self.value.replace(i,"")
                
        for i in string.ascii_uppercase:
            if i in self.value:
                self.value = self.value.replace(i,"")
                
        self.value = float(self.value.strip())
        return self.value
    
    
num = RealNumber("Judy 2023")
print(float(num))
    
    