# Inventory Mangement Backend

![Python Version](https://img.shields.io/badge/python-v3.8-brightgreen)
![Django Version](https://img.shields.io/badge/django-v3.2-brightgreen)
![DB](https://img.shields.io/badge/db-postgres-brightgreen)
![Docker](https://img.shields.io/badge/docker-yes-brightgreen)
![Swagger UI](https://img.shields.io/badge/swagger_ui-yes-brightgreen)

A simple inventory management backend built using Django with CRUD APIs for Warehouse and Items.

Internal APIs include:
 - Country
 - State
 - City
 - Address

**Find the low level design [here](https://github.com/harsh020/inventory_mangement/blob/master/design.md)**


## Content
1. [How to run](https://github.com/harsh020/inventory_mangement/new/master?readme=1#how-to-run)
2. [E-R Diagram](https://github.com/harsh020/inventory_mangement/new/master?readme=1#e-r--diagram)
3. [Swagger Open API Specification](https://github.com/harsh020/inventory_mangement/new/master?readme=1#swagger-open-api-specification)
4. [Admin Panel](https://github.com/harsh020/inventory_mangement/new/master?readme=1#admin-panel)
5. [APIs](https://github.com/harsh020/inventory_mangement/new/master?readme=1#apis)
    - [Warehouse API](https://github.com/harsh020/inventory_mangement/new/master?readme=1#warehouse-api)
    - [Item API](https://github.com/harsh020/inventory_mangement/new/master?readme=1#item-api)
6. [How to use](https://github.com/harsh020/inventory_mangement/new/master?readme=1#how-to-use)


## How to run

- **Method 1:** Using docker (**Note:** Make sure that your ports 8000 and 5432 are free)
  - Make user your Docker Engine is running, then type the following command
    ```sh
    $ docker-compose -f local.yml up
    ```
    
- **Method 2:** Using plain old django locally. **Note:** Make sure you have a postgres with a db and don't forget to set the same in the environment variables in `.envs/.local/.postgres`
  - Create a virtual environment, if you don't want you global packages to be disturbed.
  - Using `pip` install the requirements using following command
    ```sh
    $ pip3 install -r requirements/local.txt
    ```
  - Migrate
    ```sh
    $ python3 manage.py migrate
    ```
  - Run the following commands and type the asked details
    ```sh
    $ python3 manage.py createsuperuser
    ```
  - Collect static files and run django server using
    ```sh
    $ python3 manage.py collectstatic
    $ python3 manage.py runserver 0.0.0.0:8000
    ```

## E-R Diagram

![Inventory Management - ER](https://user-images.githubusercontent.com/39561084/171666796-aafa8b0c-02a8-483a-a007-da5ca91967e1.jpg)



**Note**

`${BASE_URL}`: The base url on which the django app can be reached.

If Running locally, it is `http://localhost:8000`

## Swagger Open API Specifications
  - url: `${BASE_URL}/`

## Admin Panel
The admin panel is provided by Django itself.
  - url: `${BASE_URL}/admin/`

## APIs

### Warehouse API
 **Note:** Please ensure you pass `id` for `city`, `state` and `country` in address. One can create them using the admin panel.

  - #### Create:
    - **url:** `${BASE_URL}/warehouse/v1/create/`
    - **method:** `POST`
    - **data:**
      ```json
      {
        "address": {},
        "is_active": true,
        "is_deleted": false,
        "name": "string"
      }
      ```
    - **response:**
      ```json
      {
          "error": false,
          "data": {
              "id": "int",
              "address": {
                  "id": "int",
                  "city": "string",
                  "state": "string",
                  "country": "string",
                  "address": "string",
                  "pincode": "string",
                  "mobile": "string",
                  "latitude": "string",
                  "longitude": "string"
              },
              "created": "string",
              "modified": "string",
              "is_active": true,
              "is_deleted": false,
              "name": "string"
          }
      }
      ```
    - **example curl:**
      ```sh
      curl --location --request POST 'http://localhost:8000/warehouse/v1/create/' \
      --header 'Content-Type: application/json' \
      --data-raw '{
          "name": "test warehouse",
          "address": {
              "address": "test line",
              "country": 1,
              "state": 1,
              "city": 1,
              "pincode": "226010",
              "mobile": "9876543211",
              "latitude": "80.999",
              "longitude": "56.999"
          }
      }'
      ```
      
  - #### Details
    - **url:** `${BASE_URL}/warehouse/v1/{id}/`
    - **method:** `GET`
    - **url params:**
      ```json
      {
        "id": "int"
      }
      ```
    - **response:**
      ```json
      {
          "error": false,
          "data": {
              "id": "int",
              "address": {
                  "id": "int",
                  "city": "string",
                  "state": "string",
                  "country": "string",
                  "address": "string",
                  "pincode": "string",
                  "mobile": "string",
                  "latitude": "string",
                  "longitude": "string"
              },
              "created": "string",
              "modified": "string",
              "is_active": true,
              "is_deleted": false,
              "name": "string"
          }
      }
      ```
    - **example curl:**
      ```sh
      curl --location --request GET 'http://localhost:8000/warehouse/v1/1/'
      ```
      
  - #### List
    - **url:** `${BASE_URL}/warehouse/v1/list/`
    - **method:** `GET`
    - **response:**
    ```json
    {
        "error": false,
        "data": [
            {
                "id": "int",
                "address": {
                    "id": "int",
                    "city": "string",
                    "state": "string",
                    "country": "string",
                    "address": "string",
                    "pincode": "string",
                    "mobile": "string",
                    "latitude": "string",
                    "longitude": "string"
                },
                "created": "string",
                "modified": "string",
                "is_active": true,
                "is_deleted": false,
                "name": "string"
            }
        ]
    }
    ```
    - **example curl:**
    ```sh
    curl --location --request GET 'http://localhost:8000/warehouse/v1/list/'
    ```
    
  - #### Update
    - **url:** `${BASE_URL}/warehouse/v1/{id}/`
    - **method:** `PATCH`
    - **url params:**
      ```json
      {
        "id": "int"
      }
      ```
    - **request:** (Example)
      ```json
      {
          "is_deleted": "boolean",
          "address": {
              "pincode": "string"
          }
      }
      ```
    - **response:**
      ```json
      {
          "error": false,
          "data": 
            {
              "id": "int",
              "address": {
                  "id": "int",
                  "city": "string",
                  "state": "string",
                  "country": "string",
                  "address": "string",
                  "pincode": "string",
                  "mobile": "string",
                  "latitude": "string",
                  "longitude": "string"
              },
              "created": "string",
              "modified": "string",
              "is_active": true,
              "is_deleted": false,
              "name": "string"
          }
      }
      ```
    - **example curl:**
      ```sh
      curl --location --request PATCH 'http://localhost:8000/warehouse/v1/1/' \
      --header 'Content-Type: application/json' \
      --data-raw '{
          "is_deleted": false,
          "address": {
              "pincode": "226010"
          }
      }'
      ```
      
  - #### Delete
    - **url:** `${BASE_URL}/warehouse/v1/{id}/`
    - **method:** `DELETE`
    - **url params:**
      ```json
      {
        "id": "int"
      }
      ```
    - **response:**
      ```json
      {
          "error": false,
          "message": "Warehouse deleted successfully"
      }
      ```
    - **example curl:**
      ```sh
      curl --location --request DELETE 'http://localhost:8000/warehouse/v1/1/delete/'
      ```
      
### Item API
 **Note:** Please ensure you pass `id` for `warehouse` in warehouse. One can create them using the above provided API.
 
 **Note:** Please ensure you pass `id` for `category` in category. One can create them using the admin panel.
 
  - #### Create:
    - **url:** `${BASE_URL}/item/v1/create/`
    - **method:** `POST`
    - **data:**
      ```json
      {
          "name": "string",
          "description": "string",
          "brand": "string",
          "price": "decimal",
          "category": "int",
          "quantity": "int",
          "warehouse": "int"
      }
      ```
    - **response:**
      ```json
      {
          "error": false,
          "data": {
              "id": "int",
              "category": {
                  "id": "int",
                  "is_active": "boolean",
                  "name": "string",
                  "slug": "string"
              },
              "warehouse": {
                  "id": "int",
                  "address": {
                      "id": "int",
                      "address": "string",
                      "pincode": "string",
                      "mobile": "string",
                      "latitude": "string",
                      "longitude": "string",
                      "country": "string",
                      "state": "string",
                      "city": "string"
                  },
                  "created": "string",
                  "modified": "string",
                  "is_active": "boolean",
                  "is_deleted": "boolean",
                  "name": "string"
              },
              "created": "string",
              "modified": "string",
              "is_active": true,
              "is_deleted": false,
              "name": "string",
              "image": "string",
              "description": "string",
              "brand": "string",
              "price": "string",
              "quantity": "int"
          }
      }
      ```
    - **example curl:**
      ```sh
      curl --location --request POST 'http://localhost:8000/item/v1/create/' \
      --header 'Content-Type: application/json' \
      --data-raw '{
          "name": "test item",
          "description": "test description",
          "brand": "test brand",
          "price": "100.50",
          "category": 1,
          "quantity": 10,
          "warehouse": 5
      }'
      ```
      
  - #### Details
    - **url:** `${BASE_URL}/item/v1/{id}/`
    - **method:** `GET`
    - **url params:**
      ```json
      {
        "id": "int"
      }
      ```
    - **response:**
      ```json
      {
          "error": false,
          "data": {
              "id": "int",
              "category": {
                  "id": "int",
                  "is_active": "boolean",
                  "name": "string",
                  "slug": "string"
              },
              "warehouse": {
                  "id": "int",
                  "address": {
                      "id": "int",
                      "address": "string",
                      "pincode": "string",
                      "mobile": "string",
                      "latitude": "string",
                      "longitude": "string",
                      "country": "string",
                      "state": "string",
                      "city": "string"
                  },
                  "created": "string",
                  "modified": "string",
                  "is_active": "boolean",
                  "is_deleted": "boolean",
                  "name": "string"
              },
              "created": "string",
              "modified": "string",
              "is_active": true,
              "is_deleted": false,
              "name": "string",
              "image": "string",
              "description": "string",
              "brand": "string",
              "price": "string",
              "quantity": "int"
          }
      }
      ```
    - **example curl:**
      ```sh
      curl --location --request GET 'http://localhost:8000/item/v1/1/'
      ```
      
  - #### List
    - **url:** `${BASE_URL}/item/v1/list/`
    - **method:** `GET`
    - **response:**
    ```json
    {
        "error": false,
        "data": [
            {
                "id": "int",
                "category": {
                    "id": "int",
                    "is_active": "boolean",
                    "name": "string",
                    "slug": "string"
                },
                "warehouse": {
                    "id": "int",
                    "address": {
                        "id": "int",
                        "address": "string",
                        "pincode": "string",
                        "mobile": "string",
                        "latitude": "string",
                        "longitude": "string",
                        "country": "string",
                        "state": "string",
                        "city": "string"
                    },
                    "created": "string",
                    "modified": "string",
                    "is_active": "boolean",
                    "is_deleted": "boolean",
                    "name": "string"
                },
                "created": "string",
                "modified": "string",
                "is_active": true,
                "is_deleted": false,
                "name": "string",
                "image": "string",
                "description": "string",
                "brand": "string",
                "price": "string",
                "quantity": "int"
            }
        ]
    }
    ```
    - **example curl:**
    ```sh
    curl --location --request GET 'http://localhost:8000/item/v1/list/'
    ```
    
  - #### Update
    - **url:** `${BASE_URL}/item/v1/{id}/`
    - **method:** `PATCH`
    - **url params:**
      ```json
      {
        "id": "int"
      }
      ```
    - **request:** (Example)
      ```json
      {
          "is_deleted": "boolean",
      }
      ```
    - **response:**
      ```json
      {
          "error": false,
          "data": 
            {
              "id": "int",
              "category": {
                  "id": "int",
                  "is_active": "boolean",
                  "name": "string",
                  "slug": "string"
              },
              "warehouse": {
                  "id": "int",
                  "address": {
                      "id": "int",
                      "address": "string",
                      "pincode": "string",
                      "mobile": "string",
                      "latitude": "string",
                      "longitude": "string",
                      "country": "string",
                      "state": "string",
                      "city": "string"
                  },
                  "created": "string",
                  "modified": "string",
                  "is_active": "boolean",
                  "is_deleted": "boolean",
                  "name": "string"
              },
              "created": "string",
              "modified": "string",
              "is_active": true,
              "is_deleted": false,
              "name": "string",
              "image": "string",
              "description": "string",
              "brand": "string",
              "price": "string",
              "quantity": "int"
          }
      }
      ```
    - **example curl:**
      ```sh
      curl --location --request PATCH 'http://localhost:8000/item/v1/1/' \
      --header 'Content-Type: application/json' \
      --data-raw '{
          "is_deleted": false
      }'
      ```
      
  - #### Delete
    - **url:** `${BASE_URL}/item/v1/{id}/`
    - **method:** `DELETE`
    - **url params:**
      ```json
      {
        "id": "int"
      }
      ```
    - **response:**
      ```json
      {
          "error": false,
          "message": "Item deleted successfully"
      }
      ```
    - **example curl:**
      ```sh
      curl --location --request DELETE 'http://localhost:8000/item/v1/1/delete/'
      ```

## How to use

1. Go to admin panel and log in. If using docker the default username and password is admin, admin.
2. Create Country, then State and then City.
3. Then create warehouse either using above mentioned APIs or using admin panel itself.
4. Then create item either using above mentioned APIs or using admin panel itself.
