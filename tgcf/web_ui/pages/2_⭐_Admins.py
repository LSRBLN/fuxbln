import streamlit as st

from tgcf.config import CONFIG, read_config, write_config
from tgcf.web_ui.password import check_password
from tgcf.web_ui.utils import get_list, get_string, hide_st, switch_theme

CONFIG = read_config()

st.set_page_config(
    page_title="Administratoren",
    page_icon="⭐",
)
hide_st(st)
switch_theme(st, CONFIG)
if check_password(st):

    CONFIG.admins = get_list(st.text_area("Administratoren", value=get_string(CONFIG.admins)))
    st.write("Fügen Sie die Benutzernamen der Administratoren hinzu. Einen pro Zeile.")

    if st.button("Speichern"):
        write_config(CONFIG)
