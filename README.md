
# Django API'S
1. User registration API.
2. Make Login API using JWT Authentication.
3. CRUD(Create, Read, Update and Delete) API of product
4. CRUD(Create, Read, Update and Delete) API for cart.



## Features

this project consist 3 Apps in it.
- 1st app is for user registration and login
- 2nd is for product management
- 3rd is for product cart management
- only aothorized user can accesss the cart


## Usage/Examples

to use Login API you have to send POST request to following URL'S
- http://serverurl/register/

    POST Request must consist 
    
        {
        username, 
        password
        }

    Resposce we get is in JSON format 
    
        {
        status, 
        access token, 
        refresh token
        }
- http://serverurl/login/

    POST Request must consist 
    
        {
        username, 
        password
        }

    Resposce we get is in JSON format 
    
        {
        status, 
        access token, 
        refresh token
        }

- http://serverurl/brand/

    GET Request required token in header and send responce in JSON format

        {
        registration_number 
        company_name
        }
    
    For adding brand, POST Request must consist

        {
        registration_number 
        company_name
        }
    
- http://serverurl/category/

    GET Request required token in header and send responce in JSON format

        {
        category_name
        }
    
    For adding category, POST Request must consist

        {
        category_name
        }
    
- http://serverurl/products/

    GET Request required token in header and send responce in JSON format

        {
        product_id
        product_name
        price
        brand_name
        category_name
        }
    
    for adding products, POST Request must consist

        {
        product_id
        product_name
        price
        brand_name(foreign key)
        category_name(foreign key)
        }

    for deleting products, DELETE Request must consist
        
        {
            product_id
        }
- http://serverurl/products/sort/<orderby>
        
    for sorting products it required 'orderby' field on wich we will perform sorting
        
        eg. 'http://serverurl/products/sort/price'

- http://serverurl/products/search/<search>

    for search products it required product name as a search field

        eg. http://serverurl/products/search/productNameXYZ

- http://serverurl/cart?username="pass_user_name"

    for adding data in cart it must required Token in header for authentication and following data in POST Request

        {
            username
            product_id
            quntity
        }

    GET Request required token in header and send responce in JSON format
        
        {
            username
            product_id
            quntity
        }

    for deleting product from cart username and product id is required in DELETE request
        
        {
            username
            product_id
        }
