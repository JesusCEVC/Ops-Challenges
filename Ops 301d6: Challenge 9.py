#!/usr/bin/env python3

# Create the file, then add the lines.
with open('Boku_no_Hero_Academia.txt', 'a') as Dynamight:
    first_line = "I enjoy BNHA.\n"
    Dynamight.write(first_line)
    Dynamight.write("The recent seasons make it worth the middle series slog.\n")
    Dynamight.write("The creativity is palpable!")

# print the first line of the file to the screen
with open('Boku_no_Hero_Academia.txt') as Dynamight:
    print(Dynamight.readline())

# delete the file
import os
os.remove('Boku_no_Hero_Academia.txt')
