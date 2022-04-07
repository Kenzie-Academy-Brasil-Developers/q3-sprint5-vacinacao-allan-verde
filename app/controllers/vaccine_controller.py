from app.models.exc_model import CPFError, KeyDataError, TypeDataError
from sqlalchemy.exc import IntegrityError
from app.models.vaccine_model import VaccineCards
from datetime import datetime, timedelta
from flask import current_app, request
from http import HTTPStatus


def create_vaccine():
    try:
        data = request.get_json()
        VaccineCards.type_value_and_keys_is_valids(data)
        
        data["first_shot_date"] = datetime.now()
        data["second_shot_date"] = data["first_shot_date"] + timedelta(days=90)

        vaccine = VaccineCards(**data)
        VaccineCards.cpf_is_valid(vaccine.cpf)

        current_app.db.session.add(vaccine)
        current_app.db.session.commit()

    except CPFError:
        return {"error": 'O CPF deve possuir 11 caracteres numéricos'}, HTTPStatus.BAD_REQUEST
    except KeyDataError as e:
        return {"error": e.message}, HTTPStatus.BAD_REQUEST
    except TypeDataError as e:
        return {"error": e.message}, HTTPStatus.BAD_REQUEST
    except IntegrityError:
        return {"error": "CPF já cadastrado"}, HTTPStatus.CONFLICT


    return {
        "cpf": vaccine.cpf,
        "name": vaccine.name,
        "first_shot_date": vaccine.first_shot_date,
        "second_shot_date": vaccine.second_shot_date,
        "vaccine_name": vaccine.vaccine_name,
        "health_unit_name": vaccine.health_unit_name,
    }, HTTPStatus.CREATED

def get_all():
    vaccines = (VaccineCards.query.all())

    serializer = [
        {
            "cpf": vaccine.cpf,
            "name": vaccine.name,
            "first_shot_date": vaccine.first_shot_date,
            "second_shot_date": vaccine.second_shot_date,
            "vaccine_name": vaccine.vaccine_name,
            "health_unit_name": vaccine.health_unit_name,
        } for vaccine in vaccines
    ]

    return {"vaccines": serializer}, HTTPStatus.OK