import re

def is_palindrome(sentence):
    sentence = re.sub(r'[^A-Za-z]', "", (sentence.lower()))
    if len(sentence) <=1:
        return True
    elif sentence[0] == sentence[len(sentence)-1]:
        return is_palindrome(sentence[1:-1])
    else:
        return False

def main():
    sentence = input("Enter your string: ")
    is_palindrome(sentence)
    check = is_palindrome(sentence)
    if check:
       print("{} is a palindrome".format(sentence))
    else:
       print("{} is not a palindrome".format(sentence))

if __name__ == '__main__':
   main()
