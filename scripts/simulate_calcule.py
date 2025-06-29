import json

def calculer_difference_percent(prix_entree, prix_catastrophique):
    return ((prix_entree - prix_catastrophique) / prix_entree) * 100

def generer_prix_iterations(prix_entree, prix_catastrophique, drop_percent):
    prix_actuel = prix_entree
    prix_iterations = []

    while prix_actuel > prix_catastrophique:
        prix_iterations.append(prix_actuel)
        prix_actuel *= (1 - drop_percent / 100)

    # Inclure la dernière valeur si elle tombe sous le seuil
    if prix_actuel <= prix_catastrophique:
        prix_iterations.append(prix_actuel)

    return prix_iterations

def calculer_montant_par_iteration(balance, nb_iterations):
    return balance / nb_iterations if nb_iterations > 0 else 0

def generer_repartition(prix_iterations, montant_par_iteration):
    repartition = []
    for i, prix in enumerate(prix_iterations, 1):
        quantite = montant_par_iteration / prix
        repartition.append({
            "iteration": i,
            "prix": prix,
            "montant": montant_par_iteration,
            "quantite": round(quantite, 6)
        })
    return repartition

def construire_resultat(balance, prix_entree, prix_catastrophique, drop_percent):
    difference_percent = calculer_difference_percent(prix_entree, prix_catastrophique)
    prix_iterations = generer_prix_iterations(prix_entree, prix_catastrophique, drop_percent)
    nb_iterations = len(prix_iterations)
    montant_par_iteration = calculer_montant_par_iteration(balance, nb_iterations)
    repartition = generer_repartition(prix_iterations, montant_par_iteration)

    return {
        "balance": balance,
        "prix_entree": prix_entree,
        "prix_catastrophique": prix_catastrophique,
        "drop_percent": drop_percent,
        "difference_percent": round(difference_percent, 2),
        "nombre_total_iterations": nb_iterations,
        "montant_par_iteration": montant_par_iteration,
        "iterations": repartition
    }

def exporter_json(resultat, fichier_path):
    with open(fichier_path, "w", encoding="utf-8") as f:
        json.dump(resultat, f, ensure_ascii=False, indent=4)

def afficher_resultat(resultat):
    print(json.dumps(resultat, indent=4, ensure_ascii=False))

def executer_calcul(balance, prix_entree, prix_catastrophique, drop_percent, export_file=None):
    resultat = construire_resultat(balance, prix_entree, prix_catastrophique, drop_percent)

    if export_file:
        exporter_json(resultat, export_file)
        print(f"\n✅ Résultat exporté dans : {export_file}")
    else:
        afficher_resultat(resultat)

# === Entrée utilisateur ===
def demander_parametres_utilisateur():
    balance = float(input("Entrez la balance: "))
    prix_entree = float(input("Entrez le prix d'entrée: "))
    prix_catastrophique = float(input("Entrez le prix catastrophique: "))
    drop_percent = float(input("Entrez le pourcentage de drop: "))
    fichier = input("Nom du fichier de sortie (laisser vide pour ignorer l'export): ").strip()
    return balance, prix_entree, prix_catastrophique, drop_percent, fichier or None

# === Exemple principal ===
if __name__ == "__main__":
    print("=== EXEMPLE ===")
    executer_calcul(1000, 40, 4, 50, export_file="resultat_exemple.json")

    print("\n" + "=" * 60 + "\n")
    print("=== CALCULATEUR PERSONNALISÉ ===")

    try:
        balance, prix_entree, prix_catastrophique, drop_percent, fichier = demander_parametres_utilisateur()
        print("\n" + "-" * 60)
        executer_calcul(balance, prix_entree, prix_catastrophique, drop_percent, export_file=fichier)
    except ValueError:
        print("Erreur: Veuillez entrer des valeurs numériques valides.")
    except ZeroDivisionError:
        print("Erreur: Le prix catastrophique ne peut pas être atteint avec ces paramètres.")
