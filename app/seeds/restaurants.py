from app.models import db, Restaurant


def seed_restaurants():

    restaurant1 = Restaurant(name="Nothing Bundt Cakes",
                            description="Bakery chain with bundt cakes ranging from bite-sized to tiered, plus platters, candles & cards.",
                            address=" 2785 Bee Cave Rd",
                            city="Austin",
                            state="TX",
                            zip_code="78746",
                            latitude=30.274082967865112,
                            longitude=-97.78770001461015,
                            hours="9:00AM - 6:00PM",
                            price="$$",
                            rating=4.8,
                            )

    restaurant2 = Restaurant(name="Paper Route Baker",
                        description="Small batch artisanal bakery homegrown here in Austin! Homemade delicacies, organic & local ingredients.",
                        address="1835 W Alambama St",
                        city="Austin",
                        state="TX",
                        zip_code="78702",
                        latitude=30.261396556115916,
                        longitude=-97.73375683068825,
                        hours="8:00AM - 4:00PM",
                        price="$",
                        rating=4.9,
                        )
    restaurant3 = Restaurant(name="Sugar Mama's Bakeshop",
                        description="Well-known bakery offering cupcakes, cookies, bars & mini-pies in a vintage space with a few seats.",
                        address="1905 S 1st St",
                        city="Austin",
                        state="TX",
                        zip_code="78704",
                        latitude=30.24722791833769,
                        longitude=-97.75662594603243,
                        hours="10:00AM - 7:00PM",
                        price="$",
                        rating=4.3,
                        )
    restaurant4 = Restaurant(name="Capital City Bakery",
                        description="Local bakery preparing all-vegan treats including cupcakes, brownies & special-occasion cakes.",
                        address="2211 E Cesar Chavez St",
                        city="Austin",
                        state="TX",
                        zip_code="78702",
                        latitude=30.25627587968311,
                        longitude=-97.72009946137655,
                        hours="10:00AM - 6:00PM",
                        price="$",
                        rating=4.7,
                        )
    restaurant5 = Restaurant(name="Word of Mouth Bakery",
                        description="Word of Mouth Bakery is an Austin Bakery with a cafe menu that features breakfast sandwiches, pastries, muffins, cookies, cake by the slice, cupcakes, salads, sandwiches, and a catering to go menu. Let us do the cooking!",
                        address="917 W 12th St",
                        city="Austin",
                        state="TX",
                        zip_code="78703",
                        latitude=30.27756356269626,
                        longitude=-97.7507719,
                        hours="10:00AM - 4:00PM",
                        price="$$",
                        rating=4.7,
                        )
    restaurant6 = Restaurant(name="Hayleycakes and Cookies",
                        description="Petite stop-in for sweet treats, from inventive cupcakes to cookies, plus special-occasion cakes.",
                        address="1700 S Lamar Blvd",
                        city="Austin",
                        state="TX",
                        zip_code="78704",
                        latitude=30.251858996097788,
                        longitude=-97.76640427672069,
                        hours="7:00AM - 7:00PM",
                        price="$$",
                        rating=4.3,
                        )
    restaurant7 = Restaurant(name="Manolis Ice Cream Pastries & Cakes",
                        description="Housemade ice cream, popsicles & pastries are doled out at this busy food truck with outdoor tables",
                        address="603 W Live Oak St",
                        city="Austin",
                        state="TX",
                        zip_code="78704",
                        latitude=30.245213622657094,
                        longitude=-97.75797916931172,
                        hours="2:00PM - 11:00PM",
                        price="$",
                        rating=4.9,
                        )
    restaurant8 = Restaurant(name="Whole Foods",
                        description="We believe in the best, from our kitchens to your table. From our cult-favorite Berry Chantilly Cake to wholesome Seeduction Bread, our baked goods are made with unbleached, unbromated flour and cage-free or better eggs — and we don’t use hydrogenated fats or high-fructose corn syrup.",
                        address="525 N Lamar Blvd",
                        city="Austin",
                        state="TX",
                        zip_code="78703",
                        latitude=30.270744292416065,
                        longitude=-97.75320356423829,
                        hours="7:00AM - 9:00PM",
                        price="$$$",
                        rating=4.5,
                        )
    restaurant9 = Restaurant(name="Polkadots Cupcake Factory",
                        description="Cheery bakery crafting cupcakes in creative flavors, plus made-to-order cakes & hand-iced cookies.",
                        address="2826 Rio Grande St",
                        city="Austin",
                        state="TX",
                        zip_code="78705",
                        latitude=30.296683931389214,
                        longitude=-97.74425971534413,
                        hours="7:00AM - 9:00PM",
                        price="$",
                        rating=4.3,
                        )
    restaurant10 = Restaurant(name="Hey Cupcake!",
                        description="Cupcakes are the draw at this whimsical shop operating out of a parked trailer with outdoor seating.",
                        address="1511 S Congress Ave",
                        city="Austin",
                        state="TX",
                        zip_code="78704",
                        latitude=30.24935067782933,
                        longitude=-97.74942885396759,
                        hours="11:00AM - 9:00PM",
                        price="$",
                        rating=4.1,
                        )
    restaurant10 = Restaurant(name="Zucchini Kill Bakery",
                        description="Punk rock, female-led bakery serving vegan sweet & savory goods that are also soy & gluten-free.",
                        address="701 E 53rd S",
                        city="Austin",
                        state="TX",
                        zip_code="78751",
                        latitude=30.316314014490814,
                        longitude=-97.71660398465573,
                        hours="3:00PM - 8:00PM",
                        price="$$",
                        rating=4.8,
                        )
    restaurant11 = Restaurant(name="Tiny Pies",
                        description="Handmade by Scratch Daily Using Traditional Baking Methods and Natural Ingredients. Made fresh Daily!",
                        address="2032 S Lamar Blvd",
                        city="Austin",
                        state="TX",
                        zip_code="78704",
                        latitude=30.250212425241358,
                        longitude=-97.7687649,
                        hours="8:00AM - 8:00PM",
                        price="$$",
                        rating=4.5,
                        )
    restaurant12 = Restaurant(name="Quack's 43rd Street Bakery",
                        description="Quack’s line of bakery products grew out of a need to provide freshly baked goods for our customers. All the baked items sold here are made here from scratch. We use high quality, natural ingredients. We do not use frozen dough or mixes. Our bakery products contain no preservatives, high fructose corn syrups or additives. We provide service to many wholesale accounts that elect to serve their customers better quality baked goods in lieu of more commonly available, less expensive commercial products",
                        address="411 E 43rd St",
                        city="Austin",
                        state="TX",
                        zip_code="78751",
                        latitude=30.30534896953304,
                        longitude=-97.72654048465586,
                        hours="7:00AM - 9:00PM",
                        price="$",
                        rating=4.6,
                        )
    restaurant13 = Restaurant(name="The Cake and Spoon",
                        description="The Cake and Spoon is a wholesale and special order bakery concentrating on English, American, and European desserts and pastries.",
                        address="3008 Gonzales St",
                        city="Austin",
                        state="TX",
                        zip_code="78702",
                        latitude=30.250212425241358,
                        longitude=-97.7687649,
                        hours="8:00AM - 1:00PM",
                        price="$",
                        rating=4.6,
                        )
    restaurant14 = Restaurant(name="Upper Crust Bakery",
                        description="Well-known bakery with a cozy ambiance selling made-from-scratch pastries, bread & lunch fare.",
                        address="4508 Burnet Rd",
                        city="Austin",
                        state="TX",
                        zip_code="78756",
                        latitude=30.31652058929442,
                        longitude=-97.7415639,
                        hours="7:00AM - 3:00PM",
                        price="$",
                        rating=4.6,
                        )
    restaurant15 = Restaurant(name="Big Top",
                        description="Colorful, circus-themed sweets store featuring old-school confections & a soda fountain.",
                        address="1706 S Congress Ave",
                        city="Austin",
                        state="TX",
                        zip_code="78704",
                        latitude=30.247915810809495,
                        longitude=-97.7508139232793,
                        hours="11:00AM - 6:00PM",
                        price="$$",
                        rating=4.6,
                        )
    restaurant16 = Restaurant(name="Edis Chocolates",
                        description="Locally owned shop creating specialty chocolates, cakes, cookies, pastries & other confections.",
                        address="3808 Spicewood Springs Rd",
                        city="Austin",
                        state="TX",
                        zip_code="78759",
                        latitude=30.365796276705574,
                        longitude=-97.74900098465586,
                        hours="10:00AM - 5:00PM",
                        price="$$",
                        rating=4.8,
                        )
    restaurant17 = Restaurant(name="Delysia Chocolatier",
                        description="Our chocolates are handcrafted in Austin, Texas at our Culinary Center & Chocolate Boutique. Many include unique, local ingredients that are not available anywhere else. Relish in our passion for creating the finest quality and most unique chocolates available.",
                        address="2000 Windy Terrace",
                        city="Austin",
                        state="TX",
                        zip_code="78726",
                        latitude=30.461966325891236,
                        longitude=-97.83330320740897,
                        hours="12:00PM - 4:00PM",
                        price="$",
                        rating=4.7,
                        )
    restaurant17 = Restaurant(name="Yummi Joy",
                        description="Craft sodas, mix-and-match candy, & coffee, plus vegan ice cream in playful, cartoon-ish surrounds.",
                        address="409 W 2nd St",
                        city="Austin",
                        state="TX",
                        zip_code="78701",
                        latitude=30.265914420466785,
                        longitude=-97.74820453068827,
                        hours="11:00AM - 7:00PM",
                        price="$",
                        rating=4.6,
                        )
    restaurant17 = Restaurant(name="Madhu Chocolate",
                        description="Austin made small batch chocolate bars with an emphasis on unique Indian flavors.",
                        address="6814 Northeast Dr",
                        city="Austin",
                        state="TX",
                        zip_code="78723",
                        latitude=30.31936931469751,
                        longitude=-97.6804175,
                        hours="10:00AM - 2:00PM",
                        price="$",
                        rating=5.0,
                        )
    restaurant17 = Restaurant(name="Lammes Candies",
                        description="Austin's hometown candy store and home of the world-famous Texas Chewie® Pecan Praline. ",
                        address="2927 W Anderson Ln",
                        city="Austin",
                        state="TX",
                        zip_code="78757",
                        latitude=30.359302551025714,
                        longitude=-97.73851866983784,
                        hours="11:00AM - 5:30PM",
                        price="$",
                        rating=4.6,
                        )
    restaurant18 = Restaurant(name="IT'SUGAR",
                        description="IT'SUGAR is a trendy candy store specializing in innovative sweets, fun novelty gifts, and giant candy.",
                        address="11621 Rock Rose Ave",
                        city="Austin",
                        state="TX",
                        zip_code="78758",
                        latitude=30.40295485903219,
                        longitude=-97.72194801177815,
                        hours="12:00PM - 8:00PM",
                        price="$",
                        rating=4.2,
                        )
    restaurant19 = Restaurant(name="See's Candies",
                        description="Candies & chocolates are sold by the piece or box at this old-school chain, in business since 1921.",
                        address="10710 Research Blvd",
                        city="Austin",
                        state="TX",
                        zip_code="78759",
                        latitude=30.399847844610722,
                        longitude=-97.74799219259104,
                        hours="9:00AM - 7:30PM",
                        price="$",
                        rating=4.9,
                        )
    restaurant19 = Restaurant(name="Amy's Ice Creams",
                        description="Local chain serving inventive ice creams, milkshakes, ices & frozen yogurts with clever fixings.",
                        address="1301 S Congress Ave",
                        city="Austin",
                        state="TX",
                        zip_code="78704",
                        latitude=30.25218564971291,
                        longitude=-97.74876643862343,
                        hours="11:00AM - 11:00PM",
                        price="$",
                        rating=4.5,
                        )
    restaurant19 = Restaurant(name="Jeni's Splendid Ice Creams",
                        description="Chain scooping creative flavors of ice cream & frozen yogurt made from local ingredients.",
                        address="1208 S Congress Ave",
                        city="Austin",
                        state="TX",
                        zip_code="78704",
                        latitude=30.252835459387956,
                        longitude=-97.74918206137656,
                        hours="12:00PM - 10:00PM",
                        price="$$",
                        rating=4.6,
                        )
    restaurant20 = Restaurant(name="Dolce Neve Gelato",
                        description="Busy gelato shop whipping up various inventive flavors of ice cream in a pint-sized setting.",
                        address="1713 S 1st St",
                        city="Austin",
                        state="TX",
                        zip_code="78704",
                        latitude=30.248419896043455,
                        longitude=-97.75562374603243,
                        hours="12:00PM - 9:00PM",
                        price="$",
                        rating=4.7,
                        )
    restaurant20 = Restaurant(name="Lick Honest Ice Creams",
                        description="This hip ice creamery churns out offbeat flavors made from local, natural & sustainable ingredients.",
                        address="1100 S Lamar Blvd",
                        city="Austin",
                        state="TX",
                        zip_code="78704",
                        latitude=30.256305291156544,
                        longitude=-97.76265934603252,
                        hours="12:00PM - 10:00PM",
                        price="$$",
                        rating=4.6,
                        )
    restaurant21 = Restaurant(name="NadaMoo! Scoop Shop",
                        description="Festive counter-serve featuring homemade, dairy-free ice cream in traditional & seasonal flavors.",
                        address="1701 S Lamar Blvd",
                        city="Austin",
                        state="TX",
                        zip_code="78704",
                        latitude=30.25144088571262,
                        longitude=-97.76563339206633,
                        hours="2:00PM - 10:00PM",
                        price="$",
                        rating=4.6,
                        )
    restaurant22 = Restaurant(name="Sweet Ritual",
                        description="Colorful ice cream parlor serving gluten-free & vegan scoops in cups, cones, shakes & sundaes.",
                        address="4631 Airport Blvd",
                        city="Austin",
                        state="TX",
                        zip_code="78751",
                        latitude=30.30738290616657,
                        longitude=-97.71527361534415,
                        hours="12:00PM - 10:00PM",
                        price="$",
                        rating=4.7,
                        )
    restaurant23 = Restaurant(name="Voodoo Doughnut",
                        description="This counter-serve bakeshop serves creative donuts in colorful, quirky environs.",
                        address="212 E 6th St",
                        city="Austin",
                        state="TX",
                        zip_code="78701",
                        latitude=30.268674458003204,
                        longitude=-97.74110379206493,
                        hours="8:00AM - 12:00AM",
                        price="$",
                        rating=4.4,
                        )
    restaurant24 = Restaurant(name="Little Lucy's",
                        description="Colorful, late-night food truck making mini-donuts with creative flavors, toppings & dipping sauces.",
                        address="75 1/2 Rainey St",
                        city="Austin",
                        state="TX",
                        zip_code="78701",
                        latitude=30.25933696827229,
                        longitude=-97.73863651534413,
                        hours="5:00PM - 2:00AM",
                        price="$",
                        rating=4.4,
                        )
    restaurant25 = Restaurant(name="Gourdough's Big. Fat. Donuts.",
                        description="Gourdough's Big. Fat. Donuts. is housed in a vintage Airstream Trailer located on South Lamar and doles out the most delectable and crazy donut concoctions your mind and taste buds will allow.",
                        address="1503 S 1st St",
                        city="Austin",
                        state="TX",
                        zip_code="78704",
                        latitude=30.25056331384392,
                        longitude=-97.75472767114883,
                        hours="10:00AM - 12:00AM",
                        price="$",
                        rating=4.7,
                        )
    restaurant26 = Restaurant(name="Julie Myrtille Bakery",
                        description="Authentic French bakery and fine pastry in Austin founded by French pastry chef Julie Myrtille. Bake the world a better place.",
                        address="1023 Springdale Rd",
                        city="Austin",
                        state="TX",
                        zip_code="78721",
                        latitude=30.26853112905222,
                        longitude=-97.69396151534413,
                        hours="8:30AM - 2:00PM",
                        price="$$",
                        rating=4.7,
                        )
    restaurant27 = Restaurant(name="Milky Way Shakes",
                        description="Milky Way Shakes, a vegan milkshake trailer located in Austin, TX.",
                        address="2324 E Cesar Chavez St",
                        city="Austin",
                        state="TX",
                        zip_code="78702",
                        latitude=30.255831594732026,
                        longitude=-97.71826961534413,
                        hours="5:00PM - 10:00PM",
                        price="$",
                        rating=4.9,
                        )
    restaurant28 = Restaurant(name="Tiff's Treats",
                        description="Fresh-baked cookies for pre-order & pickup, or delivery, with a limited selection for walk-ins.",
                        address="1700 E Oltorf St",
                        city="Austin",
                        state="TX",
                        zip_code="78741",
                        latitude=30.234797164809567,
                        longitude=-97.73945371534413,
                        hours="9:00AM - 10:00PM",
                        price="$",
                        rating=4.0,
                        )
    restaurant29 = Restaurant(name="Tinys Milk & Cookies",
                        description="Milk & Cookies is a walk up coffee shop serving homemade ice cream, pastries, and of course, our cookie.",
                        address="1515 W 35th St",
                        city="Austin",
                        state="TX",
                        zip_code="78703",
                        latitude=30.307501456412382,
                        longitude=-97.7503918,
                        hours="7:00AM - 9:00PM",
                        price="$",
                        rating=4.7,
                        )
    restaurant30 = Restaurant(name="Insomnia Cookies",
                        description="Bakery chain known for late-night deliveries, with some locations selling ice cream.",
                        address="2323 San Antonio St",
                        city="Austin",
                        state="TX",
                        zip_code="78705",
                        latitude=30.288449263565315,
                        longitude=-97.7425249,
                        hours="11:00AM - 12:00AM",
                        price="$$",
                        rating=3.7,
                        )
    restaurant31 = Restaurant(name="Crumbl Cookies",
                        description="Each week, our menu rotates to give you 4 different specialty flavors to taste and enjoy. Don’t worry, our famous milk chocolate chip and chilled sugar cookie are always available.",
                        address="5207 Brodie Ln",
                        city="Austin",
                        state="TX",
                        zip_code="78745",
                        latitude=30.230633408810952,
                        longitude=-97.81658836137646,
                        hours="8:00AM - 10:00PM",
                        price="$$",
                        rating=4.8,
                        )
    restaurant32 = Restaurant(name="The Baked Bear",
                        description="Decadent build-your-own custom ice cream sandwiches with artisanal ice cream & house-made cookies.",
                        address="211 Walter Seaholm Dr",
                        city="Austin",
                        state="TX",
                        zip_code="78701",
                        latitude=30.268031906876974,
                        longitude=-97.75267155396759,
                        hours="12:00PM - 11:00PM",
                        price="$",
                        rating=4.7,
                        )


    db.session.add(restaurant1)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_restaurants():
    db.session.execute('TRUNCATE restaurants CASCADE;')
    db.session.commit()
