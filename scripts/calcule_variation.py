def calculer_variation(prix_initial, prix_final):
    if prix_initial <= 0:
        raise ValueError("Le prix initial doit être supérieur à 0.")

    variation = prix_final - prix_initial
    pourcentage = (abs(variation) / prix_initial) * 100

    if variation < 0:
        print(f"Le prix a baissé de {pourcentage:.2f}%")
    elif variation > 0:
        print(f"Le prix a augmenté de {pourcentage:.2f}%")
    else:
        print("Le prix n'a pas changé.")

if __name__ == "__main__":
    try:
        prix1 = float(input("Entrez le prix initial : "))
        prix2 = float(input("Entrez le prix final : "))
        calculer_variation(prix1, prix2)
    except ValueError as e:
        print(f"Erreur : {e}")
