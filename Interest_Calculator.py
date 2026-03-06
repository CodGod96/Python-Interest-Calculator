import sys,math,os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def main():
    while True:
        clear_screen()
        print('===================')
        print('Interest Calculator')
        print('===================')
        print(' ')
        print("1. Simple Interest")
        print("2. Compound Interest")
        print("3. Debt Interest")
        print("4. Continuous Interest")
        print("5. Exit")
        print(' ')

        option = input("Enter your choice: ")

        print(' ')
        if option == '1': sim_menu()
        elif option == '2': comp_menu()
        elif option == '3': debt_menu()
        elif option == '4': cont_menu()
        elif option == '5': sys.exit()

#simple interest calculations


def sim_menu():
    while True:
        clear_screen()
        print('-----------')
        print('Solving For')
        print('-----------')
        print(' ')
        print("1. Total")
        print("2. Principal")
        print("3. Return")

        option = input ('Solve For? : ')

        print(' ')

        #solving for total amount
        if option == '1':
            clear_screen()
            print('-----------------')
            print("Solving for Total")
            print('-----------------')
            print(' ')
            P = int(input("Principal Amount($): "))
            A = int(input("Annual Percentage Rate(%): "))
            t = int(input("Period (Years): "))
            APR = A / 100
            I = P * APR * t
            T = I + P
            print(f"Total Interest: {I}")
            print(' ')
            print(f'Total Value: {T}')
            print(' ')
            answer = input("Restart y/n?: ")
            if answer == 'y': main()
            elif answer == 'n': sys.exit()

        #solving for the principal
        elif option == '2':
            clear_screen()
            print("Solving for Principal")
            A = int(input("Annual Percentage Rate(%): "))
            t = int(input("Period (Years): "))
            T = int(input("Total Value($): "))
            APR = A / 100
            P = round(T / (1 + (APR * t)),2)
            print(f"Principal: {P}")
            print(' ')
            answer = input("Restart y/n?: ")
            if answer == 'y': main()
            elif answer == 'n': sys.exit()
        elif option == '3': main()



def comp_menu():
    while True:
        clear_screen()
        print('-----------------')
        print('Solving For')
        print('-----------------')
        print(' ')
        print("1. Total Value")
        print("2. Principal")
        print("3. Return")

        option = input ('Solve For? : ')
        if option == '1':
            clear_screen()
            print('-----------------')
            print("Solving for Total Value")
            print('-----------------')
            print(' ')
            P = int(input("Principal Amount($): "))
            A = int(input("Annual Percentage Rate(%): "))
            n = int(input('Compounding Periods(per year):'))
            t = int(input('Period (Years): '))
            APR = A / 100
            R = ( 1 + ( APR / n ) ) ** ( n * t )
            T = P * R
            I = T-P
            print(f"Total Value: {T}")
            print(f'Total Interest: {I}')
            answer = input("Restart y/n?: ")
            print(' ')
            if answer == 'y': main()
            elif answer == 'n': sys.exit()
        elif option == '2':
            clear_screen()
            T = int(input("Total Value($): "))
            A = int(input("Annual Percentage Rate(%): "))
            n = int(input('Compounding Periods(per year):'))
            t = int(input('Period (Years): '))
            X = A / 100 / n
            D = (1 + X) ** (n * t)
            P = T / D
            print(f'Principal: {P}')
            answer = input("Restart y/n?: ")
            if answer == 'y': main()
            elif answer == 'n': sys.exit()
        elif option == '3': main()



def debt_menu():
    while True:
        clear_screen()
        print('-----------------')
        print('Solving For')
        print('-----------------')
        print(' ')
        print("1. Total Value")
        print("2. Principal")
        print("3. Return")
        option = input ('Solve For? : ')
        if option == '1':
            clear_screen()
            print('-----------------')
            print("Solving for Total Value")
            print('-----------------')
            print(' ')
            P = int(input("Principal Amount($): "))
            A = int(input("Annual Percentage Rate(%): "))
            n = int(input('Compounding Periods(per year):'))
            t = int(input('Period (Years): '))
            APR = A / 100
            R = APR / n
            N = P * R
            D = ( 1 - ( 1 + R)**( -n * t ))
            M = round(N / D, 2)
            T = round(M * n * t , 2)
            I = round(T - P, 2)
            L = round((I / T) * 100, 2)
            k = round(100 - L,2)
            print(f"Total Value: {T}")
            print(f'Monthly Payment: {M}')
            print(f'Total Interest: {I}')
            print(f'Interest Percentage: {L}')
            print(f'Principal Percentage: {k}')
            print(' ')
            answer = input("Restart y/n?: ")
            print(' ')
            if answer == 'y': main()
            elif answer == 'n': sys.exit()
            if answer == 'y': main()
            elif answer == 'n': sys.exit()
        elif option == '2':
            clear_screen()
            print("Solving for Principal")
            M = int(input("Monthly Payment($): "))
            A = int(input("Annual Percentage Rate(%): "))
            n = int(input('Compounding Periods(per year):'))
            t = int(input('Period (Years): '))
            D = ( A / 100 / n)
            N = ( 1 - (( 1 + D )**( -n * t ))) * M
            P = N / D
            print(f"Principal: {P}")
            print(' ')
            answer = input("Restart y/n?: ")
            print(' ')
            if answer == 'y': main()
            elif answer == 'n': sys.exit()
        elif option == '3':main()



def cont_menu():
    while True:
        clear_screen()
        print('-----------------')
        print('Solving For')
        print('-----------------')
        print(' ')
        print("1. Total Value")
        print("2. APY")
        print("3. Return")

        option = input ('Solve For? : ')
        if option == '1':
            clear_screen()
            print('-----------------')
            print("Solving for Total Value")
            print('-----------------')
            print(' ')
            P = int(input("Principal Amount($): "))
            A = int(input("Annual Percentage Rate(%): "))
            t = int(input("Period (Years): "))
            APR = A / 100
            T = P * math.e ** (APR * t)
            print(f"Total Value: {T}")
            print(' ')
            answer = input("Restart y/n?: ")
            print(' ')
            if answer == 'y': main()
            elif answer == 'n': sys.exit()
        elif option == '2':
            clear_screen()
            print('---------------')
            print("Solving for APY")
            print('-----------------')
            print(' ')
            A = int(input("Annual Percentage Rate(%): "))
            t = int(input("Period (Years): "))
            APR = A / 100
            APY = math.e ** (APR * t)
            print(f"Total Value: {APY}")
            print(' ')
            answer = input("Restart y/n?: ")
            print(' ')
            if answer == 'y': main()
            elif answer == 'n': sys.exit()
        elif option == '3': main()


main()
