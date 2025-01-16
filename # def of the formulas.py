import json

# Fonctions mathématiques
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

# Fonction pour enregistrer un calcul dans l'historique
def enregistrer_historique(operation, a, b, result):
    historique = []
    fichier = "historique.json"
    
    # Charger l'historique existant
    try:
        with open(fichier, "r") as f:
            historique = json.load(f)
    except FileNotFoundError:
        pass  # Le fichier n'existe pas encore, aucun problème

    # Ajouter le nouveau calcul
    historique.append({
        "operation": operation,
        "a": a,
        "b": b,
        "result": result
    })

    # Enregistrer dans le fichier
    with open(fichier, "w") as f:
        json.dump(historique, f, indent=4)

# Fonction pour afficher l'historique
def afficher_historique():
    fichier = "historique.json"
    try:
        with open(fichier, "r") as f:
            historique = json.load(f)
            if not historique:
                print("Aucun calcul dans l'historique.")
                return
            print("\nHistorique des calculs :")
            for calcul in historique:
                print(f"{calcul['a']} {calcul['operation']} {calcul['b']} = {calcul['result']}")
    except FileNotFoundError:
        print("Aucun historique trouvé.")

# Fonction principale
def calculatrice():
    print("Bienvenue dans la calculatrice.")
    print("Opérations disponibles :")
    print("1. Addition (+)")
    print("2. Soustraction (-)")
    print("3. Multiplication (x)")
    print("4. Division (/)")
    print("5. Afficher l'historique")
    
    while True:
        try:
            operation = input("\nChoisissez l'opération (+, -, *, /, h pour historique) ou tapez 'q' pour quitter : ")
            if operation == 'q':
                print("Au revoir!")
                break
            if operation == 'h':
                afficher_historique()
                continue
            if operation not in ['+', '-', '*', '/']:
                print("Opération invalide. Veuillez choisir parmi +, -, *, / ou h.")
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
            enregistrer_historique(operation, a, b, result)
        
        except ValueError as e:
            print(f"Erreur : {e}")
        except Exception as e:
            print(f"Une erreur inattendue s'est produite : {e}")

# Lancer la calculatrice
calculatrice()
