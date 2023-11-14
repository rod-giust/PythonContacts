#!/usr/bin/python3
import click
import os

@click.command()
@click.argument("contacts", type=click.Path(exists=False), required=0)
@click.option("-n", "--name", prompt="Ingrese el nombre: ", help="El nombre del usuario")
@click.option("-l", "--lname", prompt="Ingrese el apellido: ", help="El apellido del usuario")
@click.option("-m", "--mail", prompt="Ingrese el e-mail: ", help="El e-mail del usuario")
@click.option("-p", "--phone", prompt="Ingrese el telefono: ", help="El telefono del usuario")
def add(name, lname, mail, phone, contacts):
	filename = contacts if contacts is not None else "contacts.txt"
	with open(filename, "a+") as f:
		f.write(f"{name}: {lname}: {mail}: {phone}\n")
	print(" ")
	print("Contacto agregado!")
	print(" ")
	main()

@click.command()
@click.argument("contacts", type=click.Path(exists=True), required=False)
@click.option("-i", "--input", prompt="Ingrese el parametro de busqueda", help="El texto a buscar")
def find(input, contacts):
    filename = contacts if contacts is not None else "contacts.txt"
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        matching_lines = [line for line in lines if input.lower() in line.lower()]
        for line in matching_lines:
            print(" ")
            print(line)
            print(" ")
    main()

def menu():
    print("Libreta de contactos:")
    print("1. Agregue un nuevo contacto")
    print("2. Busqueda")
    print("3. Ayuda")
    print("4. Salir")

def help():
    print("Lorem Ipsum")
    main()

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

