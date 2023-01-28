"""Seed file to make sample data for pets db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add pets
Agent = User(
    first_name='Agent', 
    last_name='Smith',
    image_url="https://static.wikia.nocookie.net/matrix/images/4/4d/Agent-smith-the-matrix-movie-hd-wallpaper-2880x1800-4710.png/revision/latest?cb=20140504013834")
Joseph = User(
    first_name='Joseph', 
    last_name='Smith',
    image_url="https://newsroom.churchofjesuschrist.org/media/orig/Joseph-Smith-prophet.jpg")
Will = User(
    first_name='Will', 
    last_name='Smith',
    image_url="https://m.media-amazon.com/images/M/MV5BNTczMzk1MjU1MV5BMl5BanBnXkFtZTcwNDk2MzAyMg@@._V1_FMjpg_UX1000_.jpg")

# Add new objects to session, so they'll persist
db.session.add(Agent)
db.session.add(Joseph)
db.session.add(Will)

# Commit--otherwise, this never gets saved!
db.session.commit()
