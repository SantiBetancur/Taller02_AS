from flask import Blueprint
from flask import render_template
from app_controller import get_random_pokenea

home = Blueprint('home', __name__)

@home.route('/')
def index():
    pokenea = get_random_pokenea()
    pokenea_context = {
        'id': pokenea['id'],
        'nombre': pokenea['nombre'],
        'altura': pokenea['altura'],
        'habilidad': pokenea['habilidad'],
        'container_id': ""
    }
    return render_template('index.html', pokenea=pokenea_context)