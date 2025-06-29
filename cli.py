# cli.py

import typer
from commands import simulate_calcule_command, calcule_variation_command

app = typer.Typer()
app.add_typer(simulate_calcule_command.app, name="simulate")
app.add_typer(calcule_variation_command.app, name="variation")

if __name__ == "__main__":
    app()
