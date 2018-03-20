#!/usr/bin/env python3

def char_count(str):
    for i in set(str):
        print(i,str.count(i))

if __name__ == '__main__':
    in_word = input("Please enter something:\n")
    char_count(in_word)
