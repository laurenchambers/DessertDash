## `/`

- Home page with featured restaurants
- Buttons to sign-in/create account

## `/login`

- Log in page with form
- Demo user sign-in button
- Hyperlink to create an account at bottom of form
- (Sign up via Facebook - a probably-wont-happen-but-maybe bonus feature)

## `/signup`

- Sign up page with form
- Hyperlink to login if you already have an account

## `/home`

- Page that displays all Restaurants
- Displays genre of restaurants (clickable icons)
- Collapsable menu bar on the left

## `/restaurants/:id`

- Individual restaurant page that displays all available information for that restaurant
  > - Genre, Overall Rating, Price ($-$$$$), Hours, Full Menu
- Displays the restaurants full menu
- Can click on any menu item to view the item's full description and to add the item to your cart (if you are logged in)

## `/restaurants/genre`

- Upon clicking on a genre icon on the /home route, a user will be taken to the /restaurants/genre route
- This page will display all restaurants that match the specified genre

## `/checkout`

- This route will display the logged-in User's cart
- The total price of the cart will be displayed
- They User will have the option to remove any item from the cart
