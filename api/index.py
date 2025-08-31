import subprocess
import sys


class StreamlitHandler:
    def __init__(self):
        pass

    def start_streamlit(self):
        try:
            subprocess.run([
                sys.executable, '-m', 'streamlit', 'run',
                'tgcf/web_ui/0_👋_Hello.py',
                '--server.port=8080',
                '--server.address=0.0.0.0',
                '--server.headless=true'
            ], check=True)
        except subprocess.CalledProcessError as e:
            return f"Error: {e}"


def handler(request, context):
    return {
        'statusCode': 200,
        'body': 'FUXBLN Marketing Tool is starting...',
        'headers': {
            'Content-Type': 'text/html'
        }
    }
