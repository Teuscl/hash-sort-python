import os
import time
from employees import Employees

array_emp = []
num_emp = 0
def binary_search(id_to_find):
    
    left, right = 0, len(array_emp)-1    
    while left<=right:
        mid = (left + right) // 2
        if array_emp[mid].id == id_to_find:
            return array_emp[mid]
        elif array_emp[mid].id < id_to_find:
            left = mid + 1
        else:
            right = mid - 1
            
    return None #Return None if the value was not found
            


def insert_emp():    
    os.system('cls || clear') # Clear the screen
    global array_emp
    #Check if the array has more than 500 registers
    if len(array_emp)>500:
        print("Max number of employees registered!")
        input("Press any key to return...")        
    
    aux_id = int(input("Please enter the employee's ID: "))
    
    #Call the method function binary_search to check if the id entered exists or not
    if binary_search(aux_id) is None:
        name = (input("Please enter the employee's name: "))
        
        #Check if the string name is not empty or a whitespace
        if len(name) == 0 or name == " ":
            print("Please enter a valid name!")
            time.sleep(3)
            return    
        else:
            try:
                salary = float(input("Enter the employee's salary: "))
                if salary < 0:
                    raise ValueError("Salary can't be negative value")
            except ValueError:
                print("Invalid salary! Try another one.")
                time.sleep(2)
                return
        
        #Create the object     
        temp = Employees(aux_id, name,  salary)
        #Insert the object into the array and sort by id
        array_emp.append(temp)        
        array_emp = sorted(array_emp, key=lambda x: x.id)        
        print("Employee inserted successfully!!!")
        time.sleep(2)
        
    else:
        print("ID already in use! Please try another one.")
        time.sleep(2)
        return
    
def edit_emp():
    os.system('cls || clear')
    id = int(input("Please enter the employee's ID: "))
    search_res = binary_search(id)
    
    if search_res is not None:
        print(f"Employee ID: {search_res.id}, Name: {search_res.name}, Salary: {search_res.salary}")
        
        print("Is that the employee desired?\ny-yes\nn-no")
        ans = input()
        if ans in ['y', 'yes','Y','YES']:
            print("What do you want to edit?")
            print("1-Name")
            print("2-Salary")
            op = int(input())
            if op == 1:
                new_name = input("Please enter the new name: ")
                search_res.name = new_name #Use the property setter to update the name
                input("Name updated successfuly! Press enter to return to menu.")
            elif op == 2:
                try: #try except to avoid ValueError and assure that the inputed value is numeric
                    new_salary = float(input("Please enter the new salary: "))
                    if new_salary < 0:
                        raise ValueError("Salary can't be a negative value")
                    search_res.salary = new_salary  # Use the property setter to update the salary
                    print("Salary updated successfully!")
                    input("Press Enter to return to the menu.")
                except ValueError:
                    print("Invalid salary! Please enter a valid number.")
                    input("Press Enter to return to the menu.")                
            else:
                print("Invalid option!")
                time.sleep(2)
                
        elif ans in ['n','no','N','NO']:
            input("Press enter to return to menu!")
            return
        else:
            input("Invalid option! Press enter to continue")
    else:
        print("Employee not found! Please try another ID")
        input()
        
        
def delete_emp():
    os.system('cls || clear')
    id = int(input("Please enter the employee's ID: "))
    search_res = binary_search(id)
    if search_res is not None:                
        print(f"Employee ID: {search_res.id}, Name: {search_res.name}, Salary: {search_res.salary}")
        ans = input("Are you sure that you want to delete this register?\ny-yes n-no\n")
        if ans in ['y', 'yes','Y','YES']:
            array_emp.remove(search_res)
        elif ans in ['n','no','N','NO']:
            input("Press enter to return to menu")
            return
        else:
            input("Invalid option! Press enter to continue")
            
    else:
        input("Id not found! Press enter to continue...")
    

def print_employees():
    os.system('cls || clear')
    print("#List of employees#")
    for employee in array_emp:
        print(f'-> {employee}')
    input("Press any key to continue....")      

def salaries_higher10k():
    
    ##Implementar algoritmo de ordenação de O(n²)
    os.system('cls || clear')
    print("##Salaries Higher than 10k##")
    for employee in array_emp:
        if employee.salary > 10000:
            print(f'-> {employee}')
    input("Press any key to continue....")
                        



def menu_employees():
    op = -1
    while(op != 0):
        os.system('cls || clear')
        print("[1]Insert employee")
        print("[2]Remove employee")
        print("[3]Edit employee")
        print("[4]List employee's")
        print("[5]Search employee by ID")
        print("[6]List employees by salaries higher than 10k")
        print("[7]Search employee by ID")
        print("[0]Back to Main Menu")
        
        op = int(input("Choose an option:"))
        
        if op == 0:
            exit()
        elif op == 1:
            insert_emp()            
        elif op == 2:
            delete_emp()        
        elif op == 3:
            edit_emp()                
        elif op == 4:
            print_employees()     
        elif op == 5:
            os.system('cls || clear')
            id = int(input("Please enter the employee's ID:"))
            search_res = binary_search(id)
            if search_res is not None:
                print(f"Employee ID: {search_res.id}, Name: {search_res.name}, Salary: {search_res.salary}")
                input("Press enter to continue...")
            else:
                input("Id not found! Press enter to continue...")
        elif op ==6:
            salaries_higher10k()        
        elif op == 7:
            print()
            
                
        else:
            os.system('cls || clear')
            print("Invalid option! Please try another one!")