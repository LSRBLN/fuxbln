import json

import streamlit as st

from tgcf.config import CONFIG_FILE_NAME, read_config, write_config
from tgcf.utils import platform_info
from tgcf.web_ui.password import check_password
from tgcf.web_ui.utils import hide_st, switch_theme

CONFIG = read_config()

st.set_page_config(
    page_title="Erweitert",
    page_icon="🔬",
)
hide_st(st)
switch_theme(st, CONFIG)

if check_password(st):

    st.warning("Diese Seite ist für Entwickler und fortgeschrittene Benutzer.")
    if st.checkbox("Ich stimme zu"):

        with st.expander("Version & Plattform"):
            st.code(platform_info())

        with st.expander("Konfiguration"):
            with open(CONFIG_FILE_NAME, "r") as file:
                data = json.loads(file.read())
                dumped = json.dumps(data, indent=3)
            st.download_button(
                f"Konfiguration JSON herunterladen", data=dumped, file_name=CONFIG_FILE_NAME
            )
            st.json(data)

        with st.expander("Spezielle Optionen für Live-Modus"):
            CONFIG.live.sequential_updates = st.checkbox(
                "Sequenzielle Updates erzwingen", value=CONFIG.live.sequential_updates
            )

            CONFIG.live.delete_on_edit = st.text_input(
                "Nachricht löschen, wenn Quelle bearbeitet wird zu",
                value=CONFIG.live.delete_on_edit,
            )
            st.write(
                "Wenn Sie die Nachricht in der Quelle zu etwas Bestimmtem bearbeiten, wird die Nachricht sowohl in der Quelle als auch in den Zielen gelöscht."
            )
            if st.checkbox("Bot-Nachrichten anpassen"):
                st.info(
                    "Hinweis: Für Userbots beginnen die Befehle mit `.` statt `/`, wie `.start` und nicht `/start`"
                )
                CONFIG.bot_messages.start = st.text_area(
                    "Bot-Antwort auf /start Befehl", value=CONFIG.bot_messages.start
                )
                CONFIG.bot_messages.bot_help = st.text_area(
                    "Bot-Antwort auf /help Befehl", value=CONFIG.bot_messages.bot_help
                )

            if st.button("Speichern"):
                write_config(CONFIG)
