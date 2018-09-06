# Stock Portfolio API
 **Authors**: Ben Hurst
 **Version**: 1.0.0
 ## Overview
 Simple Stocks API using Pyramid Restful Framework
 ## Getting Started
    1) Clone or fork repo from github.
    2) In a separate terminal instance, run 'psql' to get into the psql shell
    3) Run ```create database stocks_api;``` and then ```\c stocks_api```
    4) Back in the main terminal instance, run ```initialize_stocks_api_db development.ini``` to setup the database
    5) Run ```pserve development.ini --reload``` in the terminal to spin up the server.
    6) Using the http client of your choice (I reccomend Postman), you can hit the server with various requests (refer to API section below). I recommend going through in the order listed.
    7) To test the data visualization GET route, I suggest using chrome to see the fully rendered html response.

 ## Architecture
Python 3.7, Pyramid Resftul Framework, Pytest
GitHub
 ## API


- **GET** / - the base API route

The following routes return a token:
- **POST** /api/v1/auth/register/ - for registering a new account or logging in, with the post body in the form: {"email": "bennyboy09823745@gmail.com", "password": "seeeekret"}
- **POST** /api/v1/auth/login/ - for registering a new account or logging in, with the post body in the form: {"email": "bennyboy09823745@gmail.com", "password": "seeeekret"}

The following routes require the token to be set as Bearer Token
- **POST** /api/v1/portfolio/ - for creating a user's portfolio associated with their account, with post body in the form: `{"name": "My Portfolio"}`.

- **POST** /api/v1/stock/ - for creating a new company record associated with a specified portfolio, with post body in the form: `{"symbol": "aapl"}`
- **GET** /api/v1/portfolio/{id}/ - for retrieving a user's portfolio. Here `{id}` is the corresponding account id
- **GET** /api/v1/stock/{id}/ - for retrieving a companies information. Here `{id}` is the corresponding portfolio id
- **DELETE** /api/v1/stock/{id} - for deleting a company record

The following route does not require a bearer token:
- **GET** /api/v1/company/{symbol}/ - for retrieving company detail from 3rd party API, where `{symbol}` is variable
- **GET** /api/v1/visuals/{symbol}/ - for plotting candelstick visualization of time series stock data, where `{symbol}` is variable


 ## Change Log
 08-22-2018 20:50 Basic Functionality Done

 08-23-2018 07:30 Added more routes

 08-27-2018 20:30 Added SQLAlchemy database models/schemata. Awaiting further guidance to incorporate into routes.

 08-27-2018 21:50 Incorporated 3rd-party API called IEX. You can retrieve stock info by hitting /api/v1/company/{symbol}/

 08-28-2018 22:50 Added model relationships to the database as reflected in the API routes above

 08-29-2018 16:50 Added authentication functionality. Reference API section above.

 09-05-2018 16:50 Added data visualization route. Reference API section above.


 ## License
This project is licensed under the MIT license
