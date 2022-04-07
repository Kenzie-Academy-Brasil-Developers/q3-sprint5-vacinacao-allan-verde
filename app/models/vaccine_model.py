from sqlalchemy import Column, DateTime, Integer, String
from app.configs.database import db
from app.models.exc_model import CPFError, KeyDataError, TypeDataError
import re


class VaccineCards(db.Model):
    __tablename__ = "vaccine_cards"

    id = ...
    cpf = Column(String, primary_key=True)
    name = Column(String, nullable=True)
    first_shot_date = Column(DateTime)
    second_shot_date = Column(DateTime)
    vaccine_name = Column(String, nullable=True)
    health_unit_name = Column(String)

    @classmethod
    def cpf_is_valid(cls, cpf:str) -> None:
        if not cpf.isnumeric() or not len(cpf) == 11:
            raise CPFError

    @classmethod
    def type_value_and_keys_is_valids(cls, payload: dict) -> None: 
        EXPECTED_KEY = {"cpf", "name","vaccine_name", "health_unit_name"}

        received_key = payload.keys()

        if EXPECTED_KEY - received_key:
            raise KeyDataError(EXPECTED_KEY, received_key)
        elif received_key - EXPECTED_KEY:
            keys_extras = received_key - EXPECTED_KEY
            for key_extra in keys_extras:
                del payload[key_extra]

        for key,value in payload.items():
            if type(value) != str:
                raise TypeDataError(key)

    @classmethod
    def normalize(cls, payload: dict) -> dict:
        payload["name"] = re.sub("\s+", " ", payload["name"].title().strip())
        payload["vaccine_name"] = re.sub("\s+", " ", payload["vaccine_name"].title().strip())
        payload["health_unit_name"] = re.sub("\s+", " ", payload["health_unit_name"].title().strip())