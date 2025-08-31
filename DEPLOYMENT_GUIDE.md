# 🚀 FUXBLN Marketing Tool - Deployment Guide

## 📋 **Deployment-Optionen**

### **1. Railway.com (Empfohlen)**

#### **Schritt 1: Anmeldung**
1. Gehe zu: https://railway.app
2. **"Sign up with GitHub"** wählen
3. Repository `LSRBLN/fuxbln` autorisieren

#### **Schritt 2: Projekt erstellen**
1. **"Deploy from GitHub repo"** klicken
2. Repository `LSRBLN/fuxbln` auswählen
3. **"Deploy Now"** klicken

#### **Schritt 3: Environment-Variablen setzen**
```bash
PASSWORD=dein_sicheres_passwort
API_ID=deine_telegram_api_id
API_HASH=dein_telegram_api_hash
```

#### **Schritt 4: Domain anzeigen**
- Railway generiert automatisch eine URL
- Beispiel: `https://fuxbln-marketing-tool.railway.app`

---

### **2. Render.com (Alternative)**

#### **Schritt 1: Anmeldung**
1. Gehe zu: https://render.com
2. **"Sign up with GitHub"** wählen
3. Repository `LSRBLN/fuxbln` verbinden

#### **Schritt 2: Web Service erstellen**
1. **"New Web Service"** klicken
2. Repository `LSRBLN/fuxbln` auswählen
3. **Name:** `fuxbln-marketing-tool`
4. **Environment:** `Python 3`
5. **Build Command:** `pip install -r requirements.txt`
6. **Start Command:** `streamlit run tgcf/web_ui/0_👋_Hello.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true`

#### **Schritt 3: Environment-Variablen**
```bash
PASSWORD=dein_sicheres_passwort
API_ID=deine_telegram_api_id
API_HASH=dein_telegram_api_hash
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

#### **Schritt 4: Deploy**
- **"Create Web Service"** klicken
- Render baut und deployt automatisch

---

### **3. Lokales Docker-Deployment**

#### **Schritt 1: Docker-Image bauen**
```bash
docker build -t fuxbln-marketing-tool .
```

#### **Schritt 2: Container starten**
```bash
docker run -p 8501:8501 \
  -e PASSWORD=dein_passwort \
  -e API_ID=deine_api_id \
  -e API_HASH=dein_api_hash \
  fuxbln-marketing-tool
```

#### **Schritt 3: Zugriff**
- Browser: http://localhost:8501

---

## 🔧 **Konfiguration**

### **Telegram API-Zugangsdaten**
1. Gehe zu: https://my.telegram.org
2. **"API development tools"** wählen
3. **App erstellen** und Zugangsdaten kopieren

### **Umgebungsvariablen**
```bash
# Pflicht
PASSWORD=dein_sicheres_passwort
API_ID=deine_telegram_api_id
API_HASH=dein_telegram_api_hash

# Optional
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

---

## 🌐 **Online-Zugriff**

### **Railway**
- **URL:** `https://fuxbln-marketing-tool.railway.app`
- **Status:** Automatische Deployments bei Git-Push

### **Render.com**
- **URL:** `https://fuxbln-marketing-tool.onrender.com`
- **Status:** Automatische Deployments bei Git-Push

### **Lokal**
- **URL:** `http://localhost:8501`
- **Status:** Manueller Start erforderlich

---

## 📊 **Monitoring**

### **Logs anzeigen**
- **Railway:** Dashboard → Service → Logs
- **Render:** Dashboard → Service → Logs
- **Docker:** `docker logs <container_id>`

### **Status überprüfen**
- **Health Check:** `https://deine-url.com/_stcore/health`
- **Streamlit:** `https://deine-url.com`

---

## 🚨 **Troubleshooting**

### **Railway-Probleme**
1. **Build-Fehler:** Requirements.txt überprüfen
2. **Port-Probleme:** `$PORT` Variable verwenden
3. **Timeout:** Healthcheck-Pfad anpassen

### **Render-Probleme**
1. **Build-Fehler:** Python-Version prüfen
2. **Start-Fehler:** Start-Command überprüfen
3. **Timeout:** Build-Timeout erhöhen

### **Docker-Probleme**
1. **Port-Konflikte:** Anderen Port verwenden
2. **Speicher-Probleme:** Docker-Image optimieren
3. **Netzwerk-Probleme:** Port-Mapping prüfen

---

## ✅ **Deployment-Checkliste**

- [ ] **GitHub Repository** veröffentlicht
- [ ] **Telegram API-Zugangsdaten** bereit
- [ ] **Environment-Variablen** konfiguriert
- [ ] **Deployment-Plattform** gewählt
- [ ] **Domain/URL** verfügbar
- [ ] **Health Check** erfolgreich
- [ ] **Login** funktioniert
- [ ] **Telegram-Verbindung** getestet

---

## 🎯 **Empfehlung**

**Für Produktionsumgebung:**
1. **Railway** (einfach, kostenlos, zuverlässig)
2. **Render.com** (alternativ, auch kostenlos)
3. **Lokales Docker** (für Entwicklung/Testing)

**Für QNAP-System:**
- **Container Station** verwenden
- **Docker-Image** importieren
- **Port 8501** freigeben
