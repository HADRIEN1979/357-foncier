# Cahier des charges V0 — 3.5.7 FONCIER

## 1. Vision

3.5.7 FONCIER est un assistant de développement foncier destiné à repérer les propriétés privées présentant un potentiel de division, de densification ou de valorisation.

## 2. Objectif du MVP

Permettre à l'utilisateur de sélectionner une commune, d'identifier les parcelles de plus de 1 000 m² et de calculer un premier score de potentiel foncier.

## 3. Critères métier V0

- Surface minimale : 1 000 m²
- Priorité aux zones U et 1AU
- Recherche de maisons implantées en façade avec jardin arrière
- Recherche de grandes propriétés sous-exploitées
- Recherche de dents creuses et parcelles d'angle
- Exclusion ou dépriorisation des zones A, N et 2AU

## 4. Classement

- A+ : prospection immédiate
- A : très forte cible
- B : à étudier
- C : faible priorité
- D : à écarter

## 5. Livrables V0

- API de scoring
- Modèle de données parcelle
- Export Excel
- Documentation technique
