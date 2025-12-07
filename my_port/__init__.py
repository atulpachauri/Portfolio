from flask import Blueprint

port_bp = Blueprint(
    "port_bp",
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

from . import routes