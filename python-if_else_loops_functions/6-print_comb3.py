#!/usr/bin/python3
combinations = []
for i in range(10):
    for j in range(i + 1, 10):
        combinations.append(f"{i}{j}")
print(", ".join(combinations))
