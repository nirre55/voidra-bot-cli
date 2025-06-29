from pathlib import Path
from constants.supported_exchanges import is_exchange_supported

def ajouter_cles_api(exchange: str, api_key: str, api_secret: str, env_file: str = ".env"):
    """
    Ajoute ou met à jour les clés API pour une plateforme autorisée dans le .env
    """
    if not is_exchange_supported(exchange):
        raise ValueError(f"La plateforme '{exchange}' n'est pas supportée.")

    env_path = Path(env_file)
    exchange_upper = exchange.strip().upper()

    key_line = f"{exchange_upper}_API_KEY={api_key}"
    secret_line = f"{exchange_upper}_API_SECRET={api_secret}"

    existing_lines = []
    if env_path.exists():
        existing_lines = env_path.read_text(encoding="utf-8").splitlines()
        existing_lines = [
            line for line in existing_lines
            if not line.startswith(f"{exchange_upper}_API_KEY")
            and not line.startswith(f"{exchange_upper}_API_SECRET")
        ]

    updated_lines = existing_lines + [key_line, secret_line]
    env_path.write_text("\n".join(updated_lines) + "\n", encoding="utf-8")

    return exchange_upper



def lister_cles_api(env_file: str = ".env") -> dict[str, dict[str, str]]:
    """
    Lit le fichier .env et retourne les clés API trouvées, groupées par exchange.
    """
    env_path = Path(env_file)
    if not env_path.exists():
        return {}

    lines = env_path.read_text(encoding="utf-8").splitlines()
    result = {}

    for line in lines:
        if "=" not in line:
            continue

        key, value = line.split("=", 1)
        if "_API_KEY" in key or "_API_SECRET" in key:
            parts = key.split("_API_")
            if len(parts) != 2:
                continue

            exchange = parts[0]
            key_type = parts[1].lower()  # 'key' ou 'secret'

            if exchange not in result:
                result[exchange] = {}

            result[exchange][key_type] = value

    return result

def supprimer_cles_api(exchange: str, env_file: str = ".env") -> bool:
    """
    Supprime les lignes .env liées à une plateforme donnée.
    Retourne True si quelque chose a été supprimé.
    """
    exchange_clean = exchange.lower()
    if not is_exchange_supported(exchange_clean):
        raise ValueError(f"La plateforme '{exchange}' n'est pas supportée.")

    env_path = Path(env_file)
    if not env_path.exists():
        return False

    exchange_upper = exchange_clean.upper()

    # Lire les lignes existantes
    existing_lines = env_path.read_text(encoding="utf-8").splitlines()

    # Supprimer les lignes correspondant à cette plateforme
    new_lines = [
        line for line in existing_lines
        if not line.startswith(f"{exchange_upper}_API_KEY") and
           not line.startswith(f"{exchange_upper}_API_SECRET")
    ]

    if len(new_lines) == len(existing_lines):
        return False  # Aucune ligne supprimée

    # Réécrire le fichier
    env_path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
    return True