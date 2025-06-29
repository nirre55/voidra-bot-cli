# commands/variation_command.py

import typer
from scripts import calcule_variation

app = typer.Typer()

@app.command(
    help=(
        "📊 Calcule la variation en pourcentage entre deux prix.\n\n"
        "Cette commande indique si le prix a augmenté ou baissé, et de combien.\n"
        "Exemple :\n"
        "python cli.py variation run --prix-initial 100 --prix-final 80"
    )
)
def run(
    prix_initial: float = typer.Option(..., help="Prix de départ"),
    prix_final: float = typer.Option(..., help="Prix d'arrivée")
):
    """
    Calcule et affiche la variation en pourcentage entre deux prix.
    """
    try:
        result = calcule_variation.calculer_variation(prix_initial, prix_final)
        typer.echo(result)
    except ValueError as e:
        typer.secho(f"❌ Erreur : {e}", fg=typer.colors.RED)
