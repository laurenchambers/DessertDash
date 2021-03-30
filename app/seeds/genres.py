from app.models import db, Genre


def seed_genres():

    genre1 = Genre(name="Cakes")
    genre2 = Genre(name="Cupcakes")
    genre3 = Genre(name="Pies")
    genre4 = Genre(name="Chocolate")
    genre5 = Genre(name="Candy")
    genre6 = Genre(name="Ice Cream")
    genre7 = Genre(name="Donuts")
    genre8 = Genre(name="Pastries")
    genre9 = Genre(name="Gelato")
    genre10 = Genre(name="Vegan")
    genre11 = Genre(name="Cookies")


    db.session.add(genre1)
    db.session.add(genre2)
    db.session.add(genre3)
    db.session.add(genre4)
    db.session.add(genre5)
    db.session.add(genre6)
    db.session.add(genre7)
    db.session.add(genre8)
    db.session.add(genre9)
    db.session.add(genre10)
    db.session.add(genre11)



    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_genres():
    db.session.execute('TRUNCATE genres CASCADE;')
    db.session.commit()
