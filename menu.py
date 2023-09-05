import os
from menu_employees import menu_employees
def main_menu():
    op = -1
    while(op != 0):
        print("[1]Employees")
        print("[2]Projects")
        print("[0]Exit")
        op = int(input("Choose an option:"))
        
        if op == 0:
            exit()
        elif op == 1:
            menu_employees()
        elif op == 2:
            os.system('cls || clear')
            #menu_project()
        else:
            os.system('cls || clear')
            print("Invalid option! Please try another one!")
        


def main():    
    os.system('cls || clear')
    print("======================Main Menu======================")
    main_menu()
    

if __name__ == '__main__':
    main()