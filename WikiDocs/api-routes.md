## Index

- `GET /` - populate all restaurants

## Sessions

User authorization

- `GET /api/session` - get/restore current session
- `POST /api/session` - login user via credentials
- `DELETE /api/session` - logout user/clear session user

## Users

- ` POST /api/users` - signup/create new user
- ` GET /api/users/:id/sips` - get sips

## Restaurants

- `GET /api/restaurants` - get all restaurants
- `GET /api/restaurants/:id` - get a specific restaurant
- `GET /api/restaurants/genres` - get all restauants based on genre

## Checkout

- `GET /api/checkout/:id` - get the cart
- `POST /api/checkout/ ` - create the cart
- ` POST /api/checkout/:id` - edit your cart
- `DELETE /api/checkout/:id ` - remove item from cart
