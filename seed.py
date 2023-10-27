from app import app
from init import db
from models import Pet


with app.app_context():
    db.drop_all()
    db.create_all()

    
pets = [
    Pet(
        name='Chronos',
        spices='dog',
        photo_url='https://hips.hearstapps.com/hmg-prod/images/little-cute-maltipoo-puppy-royalty-free-image-1652926025.jpg?crop=0.444xw:1.00xh;0.129xw,0&resize=980:*',
        age=3,
        note="Bad dog",
        available=True
    ),
    Pet(
        name='Luna',
        spices='cat',
        photo_url='https://hips.hearstapps.com/hmg-prod/images/large-cat-breed-maine-coon-1553270773.jpg?crop=1xw:1xh;center,top&resize=980:*',
        age=1,
        note="Bad cat",
        available=True
    ),
    Pet(
        name='Moonlight',
        spices='dog',
        photo_url='https://hips.hearstapps.com/ghk.h-cdn.co/assets/16/08/gettyimages-464163411.jpg?crop=1.0xw:1xh;center,top&resize=980:*',
        age=8,
        note="Bad dog",
        available=False
    ),
    Pet(
        name='Knight',
        spices='lion',
        photo_url='https://images.pexels.com/photos/6180778/pexels-photo-6180778.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
        age=9,
        note="Bad zebra",
        available=True
    ),
    Pet(
        name='Foxy',
        spices='dog',
        photo_url='https://hips.hearstapps.com/ghk.h-cdn.co/assets/16/15/welsh-springer-spaniel.jpg?crop=0.44423529411764706xw:1xh;center,top&resize=980:*',
        age=1,
        note="Bad dog",
        available=True
    ),
    Pet(
        name='Huma',
        spices='cat',
        photo_url='https://hips.hearstapps.com/hmg-prod/images/chausie-abyssinian-cat-on-dark-brown-background-royalty-free-image-837639058-1553192486.jpg?crop=0.447xw:1.00xh;0.397xw,0&resize=980:*',
        age=4,
        note="Bad cat",
        available=True
    ),
]

with app.app_context():
    db.session.add_all(pets)
    db.session.commit()
