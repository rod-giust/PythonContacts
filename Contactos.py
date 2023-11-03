#!/usr/bin/python3
import click
import json

def main():
# try:
#    with open("contacts.txt", "r") as file:
#	contacts = json.load(file)
# except FileNotFoundError:
    mylist = []
    while True:
        operation = input('''
Menu de contactos:
[1] Crear
[2] Buscar
[3] Ayuda
[4] Salir

''')
        if operation == '1':
            print("Introduzca el Nombre: ")
            name = str(input())
            mylist.append(name)
            print("Introduzca el Apellido: ")
            lname = str(input())
            mylist.append(lname)
            print("Introduzca el Telefono: ")
            phone = int(input())
            mylist.append(phone)
            print("Introduzca el email: ")
            email = str(input())
            mylist.append(email)
            
            with open("contacts.txt", "w") as file:
            	json.dump(mylist, file)
            print("Contacto guardado")

        elif operation == '2':
            nameSearch = input("Introduzca el Nombre o numero para buscar: \n")
            if nameSearch in mylist:
            	print(f"Encontrado el siguiente Contacto:\n Nombre: {name}\n Apellido: {lname}\n Telefono {phone}\n email: {email}\n")
            else:
            	print(f"no se encontro {nameSearch}")

        elif operation == '3':
            print(mylist)

        elif operation == '4':
            break

        else:
            print("Invalid choice. Please try again.")

main()
