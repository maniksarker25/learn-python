class Calculator:
    brand = 'Casio MS990'
    def add(self,num1,num2):
        return num1 + num2

    # deduct method
    def deduct(self,num1,num2):
        return num2 - num1

   #multiple
    def multiple(self,num1,num2):
        return num1 * num2


my_calculator = Calculator()

sum = my_calculator.add(2,3)
deduct = my_calculator.deduct(4,2)
multify = my_calculator.multiple(3,3)

print(sum," ",deduct," ", multify)
