import os
from pathlib import Path

from tgcf.config import CONFIG

# Get the package directory using a simple and reliable method
package_dir = Path(__file__).parent

def main():
    print(package_dir)
    path = os.path.join(package_dir, "0_👋_Hello.py")
    os.environ["STREAMLIT_THEME_BASE"] = CONFIG.theme
    os.environ["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"
    os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
    os.system(f"streamlit run {path}")
