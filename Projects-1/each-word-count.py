"""
Count Words in a String - Counts the number of individual words in a string.
For added complexity read these strings in from a text file and generate a summary.
"""
class Words:
    def each_word_count(self,text):
        self.sentances = list()
        self.words = list()
        self.word_counts = dict()
        self.lines = text.split('\n')
        
        for line in self.lines:
            self.sentances.extend(line.split("."))
        
        for sentance in self.sentances:
            self.words.extend(sentance.split(" "))
        
        for word in self.words:
            if word in self.word_counts.keys():
                self.word_counts[word] += 1
            else:
                self.word_counts[word] = 1
        return self.word_counts
        
        # print(self.words)

x = Words()

filename = input("Enter file name : ")
if filename == '':
    filename = "demo.txt"

file = open(filename,'r')

y = x.each_word_count(file.read())
print(y)

