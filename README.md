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
    2) Run ```pserve development.ini --reload``` in the terminal to spin up the server.
    3) Using the http client of your choice (I reccomend Postman), you can hit the server with various requests (refer to API section below). I recommend going through in the order listed.

 ## Architecture
Python 3.7, Pyramid Resftul Framework, Pytest
GitHub
 ## API

- [x] GET / - the base API route
- [x] POST /api/v1/auth/register/ - for registering a new account or logging in, with the post body in the form: {"email": "bennyboy129802931@gmail.com", "password": "seeeekret"}
- [x] POST /api/v1/portfolio/{id}/ - for creating a user's portfolio associated with their account, with post body in the form: {"name": "My Portfolio"}. NOTE: {id} is the account_id and will likely be 1 the first time
- [x] POST /api/v1/stock/ - for creating a new company record associated with a specified portfolio, with post body in the form: {"symbol": "aapl", "portfolio_id": 1}
- [x] GET /api/v1/portfolio/{id}/ - for retrieving a user's portfolio
- [x] GET /api/v1/stock/{id}/ - for retrieving a companies information
- [x] DELETE /api/v1/stock/{id} - for deleting a company record
- [x] GET /api/v1/company/{symbol} - for retrieving company detail from 3rd party API, where `{symbol}` is variable

 ## Change Log
 08-22-2018 20:50 Basic Functionality Done

 08-23-2018 07:30 Added more routes

 08-27-2018 20:30 Added SQLAlchemy database models/schemata. Awaiting further guidance to incorporate into routes.

 08-27-2018 21:50 Incorporated 3rd-party API called IEX. You can retrieve stock info by hitting /api/v1/company/{symbol}/

 08-28-2018 22:50 Added model relationships to the database as reflected in the API routes above

 ## License
This project is licensed under the MIT license
