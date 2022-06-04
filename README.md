# Inventory Mangement Backend

![Python Version](https://img.shields.io/badge/python-v3.8-brightgreen)
![Django Version](https://img.shields.io/badge/django-v3.2-brightgreen)
![DB](https://img.shields.io/badge/db-postgres-brightgreen)
![Docker](https://img.shields.io/badge/docker-yes-brightgreen)
![Swagger UI](https://img.shields.io/badge/swagger_ui-yes-brightgreen)
[![Deployment](https://img.shields.io/badge/deploy-replit-brightgreen)](https://replit.com/@harsh020/inventorymangement/)

A simple inventory management backend built using Django with CRUD APIs for Warehouse and Items.

Internal APIs include:
 - Country
 - State
 - City
 - Address

Find the low level design [here](https://github.com/harsh020/inventory_mangement/blob/master/design.md).

:exclamation:**Before deploying on replit please refer [how to use guide](#how-to-use) and [replit guide](#replit-deployment-usage) first.**:exclamation:

The application can be deployed on replit using [this link](https://replit.com/@harsh020/inventorymangement/). (Hint: You can also use the above replit badge to access)


## Content
1. [How to run](#how-to-run)
2. [E-R Diagram](#e-r-diagram)
3. [Swagger Open API Specification](#swagger-open-api-specifications)
4. [Admin Panel](#admin-panel)
5. [APIs](#apis)
    - [Warehouse API](#warehouse-api)
    - [Item API](#item-api)
6. [How to use](#how-to-use)
7. [Replit Deployment: Usage](#replit-deployment-usage)


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
If running locally, it is `http://localhost:8000`

## Swagger Open API Specifications
  - url: `${BASE_URL}/`

## Admin Panel
The admin panel is provided by Django itself.
  - url: `${BASE_URL}/admin/`

## APIs

:exclamation::exclamation: **Note: Please click on `Create`, `Details`, `List`, `Update` and `Delete` in both APIs to expand details.** :exclamation::exclamation:

### Warehouse API
 **Note:** Please ensure you pass `id` for `city`, `state` and `country` in address. One can create them using the admin panel.

  - <details><summary> Create (Click me for details!) </summary>
 
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
 </details>
      
  - <details><summary> Details </summary>
 
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
  </details>
      
  - <details><summary> List </summary>
 
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
  </details>
    
  - <details><summary> Update </summary>
 
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
  </details>
      
  - <details><summary> Delete </summary>
 
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
  </details>
      
### Item API
 **Note:** Please ensure you pass `id` for `warehouse` in warehouse. One can create them using the above provided API.
 
 **Note:** Please ensure you pass `id` for `category` in category. One can create them using the admin panel.
 
  - <details><summary> Create </summary>
 
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
  </details>
      
  - <details><summary> Details </summary>
 
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
  </details>
      
  - <details><summary> List </summary>
 
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
  </details>
    
  - <details><summary> Update </summary>
 
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
  </details>
      
  - <details><summary> Delete </summary>
 
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
  </details>

## How to use

1. Go to admin panel and log in. If using docker the default username and password is admin, admin.
2. Create Country, then State and then City.
3. Then create warehouse either using above mentioned APIs or using admin panel itself.
4. Then create item either using above mentioned APIs or using admin panel itself.

## Replit Deployment: Usage

:exclamation::exclamation: **Note: The postgres is deployed in heroku using the free version. So please take care of data limit.** :exclamation::exclamation:

- The project can be deployed using [https://replit.com/@harsh020/inventorymangement/](https://replit.com/@harsh020/inventorymangement/). In the landing page you will find the API speifications.
- Admin panel can be accessed by appending `/admin/` to the end of replit deployment url. The username and password are `admin` and `admin` respectively.
- A warehouse with `id=1` and and item with `id=1` are also created to use.
- The following dummy data has already been created for further use:
### Country
<table>
 <tr>
  <th>Id</th>
  <th>Name</th>
 </tr>
 
 <tr>
  <td>1</td>
  <td>India</td>
 </tr>
 
 <tr>
  <td>2</td>
  <td>United States</td>
 </tr>
 
 <tr>
  <td>3</td>
  <td>England</td>
 </tr>
 
 <tr>
  <td>4</td>
  <td>Germany</td>
 </tr>
</table>

### State
<table>
 <tr>
  <th>Id</th>
  <th>Name</th>
  <th>Country</th>
 </tr>
 
 <tr>
  <td>1</td>
  <td>Uttar Pradesh</td>
  <td>1</td>
 </tr>
 
 <tr>
  <td>2</td>
  <td>California</td>
  <td>2</td>
 </tr>
 
 <tr>
  <td>3</td>
  <td>Cambridge</td>
  <td>3</td>
 </tr>
 
 <tr>
  <td>4</td>
  <td>Berlin</td>
  <td>4</td>
 </tr>
</table>

### City
<table>
 <tr>
  <th>Id</th>
  <th>Name</th>
  <th>State</th>
 </tr>
 
 <tr>
  <td>1</td>
  <td>Lucknow</td>
  <td>1</td>
 </tr>
 
 <tr>
  <td>2</td>
  <td>San Francisco</td>
  <td>2</td>
 </tr>
 
 <tr>
  <td>3</td>
  <td>Duxford</td>
  <td>3</td>
 </tr>
 
 <tr>
  <td>4</td>
  <td>Berlin</td>
  <td>4</td>
 </tr>
</table>

### Category
<table>
 <tr>
  <th>Id</th>
  <th>Name</th>
 </tr>
 
 <tr>
  <td>1</td>
  <td>Electronic</td>
 </tr>
 
 <tr>
  <td>2</td>
  <td>Clothing</td>
 </tr>
 
</table>
