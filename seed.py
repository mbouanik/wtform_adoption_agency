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
        notes="Bad dog",
        available=True
    ),
    Pet(
        name='Luna',
        spices='cat',
        photo_url='https://hips.hearstapps.com/hmg-prod/images/large-cat-breed-maine-coon-1553270773.jpg?crop=1xw:1xh;center,top&resize=980:*',
        age=1,
        notes="Bad cat",
        available=True
    ),
    Pet(
        name='Moonlight',
        spices='dog',
        photo_url='https://hips.hearstapps.com/ghk.h-cdn.co/assets/16/08/gettyimages-464163411.jpg?crop=1.0xw:1xh;center,top&resize=980:*',
        age=8,
        notes="Bad dog",
        available=False
    ),
    Pet(
        name='Knight',
        spices='lion',
        photo_url='https://images.pexels.com/photos/6180778/pexels-photo-6180778.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
        age=9,
        notes="Bad zebra",
        available=True
    ),
    Pet(
        name='Foxy',
        spices='dog',
        photo_url='https://hips.hearstapps.com/ghk.h-cdn.co/assets/16/15/welsh-springer-spaniel.jpg?crop=0.44423529411764706xw:1xh;center,top&resize=980:*',
        age=1,
        notes="Bad dog",
        available=True
    ),
    Pet(
        name='Huma',
        spices='cat',
        photo_url='https://hips.hearstapps.com/hmg-prod/images/chausie-abyssinian-cat-on-dark-brown-background-royalty-free-image-837639058-1553192486.jpg?crop=0.447xw:1.00xh;0.397xw,0&resize=980:*',
        age=4,
        notes="Bad cat",
        available=True
    ),
    Pet(
        name='Moon',
        spices='dog',
        photo_url='https://hips.hearstapps.com/ghk.h-cdn.co/assets/16/08/gettyimages-147786673.jpg?crop=0.4444444444444445xw:1xh;center,top&resize=980:*',
        age=4,
        notes="Bad Dog",
        available=True
    ),
    Pet(
        name='Misk',
        spices='dog',
        photo_url='https://hips.hearstapps.com/ghk.h-cdn.co/assets/16/08/1280x1919/gettyimages-179494696.jpg?resize=980:*',
        age=4,
        notes="Bad cat",
        available=True
    ),
    Pet(
        name='Kaiz',
        spices='dog',
        photo_url='https://hips.hearstapps.com/ghk.h-cdn.co/assets/17/30/1500912970-shiba-inu.jpg?crop=1.0xw:1xh;center,top&resize=980:*',
        age=4,
        notes="Bad Dog",
        available=True
    ),
    Pet(
        name='Noon',
        spices='cat',
        photo_url='https://hips.hearstapps.com/hmg-prod/images/turkish-van-cat-1553270460.jpg?crop=1xw:1xh;center,top&resize=980:*',
        age=4,
        notes="Bad Cat",
        available=True
    ),
    Pet(
        name='Avalon',
        spices='cat',
        photo_url='https://hips.hearstapps.com/hmg-prod/images/american-bobtail-cat-royalty-free-image-808975462-1553192401.jpg?crop=0.447xw:1.00xh;0.175xw,0&resize=980:*',
        age=4,
        notes="Bad Cat",
        available=True
    ),
    Pet(
        name='GreyBorn',
        spices='cat',
        photo_url='https://hips.hearstapps.com/hmg-prod/images/elegant-british-short-hair-cat-sitting-and-looking-royalty-free-image-859411020-1553192330.jpg?crop=0.650xw:0.651xh;0.153xw,0.349xh&resize=980:*',
        age=4,
        notes="Bad Cat",
        available=True
    ),
    Pet(
        name='Obito',
        spices='cat',
        photo_url='https://hips.hearstapps.com/hmg-prod/images/ragdoll-cat-with-intense-blue-eyes-royalty-free-image-107791319-1553192229.jpg?crop=0.432xw:0.974xh;0.446xw,0.00512xh&resize=980:*',
        age=4,
        notes="Bad Cat",
        available=True
    ),
    Pet(
        name='Baich',
        spices='cat',
        photo_url='https://hips.hearstapps.com/hmg-prod/images/large-cat-breed-maine-coon-1553270773.jpg?crop=1xw:1xh;center,top&resize=980:*',
        age=4,
        notes="Bad Cat",
        available=True
    ),



]

with app.app_context():
    db.session.add_all(pets)
    db.session.commit()
