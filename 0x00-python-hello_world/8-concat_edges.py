#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(str[str.find("object"):str.find("language")], end="")
print(f"{str[str.find('with'):str.find('very')]}{str[:6]}", end="\n")
