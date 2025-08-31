#!/usr/bin/env python3
"""
FUXBLN Marketing Tool - Render.com Deployment Script
"""

import requests
import os
import time


def deploy_to_render():
    """Deploy to Render.com via API"""
    
    # Render.com API Configuration
    RENDER_API_URL = "https://api.render.com/v1"
    RENDER_TOKEN = os.getenv("RENDER_TOKEN")
    
    if not RENDER_TOKEN:
        print("❌ RENDER_TOKEN nicht gesetzt!")
        print("Bitte setze die Umgebungsvariable RENDER_TOKEN")
        return False
    
    headers = {
        "Authorization": f"Bearer {RENDER_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # Service Configuration
    start_cmd = ("streamlit run tgcf/web_ui/0_👋_Hello.py "
                 "--server.port=$PORT --server.address=0.0.0.0 "
                 "--server.headless=true")
    
    service_config = {
        "name": "fuxbln-marketing-tool",
        "type": "web_service",
        "env": "python",
        "buildCommand": "pip install -r requirements.txt",
        "startCommand": start_cmd,
        "envVars": [
            {
                "key": "STREAMLIT_SERVER_HEADLESS",
                "value": "true"
            },
            {
                "key": "STREAMLIT_BROWSER_GATHER_USAGE_STATS", 
                "value": "false"
            }
        ]
    }
    
    try:
        print("🚀 Starte Render.com Deployment...")
        
        # Create service
        response = requests.post(
            f"{RENDER_API_URL}/services",
            headers=headers,
            json=service_config
        )
        
        if response.status_code == 201:
            service_data = response.json()
            service_id = service_data["id"]
            print(f"✅ Service erstellt: {service_id}")
            
            # Wait for deployment
            print("⏳ Warte auf Deployment...")
            time.sleep(30)
            
            # Get service status
            status_response = requests.get(
                f"{RENDER_API_URL}/services/{service_id}",
                headers=headers
            )
            
            if status_response.status_code == 200:
                status_data = status_response.json()
                service_url = status_data.get("service", {}).get("url")
                if service_url:
                    print("🎉 Deployment erfolgreich!")
                    print(f"🌐 URL: {service_url}")
                    return True
            
        else:
            print(f"❌ Fehler beim Erstellen des Services: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"❌ Deployment-Fehler: {e}")
    
    return False


def main():
    """Main deployment function"""
    print("=" * 50)
    print("🚀 FUXBLN Marketing Tool - Render.com Deployment")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("requirements.txt"):
        print("❌ requirements.txt nicht gefunden!")
        print("Bitte führe das Script im Projektverzeichnis aus")
        return
    
    # Try deployment
    success = deploy_to_render()
    
    if not success:
        print("\n📋 Manuelle Deployment-Anleitung:")
        print("1. Gehe zu: https://render.com")
        print("2. 'Sign up with GitHub' wählen")
        print("3. Repository LSRBLN/fuxbln verbinden")
        print("4. 'New Web Service' erstellen")
        print("5. Konfiguration:")
        print("   - Name: fuxbln-marketing-tool")
        print("   - Environment: Python 3")
        print("   - Build Command: pip install -r requirements.txt")
        print("   - Start Command: streamlit run tgcf/web_ui/0_👋_Hello.py "
              "--server.port=$PORT --server.address=0.0.0.0 "
              "--server.headless=true")
        print("6. Environment-Variablen setzen:")
        print("   - API_ID=deine_telegram_api_id")
        print("   - API_HASH=dein_telegram_api_hash")
        print("   - PASSWORD=dein_sicheres_passwort")
        print("7. 'Create Web Service' klicken")


if __name__ == "__main__":
    main()
