import os
import signal
import subprocess
import time

import streamlit as st

from tgcf.config import CONFIG, read_config, write_config
from tgcf.web_ui.password import check_password
from tgcf.web_ui.utils import hide_st, switch_theme

CONFIG = read_config()


def termination():
    st.code("Prozess beendet!")
    os.rename("logs.txt", "old_logs.txt")
    with open("old_logs.txt", "r") as f:
        st.download_button(
            "Letzte Logs herunterladen", data=f.read(), file_name="tgcf_logs.txt"
        )

    CONFIG = read_config()
    CONFIG.pid = 0
    write_config(CONFIG)
    st.button("Seite aktualisieren")


st.set_page_config(
    page_title="Ausführen",
    page_icon="🏃",
)
hide_st(st)
switch_theme(st, CONFIG)
if check_password(st):
    with st.expander("Ausführung konfigurieren"):
        CONFIG.show_forwarded_from = st.checkbox(
            "'Weitergeleitet von' anzeigen", value=CONFIG.show_forwarded_from
        )
        mode = st.radio("Modus wählen", ["live", "past"], index=CONFIG.mode)
        if mode == "past":
            CONFIG.mode = 1
            st.warning(
                "Nur Benutzerkonten können im Vergangenheitsmodus verwendet werden. Telegram erlaubt Bot-Konten nicht, durch den Verlauf eines Chats zu gehen!"
            )
            CONFIG.past.delay = st.slider(
                "Verzögerung in Sekunden", 0, 100, value=CONFIG.past.delay
            )
        else:
            CONFIG.mode = 0
            CONFIG.live.delete_sync = st.checkbox(
                "Synchronisieren, wenn eine Nachricht gelöscht wird", value=CONFIG.live.delete_sync
            )

        if st.button("Speichern"):
            write_config(CONFIG)

    check = False

    if CONFIG.pid == 0:
        check = st.button("Starten", type="primary")

    if CONFIG.pid != 0:
        st.warning(
            "Sie müssen auf Stopp klicken und dann tgcf neu starten, um Änderungen in der Konfiguration zu übernehmen."
        )
        # check if process is running using pid
        try:
            os.kill(CONFIG.pid, signal.SIGCONT)
        except Exception as err:
            st.code("Der Prozess wurde gestoppt.")
            st.code(err)
            CONFIG.pid = 0
            write_config(CONFIG)
            time.sleep(1)
            st.experimental_rerun()

        stop = st.button("Stoppen", type="primary")
        if stop:
            try:
                os.kill(CONFIG.pid, signal.SIGSTOP)
            except Exception as err:
                st.code(err)

                CONFIG.pid = 0
                write_config(CONFIG)
                st.button("Seite aktualisieren")

            else:
                termination()

    if check:
        with open("logs.txt", "w") as logs:
            process = subprocess.Popen(
                ["tgcf", "--loud", mode],
                stdout=logs,
                stderr=subprocess.STDOUT,
            )
        CONFIG.pid = process.pid
        write_config(CONFIG)
        time.sleep(2)

        st.experimental_rerun()

    try:
        lines = st.slider(
            "Anzahl der Log-Zeilen anzeigen", min_value=100, max_value=1000, step=100
        )
        temp_logs = "logs_n_lines.txt"
        os.system(f"rm {temp_logs}")
        with open("logs.txt", "r") as file:
            pass

        os.system(f"tail -n {lines} logs.txt >> {temp_logs}")
        with open(temp_logs, "r") as file:
            st.code(file.read())
    except FileNotFoundError as err:
        st.write("Keine aktuellen Logs gefunden")
    st.button("Weitere Logs laden")
