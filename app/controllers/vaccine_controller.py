from datetime import datetime, timedelta
from http import HTTPStatus

from app.configs.database import db
from app.models.exc_model import CPFError, KeyDataError, TypeDataError
from app.models.vaccine_model import VaccineCards
from app.services.vaccine_service import normalize, serialize

from flask import request
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session


def create_vaccine():
    try:
        data = request.get_json()
        VaccineCards.type_value_and_keys_is_valids(data)
        normalize(data)
        
        data["first_shot_date"] = datetime.now()
        data["second_shot_date"] = data["first_shot_date"] + timedelta(days=90)

        vaccine = VaccineCards(**data)
        VaccineCards.cpf_is_valid(vaccine.cpf)

        session: Session = db.session()

        session.add(vaccine)
        session.commit()

        return serialize(vaccine), HTTPStatus.CREATED
    except CPFError:
        return {"error": 'O CPF deve possuir 11 caracteres numéricos'}, HTTPStatus.BAD_REQUEST
    except KeyDataError as e:
        return {"error": e.message}, HTTPStatus.BAD_REQUEST
    except TypeDataError as e:
        return {"error": e.message}, HTTPStatus.BAD_REQUEST
    except IntegrityError:
        return {"error": "CPF já cadastrado"}, HTTPStatus.CONFLICT


def get_all():
    vaccines = (VaccineCards.query.all())

    serializer = [ serialize(vaccine) for vaccine in vaccines]

    return {"vaccines": serializer}, HTTPStatus.OK
