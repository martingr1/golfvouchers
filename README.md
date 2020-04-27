
[![Build Status](https://travis-ci.org/martingr1/golfvouchers.svg?branch=master)](https://travis-ci.org/martingr1/golfvouchers)

![Banner](/static/media/img/gv_banner.jpg "Banner")

GolfVouchers
====== 

This application (app) has been designed and coded for the 'Full Stack Frameworks' milestone project in the Full Stack Developer course at the Code Institute.

The app is an ecommerce website for golfers to find deals on new golf equipment, reducing the cost of playing the sport.

Deployment
======

To run the live app hosted on Heroku, please go [here](https://golfvouchers.herokuapp.com/) .

This project was written in Gitpod IDE, using Python, Django, CSS, HTML and Javascript.

Payments are handled via stripe API.

All images are hosted in a specific AWS Bucket created for the project.

To log into the app please click the 'Hello! Sign In' link in the nav bar at the top of the page, and click on the register button. 

You can then create a new account with your email address. A confirmation email will be sent to your registered email confirming successful registration.

Please note, email addresses and usernames must be unique.

You will then be able to log in to the site and make purchases.

Please use the following test card details for purchases:

- Card number: 4242424242424242
- Expiry Month: 4
- Expiry Year: 2022 (Any future date will work)
- CVV: 111 (Any 3 digit number will work)

Code is stored in my github repository [here](https://github.com/martingr1/golfvouchers) .

Project Criteria
=====

The below criteria were set out by Code Institute as an example project outline to follow.

### Project purpose
In this project, you'll build a full-stack site based around business logic used to control a centrally-owned dataset. You will set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.

### Value Provided:

By authenticating on the site and paying for some of its services, users can advance their own goals. Before authenticating, the site makes it clear how those goals would be furthered by the site.

The site owner is able to make money by providing this set of services to the users. There is no way for a regular user to bypass the site's mechanisms and derive all of the value available to paid users without paying.

Project Design
=====

## Database and Data Model

The project criteria specified that PostgreSQL be used as the database for the project.

Database model can be found [here](/static/media/img/gv_db.pdf )

## Back End

The back end was developed using Django 1.11.28 and Python.

## Front end and UX 

Ux Wireframes can be found [here](/static/media/img/gv_ux.pdf )

My main design philosophies were:

1. Simple, clear display for products and related information.
2. Mobile first.
3. Blue, White, Green colour scheme.
4. Help users purchase single or multiple products as easily as possible.

## User stories 

There are two main user stories for this project.

## User

As a customer and user of the site I want to be able to register/sign in easily, find products I want to buy and make a purchase.

## Site owner

As the owner of the site, I want to be able to make money from products listed on the site.

Project Features and Apps
=====

## Login, Authentication, Registration

In order to access the site, users must first register and then login. 

This is done via the navigation bar, where the user has the option to sign in if not currently signed in.

If the user tries to login with invalid credentials, they will be sent a message and redirected to the login page.

Login and registration forms are required fields. If a user attempts to leave any fields blank they will be shown a message on the front end to prevent submission.

## Password reset

Uses can reset their password by clicking on the reset password link on the login or registration page and follwoing the instructions provided.

## Posts (Product)

On the main page, users can see a display of all products in the database. To avoid congestion, all results are limited to 12 results per page. There is pagination at the bottom of the screen so that the user can navigate through results.

A variation of a Post model was used for products to allow Admins to easily post new products to the database via the admin panel. This is only visible by admin users.

## Search and Filter

To find products, users can easily search using the search bar at the top of the page. 

Users can also filter results via the filters above the search results.

Users can click on the product title or image to navigate to the individual product page. Once there, they can add a quantity of items to the cart. The cart icon at the top of the page will show the value of items in the shopping cart for that session.

## Cart and Checkout

Users can click on the shopping cart in the navbar to view it.

Once there they can amend the items in the cart and click the button to amend the quantity.

If the cart is empty a message will be displayed to the user and the payment button will disappear.

If the user clicks the payment button they will be taken to the payment screen where they can complete their transaction and recieve a confirmation email.

Project Testing
=====

## Automated Tests

15 automated tests were created to cover the following topics:

1. Accounts - Views, Forms
2. Cart - Views
3. Checkout - Views
4. Posts - Views

These tests can be found in the respective code folders in the github repository.

## Manual Tests

Manual testing was conducted to check cart functionality, inventory management, payments and error messages.

The testing document can be found [here](/static/media/img/gv_tests.pdf) .


Technologies
=====

The app was developed with the following technologies:

1. Django 1.11.28
2. Python 3.7
3. PostgreSQL
4. Javascript / jQuery
5. Bootstrap 4
6. HTML
7. CSS
8. Stripe

Acknowledgements 
=====





Future Features
=====

As the site grows, it will be necessary to implement some new features not included in the scope of this project.

The list below is not exhaustive and will be added to over time in order to keep the site viable.

1. Build out customer profile pages for order tracking and payment details.
2. Order management system.
