from __future__ import annotations

CONSTRUCTIBLE_ZONES = {"UA", "UB", "UC", "UD", "UH", "UL", "1AU", "1AUC", "1AUD", "1AU-C", "1AU-D"}
LOW_PRIORITY_ZONES = {"A", "N", "2AU"}


def normalize_zone(zone: str | None) -> str:
    if not zone:
        return "INCONNUE"
    return zone.upper().replace(" ", "").replace("_", "-")


def score_parcelle(p: dict) -> tuple[int, dict]:
    """Score métier V0 sur 100.

    Ce score est volontairement simple au départ. Il sera amélioré après tests terrain.
    """
    details: dict[str, int | str] = {}
    total = 0

    surface = float(p.get("surface_m2") or 0)
    zone = normalize_zone(p.get("zone_plu"))
    emprise = float(p.get("emprise_batie_m2") or 0)
    maison_en_facade = p.get("maison_en_facade")
    acces_possible = p.get("acces_possible")
    terrain_angle = p.get("terrain_angle")
    contrainte_forte = p.get("contrainte_forte")

    # Urbanisme / 30
    if zone in CONSTRUCTIBLE_ZONES or zone.startswith("1AU"):
        urbanisme = 30
    elif zone in LOW_PRIORITY_ZONES:
        urbanisme = 5
    else:
        urbanisme = 15
    details["urbanisme"] = urbanisme
    total += urbanisme

    # Surface / 20
    if surface >= 3000:
        surface_score = 20
    elif surface >= 2000:
        surface_score = 17
    elif surface >= 1500:
        surface_score = 14
    elif surface >= 1000:
        surface_score = 10
    else:
        surface_score = 0
    details["surface"] = surface_score
    total += surface_score

    # Emprise bâtie faible / 10
    if surface > 0:
        ratio_bati = emprise / surface
    else:
        ratio_bati = 1
    if ratio_bati <= 0.08:
        bati_score = 10
    elif ratio_bati <= 0.15:
        bati_score = 7
    elif ratio_bati <= 0.25:
        bati_score = 4
    else:
        bati_score = 1
    details["emprise_batie"] = bati_score
    total += bati_score

    # Implantation / 15
    implantation = 15 if maison_en_facade is True else 8 if maison_en_facade is None else 3
    details["implantation"] = implantation
    total += implantation

    # Accès / 15
    acces = 15 if acces_possible is True else 8 if acces_possible is None else 2
    details["acces"] = acces
    total += acces

    # Bonus configuration / 5
    configuration = 5 if terrain_angle is True else 2
    details["configuration"] = configuration
    total += configuration

    # Contrainte / 5
    contraintes = 0 if contrainte_forte is True else 5
    details["contraintes"] = contraintes
    total += contraintes

    total = max(0, min(100, round(total)))
    details["zone_plu_normalisee"] = zone
    return total, details


def classify_score(score: int) -> str:
    if score >= 90:
        return "A+"
    if score >= 80:
        return "A"
    if score >= 65:
        return "B"
    if score >= 50:
        return "C"
    return "D"
