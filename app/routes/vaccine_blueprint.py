from flask import Blueprint
from app.controllers.vaccine_controller import create_vaccine, get_all


bp = Blueprint('vaccine', __name__, url_prefix='/vaccines')

bp.post('')(create_vaccine)
bp.get('')(get_all)