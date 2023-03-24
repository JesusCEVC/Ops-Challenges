#!/usr/bin/env python3

# Create the file, then add the lines.
with open('Boku_no_Hero_Academia.txt', 'a') as Dynamight:
    Dynamight.write("I enjoy BNHA.\n")
    Dynamight.write("The recent seasons make it worth the middle series slog.\n")
    Dynamight.write("The creativity is palpable!\n")

# print the first line of the file to the screen
with open('Boku_no_Hero_Academia.txt', 'r') as Dynamight:
    print(Dynamight.readline())

# delete the file
import os
os.remove('Boku_no_Hero_Academia.txt')
