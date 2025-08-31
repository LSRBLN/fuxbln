import streamlit as st

from tgcf.config import CONFIG, read_config, write_config
from tgcf.web_ui.password import check_password
from tgcf.web_ui.utils import hide_st, switch_theme

CONFIG = read_config()

st.set_page_config(
    page_title="Telegram Anmeldung",
    page_icon="🔑",
)
hide_st(st)
switch_theme(st,CONFIG)
if check_password(st):
    CONFIG.login.API_ID = int(
        st.text_input("API ID", value=str(CONFIG.login.API_ID), type="password")
    )
    CONFIG.login.API_HASH = st.text_input(
        "API HASH", value=CONFIG.login.API_HASH, type="password"
    )
    st.write("Sie können API ID und API HASH von https://my.telegram.org erhalten.")

    user_type = st.radio(
        "Kontotyp wählen", ["Bot", "Benutzer"], index=CONFIG.login.user_type
    )
    if user_type == "Bot":
        CONFIG.login.user_type = 0
        CONFIG.login.BOT_TOKEN = st.text_input(
            "Bot-Token eingeben", value=CONFIG.login.BOT_TOKEN, type="password"
        )
    else:
        CONFIG.login.user_type = 1
        CONFIG.login.SESSION_STRING = st.text_input(
            "Session-String eingeben", value=CONFIG.login.SESSION_STRING, type="password"
        )
        with st.expander("Wie erhalte ich einen Session-String?"):
            st.markdown(
                """

            Link zu Repl: https://replit.com/@aahnik/tg-login?v=1

            _Klicken Sie auf den obigen Link und geben Sie API ID, API HASH und Telefonnummer ein, um einen Session-String zu generieren._

            **Hinweis vom Entwickler:**

            Aufgrund einiger Probleme wird die Anmeldung mit einem Benutzerkonto über eine Telefonnummer in dieser Weboberfläche nicht unterstützt.

            Ich habe ein Kommandozeilenprogramm namens tg-login (https://github.com/aahnik/tg-login) erstellt, das den Session-String für Sie generieren kann.

            Sie können tg-login auf Ihrem Computer ausführen oder sicher in diesem Repl. tg-login ist Open Source, und Sie können auch das Bash-Skript inspizieren, das im Repl läuft.

            Was ist ein Session-String?
            https://docs.telethon.dev/en/stable/concepts/sessions.html#string-sessions

            """
            )

    if st.button("Speichern"):
        write_config(CONFIG)
