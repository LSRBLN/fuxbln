# 🚀 FUXBLN Marketing Tool - Google Cloud Run Deployment

## 📋 Voraussetzungen

1. **Google Cloud Account** (kostenlos mit $300 Guthaben)
2. **Google Cloud CLI (gcloud)** installiert
3. **Docker** installiert (optional, für lokales Testen)

## 🔧 Setup-Schritte

### 1. Google Cloud CLI installieren

```bash
# macOS
brew install google-cloud-sdk

# Oder von Google herunterladen:
# https://cloud.google.com/sdk/docs/install
```

### 2. Anmelden und Projekt einrichten

```bash
# Anmelden
gcloud auth login

# Neues Projekt erstellen (oder bestehendes verwenden)
gcloud projects create fuxbln-marketing-tool --name="FUXBLN Marketing Tool"

# Projekt setzen
gcloud config set project fuxbln-marketing-tool

# APIs aktivieren
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable containerregistry.googleapis.com
```

### 3. Deployment ausführen

#### Option A: Automatisches Deployment (Empfohlen)

```bash
# Cloud Build Trigger erstellen
gcloud builds submit --config cloudbuild.yaml .

# Oder direkt deployen
gcloud run deploy fuxbln-marketing-tool \
  --source . \
  --region europe-west1 \
  --platform managed \
  --allow-unauthenticated \
  --memory 1Gi \
  --cpu 1 \
  --max-instances 10
```

#### Option B: Manuelles Deployment

```bash
# Docker Image bauen
docker build -t gcr.io/fuxbln-marketing-tool/fuxbln-marketing-tool .

# Image pushen
docker push gcr.io/fuxbln-marketing-tool/fuxbln-marketing-tool

# Cloud Run Service erstellen
gcloud run deploy fuxbln-marketing-tool \
  --image gcr.io/fuxbln-marketing-tool/fuxbln-marketing-tool \
  --region europe-west1 \
  --platform managed \
  --allow-unauthenticated
```

### 4. Environment Variables setzen

```bash
# Environment Variables für den Service setzen
gcloud run services update fuxbln-marketing-tool \
  --region europe-west1 \
  --update-env-vars API_ID=deine_telegram_api_id \
  --update-env-vars API_HASH=dein_telegram_api_hash \
  --update-env-vars PASSWORD=dein_sicheres_passwort
```

## 🌐 Service URL

Nach dem Deployment erhältst du eine URL wie:
```
https://fuxbln-marketing-tool-xxxxx-ew.a.run.app
```

## 💰 Kosten

- **Cloud Run:** Pay-per-use (kostenlos bis 2 Millionen Requests/Monat)
- **Container Registry:** Kostenlos für öffentliche Images
- **Cloud Build:** 120 Build-Minuten/Monat kostenlos

## 🔄 Automatisches Deployment

### GitHub Actions Integration

Erstelle `.github/workflows/google-cloud-deploy.yml`:

```yaml
name: Deploy to Google Cloud Run

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Setup Google Cloud CLI
      uses: google-github-actions/setup-gcloud@v0
      with:
        project_id: ${{ secrets.GCP_PROJECT_ID }}
        service_account_key: ${{ secrets.GCP_SA_KEY }}
    
    - name: Deploy to Cloud Run
      run: |
        gcloud run deploy fuxbln-marketing-tool \
          --source . \
          --region europe-west1 \
          --platform managed \
          --allow-unauthenticated
```

## 🛠️ Troubleshooting

### Häufige Probleme:

1. **Permission Denied:**
   ```bash
   gcloud auth application-default login
   ```

2. **API nicht aktiviert:**
   ```bash
   gcloud services enable cloudbuild.googleapis.com
   gcloud services enable run.googleapis.com
   ```

3. **Memory/CPU Limits:**
   - Erhöhe Memory: `--memory 2Gi`
   - Erhöhe CPU: `--cpu 2`

4. **Port Probleme:**
   - Stelle sicher, dass die App auf `$PORT` hört
   - Cloud Run setzt automatisch die PORT Variable

## 📊 Monitoring

```bash
# Logs anzeigen
gcloud logs tail --service=fuxbln-marketing-tool

# Service Status
gcloud run services describe fuxbln-marketing-tool --region=europe-west1

# Metrics
gcloud run services list --region=europe-west1
```

## 🔒 Sicherheit

- **HTTPS:** Automatisch aktiviert
- **Authentication:** Optional über IAM
- **Secrets:** Verwende Google Secret Manager für sensitive Daten

## 🎯 Vorteile von Google Cloud Run

✅ **Serverless:** Keine Server-Verwaltung
✅ **Auto-Scaling:** Automatische Skalierung
✅ **Pay-per-use:** Nur für tatsächliche Nutzung zahlen
✅ **Global:** Verfügbar in allen Google Cloud Regionen
✅ **Secure:** Automatische HTTPS und Security
✅ **Fast:** Cold Start < 1 Sekunde
