# Architecture technique — 3.5.7 FONCIER

## V0.1

Backend Python FastAPI avec un premier moteur de scoring.

## Cible

- Backend : FastAPI
- Base : PostgreSQL/PostGIS
- Traitements SIG : GeoPandas, Shapely, GDAL/Pyogrio
- Frontend : React + TypeScript
- Cartographie : MapLibre GL ou Leaflet
- Exports : Excel, PDF, GeoPackage

## Modules

1. Import des données publiques
2. Nettoyage et normalisation
3. Analyse géométrique
4. Scoring foncier
5. Génération de rapports
6. Interface cartographique
7. CRM foncier
