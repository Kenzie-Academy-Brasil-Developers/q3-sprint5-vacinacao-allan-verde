from app.models.vaccine_model import VaccineCards


def serialize(vaccine: VaccineCards):
    return {
        "cpf": vaccine.cpf,
        "name": vaccine.name,
        "first_shot_date": vaccine.first_shot_date,
        "second_shot_date": vaccine.second_shot_date,
        "vaccine_name": vaccine.vaccine_name,
        "health_unit_name": vaccine.health_unit_name,
    }