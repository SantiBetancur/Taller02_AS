from flask import Blueprint
from flask import render_template
from app_controller import get_random_pokenea 

image_phrase = Blueprint('image_phrase', __name__)

@image_phrase.route('/imagen&frase/')
def imagen_frase():
    pokenea = get_random_pokenea()
    pokenea_context = {
        'id': pokenea['id'],
        'nombre': pokenea['nombre'],
        'imagen': pokenea['imagen'],
        'frase_filosofica': pokenea['frase_filosofica'],
        'container_id': ""
    }
    return render_template('imagen&frase.html', pokenea=pokenea_context)