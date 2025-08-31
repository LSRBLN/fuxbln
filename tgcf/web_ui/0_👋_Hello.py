import streamlit as st

from tgcf.web_ui.utils import hide_st, switch_theme
from tgcf.config import read_config

CONFIG = read_config()

st.set_page_config(
    page_title="FUXBLN Marketing Tool",
    page_icon="👋",
)
hide_st(st)
switch_theme(st, CONFIG)
st.write("# Willkommen beim FUXBLN Marketing Tool 👋")

html = """
<p align="center">
<img src = "https://user-images.githubusercontent.com/66209958/115183360-3fa4d500-a0f9-11eb-9c0f-c5ed03a9ae17.png" alt = "FUXBLN Marketing Tool Logo"  width=120>
</p>
"""

st.components.v1.html(html, width=None, height=None, scrolling=False)

with st.expander("Funktionen"):
    st.markdown(
        """
    Das FUXBLN Marketing Tool ist das ultimative Werkzeug zur Automatisierung der benutzerdefinierten Telegram-Nachrichtenweiterleitung.

    Die wichtigsten Funktionen sind:

    - Weiterleitung von Nachrichten als "weitergeleitet" oder Versand einer Kopie der Nachrichten von Quell- zu Zielchats. Ein Chat kann alles sein: eine Gruppe, ein Kanal, eine Person oder sogar ein anderer Bot.

    - Unterstützt zwei Betriebsmodi: Vergangenheit oder Live. Der Vergangenheitsmodus befasst sich mit allen bestehenden Nachrichten, während der Live-Modus für kommende Nachrichten ist.

    - Sie können sich mit einem Bot- oder Benutzerkonto anmelden. Telegram setzt bestimmte Einschränkungen für Bot-Konten. Sie können ein Benutzerkonto verwenden, um die Weiterleitungen durchzuführen, wenn Sie möchten.

    - Führen Sie benutzerdefinierte Manipulationen an Nachrichten durch. Sie können filtern, formatieren, ersetzen, Wasserzeichen hinzufügen, OCR durchführen und alles andere, was Sie benötigen!

    - Detaillierte Wiki + Video-Tutorial. Sie können auch Hilfe von der Community erhalten.

    - Wenn Sie ein Python-Entwickler sind, ist das Schreiben von Plugins für das FUXBLN Marketing Tool wie Süßigkeiten von einem Baby stehlen. Plugins modifizieren die Nachricht, bevor sie an den Zielchat gesendet werden.

    Worauf warten Sie noch? Markieren Sie das Repo mit einem Stern und klicken Sie auf Beobachten, um Updates zu erhalten.
        """
    )

with st.expander("📖 Vollständige Bedienungsanleitung"):
    st.markdown(
        """
## 🚀 FUXBLN Marketing Tool - Vollständige Bedienungsanleitung

### 📋 Inhaltsverzeichnis
1. [Erste Schritte](#erste-schritte)
2. [Telegram-Anmeldung](#telegram-anmeldung)
3. [Administratoren einrichten](#administratoren-einrichten)
4. [Verbindungen konfigurieren](#verbindungen-konfigurieren)
5. [Plugins verwenden](#plugins-verwenden)
6. [Intervall-Nachrichten](#intervall-nachrichten)
7. [Tool starten](#tool-starten)
8. [Erweiterte Einstellungen](#erweiterte-einstellungen)
9. [Troubleshooting](#troubleshooting)

---

### 🔧 Erste Schritte

#### Voraussetzungen:
- **Telegram-Konto** (Bot oder Benutzerkonto)
- **API-Zugangsdaten** von https://my.telegram.org
- **Stabile Internetverbindung**

#### Installation:
1. Das Tool ist bereits installiert und läuft auf **http://localhost:8501**
2. Öffnen Sie die URL in Ihrem Browser
3. Geben Sie das Passwort ein: `mein_sicheres_passwort_123`

---

### 🔑 Telegram-Anmeldung

#### Schritt 1: API-Zugangsdaten erhalten
1. Besuchen Sie https://my.telegram.org
2. Melden Sie sich mit Ihrer Telefonnummer an
3. Erstellen Sie eine neue Anwendung
4. Notieren Sie sich **API ID** und **API HASH**

#### Schritt 2: Kontotyp wählen

**Option A: Bot-Konto (Empfohlen für Anfänger)**
- ✅ Einfacher zu konfigurieren
- ✅ Weniger Einschränkungen
- ❌ Kann keine Chat-Verläufe lesen

**Option B: Benutzerkonto (Für erweiterte Funktionen)**
- ✅ Kann Chat-Verläufe lesen
- ✅ Mehr Funktionen verfügbar
- ❌ Komplexere Einrichtung

#### Schritt 3: Anmeldung konfigurieren
1. Gehen Sie zu **"Telegram Anmeldung"**
2. Geben Sie **API ID** und **API HASH** ein
3. Wählen Sie Ihren **Kontotyp**
4. Für Bot: Geben Sie den **Bot-Token** ein
5. Für Benutzer: Verwenden Sie **tg-login** für Session-String
6. Klicken Sie **"Speichern"**

---

### ⭐ Administratoren einrichten

#### Administrator hinzufügen:
1. Gehen Sie zu **"Administratoren"**
2. Geben Sie **Benutzernamen** oder **Telegram-ID** ein
3. Ein Administrator pro Zeile
4. Klicken Sie **"Speichern"**

**Beispiele:**
```
@benutzername
123456789
```

---

### 🔗 Verbindungen konfigurieren

#### Neue Verbindung erstellen:
1. Gehen Sie zu **"Verbindungen"**
2. Klicken Sie **"Neue Verbindung hinzufügen"**
3. Konfigurieren Sie die Verbindung:

#### Metadaten bearbeiten:
- **Name der Verbindung:** Beschreibender Name (z.B. "Marketing-Kanal")
- **Verbindung verwenden:** Aktivieren/deaktivieren

#### Quelle und Ziel:
- **Quelle:** Chat-ID oder @username der Quelle
- **Ziele:** Chat-IDs oder @usernames der Ziele (ein pro Zeile)

**Chat-IDs finden:**
- Gruppen: `-100` + Nummer
- Kanäle: `-100` + Nummer  
- Benutzer: Direkte Nummer

#### Vergangenheitsmodus-Einstellungen:
- **Offset:** Startpunkt für Nachrichten (0 = von Anfang)
- **Ende:** Endpunkt für Nachrichten (0 = bis Ende)

#### Intervall-Nachrichten:
- **Intervall-Nachrichten aktivieren:** Automatisches Senden
- **Intervall in Sekunden:** Zeit zwischen Nachrichten (10-3600)
- **Nachrichtentext:** Text für automatische Nachrichten

---

### 🔌 Plugins verwenden

#### Filter:
- **Text-Filter:** Bestimmte Wörter erlauben/blockieren
- **Benutzer-Filter:** Bestimmte Benutzer erlauben/blockieren
- **Datei-Filter:** Bestimmte Dateitypen erlauben/blockieren

#### Format:
- **Stil anwenden:** Fett, kursiv, durchgestrichen, etc.
- **Optionen:** preserve, normal, bold, italics, code, strike

#### Wasserzeichen:
- **Wasserzeichen-Bild hochladen:** PNG-Datei
- **Auf Medien anwenden:** Bilder und Videos

#### OCR:
- **OCR für Bilder aktivieren:** Texterkennung in Bildern
- **Voraussetzung:** tesseract installiert

#### Ersetzen:
- **Textersetzung anwenden:** Wörter/Ausdrücke ersetzen
- **Format:** `'original': 'ersetzung'`
- **Regex-Unterstützung:** Für komplexe Ersetzungen

#### Beschriftung:
- **Kopfzeile:** Text vor der Nachricht
- **Fußzeile:** Text nach der Nachricht

#### Absender:
- **Absender ändern:** Anderen Bot/Benutzer als Absender verwenden
- **Voraussetzung:** "Weitergeleitet von" deaktiviert

---

### ⏰ Intervall-Nachrichten

#### Konfiguration:
1. Gehen Sie zu **"Verbindungen"**
2. Erweitern Sie **"Intervall-Nachrichten"**
3. Aktivieren Sie **"Intervall-Nachrichten aktivieren"**
4. Stellen Sie das **Intervall in Sekunden** ein
5. Schreiben Sie den **Nachrichtentext**
6. Klicken Sie **"Speichern"**

#### Beispiele:
- **60 Sekunden:** Alle 1 Minute eine Nachricht
- **300 Sekunden:** Alle 5 Minuten eine Nachricht
- **3600 Sekunden:** Alle Stunde eine Nachricht

---

### 🏃 Tool starten

#### Konfiguration:
1. Gehen Sie zu **"Ausführen"**
2. Konfigurieren Sie die Ausführung:

#### Modus wählen:
- **Live:** Echtzeit-Weiterleitung neuer Nachrichten
- **Past:** Weiterleitung bestehender Nachrichten (nur Benutzerkonten)

#### Einstellungen:
- **"Weitergeleitet von" anzeigen:** Ursprung anzeigen
- **Verzögerung:** Zeit zwischen Nachrichten (Past-Modus)
- **Synchronisieren bei Löschung:** Nachrichten auch löschen

#### Starten:
1. Klicken Sie **"Starten"**
2. Überwachen Sie die Logs
3. Zum Stoppen: **"Stoppen"** klicken

---

### 🔬 Erweiterte Einstellungen

#### Konfiguration exportieren:
1. Gehen Sie zu **"Erweitert"**
2. Klicken Sie **"Ich stimme zu"**
3. **"Konfiguration JSON herunterladen"**

#### Spezielle Live-Modus-Optionen:
- **Sequenzielle Updates erzwingen:** Reihenfolge beibehalten
- **Nachricht löschen bei Bearbeitung:** Automatisches Löschen

#### Bot-Nachrichten anpassen:
- **Start-Befehl:** Antwort auf /start
- **Help-Befehl:** Antwort auf /help

---

### 🔧 Troubleshooting

#### Häufige Probleme:

**1. "API-Zugangsdaten falsch"**
- Überprüfen Sie API ID und API HASH
- Stellen Sie sicher, dass die Anwendung aktiv ist

**2. "Bot-Token ungültig"**
- Überprüfen Sie den Bot-Token bei @BotFather
- Stellen Sie sicher, dass der Bot aktiv ist

**3. "Keine Berechtigung"**
- Überprüfen Sie die Administrator-Liste
- Stellen Sie sicher, dass Sie Admin sind

**4. "Chat nicht gefunden"**
- Überprüfen Sie Chat-IDs und @usernames
- Stellen Sie sicher, dass der Bot/Benutzer im Chat ist

**5. "Intervall-Nachrichten funktionieren nicht"**
- Überprüfen Sie die Intervall-Einstellungen
- Stellen Sie sicher, dass das Tool läuft

#### Logs überprüfen:
1. Gehen Sie zu **"Ausführen"**
2. Scrollen Sie zu den Logs
3. Überprüfen Sie Fehlermeldungen
4. Verwenden Sie **"Weitere Logs laden"**

#### Support:
- **GitHub Issues:** Für technische Probleme
- **Community:** Für allgemeine Fragen
- **Wiki:** Für detaillierte Dokumentation

---

### 💡 Tipps und Tricks

#### Best Practices:
1. **Testen Sie zuerst** mit kleinen Gruppen
2. **Backup erstellen** vor großen Änderungen
3. **Logs überwachen** regelmäßig
4. **Intervall nicht zu kurz** setzen (mindestens 10 Sekunden)
5. **Wasserzeichen sparsam** verwenden

#### Performance-Optimierung:
- Verwenden Sie **Filter** um unnötige Nachrichten zu blockieren
- **Regex** für komplexe Ersetzungen
- **OCR** nur bei Bedarf aktivieren

#### Sicherheit:
- **Starke Passwörter** verwenden
- **API-Zugangsdaten** sicher aufbewahren
- **Administratoren** sorgfältig auswählen
- **Regelmäßige Updates** durchführen

---

### 📞 Support und Hilfe

#### Ressourcen:
- **GitHub Repository:** https://github.com/aahnik/tgcf
- **Wiki:** https://github.com/aahnik/tgcf/wiki
- **Video-Tutorials:** https://www.youtube.com/playlist?list=PLSTrsq_DvEgisMG5BLUf97tp2DoAnwCMG
- **Community:** GitHub Discussions

#### Kontakt:
- **Entwickler:** aahnik
- **Issues:** GitHub Issues
- **Discussions:** GitHub Discussions

---

**🎯 Das FUXBLN Marketing Tool ist Ihr ultimativer Partner für professionelle Telegram-Marketing-Automatisierung!**
        """
    )

st.warning("Bitte drücken Sie Speichern, nachdem Sie eine Konfiguration geändert haben.")
