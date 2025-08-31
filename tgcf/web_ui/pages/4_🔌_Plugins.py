import os

import streamlit as st
import yaml

from tgcf.config import CONFIG, read_config, write_config
from tgcf.plugin_models import FileType, Replace, Style
from tgcf.web_ui.password import check_password
from tgcf.web_ui.utils import get_list, get_string, hide_st, switch_theme

CONFIG = read_config()

st.set_page_config(
    page_title="Plugins",
    page_icon="🔌",
)

hide_st(st)
switch_theme(st, CONFIG)
if check_password(st):

    with st.expander("Filter"):
        CONFIG.plugins.filter.check = st.checkbox(
            "Dieses Plugin verwenden: Filter", value=CONFIG.plugins.filter.check
        )
        st.write("Bestimmte Textelemente auf Blacklist oder Whitelist setzen.")
        text_tab, users_tab, files_tab = st.tabs(["Text", "Benutzer", "Dateien"])

        with text_tab:
            CONFIG.plugins.filter.text.case_sensitive = st.checkbox(
                "Groß-/Kleinschreibung beachten", value=CONFIG.plugins.filter.text.case_sensitive
            )
            CONFIG.plugins.filter.text.regex = st.checkbox(
                "Filter als Regex interpretieren", value=CONFIG.plugins.filter.text.regex
            )

            st.write("Geben Sie einen Textausdruck pro Zeile ein")
            CONFIG.plugins.filter.text.whitelist = get_list(
                st.text_area(
                    "Text-Whitelist",
                    value=get_string(CONFIG.plugins.filter.text.whitelist),
                )
            )
            CONFIG.plugins.filter.text.blacklist = get_list(
                st.text_area(
                    "Text-Blacklist",
                    value=get_string(CONFIG.plugins.filter.text.blacklist),
                )
            )

        with users_tab:
            st.write("Geben Sie einen Benutzernamen/ID pro Zeile ein")
            CONFIG.plugins.filter.users.whitelist = get_list(
                st.text_area(
                    "Benutzer-Whitelist",
                    value=get_string(CONFIG.plugins.filter.users.whitelist),
                )
            )
            CONFIG.plugins.filter.users.blacklist = get_list(
                st.text_area(
                    "Benutzer-Blacklist", get_string(CONFIG.plugins.filter.users.blacklist)
                )
            )

        flist = [item.value for item in FileType]
        with files_tab:
            CONFIG.plugins.filter.files.whitelist = st.multiselect(
                "Dateien-Whitelist", flist, default=CONFIG.plugins.filter.files.whitelist
            )
            CONFIG.plugins.filter.files.blacklist = st.multiselect(
                "Dateien-Blacklist", flist, default=CONFIG.plugins.filter.files.blacklist
            )

    with st.expander("Format"):
        CONFIG.plugins.fmt.check = st.checkbox(
            "Dieses Plugin verwenden: Format", value=CONFIG.plugins.fmt.check
        )
        st.write(
            "Stil zum Text hinzufügen wie **fett**, _kursiv_, ~~durchgestrichen~~, `monospace` etc."
        )
        style_list = [item.value for item in Style]
        CONFIG.plugins.fmt.style = st.selectbox(
            "Format", style_list, index=style_list.index(CONFIG.plugins.fmt.style)
        )

    with st.expander("Wasserzeichen"):
        if os.system("ffmpeg -version >> /dev/null 2>&1") != 0:
            st.warning(
                "`ffmpeg` konnte nicht gefunden werden. Stellen Sie sicher, dass `ffmpeg` auf dem Server installiert ist, um dieses Plugin zu verwenden."
            )
        CONFIG.plugins.mark.check = st.checkbox(
            "Wasserzeichen auf Medien anwenden (Bilder und Videos).",
            value=CONFIG.plugins.mark.check,
        )
        uploaded_file = st.file_uploader("Wasserzeichen-Bild hochladen (png)", type=["png"])
        if uploaded_file is not None:
            with open("image.png", "wb") as f:
                f.write(uploaded_file.getbuffer())

    with st.expander("OCR"):
        st.write("Optische Zeichenerkennung.")
        if os.system("tesseract --version >> /dev/null 2>&1") != 0:
            st.warning(
                "`tesseract` konnte nicht gefunden werden. Stellen Sie sicher, dass `tesseract` auf dem Server installiert ist, um dieses Plugin zu verwenden."
            )
        CONFIG.plugins.ocr.check = st.checkbox(
            "OCR für Bilder aktivieren", value=CONFIG.plugins.ocr.check
        )
        st.write("Der Text wird in der Beschreibung des Bildes hinzugefügt, während es weitergeleitet wird.")

    with st.expander("Ersetzen"):
        CONFIG.plugins.replace.check = st.checkbox(
            "Textersetzung anwenden", value=CONFIG.plugins.replace.check
        )
        CONFIG.plugins.replace.regex = st.checkbox(
            "Als Regex interpretieren", value=CONFIG.plugins.replace.regex
        )

        CONFIG.plugins.replace.text_raw = st.text_area(
            "Ersetzungen", value=CONFIG.plugins.replace.text_raw
        )
        try:
            replace_dict = yaml.safe_load(
                CONFIG.plugins.replace.text_raw
            )  # validate and load yaml
            if not replace_dict:
                replace_dict = {}
            temp = Replace(text=replace_dict)  # perform validation by pydantic
            del temp
        except Exception as err:
            st.error(err)
            CONFIG.plugins.replace.text = {}
        else:
            CONFIG.plugins.replace.text = replace_dict

        if st.checkbox("Regeln und Verwendung anzeigen"):
            st.markdown(
                """
                Ersetzen Sie ein Wort oder einen Ausdruck durch einen anderen.

                - Schreiben Sie jede Ersetzung in eine neue Zeile.
                - Der ursprüngliche Text, dann **ein Doppelpunkt `:`** und dann **ein Leerzeichen** und dann der neue Text.
                - Es wird empfohlen, **einfache Anführungszeichen** zu verwenden. Anführungszeichen sind erforderlich, wenn Ihr String Leerzeichen oder Sonderzeichen enthält.
                - Doppelte Anführungszeichen funktionieren nicht, wenn Ihr Regex das Zeichen enthält: `\` .
                    ```
                    'original': 'neu'

                    ```
                - Siehe [Dokumentation](https://github.com/aahnik/tgcf/wiki/Replace-Plugin) für erweiterte Verwendung."""
            )

    with st.expander("Beschriftung"):
        CONFIG.plugins.caption.check = st.checkbox(
            "Beschriftungen anwenden", value=CONFIG.plugins.caption.check
        )
        CONFIG.plugins.caption.header = st.text_area(
            "Kopfzeile", value=CONFIG.plugins.caption.header
        )
        CONFIG.plugins.caption.footer = st.text_area(
            "Fußzeile", value=CONFIG.plugins.caption.footer
        )
        st.write(
            "Sie können leere Zeilen in Kopf- und Fußzeile haben, um Platz zwischen der ursprünglichen Nachricht und den Beschriftungen zu schaffen."
        )

    with st.expander("Absender"):
        st.write("Ändern Sie den Absender weitergeleiteter Nachrichten außer dem aktuellen Benutzer/Bot")
        st.warning("Die Option 'Weitergeleitet von' anzeigen muss deaktiviert sein, sonst werden Nachrichten nicht gesendet", icon="⚠️")
        CONFIG.plugins.sender.check = st.checkbox(
            "Absender setzen auf:", value=CONFIG.plugins.sender.check
        )
        leftpad, content, rightpad = st.columns([0.05, 0.9, 0.05])
        with content:
            user_type = st.radio("Kontotyp", ["Bot", "Benutzer"], index=CONFIG.plugins.sender.user_type, horizontal=True)
            if user_type == "Bot":
                CONFIG.plugins.sender.user_type = 0
                CONFIG.plugins.sender.BOT_TOKEN = st.text_input(
                    "Bot-Token", value=CONFIG.plugins.sender.BOT_TOKEN, type="password"
                )
            else:
                CONFIG.plugins.sender.user_type = 1
                CONFIG.plugins.sender.SESSION_STRING = st.text_input(
                    "Session-String", CONFIG.plugins.sender.SESSION_STRING, type="password"
                )
                st.markdown(
                """
                ###### Wie erhalte ich einen Session-String?

                Link zu Repl: https://replit.com/@aahnik/tg-login?v=1
                
                <p style="line-height:0px;margin-bottom:2em">
                    <i>Klicken Sie auf den obigen Link und geben Sie API ID, API HASH und Telefonnummer ein, um einen Session-String zu generieren.</i>
                </p>
                
                
                > <small>**Hinweis vom Entwickler:**<small>
                >
                > <small>Aufgrund einiger Probleme wird die Anmeldung mit einem Benutzerkonto über eine Telefonnummer in dieser Weboberfläche nicht unterstützt.</small>
                >
                > <small>Ich habe ein Kommandozeilenprogramm namens tg-login (https://github.com/aahnik/tg-login) erstellt, das den Session-String für Sie generieren kann.</small>
                >
                > <small>Sie können tg-login auf Ihrem Computer ausführen oder sicher in diesem Repl. tg-login ist Open Source, und Sie können auch das Bash-Skript inspizieren, das im Repl läuft.</small>
                >
                > <small>Was ist ein Session-String?</small>
                > <small>https://docs.telethon.dev/en/stable/concepts/sessions.html#string-sessions</small>
                """
                , unsafe_allow_html=True)

    if st.button("Speichern"):
        write_config(CONFIG)
