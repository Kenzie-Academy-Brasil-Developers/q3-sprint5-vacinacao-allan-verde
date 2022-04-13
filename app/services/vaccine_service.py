from app.models.vaccine_model import VaccineCards
import re


def serialize(vaccine: VaccineCards):
    return {
        "cpf": vaccine.cpf,
        "name": vaccine.name,
        "first_shot_date": vaccine.first_shot_date,
        "second_shot_date": vaccine.second_shot_date,
        "vaccine_name": vaccine.vaccine_name,
        "health_unit_name": vaccine.health_unit_name,
    }

def normalize(payload: dict):
    payload["name"] = re.sub("\s+", " ", payload["name"].title().strip())
    payload["vaccine_name"] = re.sub("\s+", " ", payload["vaccine_name"].title().strip())
    payload["health_unit_name"] = re.sub("\s+", " ", payload["health_unit_name"].title().strip())
