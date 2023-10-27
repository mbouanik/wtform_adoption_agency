from flask import Blueprint, render_template
from init import db
from models import Pet

app_routes = Blueprint('app_routes', __name__, template_folder="templates", static_folder="static", static_url_path='/app_routes/static')


@app_routes.route("/")
def home():
    pets = db.session.execute(db.select(Pet)).scalars()
    return render_template('home.html', pets=pets)
