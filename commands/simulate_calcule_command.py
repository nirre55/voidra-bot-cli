import typer
from scripts import simulate_calcule

app = typer.Typer()

@app.command(           
    help=(
        "💹 Simule une stratégie de DCA (Dollar Cost Averaging).\n\n"
        "Cette commande calcule le nombre d'itérations possibles entre un prix d'entrée "
        "et un prix catastrophique en appliquant un pourcentage de baisse à chaque étape. "
        "Elle répartit également le capital alloué (balance) sur ces itérations et peut "
        "exporter les résultats au format JSON.\n\n"
        "💾 Exemple :\n"
        "python cli.py simulate run --balance 1000 --prix-entree 40 --prix-catastrophique 4 --drop-percent 50 --export-file resultat.json"
    )
)
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
