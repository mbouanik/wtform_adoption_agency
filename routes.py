from flask import Blueprint, redirect, render_template
from forms import AddPetForm
from init import db
from models import Pet

app_routes = Blueprint('app_routes', __name__, template_folder="templates", static_folder="static", static_url_path='/app_routes/static')


@app_routes.route("/")
def home():
    pets = db.session.execute(db.select(Pet).order_by(Pet.name)).scalars()
    return render_template('home.html', pets=pets)


@app_routes.route("/add", methods=["GET", "POST"])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        pet = Pet(
            name=form.name.data,
            spices=form.species.data,
            age=form.age.data,
            photo_url=form.photo_url.data,
            notes=form.notes.data,
            available=form.available.data
        )
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    return render_template('pet_form.html', form=form, form_type='Add')


@app_routes.route("/<int:pet_id>", methods=["GET", "POST"])
def show_and_edit_pet(pet_id):
    pet = db.get_or_404(Pet, pet_id)
    form = AddPetForm(obj=pet)
    if form.validate_on_submit():
        form.populate_obj(pet)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    return render_template('pet.html', pet=pet, form=form)
