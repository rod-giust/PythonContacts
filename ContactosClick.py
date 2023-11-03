#!/usr/bin/python3
import click
import os

def add():
    name = input("Ingrese el Nombre: ")
    last_name = input("Ingrese el Apellido: ")
    email = input("Ingrese el e-mail: ")
    phone = input("Ingrese el telefono: ")
    with open("contacts.txt", "a") as file:
        file.write(f"{name},{last_name},{email},{phone}\n")
    print(" ")
    print("Contacto agregado!")
    print(" ")

def find():
    keyword = input("Ingrese el dato a buscar: ")
    with open("contacts.txt", "r") as file:
        contacts = file.readlines()
        for contact in contacts:
            if keyword in contact:
                print(contact.strip())


def menu():
    print("Libreta de contactos:")
    print("1. Agregue un nuevo contacto")
    print("2. Busqueda")
    print("3. Ayuda")
    print("4. Salir")

def help():
    print("Lorem Ipsum")

@click.command()
def main():
    while True:
        menu()
        choice = input("Cual es su opcion: ")
        if choice == "1":
            add()
        elif choice == "2":
            find()
        elif choice == "3":
            help()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

