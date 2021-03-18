"""
Binary to Decimal and Back Converter - 

Develop a converter to convert a decimal number to binary or 
a binary number to its decimal equivalent.
"""

class NumberSystemConversions:
    def binary_to_decimal(self, binary):
        self.binary = list(str(binary))
        self.dummy = list()
        self.power = 0
        for i in (self.binary[::-1]):
            self.dummy.append(int(i)*pow(2, self.power))
            self.power += 1
        return sum(self.dummy)

    def decimal_to_binary(self, decimal):
        self.dummy = list()
        while(decimal):
            if decimal % 2 == 0:
                self.dummy.append(0)
                decimal = int(decimal/2)
            else:
                self.dummy.append(1)
                decimal = int((decimal - 1)/2)

        return "".join(map(str, self.dummy[::-1]))


x = NumberSystemConversions()
choice = ""
while(choice != "q"):
    print("\n---Number System Conversions---")
    print("1. Decimal to Binary\n2. Binary to Decimal\n3.Press 'q' to Quit")
    choice = input("Enter your Choice : ")
    if choice == '1':
        try:
            dec = int(input("Enter a decimal number : "))
            print("-"*50)
            print(f"{dec} in Binary is {x.decimal_to_binary(dec)}")
        except :
            print("Enter a valid choice")
    elif choice == '2':
        try:
            binary = int(input("Enter a binary number: "))
            print("-"*50)
            print(f"{binary} in Decimal is {x.binary_to_decimal(binary)}")
        except :
            print("Enter a valid choice")
