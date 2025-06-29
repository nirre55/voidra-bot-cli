# cli.py

import typer
from commands import simulate_calcule_command

app = typer.Typer()
app.add_typer(simulate_calcule_command.app, name="simulate")

if __name__ == "__main__":
    app()
