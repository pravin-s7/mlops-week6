# MLOPS-Week-6 (Iris Classifier API – MLOps Deployment with GCP, Docker, Kubernetes & CML)

**Name**: PRAVIN S
**Roll No**: 22f1001797

This project deploys a machine learning model (Iris classifier) using a FastAPI backend served via Docker, Kubernetes (GKE Autopilot), and CI/CD powered by GitHub Actions and CML.

---

## 📆 Features

- ✅ FastAPI for serving ML model
- 🐳 Dockerized API
- ☁️ Kubernetes Autopilot deployment (GCP)
- 🔁 Continuous Deployment with GitHub Actions & CML
- 📆 Container pushed to Artifact Registry
- 🔗 Exposed with LoadBalancer via Kubernetes Service

---

## 📁 Project Structure

```

.
├── app/
│   ├── iris\_fastapi.py
│   ├── model.joblib
│   ├── requirements.txt
│   └── Dockerfile
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── iris.csv
└── .github/
└── workflows/
└── cml-deploy.yaml

````

---

## 🚀 Quickstart Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
````

---

### 2️⃣ Enable GCP Services (Run in Cloud Shell)

```bash
gcloud services enable container.googleapis.com
gcloud services enable artifactregistry.googleapis.com
```

---

### 3️⃣ Create Artifact Registry

```bash
gcloud artifacts repositories create iris-repo \
  --repository-format=docker \
  --location=us-central1
```

---

### 4️⃣ Create Kubernetes Autopilot Cluster

```bash
gcloud container clusters create-auto iris-cluster \
  --region=us-central1
```

---

### 5️⃣ Authenticate & Apply K8s Manifests

```bash
gcloud container clusters get-credentials iris-cluster \
  --region=us-central1

kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

---

### 6️⃣ Add GitHub Secrets

In your GitHub repo, go to:

**Settings → Secrets and variables → Actions → New repository secret**

Add:

| Name             | Value                       |
| ---------------- | --------------------------- |
| `GCP_PROJECT_ID` | Your GCP project ID         |
| `GCP_SA_KEY`     | JSON key of service account |

---

### 7️⃣ Trigger Deployment

Push code to `main` branch:

```bash
git add .
git commit -m "Initial CI/CD setup"
git push origin main
```

---

### 8️⃣ Test the API

```bash
kubectl get service iris-service
```

Use the external IP to test prediction:

```bash
curl -X POST http://<EXTERNAL-IP>/predict/ \
-H "Content-Type: application/json" \
-d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
```

---

## 📌 Notes

* Ensure your `Dockerfile` uses port `8200`
* Kubernetes manifests should request limited resources for Autopilot compatibility
* The Docker image is stored in GCP Artifact Registry
* CML + GitHub Actions automatically handles image build and redeployment