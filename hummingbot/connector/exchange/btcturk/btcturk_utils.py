import re
from typing import (
    Optional,
    Tuple)

from hummingbot.client.config.config_var import ConfigVar
from hummingbot.client.config.config_methods import using_exchange


CENTRALIZED = True
EXAMPLE_PAIR = "BTC-USDT"
DEFAULT_FEES = [0.1, 0.1]


USD_QUOTES = ["DAI", "USDT", "USDC", "USDS", "TUSD", "PAX", "BUSD", "USD"]


def split_trading_pair(trading_pair: str) -> Optional[Tuple[str, str]]:
    try:
        return trading_pair.split("_")[0], trading_pair.split("_")[1]
    # Exceptions are now logged as warnings in trading pair fetcher
    except Exception:
        return None


def convert_from_exchange_trading_pair(exchange_trading_pair: str) -> Optional[str]:
    if split_trading_pair(exchange_trading_pair) is None:
        return None
    base_asset, quote_asset = split_trading_pair(exchange_trading_pair)
    return f"{base_asset}-{quote_asset}"


def convert_to_exchange_trading_pair(hb_trading_pair: str) -> str:
    # Binance does not split BASEQUOTE (BTCUSDT)
    return hb_trading_pair.replace("-", "_")


KEYS = {
    "btcturk_api_key":
        ConfigVar(key="btcturk_api_key",
                  prompt="Enter your BTCTurk API key >>> ",
                  required_if=using_exchange("btcturk"),
                  is_secure=True,
                  is_connect_key=True),
    "btcturk_api_secret":
        ConfigVar(key="btcturk_api_secret",
                  prompt="Enter your BTCTurk API secret >>> ",
                  required_if=using_exchange("btcturk"),
                  is_secure=True,
                  is_connect_key=True),
}

