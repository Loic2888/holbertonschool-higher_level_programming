#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = f"{str}"[39:-54] + " " + f"{str}"[107:-18] + " " + f"{str}"[:-123]

print(str)
