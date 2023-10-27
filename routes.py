from flask import Blueprint, redirect, render_template
from forms import AddPetForm
from init import db
from models import Pet

app_routes = Blueprint('app_routes', __name__, template_folder="templates", static_folder="static", static_url_path='/app_routes/static')


@app_routes.route("/")
def home():
    pets = db.session.execute(db.select(Pet)).scalars()
    return render_template('home.html', pets=pets)

@app_routes.route("/pets/<int:pet_id>")
def show_pet(pet_id):
    pet = db.get_or_404(Pet, pet_id)
    return render_template('pet_detail.html', pet=pet)

@app_routes.route("/add", methods=["GET", "POST"])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        pet = Pet(
            name=form.name.data,
            spices=form.species.data,
            age=form.age.data,
            photo_url=form.photo_url.data,
            note=form.note.data,
            available=form.available.data
        )
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    return render_template('add_pet.html')
