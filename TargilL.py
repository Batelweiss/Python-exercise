import string
# import re
# import matplotlib.colors as mc

# Questions 1,2: 
def counter(Text):
  
    # variable to store total word count
    num_words = 0
      
    # variable to store total line count
    num_lines = 0
      
      
    # opening file using with() method
    # so that file gets closed 
    # after completion of work
    with open("TText.txt", 'r') as f:
          
        # loop to iterate file
        # line by line
        for line in f:
              
            # incrementing value of 
            # num_lines with each 
            # iteration of loop to
            # store total line count 
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
                      
                    # incrementing the word
                    # count by 1
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
                      
                    # incrementing the space
                    # count by 1
                    # num_spaces += 1
                      
                    # assigning value Y to
                    # variable word because after
                    # white space a word
                    # is supposed to occur
                    word = 'Y'
    
       # printing total line count
    print("1.Number of lines in text file: ", num_lines)
    
    # printing total word count 
    print("2.Number of words in text file: ", num_words)
      
# Driver Code: 
if __name__ == '__main__': 
    fname = 'File1.txt'
    try: 
        counter(fname) 
    except: 
        print('File not found')




# Questions 3,5:
# Open the file in read mode
text = open("TText.txt", "r")
counter = 0
  
# Create an empty dictionary
d = dict()
  
# Loop through each line of the file
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
        # wword = re.sub('[-,;:".!(){-}/?]+', '', word)
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1
# 8888888888888888888888888888888888888888888888888888888888888
# Question 8:
# colors={}
# for key, val in d.items():
#     if key in mc.cnames:
#       print(key,':',val)
# 8888888888888888888888888888888888888888888888888888888888888

# Print the contents of dictionary
# for key in list(d.keys()):
#     print(key, ":", d[key])
for key in list(d.keys()):
    if(d[key]==1):
        counter = counter + 1
print("3.The amount of unique words in the file:",counter)
z = d.values()
Maxi_word = max(z)
for key in d:
    if(d[key]==Maxi_word):
        print("5.a.The most popular word in the text is: ",key)
for key in list(d.keys()):
    if(key == 'am' or key == 'are' or key == "don't" or key == 'that' or key == 'the' or key == 'it' or key == 'was' or key == 'of'  or key == 'to'  or key == 'a'  or key == 'and'  or key == 'in' or key == '' or key == 'i' or key == 'I'):
       del(d[key])
p = d.values()
Maxi_word2 = max(p)
for key in d:
    if(d[key]==Maxi_word2):
       print("5.b.The popular word Most that is not a word with syntactic meaning: ",key)

# Question 4:
text = open("TText.txt", "r")
d = dict()
for line in text:
     d[line] = len(line.split())
x = 0
for key in d:
    x = x + d[key]
z = d.values()
Maximum_length = max(z)
Average = x /(len(d) - 1)
print("4.a. Average sentence length in text: ", Average)
print("4.b. Maximum sentence length in text: ", Maximum_length)

# Question 8:
print("8. is written here in a comment. It works at GDB Online")



