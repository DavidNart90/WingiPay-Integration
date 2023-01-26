# WingiPay Integration

Wingipay Merchant Api is an The APIs enable collection of funds either via mobile money or credit and debit cards. 

Requirements:

1. Api key - for this project the api key is hidden in the .env and included in .gitignore. Please contact personnel for api key
2. FUNDS COLLECTION URL: https://test.wingipay.com/web/checkout/add/ 

### Description
This project contain an HTML template that creates a form to collect the required information (name, email, country, and amount) and a submit button that makes a POST request to a Django view that will handle the Wingipay API request and generate a unique transaction reference for each customer.

The view handles a POST request from the above HTML form, makes a request to the Funds Collection URL, generates a unique transaction reference for each customer, and returns the redirect URL.
