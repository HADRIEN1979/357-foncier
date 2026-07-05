# 3.5.7 FONCIER

Assistant de prospection et d'analyse foncière pour détecter les parcelles à potentiel à partir de données publiques : cadastre, zonage PLU, bâtiments et contraintes.

## Objectif V0.1

Analyser une commune pilote, filtrer les parcelles de plus de 1 000 m², calculer un premier score de potentiel foncier et générer un export Excel exploitable.

## Fonctionnalités prévues

- Import des parcelles cadastrales publiques
- Filtrage par surface minimale
- Analyse de la surface, de la forme et de l'emprise bâtie
- Scoring foncier V0
- Classement A+, A, B, C, D
- Export Excel
- Documentation métier et technique

## Stack technique cible

- Backend : Python / FastAPI
- Analyse géographique : GeoPandas, Shapely
- Base future : PostgreSQL + PostGIS
- Frontend futur : React / TypeScript
- Exports : Excel, PDF, cartes

## Démarrage rapide

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows : .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Puis ouvrir : http://127.0.0.1:8000/docs

## Statut

Prototype initial en construction.
