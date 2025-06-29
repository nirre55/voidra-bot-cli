import typer
from scripts.env_script import ajouter_cles_api, lister_cles_api, supprimer_cles_api
from constants.supported_exchanges import list_supported_exchanges, is_exchange_supported

app = typer.Typer()

@app.command(help="🔐 Enregistre une clé API pour une plateforme autorisée")
def add_key(
    exchange: str = typer.Option(..., help="Nom de la plateforme (ex: binance)"),
    api_key: str = typer.Option(..., help="Clé API"),
    api_secret: str = typer.Option(..., help="Clé secrète")
):
    """
    Ajoute ou met à jour une clé API dans le fichier .env
    """
    try:
        exchange_code = ajouter_cles_api(exchange, api_key, api_secret)
        typer.secho(f"✅ Clés API pour {exchange_code} enregistrées dans .env", fg=typer.colors.GREEN)
    except ValueError as e:
        typer.secho(f"❌ Erreur : {e}", fg=typer.colors.RED)
        typer.echo("📌 Plateformes supportées :")
        for ex in list_supported_exchanges():
            typer.echo(f"  - {ex}")



@app.command("list-keys", help="📋 Liste toutes les clés API enregistrées dans le fichier .env")
def list_keys():
    """
    Affiche les clés API existantes, par plateforme.
    """
    cles = lister_cles_api()
    if not cles:
        typer.echo("ℹ️ Aucune clé API trouvée dans le fichier .env.")
        return

    typer.echo("🔐 Clés API enregistrées :\n")
    for exchange, data in cles.items():
        typer.echo(f"📦 {exchange.upper()}")
        typer.echo(f"   - Clé     : {data.get('key', '[manquante]')}")
        typer.echo(f"   - Secret  : {'[présent]' if 'secret' in data else '[manquant]'}")
        typer.echo("")



@app.command("remove-key", help="🗑️ Supprime les clés API d'une plateforme du fichier .env")
def remove_key(
    exchange: str = typer.Option(..., help="Nom de la plateforme à supprimer (ex: binance)")
):
    """
    Supprime les clés API d'une plateforme dans .env, après confirmation utilisateur.
    """
    try:
        exchange_lower = exchange.lower()
        if not is_exchange_supported(exchange_lower):
            raise ValueError(f"La plateforme '{exchange}' n'est pas supportée.")
        
        confirmation = typer.confirm(
            f"❗ Êtes-vous sûr de vouloir supprimer les clés API pour '{exchange}' ?"
        )
        if not confirmation:
            typer.echo("❌ Suppression annulée.")
            return

        removed = supprimer_cles_api(exchange_lower)
        if removed:
            typer.secho(f"✅ Clés API pour '{exchange}' supprimées avec succès.", fg=typer.colors.GREEN)
        else:
            typer.secho(f"ℹ️ Aucune clé trouvée pour '{exchange}' dans le fichier .env.", fg=typer.colors.YELLOW)

    except ValueError as e:
        typer.secho(f"❌ Erreur : {e}", fg=typer.colors.RED)
