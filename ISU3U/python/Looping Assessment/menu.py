import Rock_Paper_Seissor, Square_Roots, Permutations, Native_American_Problem
import os

def main():
    while True:
        num = ''
        while not num.isdigit():
            num = input('\n1..  Square Roots \n2..  Rock_Paper_Seissor \n3..  Permutations \n4..  Native_American_Problem \n9..  Exit\n\n')
        num = int(num)
        os.system('cls')
        if num == 1:
            Square_Roots.main()
        elif num == 2:
            Rock_Paper_Seissor.main()
        elif num == 3:
            Permutations.main()
        elif num == 4:
            Native_American_Problem.main()
        elif num == 9:
            break
        else:
            print('check your number')

os.system('cls')
print('Welcome!')
main()
print('Thank you for using this program.')
input()