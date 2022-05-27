# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    # Open for text file for reading text
    file = open(filename, "r")
    # storing file text into a variable
    file_txt = file.read()
    # print(type(file_txt))
    
    return file_txt


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    # extract words from string
    words_text = text.split()
    # print(words_text)
    print(type(words_text))
    # loop through the list words_text
    # for word in words_text:
    #     print(word)
    # for word in set(words_text):
    #     print(word)

    # used set method to convert any of the iterable to sequence of iterable elements with distinct elements
    # then used the count method to count the occurrence of a word in the text
    # dict method is to store the result in a dictionary at once
    word_count_dic = dict((word,words_text.count(word)) for word in set(words_text))
    

    # return {"as": 10, "would": 20}
    return word_count_dic


# testing read_file_content function
# txt = read_file_content("./story.txt")
# print(txt)

# testing count_words function
count = count_words()
print(count)