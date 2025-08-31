import os
from typing import Dict, List
from run import package_dir
from streamlit.components.v1 import html
from tgcf.config import write_config


def get_list(string: str):
    # string where each line is one element
    my_list = []
    for line in string.splitlines():
        clean_line = line.strip()
        if clean_line != "":
            my_list.append(clean_line)
    return my_list


def get_string(my_list: List):
    string = ""
    for item in my_list:
        string += f"{item}\n"
    return string


def dict_to_list(dict: Dict):
    my_list = []
    for key, val in dict.items():
        my_list.append(f"{key}: {val}")
    return my_list


def list_to_dict(my_list: List):
    my_dict = {}
    for item in my_list:
        key, val = item.split(":")
        my_dict[key.strip()] = val.strip()
    return my_dict


def apply_theme(st, CONFIG, hidden_container):
    """Apply theme using browser's local storage"""
    if st.session_state.theme == '☀️':
        theme = 'Light'
        CONFIG.theme = 'light'
    else:
        theme = 'Dark'
        CONFIG.theme = 'dark'
    write_config(CONFIG)
    script = f"<script>localStorage.setItem('stActiveTheme-/-v1', '{{\"name\":\"{theme}\"}}');"
    pages = os.listdir(os.path.join(package_dir, 'pages'))
    for page in pages:
        script += f"localStorage.setItem('stActiveTheme-/{page[4:-3]}-v1', '{{\"name\":\"{theme}\"}}');"
    script += 'parent.location.reload()</script>'
    with hidden_container:  # prevents the layout from shifting
        html(script, height=0, width=0)


def switch_theme(st, CONFIG):
    """Display the option to change theme (Light/Dark)"""
    with st.sidebar:
        leftpad, content, rightpad = st.columns([0.27, 0.46, 0.27])
        with content:
            st.radio(
                'Design:', ['☀️', '🌒'],
                horizontal=True,
                label_visibility="collapsed",
                index=CONFIG.theme == 'dark',
                on_change=apply_theme,
                key="theme",
                args=[st, CONFIG, leftpad]  # or rightpad
            )


def hide_st(st):
    dev = os.getenv("DEV")
    if dev:
        return
    
    # Berlin-inspired black, white, red theme
    berlin_theme_style = """
    <style>
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Berlin-inspired color scheme */
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #1a1a1a 50%, #000000 100%);
    }
    
    .stApp header {
        background: linear-gradient(90deg, #000000 0%, #cc0000 50%, #000000 100%);
        border-bottom: 2px solid #cc0000;
    }
    
    .stApp .main .block-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 10px;
        border: 2px solid #cc0000;
        box-shadow: 0 4px 15px rgba(204, 0, 0, 0.3);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #000000 0%, #1a1a1a 100%);
        border-right: 2px solid #cc0000;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(45deg, #000000, #cc0000);
        color: white;
        border: 2px solid #cc0000;
        border-radius: 8px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(45deg, #cc0000, #000000);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(204, 0, 0, 0.4);
    }
    
    /* Text input styling */
    .stTextInput > div > div > input {
        border: 2px solid #cc0000;
        border-radius: 6px;
        background: rgba(255, 255, 255, 0.9);
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #cc0000;
        box-shadow: 0 0 8px rgba(204, 0, 0, 0.3);
    }
    
    /* Checkbox styling */
    .stCheckbox > div > div > div {
        background: #cc0000;
        border: 2px solid #000000;
    }
    
    /* Radio button styling */
    .stRadio > div > div > div > label {
        background: linear-gradient(45deg, #000000, #cc0000);
        color: white;
        border: 2px solid #cc0000;
        border-radius: 6px;
        padding: 8px 12px;
        margin: 2px;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: linear-gradient(45deg, #000000, #cc0000);
        color: white;
        border-radius: 6px;
        border: 2px solid #cc0000;
    }
    
    /* Warning and info boxes */
    .stAlert {
        border: 2px solid #cc0000;
        border-radius: 8px;
        background: rgba(204, 0, 0, 0.1);
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        background: linear-gradient(90deg, #000000, #cc0000, #000000);
        border-radius: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        color: white;
        border: 2px solid #cc0000;
        border-radius: 6px;
        margin: 2px;
    }
    
    /* Berlin background pattern */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 20% 80%, rgba(204, 0, 0, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(204, 0, 0, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(0, 0, 0, 0.1) 0%, transparent 50%);
        pointer-events: none;
        z-index: -1;
    }
    </style>
    """
    st.markdown(berlin_theme_style, unsafe_allow_html=True)
