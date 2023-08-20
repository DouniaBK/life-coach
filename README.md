The life coach app is designed and dedicated for female cancer patients wanting to hire the services of a life coach/therapist to overcome the anxiety and stress that comes with chemotherapy and the hardship that comes along. The site is designed with calming feminine esthetic and intuitive workflow to not overwhelm the patient/user seeking the help they need. The patients are able to read through the resources and the different services available to them and then register to book a session with the life coach. The life coach on the other hand, being the admin, is able to see who and when a session is booked, as well as have the patients’ information at hand. The admin has also control over their image by publishing  carefully selected testimonials on their site. As of control, the patient is also equipped with CRUD functionality to manage their account and booked sessions. 

# Table of Contents
## Goals
* Target user and site owner
* Visual Design

## Features
* Page Elements
* Additional Features
* Features Not Yet Implemented
## Information Architecture
* Database Structure
* Data Models
## Technologies Used
* Languages
* Libraries
* Packages
* Platforms
* Other Tools
## Testing
* Automated Testing
* Manual Testing
* Bugs
## Deployment
* Local Deployment
* Heroku Deployment
## Credit and Developer's story
* Code
* Developer

# Goals:
### User:
The site is designed for cancer patients seeking the help of a therapist to guide them through the emotional rollercoaster of cancer treatments. The goal is to help them navigate the site with ease to get to know what the therapist's approach, techniques and services are in order to book a session and sign up for a therapy treatment.

### Site owner:
The therapist/life coach needs a landing page to inform the patients of the different techniques and services available to them to improve their life journey through these tough times. The admin part is meant to ease the process of patient management such as the sessions schedule and the billing information.

### Site Design:

This particular site is solely dedicated to women diagnosed with cancer and undergoing cancer treatment and thus the design has a feminine touch with calming pastel colours inspired by a Santa Monica pink sunset. Intended as a healing meditative space which takes the anxiety of seeking yet another medical assistance away from the patient. The header also features a carousel with inspirational quotes to encourage the cancer patients to seek help and regain their strength as well as set a meditative and empowering mood creating an emotional connection between the user and the coach. The site also features a divider image quoting self-care to remind the user that self-care is essential to self preservation. 

The site has a minimal aesthetic and colour palette to avoid sensory overstimulation often as a result of chimotherapy as well as offers an intuitive workflow leading to booking a session and start a journey of soul healing. Furtheremore, as the site contains key information about the therapy packages, familiar colors, fonts, images, and other elements have been used throughout as signals to reflect the site's organization and let the user’s brain know when to pay attention.

### Color Palette:
### Fonts:

# Features:
## Home page:
The first page welcomes the user into a simple and serene site of a life coach that offers different services and information to help female cancer patients. The site has a simple navbar that redirects the user to the Coaching Services, Free Resouces, Coaching Sessions, the login/register/Profile feature and back to the Home page. Once logged in or registered the navbar expands adding the coaching sessions section, where the user can book sessions with the therapist, and the profile section, where the user can edit or delete their account to protect their privacy. Furthermore the page is divided into 3 main section, an about the Coach section featuring a personal introduction of the coaches, a brief introduction of the coaching packages the coach offers including a button, get started, which prompts the user to register and account and eventually book a first free session with the coach using the booking calendar. Also, a testimonial section managed by the admin allowing the site owner or an assistant to publish a testimonial or update the current ones. The testimonial section allows only three testimonials to be published as the number three mimics the three steps to a happy and balanced life that is often mentioned in the hypnotherapy session offred by the coach. At the bottom of the site, a minimal footer is placed with all the social media links needed to get to know the coach better.
## Coaching services:
This part is featured twice on the site, once with brief information on the home page and again accessible from the navbar with more detailed information about the number of sessions, the duration, price and techniques used  allowing the user to delve in and find the most suitable package. This section includes a button that will redirect the user to registering or logging in and then select a service and eventually book a session at a suitable time and also cancel it in case of a change of plan.

## Coaching resources:
This page is intended to simply give more information about the free resouces avalaible to them at the clinic and during the therapy sessions. As the goal is to inform, the esthetic is clean, minimal, light and familiar to help the user's brain focus and pay attention. 
 
## Coaching sessions:
This page is accessible from the navbar once registered or logged in as well as from the coaching sections and the home page for non registered users. This section allowed the user to select a service and then book a sessions  with the coach with a handy Calendar that shows which days and time are still available in white and the sessions that are not available greyed out as well as the sessions selected by that particular user in blue. Once the user selects an appropriate time and a service and submits it that session then appears in their personal list of sessions which in turn can be cancelled. To sum up, the user selects a service from the drop-down list then an available session on the calendar, clicks submit and that session will then appear as booked by them on the calendar in a light blue colour as well as on the my sessions section. The coach/admin will then personally review their schedule and the user’s profile information on the admin panel to contact the user if needed. 

## Accounts:

A site user has to register in order to be able to book a session and edit their profile. The user can login, logout and access their profile through the right end section of the navbar, login and drop down menu list profile and logout. These account features have been implemented to give the necessary information to the admin/coach for billing purposes, client and time management. However, the account can also be deleted giving the user the right of privacy. 


## Testimonials:
The ancient Greek philosopher, Pythagoras, postulated that the number 3 was considered as the perfect number, the number of harmony, wisdom and understanding which is often used in hypnotherapy, neurolinguistics and wralm of psychology and thus the Testimonials section features only three testimonials to foster esthetic balance and harmony of the site and not overwhelm the user risking losing them as patients. The admin can update, delete, publish or choose to keep some testimonials saved as drafts for later. This site section is minimal, responsive and centred containing the author of the testimonial and the body of the testimonial. The therapist is then in control of the image they want to portray to other/future patients.

## Account management
The admin Panel contains three main sections:
### Custom User:
The patients that register are saved and displayed in the panel with the status of active or not and staff or not. The super user has then all the permission and can also grant permissions to the users for example if another user such as an assistant can be given permission to maintain the site and manage the clients sessions and accounts.

### User Profile
The custom user information section combined with the registration form display the First Name, Last Name, Address, Email address of the user that can be changed using the CRUD functionality available to the user on the home page

### Coaching Sessions:
Displaying the user information, the time and date of the session chosen by the user. These sessions can be cancelled by the user, from the site once logged in, if they chose to.

### Testimonials:
Displaying the name, body and status of the testimonials published will publish it on the site and draft will save it but not publish it. The testimonials are solely managed by and through the admin panel.

## Features Not Yet Implemented:
### Post Content;
The admin ability to post articles, meditation guides, journals and workbooks. 

# Information Architecture
## Database Structure



## Data Models
* Custom User:
* Testimonials:
* Booking:
* Profile:

## Technologies Used
### Languages

* Logic:
    - Python

* Template:
    - HTML
    - CSS
    - Bootstrap

* Database:
    - Structured Query Language

### Libraries
    1. dj_database_url==0.5.0 psycopg2
    2. os library
    3. Cloudinary


# Testing
## Automated Testing:
### why use Automated Unit Testing?
Automated testing was used for a more efficient, and more consistent process to leave no room for human error. The process started with identifying test cases to automate, especially repetitive, critical, and time-consuming tests with the goal to test how robust the code's functionality, performance, and reliability is. Furthermore, these test were executed repeatedly to identify defects and ensure the site's quality and stability, thus eliminating human error.

### The features tested with automated unit testing are:
    Login feature
    Booking sessions

 
##  Manual Testing:

### Why Use Manual Testing?
Manual testing was choosen to evaluate the application from the end user’s perspective using human intuition, providing a more genuine and human feedback.

### The features tested manualy are:

1. User registration: Enter the required information such as name, email address, password, and address. Click register. 
2. Account management: Test if the user can edit their profile information, view their newly edited saved profile.
3. Accessibility: Test if the website's features and functions are accessible to users with disabilities, such as screen readers or keyboard-only users.
4. Booking process: Select an available session, submit the session to finish the process. Verify that the sessions has been successfully booked and then the user cancels the previously booked session and see if the session has been cancels and is available for booking again and is no longer on the user's list of booked sessions.
5. Testimonials: Test if the testimonials are able to be updated/deleted or published/put to draft by the admin and that they are displayed properly to the user. 

## Bugs:

///////////////////////
## Deployment

* Local Deployment

    1. Install Django and supporting libraries mentioned above, create a requirements file, a project and an app, save, migrate and runserver using the command "python3 manage.py runserver".

* Heroku Deployment:

    1. Create an external database:
        Create an ElephantSQL account and instance and then set up the plan and the instance as instructed and finaly add the ElephantSQL database URL to Heroku.
    2. Create the Heroku app
        Create the app, add the Config Vars then attach the database .
    3. Prepare environment and settings.py file:
        Create new env.py file, import os library, set environment variables including the secret key, add the links to the DATATBASE_URL variable on Heroku and finally add Heroku Hostname to ALLOWED_HOSTS and deploy through Heroku.

## Credit
* Code






