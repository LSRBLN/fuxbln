import time

import streamlit as st

from tgcf.config import CONFIG, Forward, read_config, write_config
from tgcf.web_ui.password import check_password
from tgcf.web_ui.utils import get_list, get_string, hide_st, switch_theme

CONFIG = read_config()

st.set_page_config(
    page_title="Verbindungen",
    page_icon="🔗",
)
hide_st(st)
switch_theme(st, CONFIG)
if check_password(st):
    add_new = st.button("Neue Verbindung hinzufügen")
    if add_new:
        CONFIG.forwards.append(Forward())
        write_config(CONFIG)

    num = len(CONFIG.forwards)

    if num == 0:
        st.write(
            "Keine Verbindungen gefunden. Klicken Sie oben auf 'Neue Verbindung hinzufügen', um eine zu erstellen!"
        )
    else:
        tab_strings = []
        for i in range(num):
            if CONFIG.forwards[i].con_name:
                label = CONFIG.forwards[i].con_name
            else:
                label = f"Verbindung {i+1}"
            if CONFIG.forwards[i].use_this:
                status = "🟢"
            else:
                status = "🟡"

            tab_strings.append(f"{status} {label}")

        tabs = st.tabs(list(tab_strings))

        for i in range(num):
            with tabs[i]:
                con = i + 1
                name = CONFIG.forwards[i].con_name
                if name:
                    label = f"{con} [{name}]"
                else:
                    label = con
                with st.expander("Metadaten bearbeiten"):
                    st.write(f"Verbindungs-ID: **{con}**")
                    CONFIG.forwards[i].con_name = st.text_input(
                        "Name dieser Verbindung",
                        value=CONFIG.forwards[i].con_name,
                        key=con,
                    )

                    st.info(
                        "Sie können das folgende Kontrollkästchen deaktivieren, um diese Verbindung zu suspendieren."
                    )
                    CONFIG.forwards[i].use_this = st.checkbox(
                        "Diese Verbindung verwenden",
                        value=CONFIG.forwards[i].use_this,
                        key=f"use {con}",
                    )
                with st.expander("Quelle und Ziel"):
                    st.write(f"Verbindung {label} konfigurieren")

                    CONFIG.forwards[i].source = st.text_input(
                        "Quelle",
                        value=CONFIG.forwards[i].source,
                        key=f"source {con}",
                    ).strip()
                    st.write("nur eine Quelle ist pro Verbindung erlaubt")
                    CONFIG.forwards[i].dest = get_list(
                        st.text_area(
                            "Ziele",
                            value=get_string(CONFIG.forwards[i].dest),
                            key=f"dest {con}",
                        )
                    )
                    st.write("Schreiben Sie Ziele, ein Element pro Zeile")

                with st.expander("Vergangenheitsmodus-Einstellungen"):
                    CONFIG.forwards[i].offset = int(
                        st.text_input(
                            "Offset",
                            value=str(CONFIG.forwards[i].offset),
                            key=f"offset {con}",
                        )
                    )
                    CONFIG.forwards[i].end = int(
                        st.text_input(
                            "Ende", value=str(CONFIG.forwards[i].end), key=f"end {con}"
                        )
                    )
                
                with st.expander("Intervall-Nachrichten"):
                    st.write("Automatisches Senden von Nachrichten in regelmäßigen Abständen")
                    
                    CONFIG.forwards[i].enable_interval_posting = st.checkbox(
                        "Intervall-Nachrichten aktivieren",
                        value=CONFIG.forwards[i].enable_interval_posting,
                        key=f"interval_enable {con}",
                    )
                    
                    if CONFIG.forwards[i].enable_interval_posting:
                        CONFIG.forwards[i].interval_seconds = st.slider(
                            "Intervall in Sekunden",
                            min_value=10,
                            max_value=3600,
                            value=CONFIG.forwards[i].interval_seconds,
                            step=10,
                            key=f"interval_seconds {con}",
                        )
                        
                        CONFIG.forwards[i].interval_message = st.text_area(
                            "Nachrichtentext",
                            value=CONFIG.forwards[i].interval_message,
                            key=f"interval_message {con}",
                            help="Diese Nachricht wird in regelmäßigen Abständen an alle Zielgruppen gesendet"
                        )
                        
                        st.info(f"📅 Nachricht wird alle {CONFIG.forwards[i].interval_seconds} Sekunden gesendet")
                
                with st.expander("Diese Verbindung löschen"):
                    st.warning(
                        f"Das Klicken auf die 'Entfernen'-Schaltfläche wird die Verbindung **{label}** **löschen**. Diese Aktion kann nicht rückgängig gemacht werden.",
                        icon="⚠️",
                    )

                    if st.button(f"Verbindung **{label}** entfernen"):
                        del CONFIG.forwards[i]
                        write_config(CONFIG)
                        st.experimental_rerun()

    if st.button("Speichern"):
        write_config(CONFIG)
        st.experimental_rerun()
