"""
Count Vowels - Enter a string and the program counts the number of vowels in
the text. For added complexity have it report a sum of each vowel found
"""

class Vowels:
    def __init__(self, text):
        self.vowel = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        self.text = list((text).lower())
        for letter in self.text:
            if letter in self.vowel.keys():
                self.vowel[letter] += 1

    def count_each_vowel(self):
        return self.vowel

    def count_vowels(self):
        return sum(self.vowel.values())


text = input("Enter a string/text : ")

x = Vowels(text)

print(f"\nTotal vowels in given string are : {x.count_vowels()} \n")

print(f"--- Count of each vowel in give string ---")
for key, value in x.vowel.items():
    print(f"{key} : {value}")
