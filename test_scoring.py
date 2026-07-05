from backend.app.scoring import score_parcelle, classify_score


def test_score_good_parcel():
    score, details = score_parcelle({
        "surface_m2": 2200,
        "zone_plu": "UD",
        "emprise_batie_m2": 120,
        "maison_en_facade": True,
        "acces_possible": True,
        "terrain_angle": False,
        "contrainte_forte": False,
    })
    assert score >= 80
    assert classify_score(score) in {"A", "A+"}
