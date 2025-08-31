# 🔧 Google Cloud Setup für FUXBLN Marketing Tool

## 📋 Schritt-für-Schritt Anleitung

### 1. Billing Account einrichten

1. **Gehe zu:** https://console.cloud.google.com/billing/linkedaccount?project=fuxbln-marketing-tool
2. **Klicke auf:** "Link a billing account"
3. **Wähle:** "Create a new billing account" oder bestehenden Account
4. **Fülle aus:** Kreditkarten-Informationen (für $300 kostenloses Guthaben)

### 2. APIs aktivieren

Nach dem Billing-Setup:

```bash
# APIs aktivieren
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable containerregistry.googleapis.com
```

### 3. Service Account erstellen (für GitHub Actions)

```bash
# Service Account erstellen
gcloud iam service-accounts create fuxbln-deploy \
  --display-name="FUXBLN Deployment Service Account"

# Rollen zuweisen
gcloud projects add-iam-policy-binding fuxbln-marketing-tool \
  --member="serviceAccount:fuxbln-deploy@fuxbln-marketing-tool.iam.gserviceaccount.com" \
  --role="roles/run.admin"

gcloud projects add-iam-policy-binding fuxbln-marketing-tool \
  --member="serviceAccount:fuxbln-deploy@fuxbln-marketing-tool.iam.gserviceaccount.com" \
  --role="roles/storage.admin"

gcloud projects add-iam-policy-binding fuxbln-marketing-tool \
  --member="serviceAccount:fuxbln-deploy@fuxbln-marketing-tool.iam.gserviceaccount.com" \
  --role="roles/cloudbuild.builds.builder"

# Service Account Key erstellen
gcloud iam service-accounts keys create ~/fuxbln-deploy-key.json \
  --iam-account=fuxbln-deploy@fuxbln-marketing-tool.iam.gserviceaccount.com
```

### 4. GitHub Secrets setzen

Gehe zu: https://github.com/LSRBLN/fuxbln/settings/secrets/actions

Füge diese Secrets hinzu:

- **GCP_PROJECT_ID:** `fuxbln-marketing-tool`
- **GCP_SA_KEY:** Inhalt der `~/fuxbln-deploy-key.json` Datei
- **API_ID:** Deine Telegram API ID
- **API_HASH:** Dein Telegram API Hash
- **PASSWORD:** Dein sicheres Passwort

### 5. Deployment starten

```bash
# Manuelles Deployment
gcloud run deploy fuxbln-marketing-tool \
  --source . \
  --region europe-west1 \
  --platform managed \
  --allow-unauthenticated \
  --memory 1Gi \
  --cpu 1 \
  --max-instances 10
```

### 6. Environment Variables setzen

```bash
# Nach dem ersten Deployment
gcloud run services update fuxbln-marketing-tool \
  --region europe-west1 \
  --update-env-vars API_ID=deine_telegram_api_id \
  --update-env-vars API_HASH=dein_telegram_api_hash \
  --update-env-vars PASSWORD=dein_sicheres_passwort
```

## 🎯 Vorteile von Google Cloud Run

✅ **Kostenlos:** $300 Guthaben für neue Accounts
✅ **Pay-per-use:** Nur für tatsächliche Nutzung zahlen
✅ **Auto-scaling:** Automatische Skalierung
✅ **Global:** Verfügbar in allen Regionen
✅ **Secure:** Automatische HTTPS
✅ **Fast:** Cold Start < 1 Sekunde

## 💰 Kostenübersicht

- **Cloud Run:** Kostenlos bis 2 Millionen Requests/Monat
- **Container Registry:** Kostenlos für öffentliche Images
- **Cloud Build:** 120 Build-Minuten/Monat kostenlos
- **Networking:** Kostenlos für eingehenden Traffic

## 🚀 Nach dem Deployment

Das FUXBLN Marketing Tool wird verfügbar sein unter:
```
https://fuxbln-marketing-tool-xxxxx-ew.a.run.app
```

**Dashboard:** https://console.cloud.google.com/run/detail/europe-west1/fuxbln-marketing-tool
