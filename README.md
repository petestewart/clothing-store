# clothing-store

A collection of APIs to interact with the catalog and shopping cart of a clothing store. Created with Python, Flask and Flask Restful.

#### To start server:
`python app.py`

#### To run unit tests:
`python -m unittest tests.test_catalog`

`python -m unittest tests.test_cart`


## API documentation:
---
[![Get](https://img.shields.io/badge/-GET-GREEN?style=flat-square)](#)
**Get all items in catalog**

http://127.0.0.1:5000/catalogitems

Returns a list of all items currently in the store catalog.

#### Response:
```json
[
    {
        "id": "1",
        "name": "tshirt",
        "price": 10.0
    },
    {
        "id": "2",
        "name": "shorts",
        "price": 5.0
    },
    {
        "id": "3",
        "name": "long sleeve",
        "price": 15.0
    }
]
```

---
[![Post](https://img.shields.io/badge/-POST-yellow?style=flat-square)](#)
**Add item to cart**

http://127.0.0.1:5000/cart

Adds an item to the shopping cart and returns a list of the current items in the cart.

#### Parameters:
`item_id` (required) The id of the item from the store catalog intended to be added to the cart.

`quantity` The quantity of the item intended to be added to the cart. If `quantity` is not supplied, the API will assume a quantity of 1 and add one item to the cart.

#### Body:
```json
{
    "item_id": "2",
    "quantity": 3
}

```
#### Response:
```json
[
    {
        "id": "3",
        "name": "long sleeve",
        "price": 15.0,
        "quantity": 6,
        "line_total": 90.0
    },
    {
        "id": "2",
        "name": "shorts",
        "price": 5.0,
        "quantity": 6,
        "line_total": 30.0
    }
]
```
---
[![Patch](https://img.shields.io/badge/-PATCH-red?style=flat-square)](#) 
**Remove item from cart**

http://127.0.0.1:5000/cart

Removes an item from the shopping cart and returns a list of the current items in the cart.

#### Parameters:
`item_id` (required) The id of the item from the store catalog intended to be removed from the cart.
`quantity` The quantity of the item intended to be removed from the cart. If `quantity` is not supplied, the API will assume the entire quantity of the item should be removed from the cart.

#### Body:
```json
{
    "item_id": "2",
    "quantity": 4
}
```

#### Response:
```json
[
    {
        "id": "3",
        "name": "long sleeve",
        "price": 15.0,
        "quantity": 6,
        "line_total": 90.0
    },
    {
        "id": "2",
        "name": "shorts",
        "price": 5.0,
        "quantity": 2,
        "line_total": 30.0
    }
]
```
---

[![Get](https://img.shields.io/badge/-GET-GREEN?style=flat-square)](#) 
**Get all items in cart**

http://127.0.0.1:5000/cart

Returns the contents of the shopping cart in a list called `items`, along with a `totals_due` object containing the calculated values for `total_items`, `subtotal`, `tax`, `shipping` and `final_total`.


#### Response:
```json
{
    "items": [
        {
            "id": "3",
            "name": "long sleeve",
            "price": 15.0,
            "quantity": 6,
            "line_total": 90.0
        },
        {
            "id": "2",
            "name": "shorts",
            "price": 5.0,
            "quantity": 6,
            "line_total": 30.0
        }
    ],
    "totals_due": {
        "total_items": 12,
        "subtotal": 120.0,
        "tax": 10.68,
        "shipping": 4,
        "final_total": 134.68
    }
}
```
---

[![Delete](https://img.shields.io/badge/-DELETE-red?style=flat-square)](#)
**Clear contents of cart**

http://127.0.0.1:5000/cart

Clears the contents of the cart and returns the empty cart.

#### Response:
```json
[]
```

