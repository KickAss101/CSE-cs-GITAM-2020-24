#! /usr/bin/python3
import string

def panagram(s):
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    for c in alpha:
        if c not in s.lower():
            return False
    return True

if __name__ == '__main__':
    # "The quick brown fox jumps over the lazy dog" -> Panagram
    s = input("Enter a sentence: ")
    
    if panagram(s):
        print("Given sentence is panagram")
    else:
        print("Given sentence is not panagram")
