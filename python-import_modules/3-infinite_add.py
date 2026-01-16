#!/usr/bin/python3
import sys

if __name__ == "__main__":
    somme_totale = 0
    try:
        nombres = list(map(int, sys.argv[1:]))
        for n in nombres:
            somme_totale += n
    except ValueError:
        print("Veuillez ne fournir que des nombres entiers en arguments.")

    print(somme_totale)
