class RealNumber:
    def __init__(self, value):
        if isinstance(value, (int, float)):
            self.value = value
        else:
            raise ValueError("Value must be a real number (int or float)")
        
        
    def __str__(self) -> str:
        return str(self.value)
    
    def __repr__(self) -> str:
        return f"RealNumber({self.value})"
    
    # Arithmetic operations
    def __add__(self, other):
        if isinstance(other, RealNumber):
            other = other.value
            return RealNumber(self.value + other)
    
def __sub__(self, other):
    if isinstance(other, RealNumber):
        other = other.value
        return RealNumber(self.value - other)
    
def __mul__(self, other):
    if isinstance(other, RealNumber):
        other = other.value
        return RealNumber(self.value * other)
    
def __truediv__(self, other):
    if isinstance(other, RealNumber):
        other = other.value
    if other == 0:
        raise ValueError("Math Error, cannot divide by zero")
    return RealNumber(self.value / other)

#Comparison

def __eq__(self, other):
    if isinstance(other, RealNumber):
        other = other.value
    return self.value == other

def __ne__(self, other):
    if isinstance(other, RealNumber):
        other = other.value
        return self.value != other
    
def __lt__ (self, other):
    if isinstance(other, RealNumber):
        other = other.value
    return self.value < other

def __le__(self, other):
    if isinstance(other, RealNumber):
        other = other.value
    return self.value <= other

def __gt__(self, other):
    if isinstance(other, RealNumber):
        other = other.value
    return self.value > other

def __ge__(self, other):
    if isinstance(other, RealNumber):
        other = other.value
    return self.value >= other

# Example usage
if __name__ == "__main__":
    a = 5
    b = 3
    
    print(a + b)  # Output: RealNumber(8)
    print(a - b)  # Output: RealNumber(2)
    print(a * b)  # Output: RealNumber(15)
    print(a / b)  # Output: RealNumber(1.6666666666666667)
    
    print(a == b)  # Output: False
    print(a != b)  # Output: True
    print(a < b)   # Output: False
    print(a <= b)  # Output: False
    print(a > b)   # Output: True
    print(a >= b)  # Output: True
