from app.models import db, Item, Restaurant


def seed_items():
# 1 - Nothing Bundt Cakes

    item1 = Item(restaurant_id=1,
                 name="Cele'bundt'ing You",
                 description="Bring out the 'bundt'ing! It's going to be a party. And what better way to celebrate than with the delicious, handcrafted goodness of Nothing Bundt Cakes.",
                 price=23.00,
                 image_src="https://order.nothingbundtcakes.com/FileSystem/sync-images/group-200000004063018796_1563156485.png",
                 )
    item2 = Item(restaurant_id=1,
                 name="Dozen Bundtinis",
                 description="Our bite-sized Bundt Cakes - 3x Red Velvet, 3x Chococlate Chocolate, Chip, 3x Lemon, and 3x White Chocolate Raspberry",
                 price=20.00,
                 image_src="https://order.nothingbundtcakes.com/FileSystem/sync-images/group-200000003536267570_1617119996.jpg",
                 )
    item3 = Item(restaurant_id=1,
                 name="Single Carrot Cake Bundtlet",
                 description="Miniature Bundt Cake",
                 price=4.25,
                 image_src="https://order.nothingbundtcakes.com/FileSystem/sync-images/group-200000003616264214_1559868168.jpg",
                 )
    item4 = Item(restaurant_id=1,
                 name="Happy 'Bundt'Day",
                 description="Is it time for cake yet? This birthday favorite comes topped with a party hat and two miniature gifts. Forget about opening presents, all eyes will be glued to this masterpiece.",
                 price=33.00,
                 image_src="https://order.nothingbundtcakes.com/FileSystem/sync-images/group-200000004173327928_1564014174.png",
                 )
    item5 = Item(restaurant_id=1,
                 name="Bundtlet Tower",
                 description="3 Bundtlet Tower comes beautifully gift wrapped in cellophane.",
                 price=12.75,
                 image_src="https://order.nothingbundtcakes.com/FileSystem/sync-images/group-200000003616264216_1559868861.jpg",
                 )

    # 2 - Paper Route
    item6 = Item(restaurant_id=2,
                 name="Chocolate Chip Cookies",
                 description="",
                 price=1.75,
                 image_src="https://lh3.googleusercontent.com/kueuE4x-Sy6FHXRIv5LyJJqYA_ggbJ3mSZ6mEk7jR8R-IE50Eyl4iu5qunMK3vKbrUIkCMC1ymK9gvs=w960-h960-n-o-v1",
                 )
    item7 = Item(restaurant_id=2,
                 name="Snickerdoodle Cupcakes",
                 description="Warm and cinnamon-y!",
                 price=2.75,
                 image_src="https://lh3.googleusercontent.com/PguyhWEystziUpkjmHhbFni1vaCT8f1UqfvDetWDpkJZ1XMcqmRL-z-mjz8QoeRruLLUQq0IGsi9Bek=w960-h960-n-o-v1",
                 )

    item8 = Item(restaurant_id=2,
                 name="Scone of the Day",
                 description="Hot and fresh - chefs pick!",
                 price=3.25,
                 image_src="https://s3-media0.fl.yelpcdn.com/bphoto/DVuAU5WXLuDJeekbeWhpdw/l.jpg",
                 )
    item9 = Item(restaurant_id=2,
                 name="Chocolate Ganache Cake",
                 description="Rich chocolate cake with layers of chocolate mousse, all covered in chocolate canache.",
                 price=35.00,
                 image_src="https://cdn.vox-cdn.com/thumbor/PjG9xUEMf6Y1YZSBs9THHSF5s1k=/0x0:1080x867/1200x800/filters:focal(391x310:563x482)/cdn.vox-cdn.com/uploads/chorus_image/image/54859303/13738310_1062461730508045_3580919524386069365_o.0.jpg",
                 )
    item10 = Item(restaurant_id=2,
                  name="Chocolate Peanut Butter Drizzle Cookies",
                  description="Just as the name describes...",
                  price=2.25,
                  image_src="https://cloudinary-assets.dostuffmedia.com/res/dostuff-media/image/upload/venue-402290/1495468885.jpg",
                  )
    item11 = Item(restaurant_id=2,
                  name="Peach Scone",
                  description="Fresh Fredericksburg peaches, of course",
                  price=3.25,
                  image_src="https://s3-media0.fl.yelpcdn.com/bphoto/DWnSjht6l-Q78bT44WbQbA/l.jpg",
                  )
    item12 = Item(restaurant_id=2,
                  name="Penut Butter Cupcakes",
                  description="Chocolate base with a creamy peanut butter frosting",
                  price=2.75,
                  image_src="https://austinot.com/wp-content/uploads/2017/11/Paper-Route-Bakery-1024x768.jpg",
                  )
    item13 = Item(restaurant_id=2,
                  name="Pecan Cinnmon Roll",
                  description="Gooey Cinnamon Roll with a siky glaze",
                  price=3.50,
                  image_src="https://i2.wp.com/www.eatthis.com/wp-content/uploads/2020/02/dv8-kitchen-kentucky.jpg?fit=1200%2C879&ssl=1",
                  )


    # 3 - Sugar mama's bakeshop
    item14 = Item(restaurant_id=3,
                  name="The James Cupcake",
                  description="Sugar Mama's fave cupcake of all time. Fluffy Valrhona chocolate cake topped with rich chocolate buttercream and festive sprinkles. It's a vibe.",
                  price=3.65,
                  image_src="https://www.sugarmamasbakeshop.com/uploads/1/3/1/2/131200774/s327881890392650205_p3_i3_w486.png",
                  )

    item15 = Item(restaurant_id=3,
                  name="Champion Carrot Cake Cupcake",
                  description="The winning recipe from our carrot cake contest! Carrot cupcake chock full of golden raisins, Texas pecans, pineapple and carrots + vanilla cream cheese frosting = a winning combination.",
                  price=3.65,
                  image_src="https://www.sugarmamasbakeshop.com/uploads/1/3/1/2/131200774/s327881890392650205_p2_i1_w640.jpeg",
                  )

    item16 = Item(restaurant_id=3,
                  name="The Angelina Cupcake",
                  description="Named after our beloved grandma Angelina, we are proud to offer this ravishing red velvet cupcake topped with irresistible vanilla cream cheese frosting.",
                  price=3.65,
                  image_src="https://www.sugarmamasbakeshop.com/uploads/1/3/1/2/131200774/s327881890392650205_p5_i2_w4032.jpeg?width=640",
                  )

    item17 = Item(restaurant_id=3,
                  name="Funfetti Cupcake",
                  description="One of our standing menu flavors is this vanilla pound cake is topped with vanilla frosting and a generous helping of rainbow sprankles and a dust of magical edible glitter.",
                  price=3.65,
                  image_src="https://www.sugarmamasbakeshop.com/uploads/1/3/1/2/131200774/s327881890392650205_p371_i2_w4032.jpeg?width=640",
                  )

    item18 = Item(restaurant_id=3,
                  name="Everything Cookie",
                  description="Oatmeal, peanut butter, m&ms, pretzels, potato chips, butterscotch chips, and gluten friendly to boot. This cookie is truly errythang.",
                  price=2.75,
                  image_src="https://www.sugarmamasbakeshop.com/uploads/1/3/1/2/131200774/s327881890392650205_p9_i3_w567.png",
                  )

    item19 = Item(restaurant_id=3,
                  name="Chocolate Chip Cookie",
                  description="Our OG cookie never fails to please. Buttery and delicious, studded with milk chocolate & semisweet chocolate chips.",
                  price=2.75,
                  image_src="https://www.sugarmamasbakeshop.com/uploads/1/3/1/2/131200774/s327881890392650205_p4_i3_w574.png",
                  )

    item20 = Item(restaurant_id=3,
                  name="Banana Cream Mini Pie",
                  description="Buttery pastry crust, banana cream filling, topped with whipped cream and salted caramel!",
                  price=5.00,
                  image_src="https://www.sugarmamasbakeshop.com/uploads/1/3/1/2/131200774/s327881890392650205_p18_i2_w640.jpeg",
                  )

    item21 = Item(restaurant_id=3,
                  name="Salted Caramel Vanilla Bean Cheesecake",
                  description="A mini cheesecake just for you, but big enough to share if you'd like. Topped with gooey salted caramel.",
                  price=7.50,
                  image_src="https://www.sugarmamasbakeshop.com/uploads/1/3/1/2/131200774/s327881890392650205_p372_i1_w4032.jpeg?width=640",
                  )

    item22 = Item(restaurant_id=3,
                  name="Cookies & Cream Cake",
                  description="One of our most popular cakes (that just happens to be vegan) - decadent chocolate cake with cookies and cream frosting, decked out with cookies and chocolate ganache!",
                  price=30.00,
                  image_src="https://www.sugarmamasbakeshop.com/uploads/1/3/1/2/131200774/s327881890392650205_p385_i1_w2592.jpeg?width=640",
                  )

    item23 = Item(restaurant_id=3,
                  name="Party Pants Cake",
                  description="This 6inch cake is absurdly fun. Choose a flavor and let our decorators go nuts with swirls, colors, flowers, macarons, candies and whatnot!",
                  price=60.00,
                  image_src="https://www.sugarmamasbakeshop.com/uploads/1/3/1/2/131200774/s327881890392650205_p174_i3_w576.jpeg",
                  )

    item24 = Item(restaurant_id=3,
                  name="Chocolate Raspberry Extravaganza Cake",
                  description="If you could bake romance, this is what it would look like. Chocolate cake, raspberry filling, chocolate cream cheese hybrid frosting, drizzled with a chocolate drip, raspberry buttercream poofs, and finished off with macarons and rose gold pretzels.",
                  price=30,
                  image_src="https://www.sugarmamasbakeshop.com/uploads/1/3/1/2/131200774/s327881890392650205_p391_i2_w3024.jpeg?width=640",
                  )


    # 4 - Capital City Bakery

    item25 = Item(restaurant_id=4,
                  name="Sweet Kolache",
                  description="vegan cream cheese filling and fruit",
                  price=5.50,
                  image_src="https://ccbcurbside.square.site/uploads/1/3/1/2/131259363/s223143107668783917_p220_i1_w3024.jpeg?width=2560",
                  )

    item26 = Item(restaurant_id=4,
                  name="Unicorn Loaded Brownie",
                  description="Brownie topped with strawberry frosting and sprinkles",
                  price=5.50,
                  image_src="https://ccbcurbside.square.site/uploads/1/3/1/2/131259363/s223143107668783917_p263_i1_w960.jpeg",
                  )
    item27 = Item(restaurant_id=4,
                  name="Frosted Sugar Cookie",
                  description="",
                  price=3.50,
                  image_src="https://ccbcurbside.square.site/uploads/1/3/1/2/131259363/s223143107668783917_p190_i1_w2560.jpeg",
                  )
    item28 = Item(restaurant_id=4,
                  name="Strawberry Blonde Cupcake",
                  description="Strawberry Cake, Strawberry Buttercream, Rainbow Sprinkles",
                  price=3.50,
                  image_src="https://ccbcurbside.square.site/uploads/1/3/1/2/131259363/s223143107668783917_p209_i1_w460.jpeg",
                  )
    item29 = Item(restaurant_id=4,
                  name="Fauxstess Cupcake",
                  description="Chocolate cake, cream filling, chocolate buttercream",
                  price=3.50,
                  image_src="https://ccbcurbside.square.site/uploads/1/3/1/2/131259363/s223143107668783917_p208_i1_w460.jpeg",
                  )
    item30 = Item(restaurant_id=4,
                  name="Peanut Butter Crunch Cupcake",
                  description="Chocolate cake, Peanut butter buttercream, chocolate ganache, chick-o-stick candy",
                  price=3.50,
                  image_src="https://ccbcurbside.square.site/uploads/1/3/1/2/131259363/s223143107668783917_p211_i1_w460.jpeg",
                  )
    item31 = Item(restaurant_id=4,
                  name="Carrot Pumpkin Cupcake",
                  description="Carrot Pumpkin cake with Cream Cheese Buttercream",
                  price=3.50,
                  image_src="https://ccbcurbside.square.site/uploads/1/3/1/2/131259363/s223143107668783917_p210_i1_w460.jpeg",
                  )

    item32 = Item(restaurant_id=4,
                  name="Gluten-Free Tuxedo Cupcake",
                  description="Gluten Free Chocolate Cake, Cream Cheese Buttercream",
                  price=3.50,
                  image_src="https://ccbcurbside.square.site/uploads/1/3/1/2/131259363/s223143107668783917_p212_i1_w460.jpeg",
                  )

    # 5 - word of mouth

    item33 = Item(restaurant_id=5,
                  name="Butterscotch Cookies",
                  description="A dozen of our fresh butterscotch cookies",
                  price=35.00,
                  image_src="https://static.spacecrafted.com/df77dc52b3dc43079db1ef1b4ac14d85/i/a0678aeb6566416ca6a93fcc09c8a1ae/1/2GTQbgiNxerRr5gcT6hkjr8dsnb6NBTxXMi2obS/Amanda-Ryan-W-5110.jpg",
                  )
    item34 = Item(restaurant_id=5,
                  name="Strawberry Tart",
                  description="A creamy tart topped with fresh strawberries",
                  price=20.00,
                  image_src="https://static.spacecrafted.com/df77dc52b3dc43079db1ef1b4ac14d85/i/a9971ccafe8a4c5e9a372b800d0d1784/1/2GTQbgiNxerRr5gcT6hkjr8dsnb6NBTxXMi2obS/DSC_0218-Edit.jpg",
                  )
    item35 = Item(restaurant_id=5,
                  name="Peach Tart",
                  description="A decadent cheesecake topped with fresh peaches",
                  price=35.00,
                  image_src="https://static.spacecrafted.com/df77dc52b3dc43079db1ef1b4ac14d85/i/b04343fa5f9a45e0ba1b34c1e1f0a6c1/1/2GTQbgiNxerRr5gcT6hkjr8dsnb6NBTxXMi2obS/peach_cheesecake2.jpg",
                  )

    item36 = Item(restaurant_id=5,
                  name="Rainbow Cake",
                  description="Our vanilla buttercream cake!",
                  price=45.00,
                  image_src="https://static.spacecrafted.com/df77dc52b3dc43079db1ef1b4ac14d85/i/adb7d15106c74738b7ec5c92a0b2556b/1/2GTQbgiNxerRr5gcT6hkjr8dsnb6NBTxXMi2obS/C82FCC87-30FB-4880-8AD9-352425092D47.JPG",
                  )
    item37 = Item(restaurant_id=5,
                  name="Funfetti Cookie Sandwiches",
                  description="A dozen funfetti Cookies with decadent buttercream frosting in between",
                  price=30.00,
                  image_src="https://static.spacecrafted.com/df77dc52b3dc43079db1ef1b4ac14d85/i/b9b4fb420d584570a0521b5b82d4c7ba/1/2GTQbgiNxerRr5gcT6hkjr8dsnb6NBTxXMi2obS/Screen%20Shot%202016-09-01%20at%2010.37.05%20AM.png",
                  )

    ## 6 - haleycakes
    item38 = Item(restaurant_id=6,
                  name="Brookie",
                  description="Chocolate chip cookie on the bottom, crushed oreos in the center, and gooey brownie on top! YUM!",
                  price=4.00,
                  image_src="https://d1ohrx9ht8bvf4.cloudfront.net/wp-content/uploads/2020/11/01204248/brookies-448x597.jpg",
                  )
    item39 = Item(restaurant_id=6,
                  name="Red Velvet Brownie",
                  description="Large red velvet brownies  with cream cheese frosting!",
                  price=4.00,
                  image_src="https://d1ohrx9ht8bvf4.cloudfront.net/wp-content/uploads/2020/10/31210111/red-velvet-brownie-448x597.jpg",
                  )

    item40 = Item(restaurant_id=6,
                  name="Caramelita",
                  description="A gooey chocolate chip cookie base with an oatmeal cookie top - drizzled in caramel and topped with a dollop of cream cheese frosting",
                  price=4.00,
                  image_src="https://d1ohrx9ht8bvf4.cloudfront.net/wp-content/uploads/2021/03/18065045/CARAMELITAS-448x448.jpg",
                  )
    item41 = Item(restaurant_id=6,
                  name="Cookies And Cream Cupcake",
                  description="Chocolate base with cookies n cream frosting",
                  price=4.50,
                  image_src="https://d1ohrx9ht8bvf4.cloudfront.net/wp-content/uploads/2018/10/15154720/thumbnail_IMG_9338-448x597.jpg",
                  )
    item42 = Item(restaurant_id=6,
                  name="Chocolate Chip Cookie Dough Cupcake",
                  description="Vanilla base, stuffed with cookie dough, and topped with cookie dough frosting",
                  price=4.50,
                  image_src="https://d1ohrx9ht8bvf4.cloudfront.net/wp-content/uploads/2018/10/15154737/thumbnail_IMG_9376-448x597.jpg",
                  )
    item43 = Item(restaurant_id=6,
                  name="S’mores Cake",
                  description="Almond wedding cake with marshamellow layeres, covered in a chocolate ganache with graham cracker crumbles",
                  price=55.00,
                  image_src="https://d1ohrx9ht8bvf4.cloudfront.net/wp-content/uploads/2019/08/30074925/smores-cake-448x796.jpg",
                  )

    item44 = Item(restaurant_id=6,
                  name="Reeses Pile Cake",
                  description="Peanut butter cake with buttercream frosting and a chocolate drizzle",
                  price=45.00,
                  image_src="https://d1ohrx9ht8bvf4.cloudfront.net/wp-content/uploads/2019/08/29171523/reeses-pile-cake-2-448x448.jpg",
                  )
    item45 = Item(restaurant_id=6,
                  name="Unicorn Cake",
                  description="Red Velvet vake with buttercream frosting",
                  price=60.00,
                  image_src="https://d1ohrx9ht8bvf4.cloudfront.net/wp-content/uploads/2018/01/26181107/Unicorn-Cake-1-.jpg",
                  )


    # 7 - manoli's ice cream pastries and cakes
    item46 = Item(restaurant_id=7,
                  name="Almond Cake",
                  description="Vanilla mousse layered between vanilla sponge cake covered in chantilly cream. Finished with toasted almonds and a mirror glaze",
                  price=35.00,
                  image_src="https://honestcooking.com/wp-content/uploads/2014/12/almond-cake-022.jpg",
                  )
    item47 = Item(restaurant_id=7,
                  name="Black Forest Cake",
                  description="Black Cherry mousse layered between chocolate sponge cake. Finished with milk chocolate shavings & powdered sugar",
                  price=40.00,
                  image_src="https://cdn.sallysbakingaddiction.com/wp-content/uploads/2018/11/black-forest-cake-chocolate-ganache.jpg",
                  )
    item48 = Item(restaurant_id=7,
                  name="Caramelino Cake",
                  description="Caramel mousse layered between chocolate sponge cake. Finished with milk chocolate shavings, chocolate ganache, and a mirror glaze.",
                  price=35.00,
                  image_src="https://homecookingadventure.com/images/recipes/apple_walnut_caramel_cake_main.jpg",
                  )
    item49 = Item(restaurant_id=7,
                  name="Fragola Cake",
                  description="Vanilla mousse layered between vanilla sponge cake stuffed with sweet fresh strawberry filling and finished with dark chocolate.",
                  price=35.00,
                  image_src="https://www.passionandcooking.com/wp-content/uploads/2013/05/torta-di-fragole-scaled.jpg",
                  )
    item50 = Item(restaurant_id=7,
                  name="Black Cherry Mousse Cheesecake",
                  description="Our cookie crumb bottom with a light mousse cheesecake. Topped with Black Cherry Filling. ",
                  price=40.00,
                  image_src="https://img.taste.com.au/GQBlOVyf/taste/2019/10/choc-cherry-mousse-cake-taste-155104-2.jpg",
                  )

    # 8 - Whole Foods

    item51 = Item(restaurant_id=8,
                  name="Chocolate Eruption Cake",
                  description="This rich, dreamy dessert has layers of moist chocolate cake and Belgian chocolate mousse, topped with chocolate shavings.",
                  price=29.99,
                  image_src="https://images.wfmstatic.com/image/upload/c_scale,q_80,w_250/spice/products/Bakery_ChocolateEruptionCake8in_1each_0000000104893.jpg",
                  )
    item52 = Item(restaurant_id=8,
                  name="Tiramisu Cake Slice",
                  description="Creamy and delicious",
                  price=3.50,
                  image_src="https://m.media-amazon.com/images/S/assets.wholefoodsmarket.com/PIE/product/5f5f75b5395ead6bc2190619_00245855000007-glamor-glamor5-2020-09-09t19-10-33-iphone-x-quality-90-1-21-1-user-5984ad42a967f880524de2c4-ilt9-670811._TTD_._SR1200,1200_._QL100_.jpg",
                  )

    item53 = Item(restaurant_id=8,
                  name="Fresh Fruit Tart",
                  description="",
                  price=22.99,
                  image_src="https://m.media-amazon.com/images/S/assets.wholefoodsmarket.com/PIE/product/5fd47f61ca5cc04b86e63488_00249839000007-glamor-glamor3-2020-12-09t00-00-14-iphone-x-quality-90-1-21-8-user-5984ad42a967f880524de2c4-2yfk-385494._TTD_._SR1200,1200_._QL100_.jpg",
                  )
    item54 = Item(restaurant_id=8,
                  name="Vegan Chocolate Chip Cookie",
                  description="Pure vegan goodness",
                  price=2.99,
                  image_src="https://m.media-amazon.com/images/S/assets.wholefoodsmarket.com/PIE/product/5ef2aa54093ba846a3b967a6_00247775000006-glamor-glamor3-2020-05-29t20-53-58-pixel-3a-quality-90-1-21-1-user-5984ad42a967f880524de2c4-qf7c-840006._TTD_._SR1200,1200_._QL100_.jpg",
                  )

    item55 = Item(restaurant_id=8,
                  name="Toasted Almond Cake Slice",
                  description="*contains nuts*",
                  price=3.99,
                  image_src="https://m.media-amazon.com/images/S/assets.wholefoodsmarket.com/PIE/product/5f90a666d3a191bbcb4e7925_5f88e2eed7778bad007b6f15-00247116000009-glamor-glamor6-2020-09-17t21-03-25-iphone-x-quality-90-1-21-1-user-5984ad42a967f880524de2c4-9lzr-712736._TTD_._SR1200,1200_._QL100_.jpg",
                  )
    item56 = Item(restaurant_id=8,
                  name="German Chocolate Cake Cupcake",
                  description="Perfectly sweet",
                  price=2.99,
                  image_src="https://m.media-amazon.com/images/S/assets.wholefoodsmarket.com/PIE/product/5ef6321823dacd457ccdd144_00244651000006-glamor-nutritionglamor-2020-05-29t23-15-29-pixel-3a-quality-90-1-21-1-user-5984ad42a967f880524de2c4-gg7t-137817._TTD_._SR1200,1200_._QL100_.jpg",
                  )

    item57 = Item(restaurant_id=8,
                  name="Strawberry Fields Cupcake",
                  description="Strawberry base with strawberry cream cheese frosting",
                  price=2.99,
                  image_src="https://m.media-amazon.com/images/S/assets.wholefoodsmarket.com/PIE/product/5fd42eefee6e2c4b618bdad9_00248161000006-glamor-glamor4-2020-12-10t20-07-03-iphone-x-quality-90-1-21-8-user-5984ad42a967f880524de2c4-p5ym-393072._TTD_._SR1200,1200_._QL100_.jpg",
                  )
    item58 = Item(restaurant_id=8,
                  name="Custard Fruit Cake",
                  description="Personal-sized fruit cake",
                  price=6.99,
                  image_src="https://m.media-amazon.com/images/S/assets.wholefoodsmarket.com/PIE/product/5fd46c0dee6e2c4b618bdde0_00256033000009-glamor-glamor3-2020-12-08t01-37-19-iphone-x-quality-90-1-21-8-user-5984ad42a967f880524de2c4-sryh-955898._TTD_._SR1200,1200_._QL100_.jpg",
                  )

    item59 = Item(restaurant_id=8,
                  name="Vegan Raspberry Cheesecake",
                  description="Decadent without the guilt!",
                  price=4.99,
                  image_src="https://m.media-amazon.com/images/S/assets.wholefoodsmarket.com/PIE/product/5fe39c20917c0b6ac3fefdac_00246904000009-glamor-glamor4-2020-10-22t00-55-03-iphone-x-quality-90-1-21-7-user-5984ad42a967f880524de2c4-11sf-119375._TTD_._SR1200,1200_._QL100_.jpg",
                  )

    ## 9 - polkadots
    item60 = Item(restaurant_id=9,
                  name="Blackbottom Cupcake",
                  description="Chocolate cake baked in with cream cheese and chocolate chip, cream cheese buttercream",
                  price=2.99,
                  image_src="https://i1.wp.com/polkadotscupcakefactory.com/wp-content/uploads/2020/02/IMG_0748.jpg?resize=300%2C300",
                  )

    item61 = Item(restaurant_id=9,
                  name="Red Velvet Cupcake",
                  description="Red velvet cake, cream cheese buttercream",
                  price=2.99,
                  image_src="https://i1.wp.com/polkadotscupcakefactory.com/wp-content/uploads/2020/02/IMG_0746.jpg?resize=300%2C300",
                  )

    item62 = Item(restaurant_id=9,
                  name="Triple Chocolate Cupcake",
                  description="Chocolate cake, ganache, chocolate Swiss buttercream",
                  price=2.99,
                  image_src="https://i1.wp.com/polkadotscupcakefactory.com/wp-content/uploads/2020/02/IMG_0744.jpg?resize=300%2C300",
                  )
    item63 = Item(restaurant_id=9,
                  name="Strawberry and Cream Cupcake",
                  description="Strawberry cake, strawberry cream cheese",
                  price=2.99,
                  image_src="https://i0.wp.com/polkadotscupcakefactory.com/wp-content/uploads/2020/02/IMG_0753.jpg?resize=300%2C300",
                  )

    item64 = Item(restaurant_id=9,
                  name="Cinnamon Sugar Cupcake",
                  description="Vanilla cake, brown sugar Swiss buttercream",
                  price=2.99,
                  image_src="https://i2.wp.com/polkadotscupcakefactory.com/wp-content/uploads/2020/02/IMG_0752.jpg?resize=300%2C300",
                  )
    item65 = Item(restaurant_id=9,
                  name="Lemon and Cream Cupcake",
                  description="Vanilla cake, lemon pastry cream, lemon cream cheese",
                  price=2.99,
                  image_src="https://i1.wp.com/polkadotscupcakefactory.com/wp-content/uploads/2020/02/IMG_0750.jpg?resize=300%2C300",
                  )
    item66 = Item(restaurant_id=9,
                  name="Cookies and Cream Cupcake",
                  description="Chocolate cake with cookies and cream buttercream",
                  price=2.99,
                  image_src="https://i2.wp.com/polkadotscupcakefactory.com/wp-content/uploads/2020/02/IMG_0757-1.jpg?resize=300%2C300",
                  )

    item67 = Item(restaurant_id=9,
                  name="Chocolate Chip Cookie Dough Cupcake",
                  description="Canilla cake, chocolate chip cookie, chocolate Swiss buttercream",
                  price=2.99,
                  image_src="https://i1.wp.com/polkadotscupcakefactory.com/wp-content/uploads/2020/02/IMG_0768.jpg?resize=300%2C300",
                  )
    item68 = Item(restaurant_id=9,
                  name="Tres Leches Cupcake",
                  description="Vanilla cake, tres leches mouse, brown sugar Swiss buttercream, Caramel",
                  price=2.99,
                  image_src="https://i0.wp.com/polkadotscupcakefactory.com/wp-content/uploads/2019/11/AE4CC981-7460-4263-8636-1212094E5AB5.jpg?resize=300%2C300",
                  )
    item69 = Item(restaurant_id=9,
                  name="Mix Berries Chardonnay Cupcake",
                  description="Vanilla cake, mix berries chardonnay compote, white chocolate Swiss buttercream",
                  price=2.99,
                  image_src="https://i2.wp.com/polkadotscupcakefactory.com/wp-content/uploads/2020/02/IMG_0767.jpg?resize=300%2C300",
                  )
    item70 = Item(restaurant_id=9,
                  name="Tiramisu Cupcake",
                  description="Vanilla cake, tiramisu mousse, coffee Swiss buttercream",
                  price=2.99,
                  image_src="https://i0.wp.com/polkadotscupcakefactory.com/wp-content/uploads/2020/02/IMG_0755-1.jpg?resize=300%2C300",
                  )

    # 10 - hey cupcake
    item71 = Item(restaurant_id=10,
                  name="The Classic Cupcake",
                  description="Vanilla Cake with Chocolate Buttercream Frosting",
                  price=3.50,
                  image_src="https://cdn.shopify.com/s/files/1/0100/0980/4900/products/CLASSIC_PRODUCT_590x.png?v=1580602872",
                  )
    item72 = Item(restaurant_id=10,
                  name="The Tuxedo Cupcake",
                  description="Chocolate Cake with Cream Cheese Frosting",
                  price=3.50,
                  image_src="https://cdn.shopify.com/s/files/1/0100/0980/4900/products/TUXEDO_PRODUCT_590x.png?v=1580602971",
                  )
    item73 = Item(restaurant_id=10,
                  name="Red Velvet Cupcake",
                  description="Red Velvet Cake with Cream Cheese Frosting",
                  price=3.50,
                  image_src="https://cdn.shopify.com/s/files/1/0100/0980/4900/products/RED_VELVET_PRODUCT_590x.png?v=1580602790",
                  )
    item74 = Item(restaurant_id=10,
                  name="Sweetberry Cupcake",
                  description="Strawberry Cake with Strawberrry Cream Cheese Frosting",
                  price=3.50,
                  image_src="https://cdn.shopify.com/s/files/1/0100/0980/4900/products/SWEETBERRY_PRODUCT_590x.png?v=1580603046",
                  )
    item75 = Item(restaurant_id=10,
                  name="Double Dose Cupcake",
                  description="Chocolate Cake with Chocolate Buttercream Frosting",
                  price=3.50,
                  image_src="https://cdn.shopify.com/s/files/1/0100/0980/4900/products/DOUBLE_DOSE_PRODUCT_590x.png?v=1580602579",
                  )

    # 11 - zucchini kill
    item76 = Item(restaurant_id=11,
                  name="Coffee Cake",
                  description="A mini-loaf of Cinnamon Coffee Cake!",
                  price=3.50,
                  image_src="https://www.zucchinikill.com/uploads/1/3/0/8/130884288/s582860152980847625_p760_i2_w3024.jpeg?width=640",
                  )
    item77 = Item(restaurant_id=11,
                  name="Churro Bite Cupcake",
                  description="Cinnamon Spice Cake with Vanilla Cream and Mini Churro Bite on top!",
                  price=5.00,
                  image_src="https://www.zucchinikill.com/uploads/1/3/0/8/130884288/s582860152980847625_p714_i2_w3024.jpeg?width=640",
                  )
    item78 = Item(restaurant_id=11,
                  name="Laven-Derketa Cupcake",
                  description="Vanilla Cake with sweet Lavender Buttercream and dried Lavender Bud Sprinkles! Named after one of our favorite all grrrl doom bands, Derketa!!!!",
                  price=3.00,
                  image_src="https://www.zucchinikill.com/uploads/1/3/0/8/130884288/s582860152980847625_p658_i2_w1468.jpeg?width=640",
                  )
    item79 = Item(restaurant_id=11,
                  name="Peanut Butter Cup-Cake",
                  description="Organic Peanut Cake, filled with crunchy Peanut Buttercream, frosted with rich Chocolate, topped with salted peanuts.",
                  price=4.00,
                  image_src="https://www.zucchinikill.com/uploads/1/3/0/8/130884288/s582860152980847625_p602_i2_w3024.jpeg?width=640",
                  )
    item80 = Item(restaurant_id=11,
                  name="S'Mores Cupcake",
                  description="Graham Spiced Cake with Marshmallow Buttercream, Chocolate Drizzle, and housemade Oat Graham Cracker Crumbs!",
                  price=4.00,
                  image_src="https://www.zucchinikill.com/uploads/1/3/0/8/130884288/s582860152980847625_p618_i3_w3024.jpeg?width=640",
                  )
    item81 = Item(restaurant_id=11,
                  name="BlackPink Velvet Cupcake",
                  description="Like Red Velvet, but not!! Instead of artificial food coloring, we use Activated Coconut Ash Charcoal in the cake, and Beet Juice in the Cream Cheeze Buttercream!",
                  price=4.00,
                  image_src="https://www.zucchinikill.com/uploads/1/3/0/8/130884288/s582860152980847625_p619_i3_w3024.jpeg?width=640",
                  )
    item82 = Item(restaurant_id=11,
                  name="Oatbreaker Cookie",
                  description="Our signature Oatmeal Cookie made with Hempseeds, Gluten Free Oats, and Chocolate Chips!",
                  price=3.00,
                  image_src="https://www.zucchinikill.com/uploads/1/3/0/8/130884288/s582860152980847625_p608_i1_w640.jpeg",
                  )
    item83 = Item(restaurant_id=11,
                  name="Rosemary Chocolate Chip Cookie",
                  description="Chocolate Chip Cookie infused with fresh, chopped Rosemary!",
                  price=3.00,
                  image_src="https://www.zucchinikill.com/uploads/1/3/0/8/130884288/s582860152980847625_p607_i1_w640.jpeg",
                  )
    item84 = Item(restaurant_id=11,
                  name="Brownie Cream Pie",
                  description="Cream Pie made with our Double Chocolate Chip Cookies and Vanilla Cream!",
                  price=4.00,
                  image_src="https://www.zucchinikill.com/uploads/1/3/0/8/130884288/s582860152980847625_p612_i2_w2985.jpeg?width=640",
                  )
    item85 = Item(restaurant_id=11,
                  name="Oatmeal Cream Pie",
                  description="Fluffy Oatmeal Cookies sandwiched with Vanilla Cream!!!",
                  price=4.00,
                  image_src="https://www.zucchinikill.com/uploads/1/3/0/8/130884288/s582860152980847625_p789_i1_w2939.jpeg?width=640",
                  )
    item86 = Item(restaurant_id=11,
                  name="Vanilla Cream Coffins",
                  description="2 pack of our classic Cream Coffins (Vanilla Cream filled Spongecake)",
                  price=6.00,
                  image_src="https://www.zucchinikill.com/uploads/1/3/0/8/130884288/s582860152980847625_p606_i2_w640.jpeg",
                  )
    item87 = Item(restaurant_id=11,
                  name="Pink Coconut Cupcake",
                  description="Vanilla Cake stuffed and topped with Vanilla Cream, rolled in naturally colored pink Coconut Shred Sprinkles!",
                  price=4.00,
                  image_src="https://www.zucchinikill.com/uploads/1/3/0/8/130884288/s582860152980847625_p686_i4_w3024.jpeg?width=640",
                  )
    item88 = Item(restaurant_id=11,
                  name="Chocolate Donut 2-Pack",
                  description="Two of our classic Chocolate Cake Donuts topped with Chocolate Glaze!",
                  price=5.00,
                  image_src="https://www.zucchinikill.com/uploads/1/3/0/8/130884288/s582860152980847625_p684_i1_w640.jpeg",
                  )
    item89 = Item(restaurant_id=11,
                  name="Cinnamon Roll Donut 2-Pack",
                  description="2 Pack of Donuts made Cinnamon Roll Style with Vanilla Glaze!",
                  price=8.00,
                  image_src="https://www.zucchinikill.com/uploads/1/3/0/8/130884288/s582860152980847625_p699_i1_w640.jpeg",
                  )
    item90 = Item(restaurant_id=11,
                  name="Graveyard Dirt",
                  description="Vanilla Cream, Oat Graham Cracker Crumbs, Chocolate Pudding, and Brutal Brownie chunks!!! These are really good served cold, pop it in the fridge!!!",
                  price=5.00,
                  image_src="https://www.zucchinikill.com/uploads/1/3/0/8/130884288/s582860152980847625_p705_i2_w3024.jpeg?width=640",
                  )

    # 12 - tiny pies
    item91 = Item(restaurant_id=12,
                  name="Vegan Strawberry Pie",
                  description="Fresh strawberry filling with a crumb topping in our vegan crust.",
                  price=5.45,
                  image_src="https://images.squarespace-cdn.com/content/v1/540cd7e4e4b0b83340ad9dd8/1490807683746-0X4R7WXUBW5LCVNBQQ4N/ke17ZwdGBToddI8pDm48kAf-OpKpNsh_OjjU8JOdDKBZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpzAFzFJoCInLPKyj9AG8yKe7-Q2aFvP177fkO9TY_-rz5WoqqTEZpmj4yDEOdwKV68/cherry+tiny+pie.jpg",
                  )
    item92 = Item(restaurant_id=12,
                  name="Cherry Lattice Pie",
                  description="Tart, robust cherry flavor. Perfect for those who don't like super sweet flavors.",
                  price=35.00,
                  image_src="https://storcpdkenticomedia.blob.core.windows.net/media/recipemanagementsystem/media/recipe-media-files/recipes/retail/x17/21069-cherry-apple-pie-600x600.jpg?ext=.jpg",
                  )
    item93 = Item(restaurant_id=12,
                  name="Key Lime Pie",
                  description="Tart Key Lime filling topped with toasted marshmallow meringue.",
                  price=5.45,
                  image_src="https://media-cdn.tripadvisor.com/media/photo-s/09/3c/57/c0/photo0jpg.jpg",
                  )
    item94 = Item(restaurant_id=12,
                  name="Sweet Texas Pecan Pie",
                  description="Named top 10 best pecan pie in Texas. Made with local pecans. Not as sweet as traditional pecan pies!",
                  price=30.00,
                  image_src="https://cdn.vox-cdn.com/thumbor/6B0-6Of0xk-h5C20xSpDlecPy4w=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/21996922/websitepecanNST21_700x.jpg",
                  )
    item95 = Item(restaurant_id=12,
                  name="Texas Two Step Pie",
                  description="Fan Favorite! Sweet Texas Pecan Pie layered with Chocolate Brownie. Has a bit of a kick to it!",
                  price=30.00,
                  image_src="https://items-static.postmates.com/uploads/media/ee741926-3475-4e45-be4b-7bf8755c80b3/original.jpg?v=63749970001",
                  )
    item96 = Item(restaurant_id=12,
                  name="Banana Cream Pie",
                  description="Vanilla pastry cream with fresh bananas mixed in. A layer of chocolate ganache in the bottom of the crust and drizzled on top of the whipped cream.",
                  price=4.95,
                  image_src="https://b.zmtcdn.com/data/reviews_photos/798/7306aa422cf10d39c4757615085e7798_1544145755.jpg",
                  )
    item97 = Item(restaurant_id=12,
                  name="Chocolate Cream Pie",
                  description="Chocolate pastry cream filling topped with fresh whipped cream and dark chocolate shavings.",
                  price=4.95,
                  image_src="https://raster-static.postmates.com/?url=https%3A%2F%2Fitems-static.postmates.com%2Fuploads%2Fmedia%2F8fd39c7d-b618-44b2-99f6-f203a7fc2ec8%2Foriginal.jpg%3Fv%3D63749969765&quality=85&w=320&h=0&mode=auto&format=&v=4",
                  )
    item98 = Item(restaurant_id=12,
                  name="Dutchy's Apple Pie",
                  description="Made with granny smith apples; has a traditional apple pie flavor with a hint of cinnamon. Not too sweet!",
                  price=4.95,
                  image_src="https://cdn.vox-cdn.com/thumbor/_1cXtr-mtqRcJEjqJl5Bktb7VqA=/0x0:2016x1504/1200x800/filters:focal(769x590:1091x912)/cdn.vox-cdn.com/uploads/chorus_image/image/66399075/75576438_2480255652043332_1609948046861271040_o.0.jpg",
                  )
    item99 = Item(restaurant_id=12,
                  name="Cherry Pie",
                  description="Tart, robust cherry flavor. Perfect for those who don't like super sweet flavors.",
                  price=4.95,
                  image_src="https://items-static.postmates.com/uploads/media/e136f66c-3198-4619-8bbe-5ec41059ad0f/original.jpg?v=63749969821",
                  )

    # 14 - the cake and spoon
    item100 = Item(restaurant_id=14,
                   name="Pecan Pie",
                   description="Our best-selling pie, made with browned butter and new crop pecans from Millican Pecan in San Saba Texas.",
                   price=40.00,
                   image_src="https://images.squarespace-cdn.com/content/v1/57a650aabebafb38e0d81a44/1605627777672-JAL8COJV78EN7DE7ASSG/ke17ZwdGBToddI8pDm48kD3QnjX76PDVQPrQk5uTQ9sUqsxRUqqbr1mOJYKfIPR7LoDQ9mXPOjoJoqy81S2I8N_N4V1vUb5AoIIIbLZhVYxCRW4BPu10St3TBAUQYVKccMncbqZFIex_fe1Pf1OGDPLanTCfx74eztBr6QjBDlZWqfPZYNyd3PqgRv3blzpc/pecan-pie-holiday.png?format=750w",
                   )
    item101 = Item(restaurant_id=14,
                   name="Cherry Pie",
                   description="Organic cherries with a hint of lemon and topped with a pastry lattice.",
                   price=40.00,
                   image_src="https://images.squarespace-cdn.com/content/v1/57a650aabebafb38e0d81a44/1604952922299-24EYYUEPKUX7FV7DUINR/ke17ZwdGBToddI8pDm48kG87Sfbgg29A4BYEDq3OXvgUqsxRUqqbr1mOJYKfIPR7LoDQ9mXPOjoJoqy81S2I8N_N4V1vUb5AoIIIbLZhVYxCRW4BPu10St3TBAUQYVKcf4OxbJOyh_wHUnyc4kQLQ6SBshRGOku7c30Y_IRDNPta8R2IY5BHMaEj1zOWoDTZ/Cherry+Pie.jpg?format=750w",
                   )
    item102 = Item(restaurant_id=14,
                   name="Banana Pie",
                   description="This pie features a crispy cookie crust layered with fresh bananas and bourbon pastry cream. A side of fresh whipped cream accompanies this pie",
                   price=40.00,
                   image_src="https://images.squarespace-cdn.com/content/v1/57a650aabebafb38e0d81a44/1605641591156-JBNUQ9XJ52Q2UHNZD95W/ke17ZwdGBToddI8pDm48kG87Sfbgg29A4BYEDq3OXvgUqsxRUqqbr1mOJYKfIPR7LoDQ9mXPOjoJoqy81S2I8N_N4V1vUb5AoIIIbLZhVYxCRW4BPu10St3TBAUQYVKcf4OxbJOyh_wHUnyc4kQLQ6SBshRGOku7c30Y_IRDNPta8R2IY5BHMaEj1zOWoDTZ/IMG_7615.jpg?format=750w",
                   )
    item103 = Item(restaurant_id=14,
                   name="Dark Chocolate Espresso Shortbread",
                   description="Classic shortbread with Valrhona chocolate and Italian espresso powder.",
                   price=4.50,
                   image_src="https://images.squarespace-cdn.com/content/v1/57a650aabebafb38e0d81a44/1602097970052-KYLLR79VA995T1CRDL1P/ke17ZwdGBToddI8pDm48kGimpnGS74lOCXEVScmdKfQUqsxRUqqbr1mOJYKfIPR7LoDQ9mXPOjoJoqy81S2I8GRo6ASst2s6pLvNAu_PZdJblJnDTNjTASBy3WMly_ic7RFeFNz6WHDDme815vyzW9AukLhYm2lpbtr2HKmuE68/Dark+Chocolate+Espresso+Shortbread.jpg?format=750w",
                   )
    item104 = Item(restaurant_id=14,
                   name="Lemon Lavender Shortbread",
                   description="Shortbread with the addition of fresh lemon zest and Hill Country lavender",
                   price=4.50,
                   image_src="https://images.squarespace-cdn.com/content/v1/57a650aabebafb38e0d81a44/1602097973801-5FQRJALLPAJLFBWK4AE7/ke17ZwdGBToddI8pDm48kGimpnGS74lOCXEVScmdKfQUqsxRUqqbr1mOJYKfIPR7LoDQ9mXPOjoJoqy81S2I8GRo6ASst2s6pLvNAu_PZdJblJnDTNjTASBy3WMly_ic7RFeFNz6WHDDme815vyzW9AukLhYm2lpbtr2HKmuE68/Lemon+Lavender+Shortbread.jpg?format=750w",
                   )
    item105 = Item(restaurant_id=14,
                   name="Blackberry Almond Bar",
                   description="Layered shortbread bar made with almond flour and French Blackberry Preserves.",
                   price=4.50,
                   image_src="https://images.squarespace-cdn.com/content/v1/57a650aabebafb38e0d81a44/1602097965730-CCZOUQ01RAQV1CJFEPAK/ke17ZwdGBToddI8pDm48kGimpnGS74lOCXEVScmdKfQUqsxRUqqbr1mOJYKfIPR7LoDQ9mXPOjoJoqy81S2I8GRo6ASst2s6pLvNAu_PZdJblJnDTNjTASBy3WMly_ic7RFeFNz6WHDDme815vyzW9AukLhYm2lpbtr2HKmuE68/Blackberry+Almond+Bar+.jpg?format=750w",
                   )
    item106 = Item(restaurant_id=14,
                   name="Ricotta Lime Cookies",
                   description="Five tea-sized cookies made with fresh lime, lime zest and covered in a fresh lime glaze.",
                   price=4.50,
                   image_src="https://images.squarespace-cdn.com/content/v1/57a650aabebafb38e0d81a44/1602098217825-ARQHU1ZHDPQNUG844980/ke17ZwdGBToddI8pDm48kG87Sfbgg29A4BYEDq3OXvgUqsxRUqqbr1mOJYKfIPR7LoDQ9mXPOjoJoqy81S2I8N_N4V1vUb5AoIIIbLZhVYxCRW4BPu10St3TBAUQYVKcf4OxbJOyh_wHUnyc4kQLQ6SBshRGOku7c30Y_IRDNPta8R2IY5BHMaEj1zOWoDTZ/Ricotta+Lime+Cookies+2.jpg?format=750w",
                   )
    item107 = Item(restaurant_id=14,
                   name="Buttermilk Small Pie",
                   description="A Southern favorite. Vanilla buttermilk custard pie.",
                   price=7.00,
                   image_src="https://images.squarespace-cdn.com/content/v1/57a650aabebafb38e0d81a44/1608404443863-XEHEPYCPUYQEHE0C2OVY/ke17ZwdGBToddI8pDm48kG87Sfbgg29A4BYEDq3OXvgUqsxRUqqbr1mOJYKfIPR7LoDQ9mXPOjoJoqy81S2I8N_N4V1vUb5AoIIIbLZhVYxCRW4BPu10St3TBAUQYVKcf4OxbJOyh_wHUnyc4kQLQ6SBshRGOku7c30Y_IRDNPta8R2IY5BHMaEj1zOWoDTZ/IMG_8841.jpg?format=750w",
                   )
    item108 = Item(restaurant_id=14,
                   name="Chocolate Chip Cookies",
                   description="Three cookies made with both white and brown sugar, Texas pecans, and dark chocolate chips.",
                   price=4.50,
                   image_src="https://images.squarespace-cdn.com/content/v1/57a650aabebafb38e0d81a44/1602098214437-X51QDWJZRIGCYDLW4P70/ke17ZwdGBToddI8pDm48kGimpnGS74lOCXEVScmdKfQUqsxRUqqbr1mOJYKfIPR7LoDQ9mXPOjoJoqy81S2I8GRo6ASst2s6pLvNAu_PZdJblJnDTNjTASBy3WMly_ic7RFeFNz6WHDDme815vyzW9AukLhYm2lpbtr2HKmuE68/Chocolate+Chip+Cookie.jpg?format=750w",
                   )
    item109 = Item(restaurant_id=14,
                   name="Mini German Chocolate Cake",
                   description="Classic light German Chocolate cake layered with a gooey pecan coconut frosting.",
                   price=7.50,
                   image_src="https://images.squarespace-cdn.com/content/v1/57a650aabebafb38e0d81a44/1608404118229-00VQLMRGM0IDBFRX3DHR/ke17ZwdGBToddI8pDm48kG87Sfbgg29A4BYEDq3OXvgUqsxRUqqbr1mOJYKfIPR7LoDQ9mXPOjoJoqy81S2I8N_N4V1vUb5AoIIIbLZhVYxCRW4BPu10St3TBAUQYVKcf4OxbJOyh_wHUnyc4kQLQ6SBshRGOku7c30Y_IRDNPta8R2IY5BHMaEj1zOWoDTZ/IMG_8846.jpg?format=750w",
                   )
    item110 = Item(restaurant_id=14,
                   name="Mini Eggnog Cake",
                   description="Butter Cake made with Eggnog, soaked in rum and layered with a rum French buttercream",
                   price=7.50,
                   image_src="https://images.squarespace-cdn.com/content/v1/57a650aabebafb38e0d81a44/1608404118260-JV7OIXV9BONSK1HE1BW7/ke17ZwdGBToddI8pDm48kG87Sfbgg29A4BYEDq3OXvgUqsxRUqqbr1mOJYKfIPR7LoDQ9mXPOjoJoqy81S2I8N_N4V1vUb5AoIIIbLZhVYxCRW4BPu10St3TBAUQYVKcf4OxbJOyh_wHUnyc4kQLQ6SBshRGOku7c30Y_IRDNPta8R2IY5BHMaEj1zOWoDTZ/IMG_8862.jpg?format=750w",
                   )

    # 15 - upper crust
    item111 = Item(restaurant_id=15,
                   name="Strawberry Rhubarb Pie",
                   description="The tartness of rhubarb paired with sweet strawberries make this a delectable summer pie. Doesn't hurt to add some ice cream. ",
                   price=25.00,
                   image_src="https://www.uppercrustbakery.com/wp-content/themes/uppercrust/images/cakes/full/strawberry_rhubarb_pie_lg.jpg",
                   )
    item112 = Item(restaurant_id=15,
                   name="Blueberry Pie",
                   description="Another summer classic. Fresh blueberries thickened with tapioca combined with our buttery, flaky crust.",
                   price=25.00,
                   image_src="https://www.uppercrustbakery.com/wp-content/themes/uppercrust/images/cakes/full/blueberry_pie_lg.jpg",
                   )
    item113 = Item(restaurant_id=15,
                   name="Chocolate Croissant",
                   description="Filled with callebaut chocolate",
                   price=2.50,
                   image_src="https://zagat-photos.imgix.net/ChIJ8dfGAGLKRIYROUESDBsSgoE/fcf4df44f22284483ae56e4c9d1ede46.jpg",
                   )
    item114 = Item(restaurant_id=15,
                   name="Strawberry Cream Cheese Croissant",
                   description="Filled with strawberry preserves & cream cheese",
                   price=2.25,
                   image_src="https://media-cdn.tripadvisor.com/media/photo-p/17/e1/60/9c/photo0jpg.jpg",
                   )
    item115 = Item(restaurant_id=15,
                   name="Black Gold Cookie",
                   description="Imagine the offspring of a brownie and a cookie. Crumbly & soft with Callebaut chocolate, toasted pecans, walnuts and a hint of espresso. It's a meal!",
                   price=2.35,
                   image_src="https://zagat-photos.imgix.net/ChIJ8dfGAGLKRIYROUESDBsSgoE/f5df21368839a9ae5059df14d691aa28.jpg",
                   )
    item116 = Item(restaurant_id=15,
                   name="Raspberry Hearts Cookie",
                   description="Delicious sugar cookies layered with rasberry preserves and dusted with powdered sugar",
                   price=2.10,
                   image_src="https://bakingamoment.com/wp-content/uploads/2016/01/7700featured.jpg",
                   )
    item117 = Item(restaurant_id=15,
                   name="PBOCC Cookie",
                   description="Peanut Butter, Oatmeal & Chocolate Chips",
                   price=1.75,
                   image_src="https://abountifulkitchen.com/wp-content/uploads/2017/01/Levain-Bakery-Chocolate-Chip-Cookie-Recipe_A-Bountiful-Kitchen-1.jpg",
                   )
    item118 = Item(restaurant_id=15,
                   name="Hot Cross Buns",
                   description="Aromatic spiced sweet buns marked with an iced cross on top.",
                   price=2.50,
                   image_src="http://static1.squarespace.com/static/540cd7e4e4b0b83340ad9dd8/59d9505837c581e591c6e62e/58dbeac720099ebcba5f1aa2/1582043090675/upper+crust.jpg?format=1500w",
                   )

    # 17 -  edi's chocolates
    item119 = Item(restaurant_id=17,
                   name="Half Dozen Milk Chocolate Covered Salted Caramels",
                   description="Six Milk Chocolate Chocolate Dipped Salted Caramel",
                   price=12.75,
                   image_src="https://www.inspiredtaste.net/wp-content/uploads/2012/12/Chocolate-Covered-Caramels-Recipe-1-1200.jpg",
                   )
    item120 = Item(restaurant_id=17,
                   name="Half Dozen Dark Chocolate Covered Salted Caramels",
                   description="Six Dark Chocolate Chocolate Dipped Salted Caramel",
                   price=12.75,
                   image_src="https://s3.amazonaws.com/cdn.ruthhuntcandy.com/images/popup/woodford-sea-salt-caramel3.jpg",
                   )
    item121 = Item(restaurant_id=17,
                   name="Half Dozen Truffle Assortment",
                   description="Assortment of the week six chocolate truffles",
                   price=16.75,
                   image_src="https://static.wixstatic.com/media/60e647_c9595232184c41a5bf8b9f9f549ec95e~mv2.jpg/v1/fill/w_363,h_260,fp_0.47_0.56,q_80,usm_0.66_1.00_0.01/60e647_c9595232184c41a5bf8b9f9f549ec95e~mv2.webp",
                   )
    item122 = Item(restaurant_id=17,
                   name="Fresh Croissant",
                   description="Buttery Croissant",
                   price=2.75,
                   image_src="https://static.wixstatic.com/media/60e647_a1a1843ba28a4ccf94b9d665797d0442~mv2.jpg/v1/fill/w_363,h_260,fp_0.50_0.50,q_80,usm_0.66_1.00_0.01/60e647_a1a1843ba28a4ccf94b9d665797d0442~mv2.webp",
                   )
    item123 = Item(restaurant_id=17,
                   name="Lemon Bar",
                   description="Tart and Rich",
                   price=3.75,
                   image_src="https://static.wixstatic.com/media/60e647_608db79b7a5c4c3588cb1282b8efff93~mv2_d_4608_3456_s_4_2.jpg/v1/fill/w_363,h_260,fp_0.50_0.50,q_80,usm_0.66_1.00_0.01/60e647_608db79b7a5c4c3588cb1282b8efff93~mv2_d_4608_3456_s_4_2.webp",
                   )
    item124 = Item(restaurant_id=17,
                   name="Maple Pecan & Walnut Bar",
                   description="Like Pecan Pie but Better",
                   price=3.75,
                   image_src="https://static.wixstatic.com/media/60e647_5a4b3e9ed8be44138281d0c4b324f8cf~mv2.jpg/v1/fill/w_363,h_260,fp_0.50_0.50,q_80,usm_0.66_1.00_0.01/60e647_5a4b3e9ed8be44138281d0c4b324f8cf~mv2.webp",
                   )
    item125 = Item(restaurant_id=17,
                   name="Lime Margarita Bar",
                   description="Margarita in a Bar",
                   price=3.75,
                   image_src="https://static.wixstatic.com/media/60e647_6cb7f3283c1e43258f309bda81c99327~mv2.jpg/v1/fill/w_363,h_260,fp_0.50_0.50,q_80,usm_0.66_1.00_0.01/60e647_6cb7f3283c1e43258f309bda81c99327~mv2.webp",
                   )
    item126 = Item(restaurant_id=17,
                   name="Biscotti",
                   description="Tailor-made for dunking into coffee",
                   price=2.75,
                   image_src="https://static.wixstatic.com/media/60e647_b23c52148ebe4d67b1611bba86f27b88~mv2.jpg/v1/fill/w_363,h_260,fp_0.50_0.50,q_80,usm_0.66_1.00_0.01/60e647_b23c52148ebe4d67b1611bba86f27b88~mv2.webp",
                   )

    # 20 - madhu chocolatier
    item127 = Item(restaurant_id=20,
                   name="Idukki Black Pepper Chocolate",
                   description="A dark chocolate made with Idukki Hills beans from Kerala, India. This amazing bar is flavored with Diaspora Co. single origin black pepper from Thirunelly, Kerala, which adds a unique, almost savory flavor that makes this bar truly special.",
                   price=10.00,
                   image_src="https://static.wixstatic.com/media/f358f9_79963e60eb0241238dbdb2c31fe566c4~mv2.jpg/v1/fill/w_500,h_750,al_c,q_85,usm_0.66_1.00_0.01/f358f9_79963e60eb0241238dbdb2c31fe566c4~mv2.webp",
                   )
    item128 = Item(restaurant_id=20,
                   name="Saffron Milk Chocolate",
                   description="Delicate saffron flavor perfectly combined with our milk chocolate.",
                   price=9.00,
                   image_src="https://static.wixstatic.com/media/f358f9_2e9aae24b1b54b28931d4c82bba3e700~mv2.jpg/v1/fill/w_500,h_750,al_c,q_85,usm_0.66_1.00_0.01/f358f9_2e9aae24b1b54b28931d4c82bba3e700~mv2.webp",
                   )
    item129 = Item(restaurant_id=20,
                   name="Rose Pistachio Dark Chocolate",
                   description="We add crushed rose petals and pistachios to this smooth dark chocolate, creating a beautiful and flavorful bar",
                   price=9.00,
                   image_src="https://static.wixstatic.com/media/f358f9_44416dd5861a46ceb46c3ec359ad56a9~mv2.jpg/v1/fill/w_500,h_750,al_c,q_85,usm_0.66_1.00_0.01/f358f9_44416dd5861a46ceb46c3ec359ad56a9~mv2.webp",
                   )
    item130 = Item(restaurant_id=20,
                   name="Coconut Milk Cashew Chocolate",
                   description="The silkiness of coconut milk and the crunchiness of cashews will make this bar a crowd pleaser. This is our very first vegan milk chocolate! ",
                   price=9.00,
                   image_src="https://static.wixstatic.com/media/f358f9_e45752c0fada472eb07bd7dd4c043266~mv2.jpg/v1/fill/w_500,h_750,al_c,q_85,usm_0.66_1.00_0.01/f358f9_e45752c0fada472eb07bd7dd4c043266~mv2.webp",
                   )
    item131 = Item(restaurant_id=20,
                   name="Masala Chai Dark Chocolate",
                   description="Spiced with a homemade masala chai mixture, perfectly balancing the dark chocolate.",
                   price=9.00,
                   image_src="https://static.wixstatic.com/media/f358f9_9edac3a2152648a6a59f6eacabd8340b~mv2.jpg/v1/fill/w_500,h_750,al_c,q_85,usm_0.66_1.00_0.01/f358f9_9edac3a2152648a6a59f6eacabd8340b~mv2.webp",
                   )
    item132 = Item(restaurant_id=20,
                   name="Vanilla Fennel Dark Chocolate",
                   description="The warm sweet notes of Madagascar vanilla blend smoothly with the herbal, candy flavor of Fennel. All together makes for a lovely dark chocolate bar.",
                   price=9.00,
                   image_src="https://static.wixstatic.com/media/f358f9_bffa58798aec443aa43b9b58f8bf5ef8~mv2.jpg/v1/fill/w_500,h_750,al_c,q_85,usm_0.66_1.00_0.01/f358f9_bffa58798aec443aa43b9b58f8bf5ef8~mv2.webp",
                   )
    item133 = Item(restaurant_id=20,
                   name="Lemon Coriander Dark Chocolate",
                   description="This very dark chocolate is infused with the brightness of house dried lemon peel and herbaceous and spicy notes of freshly ground coriander.",
                   price=9.00,
                   image_src="https://static.wixstatic.com/media/f358f9_a6dc49a6848940088e0fe75db2f18cac~mv2.jpg/v1/fill/w_500,h_750,al_c,q_85,usm_0.66_1.00_0.01/f358f9_a6dc49a6848940088e0fe75db2f18cac~mv2.webp",
                   )

    # 21 - lammes candies
    item134 = Item(restaurant_id=21,
                   name="Texas Chewie Pecan Praline",
                   description="Lammes still uses its 109 year-old secret family recipe to cook the world-famous Texas Chewie® Pecan Praline. Rich, buttery caramel surrounding the choicest large Texas pecans creates a sweet and nutty combination, making this our customers' most popular selection.",
                   price=2.99,
                   image_src="https://cdn11.bigcommerce.com/s-3imi3jzw3p/images/stencil/1024x1024/products/112/396/lammes-pralines-simple__31190.1574309629.jpg?c=2",
                   )
    item135 = Item(restaurant_id=21,
                   name="Milk Chocolate Longhorn",
                   description=" Texas pecans, clustered with chewy caramel then smothered in milk chocolate, combine to create the cornerstone of Lammes chocolate confections. ",
                   price=2.99,
                   image_src="https://cdn11.bigcommerce.com/s-3imi3jzw3p/images/stencil/1024x1024/products/114/594/longhornpostcard2__99465.1559829094.png?c=2",
                   )
    item136 = Item(restaurant_id=21,
                   name="Habanero Pralines",
                   description="Our world-famous 'Texas Chewies,' with a heck of a habanero kick! CAUTION: may be too hot for delicate palates. If you love spicy foods, this will be your new favorite sweet treat. ",
                   price=3.49,
                   image_src="https://cdn11.bigcommerce.com/s-3imi3jzw3p/images/stencil/1024x1024/products/160/535/Hab-Praline-lammes__67032.1543082230.png?c=2",
                   )
    item137 = Item(restaurant_id=21,
                   name="Choc'Adillos",
                   description="If you love our chocolate Longhorns, and you really like almonds, Choc'Adillos are about to be your new favorite candy! Rich, creamy milk or dark chocolate enrobe a cluster of almonds and Lammes' signature caramel. Made in Austin, with an ode to the unique and symbolic Texas armadillo.",
                   price=2.49,
                   image_src="https://cdn11.bigcommerce.com/s-3imi3jzw3p/images/stencil/1024x1024/products/116/387/chocadillos1__91065.1538063204.png?c=2",
                   )
    item138 = Item(restaurant_id=21,
                   name="Divinity",
                   description="Many families consider soft, pillowy Divinity to be the definitive candy for just about every holiday throughout the year. Some families have even mastered the very tricky recipe to make sure they always have some to share at get-togethers.",
                   price=1.99,
                   image_src="https://cdn11.bigcommerce.com/s-3imi3jzw3p/images/stencil/1024x1024/products/145/479/divinity1__10361.1539961516.png?c=2",
                   )

    # 22 - IT"SUGAR
    item139 = Item(restaurant_id=22,
                   name="Giant 1lb Hershey's Bar",
                   description="Get your chocolate fix! 1 full pound of Hershey's Milk Chocolate is all yours. Smooth. Creamy. Luscious. 16 1oz squares ready to snap off and devour. Selfishly hoard all that chocolate for yourself, or if you're a saint, share. ",
                   price=19.99,
                   image_src="https://itsugar.com/media/catalog/product/cache/9392bcc61c6b22792bba4834355aed07/1/l/1lb_hershey.png",
                   )
    item140 = Item(restaurant_id=22,
                   name="World's Largest 2lb Rice Krispies Treat",
                   description="The one, the only, the original Rice Krispies Treats, now super-sized! Perfect for parties and get-togethers, this mega 32oz Rice Krispie Treat Sheet is ooey, gooey, sticky and delicious!",
                   price=22.99,
                   image_src="https://itsugar.com/media/catalog/product/cache/9392bcc61c6b22792bba4834355aed07/r/i/rice482.jpg",
                   )
    item141 = Item(restaurant_id=22,
                   name="Sour Patch Kids Watermelon Gift Box",
                   description="Our exclusive SOUR PATCH KIDS Watermelon box is one in a melon! Filled with nearly 2 pounds of tangy, chewy SOUR PATCH KIDS watermelon candy, this giant watermelon-shaped box is guaranteed to satisfy even the most crazed candy fanatics.",
                   price=19.99,
                   image_src="https://itsugar.com/media/catalog/product/cache/9392bcc61c6b22792bba4834355aed07/w/a/watermelon_gift_box_candy_1.png",
                   )

    item142 = Item(restaurant_id=22,
                   name="World's Largest Box of Nerds",
                   description="Nerds, Nerds, Nerds. Nerdy Nerd, Nerds. Yes -- 1 and 1/2 pounds of strawberry-and-grape Wonka candy goodness. Each giant cereal-sized box is packed with adorably nerdy treat-size mini boxes. Grape fans, pop a box of grape. Strawberry lovers, gobble up a box of strawberry. ",
                   price=19.99,
                   image_src="https://itsugar.com/media/catalog/product/cache/9392bcc61c6b22792bba4834355aed07/g/i/giant_nerds_1_1.png",
                   )

    item143 = Item(restaurant_id=22,
                   name="Sour Patch Kids Tin",
                   description="What's sweet, sour, and delicious all over? Sour Patch Kids! Making the perfect gift for all you Sour Patch fanatics, our exclusive collector's tin holds 14 oz of your favorite tangy, chew candy!",
                   price=14.99,
                   image_src="https://itsugar.com/media/catalog/product/cache/9392bcc61c6b22792bba4834355aed07/s/p/spt_tin_candy.png",
                   )

    item144 = Item(restaurant_id=22,
                   name="Giant Hershey's Kiss",
                   description="Tiny Hershey's Kisses Milk Chocolates are super cute, but this big daddy will knock your socks off! A solid 7oz of deliciously sweet Kisses Milk Chocolate candy packaged in Hershey's signature silver foil makes for the sweetest gift ever.",
                   price=8.99,
                   image_src="https://itsugar.com/media/catalog/product/cache/9392bcc61c6b22792bba4834355aed07/g/i/giant_hershey_kiss_front.jpg",
                   )

    # 23 - see's candies

    item145 = Item(restaurant_id=23,
                   name="Soft Centers Chocolates",
                   description="Indulge in these rich, creamy favorites enrobed in our original milk and dark chocolate.",
                   price=24.50,
                   image_src="https://www.sees.com/dw/image/v2/AATS_PRD/on/demandware.static/-/Sites-sees-catalog/default/dw5fe7ca1e/images/centennial/centennial-soft-centers-1lb-40338-easter-candy-box-alt1.jpg?sw=1036&sh=1036",
                   )
    item146 = Item(restaurant_id=23,
                   name="Assorted Truffles",
                   description="An unforgettable taste experience featuring See's aged milk, dark and white chocolate.",
                   price=27.50,
                   image_src="https://www.sees.com/dw/image/v2/AATS_PRD/on/demandware.static/-/Sites-sees-catalog/default/dw17072bf7/images/all-year/truffles-902-candy-alt2.jpg?sw=1036&sh=1036",
                   )
    item147 = Item(restaurant_id=23,
                   name="Dark Bordeaux Truffle",
                   description="Creamy brown sugar soft center covered in rich dark chocolate and decorated with chocolate rice.",
                   price=1.49,
                   image_src="https://www.sees.com/dw/image/v2/AATS_PRD/on/demandware.static/-/Sites-sees-catalog/default/dwbbb04221/images/custom-mix-pieces/dark-bordeaux-009-cut.jpg?sw=1036&sh=1036",
                   )
    item148 = Item(restaurant_id=23,
                   name="Light Chocolate Truffle",
                   description="Truffle center of semi-sweet chocolate and chocolate liquor covered in smooth milk chocolate.",
                   price=1.49,
                   image_src="https://www.sees.com/dw/image/v2/AATS_PRD/on/demandware.static/-/Sites-sees-catalog/default/dw7adda425/images/custom-mix-pieces/light-chocolate-truffle-cut.jpg?sw=1036&sh=1036",
                   )
    item149 = Item(restaurant_id=23,
                   name="Dark Vanilla Buttercream",
                   description="Buttery, creamy soft center with a touch of vanilla, enrobed in rich dark chocolate.",
                   price=1.49,
                   image_src="https://www.sees.com/dw/image/v2/AATS_PRD/on/demandware.static/-/Sites-sees-catalog/default/dw9eb548d9/images/custom-mix-pieces/dark-buttercream-004-cut.jpg?sw=1036&sh=1036",
                   )
    item150 = Item(restaurant_id=23,
                   name="Kona Mocha",
                   description="Creamy center of coffee and milk chocolate covered in white chocolate and topped with toasted coconut flakes.",
                   price=1.49,
                   image_src="https://www.sees.com/dw/image/v2/AATS_PRD/on/demandware.static/-/Sites-sees-catalog/default/dw8517df00/images/custom-mix-pieces/kona-mocha-068-cut.jpg?sw=1036&sh=1036",
                   )
    item151 = Item(restaurant_id=23,
                   name="Dark Coconut Cream",
                   description="Creamy soft center with angel flake coconut covered in rich dark chocolate.",
                   price=1.49,
                   image_src="https://www.sees.com/dw/image/v2/AATS_PRD/on/demandware.static/-/Sites-sees-catalog/default/dw7af2dc80/images/custom-mix-pieces/dark-cocoanut-102-cut.jpg?sw=1036&sh=1036",
                   )
    item152 = Item(restaurant_id=23,
                   name="Blueberry Truffle",
                   description="Rich, smooth truffle center of white chocolate with blueberries and cream covered in dark chocolate and decorated with white chocolate lace.",
                   price=1.49,
                   image_src="https://www.sees.com/dw/image/v2/AATS_PRD/on/demandware.static/-/Sites-sees-catalog/default/dwb0e8e85a/images/custom-mix-pieces/blueberry-truffle-059-cut.jpg?sw=1036&sh=1036",
                   )
    item153 = Item(restaurant_id=23,
                   name="Milk Strawberry Cream Truffle",
                   description="Creamy soft center with pureed strawberries covered in smooth milk chocolate.",
                   price=1.49,
                   image_src="https://www.sees.com/dw/image/v2/AATS_PRD/on/demandware.static/-/Sites-sees-catalog/default/dw6740b1dd/images/custom-mix-pieces/strawberry-cream-037-cut.jpg?sw=1036&sh=1036",
                   )

    # 25 - jeni's
    item154 = Item(restaurant_id=25,
                   name="Bllackout Chocolate Cake Ice Cream",
                   description="A chocolate ice cream quadruple threat with cake, extra-bitter fudge, and chocolate pieces.",
                   price=12.00,
                   image_src="https://cdn11.bigcommerce.com/s-91692/images/stencil/500x659/products/894/5563/BlackoutChocolateCake-Spoonhead-505px__68559.1590611620.jpg?c=2",
                   )
    item155 = Item(restaurant_id=25,
                   name="Goat Cheese with Red Cherries Ice Cream",
                   description="Mackenzie Creamery goat cheese and sweet-tart, bright red cherries. Mouthwatering and rich, it’s like a scoopable cherry cheesecake.",
                   price=12.00,
                   image_src="https://cdn11.bigcommerce.com/s-91692/images/stencil/500x659/products/461/4543/Goat_Cheese_with_Red_Cherries_Spoonhead_1-505__74616.1588680016.jpg?c=2",
                   )

    item156 = Item(restaurant_id=25,
                   name="Skillet Cinnamon Roll Ice Cream",
                   description="Dark caramel, cream cheese, pastry, and cinnamon (lots of it).",
                   price=12.00,
                   image_src="https://cdn11.bigcommerce.com/s-91692/images/stencil/500x659/products/956/5801/SkilletCinnamonRoll-Spoon-2__07038.1579197502.jpg?c=2",
                   )
    item157 = Item(restaurant_id=25,
                   name="Brambleberry Crisp Ice Cream",
                   description="Oven-toasted oat streusel and a sweet-tart 'brambleberry' jam of blackberries and blackcurrants layered throughout vanilla ice cream.",
                   price=12.00,
                   image_src="https://cdn11.bigcommerce.com/s-91692/images/stencil/500x659/products/455/5040/Brambleberry_Spoonhead_2016-505__20076.1499277019.jpg?c=2",
                   )
    item158 = Item(restaurant_id=25,
                   name="Wildberry Lavendar Ice Cream",
                   description="Intensely fruity, brambly berry ice cream with a pop of sweet orange and lavender.",
                   price=12.00,
                   image_src="https://cdn11.bigcommerce.com/s-91692/images/stencil/500x659/products/468/5864/wildberrylavenderspoon2020-2__17877.1594658097.jpg?c=2",
                   )
    item159 = Item(restaurant_id=25,
                   name="Boston Cream Pie Ice Cream",
                   description="A salted vanilla custard layered with yellow cake pieces and darkest chocolate fudge.",
                   price=12.00,
                   image_src="https://cdn11.bigcommerce.com/s-91692/images/stencil/500x659/products/902/5583/BostonCreamPie-Spoon-505px__59614.1590611643.jpg?c=2",
                   )
    item160 = Item(restaurant_id=25,
                   name="Lemon and Blueberries Parfait Ice Cream",
                   description="Tart and uber creamy lemon with from-scratch blueberry jam in fresh cultured buttermilk and cream.",
                   price=12.00,
                   image_src="https://cdn11.bigcommerce.com/s-91692/images/stencil/500x659/products/903/5587/Lemon--Blueberries-Spoon-Head-505__17869.1551885836.jpg?c=2",
                   )
    item161 = Item(restaurant_id=25,
                   name="Gooey Butter Cake Ice Cream",
                   description="Cream cheese ice cream layered with crumbles of soft vanilla cake and swirls of made-from-scratch caramel-butterscotch sauce. ",
                   price=12.00,
                   image_src="https://cdn11.bigcommerce.com/s-91692/images/stencil/500x659/products/700/5526/Gooey_Butter_Cake_Spoon-1x1-2018-505__12795.1544709703.jpg?c=2",
                   )

    # 26 - dolce neve
    item162 = Item(restaurant_id=26,
                   name="Salted Caramel Ice Cream",
                   description="Vanilla bean with swirls of caramel and sea salt",
                   price=4.25,
                   image_src="https://images.squarespace-cdn.com/content/v1/585d9c06d2b857ddbd62abb8/1482608325379-4TJBIMD9QWQ6ISVHU3IQ/ke17ZwdGBToddI8pDm48kDOoRlTIK78XnuDo0Py62U17gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1USvzdDhJzqaDYJeofUG_ucOevypXrHwOGmSKKmThailuOcTOxFyN6ZGR4RZliLRewA/IMG_5696.JPG?format=300w",
                   )
    item163 = Item(restaurant_id=26,
                   name="Oat Milk, Maple Syrup, and Pecan Ice Cream",
                   description="Texas pecans, of course",
                   price=4.25,
                   image_src="https://images.squarespace-cdn.com/content/v1/585d9c06d2b857ddbd62abb8/1482608355604-IA7U1G458BT62H51DXP9/ke17ZwdGBToddI8pDm48kIyvoTDOqK6tuLbY8s33gHl7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1UTzjvHSAOXjnTxN2sJb-n4pP61BYfWtluh1bxbCEA7ounr1xKjsq_-rO8kOgOtwYvw/IMG_6475.JPG?format=300w",
                   )
    item164 = Item(restaurant_id=26,
                   name="Organic Watermelon Sorbet",
                   description="Fruty and refreshing",
                   price=5.25,
                   image_src="https://images.squarespace-cdn.com/content/v1/585d9c06d2b857ddbd62abb8/1482608361106-UW164CCGGYK7YCM9YZE2/ke17ZwdGBToddI8pDm48kKJDZbuIYkrlmx5aE-J1Brx7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1UbBkYU5rhbv66RuNWYSxEmmK7luYVBB42NaB0vPJvuELSkf28yxfMn4Vem2XljIbPg/IMG_4802.JPG?format=300w",
                   )
    # 27 - Lick
    item165 = Item(restaurant_id=27,
                   name="Orange Chiffon Cake Ice Cream",
                   description="Bites of our delicate Texas Valley orange juice-infused chiffon cake drift through orange scented fresh cheese ice cream courtesy of River Whey Creamery.",
                   price=3.75,
                   image_src="https://static.wixstatic.com/media/c58e38_df2f64d5f0d74fff84d6d83d86d0e778~mv2.jpg/v1/crop/x_58,y_0,w_365,h_266/fill/w_266,h_194,al_c,q_80,usm_0.66_1.00_0.01/lemonade%20poundcake.webp",
                   )
    item166 = Item(restaurant_id=27,
                   name="Cream Cheese Kolache Ice Cream",
                   description="Inspired by our favorite kolaches baked in Hallettsville, TX, this flavor features our own house made yeasted kolaches folded into Mother Culture cream cheese ice cream. Czech it out, y’all!",
                   price=3.75,
                   image_src="https://static.wixstatic.com/media/c58e38_1e586236e2494f60854bbbd7711f6a69~mv2.jpg/v1/crop/x_46,y_14,w_335,h_245/fill/w_266,h_194,al_c,q_80,usm_0.66_1.00_0.01/honeypeanutbrittle.webp",
                   )
    item167 = Item(restaurant_id=27,
                   name="Grandma's Lemon Cake Roll Ice Cream",
                   description="Our classic buttery lemon cake, combined with tart Meyer lemon curd and cream in our ice cream, tastes just like Grandma Hilda made it!",
                   price=4.25,
                   image_src="https://static.wixstatic.com/media/c58e38_bf329b38b7ef4bfd92815311047df978~mv2.jpg/v1/crop/x_61,y_2,w_346,h_253/fill/w_266,h_194,al_c,q_80,usm_0.66_1.00_0.01/cinnamonsugarcookie.webp",
                   )
    item168 = Item(restaurant_id=27,
                   name="Dark Chocolate Mocha Ice Cream",
                   description="Austin’s own Third Coast Coffee beans are steeped in our SRSLY Chocolate ice cream and finished with a splash of Revolution Spirits’ Cafecito coffee liqueur and a swirl of chocolate sauce.",
                   price=4.25,
                   image_src="https://static.wixstatic.com/media/c58e38_8260c9071001433e8bf146adc248d1e1~mv2.jpg/v1/crop/x_32,y_0,w_365,h_266/fill/w_266,h_194,al_c,q_80,usm_0.66_1.00_0.01/texassheetcake.webp",
                   )
    item169 = Item(restaurant_id=27,
                   name="Tequila Lime Pie Ice Cream",
                   description="Sweet lime curd made with G&S Groves limes is mixed with our crisp graham cracker cookie and spiked with Austin’s own Dulce Vida tequila.",
                   price=4.25,
                   image_src="https://static.wixstatic.com/media/c58e38_a1f444d01da04cd58bd4082251b5d511~mv2.jpg/v1/crop/x_54,y_11,w_335,h_245/fill/w_266,h_194,al_c,q_80,usm_0.66_1.00_0.01/lady%20bird%20lavender.webp",
                   )
    item170 = Item(restaurant_id=27,
                   name="Yaupon Matcha Chip Ice Cream",
                   description="Local Leaf Yaupon Matcha, made with native Central Texas yaupon, and Austin's own SRSLY Chocolate star in this naturally green, wildly unique East-meets-West flavor.",
                   price=3.75,
                   image_src="https://static.wixstatic.com/media/c58e38_17c1e290c6894fca9d2e93c3f4713e4f~mv2.jpg/v1/crop/x_59,y_12,w_335,h_245/fill/w_266,h_194,al_c,q_80,usm_0.66_1.00_0.01/yaupon%20matcha%20chip.webp",
                   )
    item171 = Item(restaurant_id=27,
                   name="Grapefruit with Champagne Marshmallows Ice Cream",
                   description="House made champagne marshmallows float through tart and refreshing fresh Texas grapefruit ice cream.",
                   price=4.25,
                   image_src="https://static.wixstatic.com/media/c58e38_d78d00df2e1d429390e83c58536f517f~mv2.jpg/v1/crop/x_35,y_0,w_365,h_266/fill/w_266,h_194,al_c,q_80,usm_0.66_1.00_0.01/grapefruitchampagnemarshmallow.webp",
                   )


    # 28 - nada moo
    item172 = Item(restaurant_id=28,
                   name="S'Mores",
                   description="GIVE YOUR ROASTING STICK THE NIGHT OFF AND DIG INTO YOUR FAVORITE CAMPFIRE TREAT, COMPLETE WITH TOASTED MARSHMALLOW FLAVOR AND A SMOOTH CHOCOLATEY SWIRL.",
                   price=5.99,
                   image_src="https://cdn.shopify.com/s/files/1/0315/8766/3917/products/Smores_INSIDE_525x555_8675badc-3022-4973-bf79-da1b3cbea634_180x.png?v=1616537393",
                   )
    item173 = Item(restaurant_id=28,
                   name="Peppermint Bark",
                   description="MOVE OVER CANDY CANES, THERE'S A NEW SWEET TREAT IN TOWN! FRESH PEPPERMINT PIECES SWIRLED WITH CHOCOLATE FUDGE, ALL HOUSED IN OUR CREAMY COCONUT MILK BASE, IS THE TASTE OF THE HOLIDAYS YOU'LL WANT AT THE TOP OF YOUR WISHLIST.",
                   price=5.99,
                   image_src="https://cdn.shopify.com/s/files/1/0315/8766/3917/products/PeppermintBarkPint_Inside_180x.png?v=1609783811",
                   )
    item174 = Item(restaurant_id=28,
                   name="Caramel Cold Brew and Cookies",
                   description="TALK ABOUT A PICK-ME-UP! CARAMEL COLD BREW & COOKIES COMBINES THE FLAVORS OF COLD BREW COFFEE, SILKY SMOOTH CARAMEL, AND CHOCOLATE COOKIE CHUNKS.",
                   price=5.99,
                   image_src="https://cdn.shopify.com/s/files/1/0315/8766/3917/products/ColdBrew-Caramel-Cookies-UPDATED_INSIDE_525x555_af9fa93a-daaf-419b-bacc-435106020f66_180x.png?v=1616537346",
                   )
    item175 = Item(restaurant_id=28,
                   name="Cookie Dough Fudge",
                   description="WHEN YOU CAN’T CHOOSE BETWEEN COOKIE DOUGH AND FUDGE, QUIT TRYING. ESPECIALLY WHEN YOU CAN HAVE THEM HOUSED IN A CREAMY COCONUT BASE.",
                   price=5.99,
                   image_src="https://cdn.shopify.com/s/files/1/0315/8766/3917/products/cookie-dough-fudge-3x-hover_180x.png?v=1614025688",
                   )
    item176 = Item(restaurant_id=28,
                   name="Marshmallow Dust",
                   description="WE’RE SURE A RAINBOW TASTES LIKE AN EXPLOSION OF CONFETTI SPRINKLES, RASPBERRY, AND MARSHMALLOWY-NESS.",
                   price=5.99,
                   image_src="https://cdn.shopify.com/s/files/1/0315/8766/3917/products/marshmallow-stardust-3x-hover_180x.png?v=1609783829",
                   )
    item177 = Item(restaurant_id=28,
                   name="Peach Cobbler",
                   description="UNSURE WHETHER THIS CREAMY COMBINATION OF LUSCIOUS PEACHES AND DECADENT PIE CRUST PIECES IS GOING TO HIT THE SPOT? PEACH, PLEASE!",
                   price=5.99,
                   image_src="https://cdn.shopify.com/s/files/1/0315/8766/3917/products/peach-cobbler-3x-hover_180x.png?v=1609783819",
                   )
    item178 = Item(restaurant_id=28,
                   name="Banana Caramel Crunch",
                   description="BANANA CARAMEL CRUNCH IS A DAIRY-FREE DREAM COME TRUE, WITH CREAMY BANANA, A DECADENT CARAMEL SWIRL, AND PIE CRUST PIECES MIXED IN.",
                   price=5.99,
                   image_src="https://cdn.shopify.com/s/files/1/0315/8766/3917/products/banana-caramel-crunch-3x-hover_180x.png?v=1609783817",
                   )
    item179 = Item(restaurant_id=28,
                   name="Rockiest Road",
                   description="THE ROCKIER THE ROAD, THE MORE REWARDING THE TRIP. WITH CHOCOLATE COOKIE CRUMBLES, CRUNCHY ALMONDS, AND TWIRLY SWIRLY MARSHMALLOW, OURS IS THE ROCKIEST!",
                   price=5.99,
                   image_src="https://cdn.shopify.com/s/files/1/0315/8766/3917/products/rockiest-road-3x-hover_180x.png?v=1614025576",
                   )

    # 29 - sweet ritual
    item180 = Item(restaurant_id=29,
                   name="Peanut Butter Chocolate Pint",
                   description="Swirls of chocolate chunks in a creamy peanut butter base. A best seller!",
                   price=8.99,
                   image_src="https://sweet-ritual.square.site/uploads/1/2/2/4/122488730/s478793392425521775_p33_i3_w1879.jpeg?width=640",
                   )
    item181 = Item(restaurant_id=29,
                   name="Sunflower Chocolate Chip Pint",
                   description="Chocolate mini chips scattered in salty sweet sunflower seed butter base. Nut free!",
                   price=8.99,
                   image_src="https://sweet-ritual.square.site/uploads/1/2/2/4/122488730/s478793392425521775_p17_i3_w1879.jpeg?width=640",
                   )
    item182 = Item(restaurant_id=29,
                   name="Death Metal By Chocolate Pint",
                   description="Our BEST seller! Locally baked gluten-free chocolate cookies from Pie Jacked Bakery and chocolate freckles in a double chocolate sunflower seed butter base.",
                   price=8.99,
                   image_src="https://sweet-ritual.square.site/uploads/1/2/2/4/122488730/s478793392425521775_p19_i3_w1879.jpeg?width=640",
                   )
    item183 = Item(restaurant_id=29,
                   name="Strawberry Shake",
                   description="House made strawberry sauce swirled into our signature coconut/soy vanilla soft serve. Topped with soft serve 'whipped cream.' 16oz shake, served in a compostable cup with compostable lid and straw. Add a topping or sauce to make your own shake creation",
                   price=6.85,
                   image_src="https://sweet-ritual.square.site/uploads/1/2/2/4/122488730/s478793392425521775_p130_i2_w1879.jpeg?width=640",
                   )
    item184 = Item(restaurant_id=29,
                   name="Coffee Shake",
                   description="Coffee and our signature coconut/soy vanilla soft serve. Topped with soft serve 'whipped cream.' 16oz shake, served in a compostable cup with compostable lid and straw. Add a topping or sauce to make your own shake creation",
                   price=6.85,
                   image_src="https://sweet-ritual.square.site/uploads/1/2/2/4/122488730/s478793392425521775_p131_i2_w1879.jpeg?width=640",
                   )
    item185 = Item(restaurant_id=29,
                   name="Caramel Shake",
                   description="House made salted caramel sauce swirled into our signature coconut/soy vanilla soft serve. Topped with soft serve 'whipped cream.' 16oz shake, served in a compostable cup with compostable lid and straw. Add a topping or sauce to make your own shake creation.",
                   price=6.85,
                   image_src="https://sweet-ritual.square.site/uploads/1/2/2/4/122488730/s478793392425521775_p131_i2_w1879.jpeg?width=640",
                   )
    item186 = Item(restaurant_id=29,
                   name="Rainbow Chaser - Fancy Shake",
                   description="Roasted strawberry sauce, lavender sauce, vegan gummies, rainbow sprinkles. Served in a compostable cup with a compostable straw.",
                   price=8.95,
                   image_src="https://sweet-ritual.square.site/uploads/1/2/2/4/122488730/s478793392425521775_p261_i3_w3644.jpeg?width=640",
                   )
    item187 = Item(restaurant_id=29,
                   name="Mint S'wich",
                   description="Mint scoop sandwiched between two chocolate cookies. Contains gluten. Comes packaged so you can save it for later, or eat it now!",
                   price=4.99,
                   image_src="https://sweet-ritual.square.site/uploads/1/2/2/4/122488730/s478793392425521775_p137_i3_w3024.jpeg?width=640",
                   )
    item188 = Item(restaurant_id=29,
                   name="Cookies 'n' Creme Cake",
                   description="This cake starts with a base of gluten-free chocolate cookie pieces from Pie Jacked Gluten Free Bakery. Then we layer it with loads of our own coconut-based cookies 'n' creme, and top it with Glutino chocolate cookies and a drizzle of chocolate.",
                   price=42.00,
                   image_src="https://sweet-ritual.square.site/uploads/1/2/2/4/122488730/s478793392425521775_p24_i2_w1879.jpeg?width=640",
                   )
    item189 = Item(restaurant_id=29,
                   name="Peanut Butter Cup Cake",
                   description="A layer of gluten-free chocolate cookie pieces from Pie Jacked Gluten Free Bakery forms the base for this cake. Next we load it up with our peanut butter cup ice creme. We finish it with our house-made peanut butter chocolate cups and a drizzle of Enjoy Life chocolate shell. ",
                   price=42.00,
                   image_src="https://sweet-ritual.square.site/uploads/1/2/2/4/122488730/s478793392425521775_p34_i2_w1879.jpeg?width=640",
                   )

    # 30 - voodoo
    item190 = Item(restaurant_id=30,
                   name="Lemon Sunshine",
                   description="Raised yeast doughnut with lemon buttercream filling, topped with powdered sugar",
                   price=3.99,
                   image_src="https://3mmqa316iwx43pzbg62umd8s-wpengine.netdna-ssl.com/wp-content/uploads/2021/03/LS_WebImage.jpg",
                   )
    item191 = Item(restaurant_id=30,
                   name="Vegan Dirt Doughnut",
                   description="Raised yeast doughnut with vanilla frosting and Oreo cookies",
                   price=4.29,
                   image_src="https://3mmqa316iwx43pzbg62umd8s-wpengine.netdna-ssl.com/wp-content/uploads/2017/11/dirt-yeast-doughnut-side-400x400.jpg",
                   )
    item192 = Item(restaurant_id=30,
                   name="Oh Captain, My Captain Dougnut",
                   description="Raised yeast doughnut with vanilla frosting and Captain Crunch",
                   price=4.29,
                   image_src="https://3mmqa316iwx43pzbg62umd8s-wpengine.netdna-ssl.com/wp-content/uploads/2017/11/captain-yeast-doughnut-side-400x400.jpg",
                   )
    item193 = Item(restaurant_id=30,
                   name="Vegan Voodoo Doll Cupcake",
                   description="Raised yeast doughnut filled with raspberry jelly topped with chocolate frosting and a pretzel stake",
                   price=4.99,
                   image_src="https://3mmqa316iwx43pzbg62umd8s-wpengine.netdna-ssl.com/wp-content/uploads/2019/09/voodoo-doll-blue-yeast-side-400x400.jpg",
                   )
    item194 = Item(restaurant_id=30,
                   name="Marshall Mathers Doughnut",
                   description="Plain cake doughnut with vanilla frosting and mini M&M’s",
                   price=2.99,
                   image_src="https://3mmqa316iwx43pzbg62umd8s-wpengine.netdna-ssl.com/wp-content/uploads/2017/11/marshall-mathers-cake-doughnut-side-400x400.jpg",
                   )
    item195 = Item(restaurant_id=30,
                   name="Buttermilk Bar Cake Doughnut",
                   description="Buttermilk doughnut with a glaze",
                   price=2.49,
                   image_src="https://3mmqa316iwx43pzbg62umd8s-wpengine.netdna-ssl.com/wp-content/uploads/2017/11/buttermilk-bar-cake-doughnut-side-400x400.jpg",
                   )
    item196 = Item(restaurant_id=30,
                   name="Vegan Apple Fritter",
                   description="Fried dough with apple chunks and cinnamon covered in a glaze",
                   price=2.29,
                   image_src="https://3mmqa316iwx43pzbg62umd8s-wpengine.netdna-ssl.com/wp-content/uploads/2017/11/apple-fritter-fried-doughnut-side-400x400.jpg",
                   )
    item197 = Item(restaurant_id=30,
                   name="Vegan School Daze PB&J",
                   description="Raised yeast shell filled with raspberry jelly, topped with peanut butter and a side dip of peanuts",
                   price=3.29,
                   image_src="https://3mmqa316iwx43pzbg62umd8s-wpengine.netdna-ssl.com/wp-content/uploads/2017/03/vegan-raised-peanut-butterandjelly-400x400.jpg",
                   )
    item198 = Item(restaurant_id=30,
                   name="Pothole Doughnut",
                   description="Raised yeast bar filled with Bavarian cream and topped with chocolate frosting, Oreos",
                   price=3.29,
                   image_src="https://3mmqa316iwx43pzbg62umd8s-wpengine.netdna-ssl.com/wp-content/uploads/2017/11/pot-hole-yeast-doughnut-side-400x400.jpg",
                   )
    item199 = Item(restaurant_id=30,
                   name="Memphis Mafia Doughnut",
                   description="Fried dough with banana chunks and cinnamon covered in glaze, drizzled in chocolate and peanut butter with peanuts and chocolate chips on top",
                   price=4.29,
                   image_src="https://3mmqa316iwx43pzbg62umd8s-wpengine.netdna-ssl.com/wp-content/uploads/2017/11/memphis-mafia-fried-doughnut-side-400x400.jpg",
                   )
    item200 = Item(restaurant_id=30,
                   name="Vegan Maple Cream Doughnut",
                   description="Raised yeast shell filled with Bavarian cream and topped with maple frosting, a set of eyes, and a mustache",
                   price=2.99,
                   image_src="https://3mmqa316iwx43pzbg62umd8s-wpengine.netdna-ssl.com/wp-content/uploads/2017/03/mcminnville-cream-400x400.jpg",
                   )

    # 32 - gourdoughs
    item201 = Item(restaurant_id=32,
                   name="Black Out Donut",
                   description="Brownie batter, chocolate fudge icing, and chocolate covered brownie bites topped chocolate syrup.",
                   price=5.99,
                   image_src="https://cdn.vox-cdn.com/thumbor/3KYGSp42QE0g5MWKKTMFkWKnmQs=/0x0:2048x1293/1200x800/filters:focal(861x484:1187x810)/cdn.vox-cdn.com/uploads/chorus_image/image/54594407/gourdoughs_chocolate_doughnut.0.jpg",
                   )
    item202 = Item(restaurant_id=32,
                   name="Miss Shortcake Donut",
                   description="Cream cheese icing with fresh cut strawberries.",
                   price=5.99,
                   image_src="http://austinfoodratings.com/wp-content/uploads/2010/08/IMG_0693.jpg",
                   )
    item203 = Item(restaurant_id=32,
                   name="Granny's Pie Donut",
                   description="Caramel, pecans, bananas, and graham crackers.",
                   price=5.99,
                   image_src="https://i.pinimg.com/originals/a6/f9/ad/a6f9ad17523255eddea8607fa1d8f413.jpg",
                   )
    item204 = Item(restaurant_id=32,
                   name="Funky Monkey Donut",
                   description="Grilled bananas and cream cheese icing with brown sugar.",
                   price=5.99,
                   image_src="https://www.femalefoodie.com/wp-content/uploads/2016/11/gourdoughs-9.jpg",
                   )
    item205 = Item(restaurant_id=32,
                   name="Squealing Pig Donut",
                   description="Cream cheese icing, house made strawberry jalapeño jelly, grilled bacon topped with candied jalapeños",
                   price=6.99,
                   image_src="https://c2.staticflickr.com/2/1699/25630153654_41e8bae717_z.jpg",
                   )

    # 33 - julie myrtille
    item206 = Item(restaurant_id=33,
                   name="Apricot Scone",
                   description="Buttery and Flaky",
                   price=2.99,
                   image_src="https://www.juliemyrtille.us/uploads/1/3/1/2/131225838/s725118144811790655_p95_i2_w2560.jpeg",
                   )
    item207 = Item(restaurant_id=33,
                   name="Blueberry Muffin",
                   description="The perfect muffin.",
                   price=5.00,
                   image_src="https://www.juliemyrtille.us/uploads/1/3/1/2/131225838/s725118144811790655_p44_i6_w1280.jpeg",
                   )

    item208 = Item(restaurant_id=33,
                   name="Marble Cake Slice",
                   description="Swirls of Vanilla and Chocolate Cake.",
                   price=6.00,
                   image_src="https://www.juliemyrtille.us/uploads/1/3/1/2/131225838/s725118144811790655_p162_i2_w1080.png",
                   )
    item209 = Item(restaurant_id=33,
                   name="Madeleines - Pack of 6",
                   description="Julie's Signature French Pastry.",
                   price=12.00,
                   image_src="https://www.juliemyrtille.us/uploads/1/3/1/2/131225838/s725118144811790655_p94_i3_w2560.jpeg",
                   )
    item210 = Item(restaurant_id=33,
                   name="Fresh Raspberry Tart",
                   description="Perfect for Summer",
                   price=9.00,
                   image_src="https://www.juliemyrtille.us/uploads/1/3/1/2/131225838/s725118144811790655_p167_i2_w1364.jpeg",
                   )
    item211 = Item(restaurant_id=33,
                   name="Pear Almond Tart",
                   description="Light yet full of flavor.",
                   price=6.00,
                   image_src="https://www.juliemyrtille.us/uploads/1/3/1/2/131225838/s725118144811790655_p87_i5_w2560.jpeg",
                   )
    item212 = Item(restaurant_id=33,
                   name="Croissant Strawberry Cream",
                   description="A buttery croissant stuffed with fresh strawberries and cream.",
                   price=8.00,
                   image_src="https://www.juliemyrtille.us/uploads/1/3/1/2/131225838/s725118144811790655_p160_i1_w1080.jpeg",
                   )

    # 34 - milk way shakes
    item213 = Item(restaurant_id=34,
                   name="Oreo Borealis Shake",
                   description="Chocolate or vanilla ice cream blended with Oreos, mint simple syrup, swirled with fudge, and sprinkled with edible glitter stars.",
                   price=5.75,
                   image_src="https://milky-way-shakes.square.site/uploads/1/3/3/7/133709550/s358519802933183252_p1_i1_w1080.jpeg?width=640",
                   )
    item214 = Item(restaurant_id=34,
                   name="Chocolate Eclipse Shake",
                   description="Vanilla ice cream blended with fudge, dark chocolate almond bark, and Celeste's Best brownies. Comes swirled with fudge and topped with a dark chocolate almond moon.",
                   price=5.75,
                   image_src="https://milky-way-shakes.square.site/uploads/1/3/3/7/133709550/s358519802933183252_p5_i1_w1440.jpeg?width=640",
                   )
    item215 = Item(restaurant_id=34,
                   name="Grackle Massacre Shake",
                   description="Caw! Chocolate or vanilla ice cream blended with fudge, caramel sauce, cinnamon, and chipotle. Comes swirled with fudge, sprinkled with cinnamon, and topped with a dark chocolate pentagram. We recommend chocolate ice cream for this one to balance out the spiciness!",
                   price=5.75,
                   image_src="https://milky-way-shakes.square.site/uploads/1/3/3/7/133709550/s358519802933183252_p4_i1_w1440.jpeg?width=640",
                   )
    item216 = Item(restaurant_id=34,
                   name="The Violet Shake",
                   description="Vanilla ice cream blended with blueberry compote and lavender simple syrup. Topped with vanilla meringues and a candied edible flower.",
                   price=5.75,
                   image_src="https://milky-way-shakes.square.site/uploads/1/3/3/7/133709550/s358519802933183252_p3_i1_w1080.jpeg?width=640",
                   )
    item217 = Item(restaurant_id=34,
                   name="Rite of Spring Shake",
                   description="Deliciously light & floral, this shake comes with your choice of chocolate or vanilla ice cream, blended with lavender simple syrup & white chocolate pistachio bark, & topped with an edible-viola-encrusted pistachio meringue medallion.",
                   price=6.75,
                   image_src="https://milky-way-shakes.square.site/uploads/1/3/3/7/133709550/s358519802933183252_p10_i14_w2880.jpeg?width=640",
                   )
    item218 = Item(restaurant_id=34,
                   name="Strawberry Shake",
                   description="Strawberry shake, plain and simple! This shake is made with our vanilla ice cream and strawberry compote. It is super popular for kids. ",
                   price=5.25,
                   image_src="https://milky-way-shakes.square.site/uploads/1/3/3/7/133709550/s358519802933183252_p14_i1_w1440.jpeg?width=640",
                   )
    item219 = Item(restaurant_id=34,
                   name="Buzz Aldrin Shake",
                   description="Chocolate ice cream blended with cold brew and house-made almond toffee.",
                   price=5.75,
                   image_src="https://milky-way-shakes.square.site/uploads/1/3/3/7/133709550/s358519802933183252_p6_i1_w1440.jpeg?width=640",
                   )

    # 35 - tiffs treats
    item220 = Item(restaurant_id=35,
                   name="Chocolate Chip Cookie",
                   description="Tiff’s original recipe features gooey, semi-sweet chocolate morsels that are still melting in that first bite. Perfectly cooked every time, these fresh-baked chocolate chip cookies are our most popular cookie of all time.",
                   price=1.99,
                   image_src="https://www.cookiedelivery.com/CookieDelivery/media/images/img/quickview_cookies_chocchip.png?ext=.png",
                   )
    item221 = Item(restaurant_id=35,
                   name="White Chocolate Chip & Almond Cookie",
                   description="The subtle flavor of melty white chocolates, along with the delicate taste of almonds make for one delicious treat in our White Chocolate Chip & Almond cookies.",
                   price=1.99,
                   image_src="https://www.cookiedelivery.com/CookieDelivery/media/newimg/04%20menu%20details/04-3%20detail%20flavor%20menus/Cookies/Quickviews/quickview_cookies_whtchocalm.png?width=435&height=193&ext=.png",
                   )
    item222 = Item(restaurant_id=35,
                   name="M&M Cookie",
                   description="We take America’s classic candy-coated delights and bake them into a soft and chewy cookie … the result is a colorful treat that satisfies the sweet tooth of all ages.",
                   price=1.99,
                   image_src="https://www.cookiedelivery.com/CookieDelivery/media/newimg/04%20menu%20details/04-3%20detail%20flavor%20menus/Cookies/Quickviews/quickview_cookies_MM.png?width=435&height=193&ext=.png",
                   )
    item223 = Item(restaurant_id=35,
                   name="Salted Caramel Blondie",
                   description="Sweet 'n salty, chewy n' crunchy, our blondie bar is made with caramel and caramel bits, white chocolate chips, walnuts, topped with toffee bits and sea salt.",
                   price=3.29,
                   image_src="https://www.cookiedelivery.com/CookieDelivery/media/newimg/04%20menu%20details/04-3%20detail%20flavor%20menus/Brownies/Quickviews/Menu-Quickview-Blondie.png?ext=.png",
                   )
    item224 = Item(restaurant_id=35,
                   name="Peanut Butter Chocolate Bar",
                   description="Layered bar made with peanut butter chocolate chip cookie dough, sandwiched around a melty milk chocolate candy bar. Topped with miniature chocolate chips and peanut butter morsels.",
                   price=3.29,
                   image_src="https://www.cookiedelivery.com/CookieDelivery/media/newimg/04%20menu%20details/04-3%20detail%20flavor%20menus/Brownies/Quickviews/Menu-Quickview-PBCBar.png?ext=.png",
                   )
    item225 = Item(restaurant_id=35,
                   name="Tiffblitz frozen dessert",
                   description="Blend of Vanilla Ice Cream and chunks of Tiff’s Treats chocolate chip cookies and brownies. Topped with crumbled sugar cookies.",
                   price=5.49,
                   image_src="https://www.cookiedelivery.com/CookieDelivery/media/newimg/04%20menu%20details/04-3%20detail%20flavor%20menus/tiffblitz/Quickviews/TiffBlitz-2018.png?width=435&height=193&ext=.png",
                   )
    item226 = Item(restaurant_id=35,
                   name="Tiffwich ice cream sandwich",
                   description="Vanilla Ice Cream sandwiched between 2 warm chocolatae chip cookies.",
                   price=4.99,
                   image_src="https://www.cookiedelivery.com/CookieDelivery/media/newimg/04%20menu%20details/04-3%20detail%20flavor%20menus/tiffwich/Quickviews/Quickview-Tiffwich.png?ext=.png",
                   )

    # 37 - insomnia
    item227 = Item(restaurant_id=37,
                   name="Double Chocolate Mint Cookie",
                   description="Our take on a favorite flavor combo. A warm dark chocolate cookie with mint chips and chunks of milk chocolate.",
                   price=1.75,
                   image_src="https://cdn1.insomniacookies.com/uploads/products/1200__0003_InsomniaCookies_TraditionalCookies_DoubleChocolateMint_1610249959.png",
                   )
    item228 = Item(restaurant_id=37,
                   name="Vegan Chocolate Chunk Cookie",
                   description="A vegan cookie that warms your soul with generous amounts of rich, buttery flavor and ooey-gooey (dairy-free) chocolate chunks.",
                   price=1.75,
                   image_src="https://cdn1.insomniacookies.com/uploads/products/1200_VeganChocolateChunk_1610134136.png",
                   )
    item229 = Item(restaurant_id=37,
                   name="Confetti Deluxe Cookie",
                   description="A tricked-out sugar cookie filled with rainbow sprinkles and creamy white chocolate chips.",
                   price=3.25,
                   image_src="https://cdn1.insomniacookies.com/uploads/products/Deluxe_Confetti-1200x1200_1611002493.png",
                   )
    item230 = Item(restaurant_id=37,
                   name="Salted Caramel Cookie",
                   description="Indulgent, sweet caramel and savory sea salt baked into a Deluxe-sized sugar cookie base.",
                   price=3.25,
                   image_src="https://cdn1.insomniacookies.com/uploads/products/Deluxe_Caramel-1200x1200_1611002530.png",
                   )
    item231 = Item(restaurant_id=37,
                   name="Cookie'wich",
                   description="A scoop of cold ice cream sandwiched between two warm Classic cookies. Note: Cookie'wiches are delivered unassembled.",
                   price=6.00,
                   image_src="https://cdn1.insomniacookies.com/uploads/products/1200_Cookiewich2_1611079892.png",
                   )
    item232 = Item(restaurant_id=37,
                   name="Chocolate Chip Brownie",
                   description="Consider this warm, chocolatey delight baked to perfection and another one of ice cream’s BFFs.",
                   price=3.25,
                   image_src="https://cdn1.insomniacookies.com/uploads/products/Brownies_ChocolateChipBrownie_1610142714.png",
                   )
    item233 = Item(restaurant_id=37,
                   name="Vegan Double Chocolate Chunk",
                   description="A vegan spin on our Classic Double Chocolate cookie with the same levels of dark chocolate decadence and melty (dairy-free) chocolate chunks.",
                   price=1.75,
                   image_src="https://cdn1.insomniacookies.com/uploads/products/1200_VeganDoubleChocolateChunk_1610134351.png",
                   )

    # 38 - Crumbl
    item234 = Item(restaurant_id=38,
                   name="Carrot Cake Cookie",
                   description="A warm carrot cake cookie topped with rich cream cheese frosting and chopped pecan pieces.",
                   price=2.99,
                   image_src="https://crumbl.video/add85afa-30e8-401b-bc62-d4317da08ed5_CarrotCake_Tech.png",
                   )
    item235 = Item(restaurant_id=38,
                   name="Cookies and Cream Cookie",
                   description="A warm cookies & cream cookie topped with Oreo® pieces and a white chocolate drizzle.",
                   price=2.99,
                   image_src="https://s3.us-west-2.amazonaws.com/media.crumbl.com/20c36648-a7b5-4abf-b19d-ad7733aeb638_A-CookiesCream1.png",
                   )
    item236 = Item(restaurant_id=38,
                   name="Sea Salt Toffee Cookie",
                   description="A warm cookie made with sweet toffee pieces and milk chocolate chips.",
                   price=2.99,
                   image_src="https://s3.us-west-2.amazonaws.com/media.crumbl.com/0d0c1b44-543d-4d46-accc-ec9a3f06c473_screen1.png",
                   )
    item237 = Item(restaurant_id=38,
                   name="Chilled Sugar Cookie (Cadbury Mini Eggs)",
                   description="A chilled sugar cookie topped with sweet almond frosting and Cadbury Eggs",
                   price=2.99,
                   image_src="https://crumbl.video/2005ac0d-876c-4320-8d67-1abf706a0807_ChilledSugarCadburyEgg.png",
                   )
    item238 = Item(restaurant_id=38,
                   name="Salted Caramel Ice Cream",
                   description="Our Crumbl Cream is made with the finest ingredients for the most delicious ice cream you’ve ever had.",
                   price=4.29,
                   image_src="https://crumbl.video/d9922853-984b-4a79-9650-bcba25a01a47_RightLeanSMALL-SaltedCaramel.png",
                   )
    item239 = Item(restaurant_id=38,
                   name="S'Mores Ice Cream",
                   description="Our Crumbl Cream is made with the finest ingredients for the most delicious ice cream you’ve ever had.",
                   price=4.29,
                   image_src="https://crumbl.video/4c1bbbc0-7c4c-46bd-b3d6-9a0eea215b4e_LeftLeanSMALL-Smores.png",
                   )
    item240 = Item(restaurant_id=38,
                   name="Churro Ice Cream",
                   description="Our Crumbl Cream is made with the finest ingredients for the most delicious ice cream you’ve ever had.",
                   price=4.29,
                   image_src="https://crumbl.video/52b44496-4b4a-45ab-92c0-8ffb57345b97_churro.png",
                   )
    item241 = Item(restaurant_id=38,
                   name="Raspberry Cheesecake Ice Cream",
                   description="Our Crumbl Cream is made with the finest ingredients for the most delicious ice cream you’ve ever had.",
                   price=4.29,
                   image_src="https://crumbl.video/8e8ba1ed-84fd-4122-a49f-246c41841ac9_raspberry-cheesecake.png",
                   )

    # 39  -the baked bear
    item242 = Item(restaurant_id=39,
                   name="Cookies & Cream Cookies with Blackberry Ice Cream",
                   description="Oreo-Cheesecake Cookies with a Vanilla Bean Ice Cream w/ a Blackberry Ripple & Pie Crust Pieces. ",
                   price=5.95,
                   image_src="https://www.qsrmagazine.com/sites/default/files/styles/story_page/public/story/baked-bear.jpg?itok=j46ZFOu1",
                   )
    item243 = Item(restaurant_id=39,
                   name="Brownies with Mint Chip Ice Cream",
                   description="Triple chocolate chip brownies with mint chocolate chip ice cream.",
                   price=6.50,
                   image_src="https://assets3.thrillist.com/v1/image/1727681/381x254/crop;jpeg_quality=65.jpg",
                   )
    item244 = Item(restaurant_id=39,
                   name="Gooey Cookies with Butter Brittle Cake Ice Cream",
                   description="Yellow cake and cream cheese cookies dipped in powdered sugar with a vanilla bean ice cream layered with Butter brittle, vanilla cake, and a sea salt caramel ripple.",
                   price=5.95,
                   image_src="https://communityimpact.com/uploads/images/2020/03/02/41996.jpeg",
                   )
    item245 = Item(restaurant_id=39,
                   name="Chocolate Chip Cookies with Cookie Dough Ice Cream",
                   description="Classic homemade chocolate chip cookies with a chocolate chip ice cream with cookie dough pieces.",
                   price=5.95,
                   image_src="https://picky-palate.com/wp-content/uploads/2013/08/Baked-Bear-4.jpg",
                   )
    item246 = Item(restaurant_id=39,
                   name="Funfetti Cookies with Cookies and Cream Ice Cream",
                   description="Birthday cake cookies with sprinkles with a cookies and cream ice cream with oreo pieces.",
                   price=5.95,
                   image_src="https://media.bizj.us/view/img/10791607/1851965312093691325252583543055055793555493n*1024xx718-404-0-317.jpg",
                   )





    db.session.add(item1)
    db.session.add(item2)
    db.session.add(item3)
    db.session.add(item4)
    db.session.add(item5)
    db.session.add(item6)
    db.session.add(item7)
    db.session.add(item8)
    db.session.add(item9)
    db.session.add(item10)
    db.session.add(item11)
    db.session.add(item12)
    db.session.add(item13)
    db.session.add(item14)
    db.session.add(item15)
    db.session.add(item16)
    db.session.add(item17)
    db.session.add(item18)
    db.session.add(item19)
    db.session.add(item20)
    db.session.add(item21)
    db.session.add(item22)
    db.session.add(item23)
    db.session.add(item24)
    db.session.add(item25)
    db.session.add(item26)
    db.session.add(item27)
    db.session.add(item28)
    db.session.add(item29)
    db.session.add(item30)
    db.session.add(item31)
    db.session.add(item32)
    db.session.add(item33)
    db.session.add(item34)
    db.session.add(item35)
    db.session.add(item36)
    db.session.add(item37)
    db.session.add(item38)
    db.session.add(item39)
    db.session.add(item40)
    db.session.add(item41)
    db.session.add(item42)
    db.session.add(item43)
    db.session.add(item44)
    db.session.add(item45)
    db.session.add(item46)
    db.session.add(item47)
    db.session.add(item48)
    db.session.add(item49)
    db.session.add(item50)
    db.session.add(item51)
    db.session.add(item52)
    db.session.add(item53)
    db.session.add(item54)
    db.session.add(item55)
    db.session.add(item56)
    db.session.add(item57)
    db.session.add(item58)
    db.session.add(item59)
    db.session.add(item60)
    db.session.add(item61)
    db.session.add(item62)
    db.session.add(item63)
    db.session.add(item64)
    db.session.add(item65)
    db.session.add(item66)
    db.session.add(item67)
    db.session.add(item68)
    db.session.add(item69)
    db.session.add(item70)
    db.session.add(item71)
    db.session.add(item72)
    db.session.add(item73)
    db.session.add(item74)
    db.session.add(item75)
    db.session.add(item76)
    db.session.add(item77)
    db.session.add(item78)
    db.session.add(item79)
    db.session.add(item80)
    db.session.add(item81)
    db.session.add(item82)
    db.session.add(item83)
    db.session.add(item84)
    db.session.add(item85)
    db.session.add(item86)
    db.session.add(item87)
    db.session.add(item88)
    db.session.add(item89)
    db.session.add(item90)
    db.session.add(item91)
    db.session.add(item92)
    db.session.add(item93)
    db.session.add(item94)
    db.session.add(item95)
    db.session.add(item96)
    db.session.add(item97)
    db.session.add(item98)
    db.session.add(item99)
    db.session.add(item100)
    db.session.add(item101)
    db.session.add(item102)
    db.session.add(item103)
    db.session.add(item104)
    db.session.add(item105)
    db.session.add(item106)
    db.session.add(item107)
    db.session.add(item108)
    db.session.add(item109)
    db.session.add(item110)
    db.session.add(item111)
    db.session.add(item112)
    db.session.add(item113)
    db.session.add(item114)
    db.session.add(item115)
    db.session.add(item116)
    db.session.add(item117)
    db.session.add(item118)
    db.session.add(item119)
    db.session.add(item120)
    db.session.add(item121)
    db.session.add(item122)
    db.session.add(item123)
    db.session.add(item124)
    db.session.add(item125)
    db.session.add(item126)
    db.session.add(item127)
    db.session.add(item128)
    db.session.add(item129)
    db.session.add(item130)
    db.session.add(item131)
    db.session.add(item132)
    db.session.add(item133)
    db.session.add(item134)
    db.session.add(item135)
    db.session.add(item136)
    db.session.add(item137)
    db.session.add(item138)
    db.session.add(item139)
    db.session.add(item140)
    db.session.add(item141)
    db.session.add(item142)
    db.session.add(item143)
    db.session.add(item144)
    db.session.add(item145)
    db.session.add(item146)
    db.session.add(item147)
    db.session.add(item148)
    db.session.add(item149)
    db.session.add(item150)
    db.session.add(item151)
    db.session.add(item152)
    db.session.add(item153)
    db.session.add(item154)
    db.session.add(item155)
    db.session.add(item156)
    db.session.add(item157)
    db.session.add(item158)
    db.session.add(item159)
    db.session.add(item160)
    db.session.add(item161)
    db.session.add(item162)
    db.session.add(item163)
    db.session.add(item164)
    db.session.add(item165)
    db.session.add(item166)
    db.session.add(item167)
    db.session.add(item168)
    db.session.add(item169)
    db.session.add(item170)
    db.session.add(item171)
    db.session.add(item172)
    db.session.add(item173)
    db.session.add(item174)
    db.session.add(item175)
    db.session.add(item176)
    db.session.add(item177)
    db.session.add(item178)
    db.session.add(item179)
    db.session.add(item180)
    db.session.add(item181)
    db.session.add(item182)
    db.session.add(item183)
    db.session.add(item184)
    db.session.add(item185)
    db.session.add(item186)
    db.session.add(item187)
    db.session.add(item188)
    db.session.add(item189)
    db.session.add(item190)
    db.session.add(item191)
    db.session.add(item192)
    db.session.add(item193)
    db.session.add(item194)
    db.session.add(item195)
    db.session.add(item196)
    db.session.add(item197)
    db.session.add(item198)
    db.session.add(item199)
    db.session.add(item200)
    db.session.add(item201)
    db.session.add(item202)
    db.session.add(item203)
    db.session.add(item204)
    db.session.add(item205)
    db.session.add(item206)
    db.session.add(item207)
    db.session.add(item208)
    db.session.add(item209)
    db.session.add(item210)
    db.session.add(item211)
    db.session.add(item212)
    db.session.add(item213)
    db.session.add(item214)
    db.session.add(item215)
    db.session.add(item216)
    db.session.add(item217)
    db.session.add(item218)
    db.session.add(item219)
    db.session.add(item220)
    db.session.add(item221)
    db.session.add(item222)
    db.session.add(item223)
    db.session.add(item224)
    db.session.add(item225)
    db.session.add(item226)
    db.session.add(item227)
    db.session.add(item228)
    db.session.add(item229)
    db.session.add(item230)
    db.session.add(item231)
    db.session.add(item232)
    db.session.add(item233)
    db.session.add(item234)
    db.session.add(item235)
    db.session.add(item236)
    db.session.add(item237)
    db.session.add(item238)
    db.session.add(item239)
    db.session.add(item240)
    db.session.add(item241)
    db.session.add(item242)
    db.session.add(item243)
    db.session.add(item244)
    db.session.add(item245)
    db.session.add(item246)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_items():
    db.session.execute('TRUNCATE items CASCADE;')
    db.session.commit()
