from flask import Blueprint

calculate_bp = Blueprint('calculate_bp', __name__, template_folder='../templates')

from . import routes
