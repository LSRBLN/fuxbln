"""Declare all global constants."""

COMMANDS = {
    "start": "Prüfen, ob ich aktiv bin",
    "forward": "Neue Weiterleitung einrichten",
    "remove": "Bestehende Weiterleitung entfernen",
    "help": "Verwendung lernen",
}

REGISTER_COMMANDS = True

KEEP_LAST_MANY = 10000

CONFIG_FILE_NAME = "tgcf.config.json"
CONFIG_ENV_VAR_NAME = "TGCF_CONFIG"

MONGO_DB_NAME = "tgcf-config"
MONGO_COL_NAME = "tgcf-instance-0"
