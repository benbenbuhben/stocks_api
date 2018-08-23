# Stock Portfolio API
 **Authors**: Ben Hurst
 **Version**: 1.0.0
 ## Overview
 Simple Stocks API using Pyramid Restful Framework
 ## Getting Started
    1) Clone or fork repo from github.
    2) Run ```pserve development.ini --reload``` in the terminal to spin up the server.
    3) Using the http client of your choice (I reccomend Postman), you can hit the server with various requests (refer to API section below)

 ## Architecture
Python 3.7, Pyramid Resftul Framework, Pytest
GitHub
 ## API
- [x] GET / - the base API route
- [x] POST /api/v1/auth/ - for registering a new account and signing up
- [x] GET /api/v1/portfolio/{id}/ - for retrieving a user's portfolio
- [x] POST /api/v1/stock/ - for creating a new company record
- [ ] GET /api/v1/stock/{id}/ - for retrieving a companies information
- [ ] DELETE /api/v1/stock/{id} - for deleting a company record
- [ ] GET /api/v1/company/{symbol} - for retrieving company detail from 3rd party API, where `{symbol}` is variable
 ## Change Log
 08-22-2018 20:50 Basic Functionality Done

 08-23-2018 07:30 Added more routes
 ## License
This project is licensed under the MIT license
