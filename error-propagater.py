class ScientificNumber():
    def __init__(self, num: float, precision: int, power: int):
        self.num = num
        if precision <= 0:
            assert "Precision must be positive."
        self.precision = precision
        self.power = power
    
class Parser():
    def __init__(self, num_str: str):
        self.num_str = num_str
    
    def parse(self) -> ScientificNumber:
        try:
            num = int(self.num_str)
            return self.parse_int()
        except:
            return self.parse_float()
            
    def parse_int(self) -> ScientificNumber:
        power = 0
        num = int(self.num_str)
        while abs(num) >= 10:


    def parse_float(self) -> ScientificNumber:
        pass


class Adder():
    def __init__(self, num1: ScientificNumber, num2: ScientificNumber):
        pass

class Subtracter():
    def __init__(self, num1: ScientificNumber, num2: ScientificNumber):
        pass

class Multiplier():
    def __init__(self, num1: ScientificNumber, num2: ScientificNumber):
        pass

class Divider():
    def __init__(self, num1: ScientificNumber, num2: ScientificNumber):
        pass