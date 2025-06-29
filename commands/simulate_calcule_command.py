# commands/simulate_command.py

import typer
from scripts import simulate_calcule

app = typer.Typer()

@app.command()
def run(
    balance: float = typer.Option(..., help="Le montant total disponible"),
    prix_entree: float = typer.Option(..., help="Le prix d'entrée initial"),
    prix_catastrophique: float = typer.Option(..., help="Le prix plancher ou d'arrêt"),
    drop_percent: float = typer.Option(..., help="Le pourcentage de baisse à chaque itération"),
    export_file: str = typer.Option(None, help="Chemin du fichier JSON à exporter (optionnel)")
):
    """
    Exécute un calcul de DCA et affiche ou exporte les résultats.
    """
    try:
        simulate_calcule.executer_calcul(balance, prix_entree, prix_catastrophique, drop_percent, export_file)
    except ValueError:
        typer.echo("❌ Erreur: valeurs numériques invalides.")
    except ZeroDivisionError:
        typer.echo("❌ Erreur: division par zéro, le prix catastrophique ne peut pas être atteint.")
