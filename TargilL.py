import string
# import re
# import matplotlib.colors as mc

# Questions 1,2: 
def counter(Text):
    num_words = 0
    num_lines = 0
      
    with open("TText.txt", 'r') as f:
        for line in f:
         
            num_lines += 1
              
            # declaring a variable word
            # and assigning its value as Y
            # because every file is 
            # supposed to start with 
            # a word or a character
            word = 'Y'
              
            # loop to iterate every
            # line letter by letter
            for letter in line:
                  
                # condition to check 
                # that the encountered character
                # is not white space and a word
                if (letter != ' ' and word == 'Y'):
    
                    num_words += 1
                      
                    # assigning value N to 
                    # variable word because until
                    # space will not encounter
                    # a word can not be completed
                    word = 'N'
                      
                # condition to check 
                # that the encountered character
                # is a white space
                elif (letter == ' '):
                      
                    # assigning value Y to
                    # variable word because after
                    # white space a word
                    # is supposed to occur
                    word = 'Y'
    
    print("1.Number of lines in text file: ", num_lines) 
    print("2.Number of words in text file: ", num_words)
      
# Driver Code: 
if __name__ == '__main__': 
    fname = 'File1.txt'
    try: 
        counter(fname) 
    except: 
        print('File not found')




# Questions 3,5,8:
text = open("TText.txt", "r")
counter = 0
d = dict()
for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()
  
    # Convert the characters in line to 
    # lowercase to avoid case mismatch
    line = line.lower()
  
    # Remove the punctuation marks from the line
    line = line.translate(line.maketrans("", "", string.punctuation))
  
    # Split the line into words
    words = line.split(" ")
  
    # Iterate over each word in line
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
# 8888888888888888888888888888888888888888888888888888888888888
# Question 8:
# for key, value in d.items():
#     if key in mc.cnames:
#       print(key,':',value)
# 8888888888888888888888888888888888888888888888888888888888888

for key in list(d.keys()):
    if(d[key]==1):
        counter = counter + 1
print("3.The amount of unique words in the file:",counter)
Thesumofeachword = d.values()
Maxi_word = max(Thesumofeachword)
for key in d:
    if(d[key]==Maxi_word):
        print("5.a.The most popular word in the text is: ",key)
for key in list(d.keys()):
    if(key == 'am' or key == 'are' or key == "don't" or key == 'that' or key == 'the' or key == 'it' or key == 'was' or key == 'of'  or key == 'to'  or key == 'a'  or key == 'and'  or key == 'in' or key == '' ):
       del(d[key])
Thesumofeachword2 = d.values()
Maxi_word2 = max(Thesumofeachword2)
for key in d:
    if(d[key]==Maxi_word2):
       print("5.b.The popular word Most that is not a word with syntactic meaning: ",key)

# Question 4:
text = open("TText.txt", "r")

fileContext = text.read()
splitFile = fileContext.split('.')
d = dict()
sumOfAllLinesLength = 0
maxLength = 0
for i, value in enumerate(splitFile):
    length = len(value.split())
    sumOfAllLinesLength += length
    if length > maxLength:
        maxLength = length
print("4.a. Average sentence length in text:", sumOfAllLinesLength / (len(splitFile)-1))
print("4.b. Maximum sentence length in text:", maxLength)

# Question 8:
print("8. is written here in a comment. It works at GDB Online")



