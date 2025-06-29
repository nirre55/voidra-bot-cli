SUPPORTED_EXCHANGES = {
    "binancetestnet": "BinanceTestNet",
    "binance": "Binance",
    "kucoin": "KuCoin",
    "bybit": "Bybit",
    # Ajoute ici d'autres plateformes si nécessaire
}

def is_exchange_supported(exchange: str) -> bool:
    return exchange.lower() in SUPPORTED_EXCHANGES

def list_supported_exchanges() -> list[str]:
    return list(SUPPORTED_EXCHANGES.keys())

