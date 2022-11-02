# Microsoft gives you reward if you search on bing
# this program lets you grab those in quick time
import string
import random
import webbrowser

lowercase_letters = string.ascii_lowercase
def lowercase_word():
    word = ''
    random_word_length = random.randint(1,10)
    while len(word) != random_word_length:
        word += random.choice(lowercase_letters)
    return word #Returns the word


random_word = lowercase_word()
# do 30 searches
for i in range(30):
    random_word = lowercase_word()
    webbrowser.open('https://www.bing.com/search?q='+random_word)

