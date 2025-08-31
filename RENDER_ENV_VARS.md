# 🔧 Render.com Environment-Variablen

## 📋 **Pflicht-Variablen für Render.com**

Füge diese Variablen in deinem Render.com Dashboard hinzu:

### **1. Telegram API-Zugangsdaten**
```
API_ID=deine_telegram_api_id_hier
API_HASH=dein_telegram_api_hash_hier
```

**Wie du sie erhältst:**
1. Gehe zu: https://my.telegram.org
2. **"API development tools"** wählen
3. **App erstellen** und Zugangsdaten kopieren

### **2. Web-Interface Passwort**
```
PASSWORD=dein_sicheres_passwort_hier
```

**Empfehlung:** Mindestens 8 Zeichen, Buchstaben + Zahlen

## 🔧 **Optionale Variablen**

### **Streamlit-Konfiguration**
```
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
STREAMLIT_SERVER_ENABLE_CORS=false
```

### **Bot-Token (falls Bot-Modus)**
```
BOT_TOKEN=dein_bot_token_hier
```

## 📝 **Schritt-für-Schritt Anleitung**

### **1. Render.com Dashboard**
1. Gehe zu deinem Web Service
2. **"Environment"** Tab wählen
3. **"Add Environment Variable"** klicken

### **2. Variablen hinzufügen**
```
Key: API_ID
Value: deine_telegram_api_id

Key: API_HASH  
Value: dein_telegram_api_hash

Key: PASSWORD
Value: dein_sicheres_passwort
```

### **3. Speichern und Deploy**
1. **"Save Changes"** klicken
2. **"Manual Deploy"** → **"Deploy latest commit"**

## ✅ **Testen**

Nach dem Deployment:
1. **URL aufrufen:** `https://fuxbln-marketing-tool.onrender.com`
2. **Passwort eingeben**
3. **Telegram-Login** konfigurieren
4. **Verbindungen** testen

## 🚨 **Wichtige Hinweise**

- **API-Zugangsdaten sicher aufbewahren**
- **Passwort nicht im Code speichern**
- **Environment-Variablen nach jedem Deploy prüfen**
- **Logs bei Problemen überprüfen**
