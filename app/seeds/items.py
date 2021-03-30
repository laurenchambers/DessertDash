from app.models import db, Item, Restaurant


def seed_items():

    item1 = Item(restaurant_id=1,
                name="Uncle Darrryl",
                description="Four layers of chocolate cake with chocolate chips and toffee bits between the layers and chocolate buttercream icing, covered in dark chocolate ganache",
                price=10.95,
                image_src='https://images.squarespace-cdn.com/content/v1/5cdb04aac2ff6107d290586c/1606534442569-PA9YU1LEX53B7B1XJSOH/ke17ZwdGBToddI8pDm48kL1r5b2IZDeo0rxHX5J2V217gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1UX8TutUE5XLdAAYB3v_UXa9NltJiWcZUP7N03QThEUmZYCNktvz-O8E62ZORL8IqRg/Photo%2BJun%2B28%252C%2B11%2B05%2B16%2BPM.jpg?format=2500w')

    db.session.add(item1)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_items():
    db.session.execute('TRUNCATE items CASCADE;')
    db.session.commit()
