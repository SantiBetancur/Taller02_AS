from flask import Flask, jsonify, render_template
from flask_cors import CORS
import random
from blueprints.home import home
from blueprints.image_phrase import image_phrase

app = Flask(__name__)
CORS(app) 

app.register_blueprint(home)
app.register_blueprint(image_phrase)



if __name__ == '__main__':
    app.run(debug=True)