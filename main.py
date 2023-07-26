#import potrzebnych modułów

import sys
import random

#definicja funkcji game
def game():

    print(f"Cześć! Zagrajmy w wisielca!\n")

    #zbiór słów
    zbior_slow = ['szynka', 'elektroniczny', 'losowe', 'warszawa', 'archeologia', 'cywilizacja', 'klawiatura', 'paralotnia', 'ekosystem', 'kontowersja']
    slowo = random.choice(zbior_slow)
    proby = ''
    kolejka = 10
    while kolejka > 0:
        blad = 0
        for char in slowo:
            if char in proby:
                print(char)
            else:
                print('_')
                blad+=1
        if blad == 0:
            print("Gratulacje")
            choice = input("Chcesz zagrać jeszcze raz? T/N")

            if "T" in choice:
                game()
            elif "N" in choice:
                sys.exit()
            else:
                print("Chcesz zagrać jeszcze raz? T/N")
        guess = input("Podaj literę:")
        proby+=guess
        if guess not in slowo:
            kolejka-=1
            print("Źle!")
            print(f"Masz jeszcze {kolejka} prób!")
            if kolejka == 0:
                print("Niestety przegrałeś!")
                choice = input("Chcesz zagrać jeszcze raz? T/N")
                if "T" in choice:
                    game()
                elif "N" in choice:
                    sys.exit()
                else:
                    print("Chcesz zagrać jeszcze raz? T/N")

game()