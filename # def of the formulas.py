def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Erreur : Division par zéro impossible")
    return a / b

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def calculatrice():
    print("Bienvenue dans la calculatrice.")
    print("Opérations disponibles :")
    print("1. Addition (+)")
    print("2. Soustraction (-)")
    print("3. Multiplication (x)")
    print("4. Division (/)")
    
    while True:
        try:
            operation = input("\nChoisissez l'opération (+, -, *, /) ou tapez 'q' pour quitter : ")
            if operation == 'q':
                print("Au revoir!")
                break
            if operation not in ['+', '-', '*', '/']:
                print("Opération invalide. Veuillez choisir parmi +, -, *, /.")
                continue
            
            # Saisie des nombres
            a = float(input("Entrez le premier nombre : "))
            b = float(input("Entrez le second nombre : "))
            
            # Exécution de l'opération choisie
            if operation == '+':
                result = addition(a, b)
            elif operation == '-':
                result = soustraction(a, b)
            elif operation == '*':
                result = multiplication(a, b)
            elif operation == '/':
                result = division(a, b)
            
            print(f"Le résultat de {a} {operation} {b} = {result}")
        
        except ValueError as e:
            print(f"Erreur : {e}")
        except Exception as e:
            print(f"Une erreur inattendue s'est produite : {e}")

# Lancer la calculatrice
calculatrice()

