from flask import Blueprint, render_template

index_route = Blueprint('main', __name__)
@index_route.route('/')
def index():
    return render_template('index.html')