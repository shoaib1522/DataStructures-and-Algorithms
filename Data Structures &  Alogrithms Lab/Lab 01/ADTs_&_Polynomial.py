class Item:
    def __init__(self, coefficient, power):
        self.coefficient=coefficient
        self.power=power
    def __str__(self):
        return f"{self.coefficient}x^{self.power}"
        
class Polynomial:
    def __init__(self):
        self.list=[]
    def addTerm(self, coefficient, power):
        object=Item(coefficient, power)
        self.list.append(object)
        return self
    def getDegree(self):
        degree=0
        for element in self.list:
            if degree<element.power:
                degree=element.power
        return degree
    def getCoefficient(self, power):
        try:
            for element in self.list:
                if power==element.power:
                    return element.coefficient
        except:
            raise Exception("No, Element exists of this power in the Polynomial")
    def setCoefficient(self, newCoefficient, power):
        try:
            for index in range(len(self.list)):
                element=self.list[index]
                if element.power==power:
                    self.list[index]=Item(newCoefficient, power)
                    return self
        except:
            raise Exception("No, Element exists of this power in the Polynomial")
    def evaluate(self, value):
        evaluation=0
        for element in self.list:
            evaluation+=(element.coefficient)*((value)**(element.power))
        return evaluation
    def derivative(self):
        derivative=Polynomial()
        for element in self.list:
            term_coeff=(element.coefficient * element.power)
            if element.power!=0:
                term_power=element.power-1
                derivative.addTerm(term_coeff,term_power)
            else:
                derivative.addTerm(term_coeff, element.power)
        return derivative
    def antiDerivative(self, constant):
        antiDerivative=Polynomial()
        for element in self.list:
            if element.power>0:
                term_power= element.power+1
                term_coeff=element.coefficient//term_power
                antiDerivative.addTerm(term_coeff, term_power)
        return f"{antiDerivative} + {constant}"
    def __add__(self, other):
        add=Polynomial()
        for i in range(len(self.list)):
            element=self.list[i]
            for j in range(len(other.list)):
                element_oth=other.list[j]
                if element.power==element_oth.power:
                    coefficient=element_oth.coefficient+element.coefficient
                    add.addTerm(coefficient,element.power)
        return add            
    def __sub__(self, other):
        pass
    def __mul__(self, other):
        pass
    def __str__(self):
        string=""
        for element in self.list:
            if element.coefficient>0:
                string+=f"+{element.coefficient}x^{element.power}"
            elif element.coefficient==0:
                string+=f"+{element.coefficient}x^{element.power}"
            else:
                string+=f"{element.coefficient}x^{element.power}"
        return string
    def clear(self):
        for element in self.list:
            self.setCoefficient(0,element.power)
        return self
    def addToCoefficient(self, coefficient, power):
        for element in self.list:
            if element.power==power:
                self.setCoefficient(element.coefficient+coefficient,power)
        return self

def main():
    p1 = Polynomial() 
    p1.addTerm(4, 5) 
    p1.addTerm(7, 3) 
    p1.addTerm(-1, 2) 
    p1.addTerm(9, 0) 
    
    p2 = Polynomial() 
    p2.addTerm(6, 4) 
    p2.addTerm(3, 2) 
    p2.addTerm(2, 1) 
    
    print ("P1: ", p1) 
    print ("P2: ", p2)
    
    print ("P1 Degree: ", p1.getDegree()) 
    print ("P2 Degree: ", p2.getDegree()) 
    
    print ("P1 coefficient at power 5 is: ",p1.getCoefficient(5))
    print ("P2 coefficient at power 2 is: ",p2.getCoefficient(1))
    
    evaluate=p1.evaluate(2)
    print("Evaluation of P1 at 2 is: ",evaluate)
    evaluate=p2.evaluate(2)
    print("Evaluation of P2 at 2 is: ",evaluate)
    
    result = p1 + p2 
    print("Addition result:", result) 
    
    
    result_derivative = p1.derivative() 
    print("Derivative result:", result_derivative) 
    
    result_anti_derivative = result_derivative.antiDerivative(3) 
    print("Anti-derivative result:", result_anti_derivative)
    
    clear_method=p1.clear()
    print("Cleared Polynomial P1: ",clear_method)    
    clear_method=p2.clear()
    print("Cleared Polynomial P2: ",clear_method)
main()
        
        
        