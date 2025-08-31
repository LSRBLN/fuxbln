# 🚀 FUXBLN Marketing Tool

Das ultimative deutsche Telegram-Marketing-Tool mit Berlin-Design und Intervall-Nachrichten-Funktion.

## 🌟 Features

### 🎨 **Berlin-Inspiriertes Design**
- **Schwarz-Weiß-Rotes Farbschema** mit Berliner Hintergrund
- **Moderne UI-Elemente** mit roten Akzenten
- **Gradient-Effekte** und professionelles Layout
- **Responsive Design** für alle Geräte

### 🇩🇪 **Vollständig auf Deutsch**
- **100% deutsche Übersetzung** aller Funktionen
- **Deutsche Menüführung** und Benutzeroberfläche
- **Deutsche Dokumentation** und Bedienungsanleitung
- **Deutsche Bot-Befehle** und Nachrichten

### ⏰ **Intervall-Nachrichten-Funktion**
- **Automatisches Senden** von Nachrichten in regelmäßigen Abständen
- **Zeitintervall einstellbar** (10-3600 Sekunden)
- **Benutzerdefinierte Nachrichten** für jedes Intervall
- **Multi-Ziel-Unterstützung** für alle konfigurierten Gruppen

### 🔌 **Erweiterte Plugin-Funktionen**
- **Filter:** Blacklist/Whitelist für Nachrichten und Benutzer
- **Format:** Textformatierung (fett, kursiv, durchgestrichen)
- **Ersetzen:** Regex-basierte Textersetzung
- **Beschriftung:** Header/Footer für Nachrichten
- **Wasserzeichen:** Für Bilder und Videos
- **OCR:** Texterkennung in Bildern
- **Absender:** Anpassung der Absenderinformationen

## 🚀 Installation

### Voraussetzungen
- Python 3.10 oder höher
- Telegram-Konto (Bot oder Benutzer)
- API-Zugangsdaten von https://my.telegram.org

### Schnellstart
```bash
# Repository klonen
git clone https://github.com/LSRBLN/fuxbln.git
cd fuxbln

# Abhängigkeiten installieren
pip install -e .

# Passwort setzen
echo "PASSWORD=dein_sicheres_passwort" > .env

# Tool starten
streamlit run tgcf/web_ui/0_👋_Hello.py --server.port 8501
```

## 📖 Vollständige Bedienungsanleitung

Das Tool enthält eine umfassende deutsche Bedienungsanleitung mit:
- **Schritt-für-Schritt Anweisungen** für alle Funktionen
- **Troubleshooting-Guide** für häufige Probleme
- **Best Practices** für optimale Nutzung
- **Video-Tutorials** und Community-Links

## 🌐 Online-Deployment

### Empfohlene Plattformen:
- **Railway** (einfachste Option)
- **Heroku** (kostenlos starten)
- **DigitalOcean** (beste Kosten-Leistung)
- **Google Cloud Run** (serverless)
- **AWS** (enterprise)

### Docker-Support
```bash
# Docker Image bauen
docker build -t fuxbln-marketing-tool .

# Container starten
docker run -p 8501:8501 -e PASSWORD=dein_passwort fuxbln-marketing-tool
```

## 🔧 Konfiguration

### Telegram-Anmeldung
1. **API-Zugangsdaten** von https://my.telegram.org erhalten
2. **Kontotyp wählen** (Bot oder Benutzer)
3. **Token/Session-String** konfigurieren

### Verbindungen einrichten
1. **Quell-Chat** definieren
2. **Ziel-Chats** hinzufügen
3. **Intervall-Nachrichten** konfigurieren (optional)

### Plugins aktivieren
- **Filter** für Nachrichtenkontrolle
- **Format** für Textgestaltung
- **Wasserzeichen** für Medien
- **OCR** für Texterkennung

## 🎯 Verwendung

### Intervall-Nachrichten
```yaml
# Beispiel-Konfiguration
Intervall-Nachrichten aktivieren: true
Intervall in Sekunden: 60
Nachrichtentext: "Automatische Nachricht vom FUXBLN Marketing Tool"
```

### Bot-Befehle
- `/start` - Prüfen, ob ich aktiv bin
- `/forward` - Neue Weiterleitung einrichten
- `/remove` - Bestehende Weiterleitung entfernen
- `/help` - Verwendung lernen

## 🔒 Sicherheit

- **Starke Passwörter** für Web-Interface
- **HTTPS/SSL** für sichere Verbindungen
- **API-Zugangsdaten** sicher aufbewahren
- **Regelmäßige Updates** durchführen

## 📞 Support

### Ressourcen
- **GitHub Repository:** https://github.com/LSRBLN/fuxbln
- **Wiki:** Detaillierte Dokumentation
- **Video-Tutorials:** Schritt-für-Schritt Anleitungen
- **Community:** GitHub Discussions

### Kontakt
- **Entwickler:** LSRBLN Team
- **Issues:** GitHub Issues für technische Probleme
- **Discussions:** GitHub Discussions für Fragen

## 🏆 Besonderheiten

### 🎨 **Berlin-Design**
- Inspiriert von der Berliner Kultur
- Professionelles Schwarz-Weiß-Rot Farbschema
- Moderne UI mit roten Akzenten
- Responsive und benutzerfreundlich

### 🇩🇪 **Deutsche Lokalisierung**
- Vollständige Übersetzung aller Funktionen
- Deutsche Benutzeroberfläche
- Deutsche Dokumentation
- Deutsche Bot-Befehle

### ⏰ **Intervall-Nachrichten**
- Automatisches Senden in regelmäßigen Abständen
- Flexibel konfigurierbare Zeitintervalle
- Benutzerdefinierte Nachrichten
- Multi-Ziel-Unterstützung

## 📄 Lizenz

Dieses Projekt basiert auf dem ursprünglichen [tgcf](https://github.com/aahnik/tgcf) Projekt und wurde für das FUXBLN Marketing Tool angepasst.

## 🎯 Roadmap

- [ ] **Mobile App** für iOS/Android
- [ ] **API-Integration** für externe Systeme
- [ ] **Analytics Dashboard** für Statistiken
- [ ] **Multi-Sprach-Support** (zusätzlich zu Deutsch)
- [ ] **Cloud-Synchronisation** für Konfigurationen

---

**🎯 Das FUXBLN Marketing Tool - Ihr ultimativer Partner für professionelle Telegram-Marketing-Automatisierung!**

*Entwickelt mit ❤️ in Berlin*
