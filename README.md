# API REST FastAPI avec Base de Données

Une API REST simple construite avec FastAPI et SQLAlchemy.

## Fonctionnalités

- CRUD complet pour les produits
- Base de données SQLite
- Documentation API automatique avec Swagger/ReDoc
- Déploiement sur Azure App Service

## Endpoints

- `GET /` - Message de bienvenue
- `POST /products/` - Créer un produit
- `GET /products/` - Lister tous les produits
- `GET /products/{id}` - Obtenir un produit par ID
- `PUT /products/{id}` - Mettre à jour un produit
- `DELETE /products/{id}` - Supprimer un produit

## Installation locale

```bash
pip install -r requirements.txt
python ApiRest.py
```

## Déploiement Azure

Cette application est configurée pour être déployée sur Azure App Service.

### Prérequis
- Compte Azure Student
- Azure CLI installé

### Étapes de déploiement

1. Créer un groupe de ressources
2. Créer un App Service Plan
3. Créer une Web App
4. Déployer le code

Voir les commandes détaillées ci-dessous.
