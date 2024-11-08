# FoodSquare
## What Problems Does It Solve:
With growing number of restaurants in Dhaka city, it has become very much indispensable part for the restaurants to have an website where they can not only manage their business but also advertise their products. And Covid-19 has just shown how much necessary it is to have an online presence even for a small organization. 


But it's not easy for all restaurants to build and manage their websites themselves. That's where FoodSquare comes into the picture. 


It gives restaurants a platform to manage their own restaurants and put their products on display. On the other hand, food-lovers get the opportunity to browse food items as per their taste and budget from hundreds of restaurants. 


## About This Repository:
This repo contains the web app for this system implemented in Django-2.2 with Model-View-Template design pattern. This was an Information System Design project, part of an academic course of CSE, BUET. So some of the best practices of system design could not be maintained properly.
  
**Spec:**
  - Web Framework: Django 2.2
  - Database Server: PostgreSQL 12.3
  
**How to run:**
 - Clone the [github repo](https://github.com/vishwajittidke/Foodsquare-Web-App)
 - Now you can either run in [docker containers](https://www.docker.com/) of a [pre-built image on docker hub](https://hub.docker.com/r/vishwajittidke/foodsquare) of this repo **or** create an python & database environment yourself
    - **Docker**
        - install [docker](https://docs.docker.com/engine/install/) & [docker-compose](https://docs.docker.com/compose/install/) on your system (if not installed)
        - move to the project directory & start the docker containers using the following commands
        ```shell
        docker-compose build
        docker-compose up
        ```
        - now browse the site at http://localhost:8000/ 
        - **N.B.** Here [remote docker image](https://hub.docker.com/repository/docker/vishwajittidke/foodsquare/general) is used in docker compose. Alternately, you can build a new docker image using `Dockerfile` & use it in composer.

    - Or, **Python Environment/Database setup**
        - install postgres database
        - create a new database in your postgres server named `foodsquare` with owner as `postgres`, password as  `postgres`   
        - start the postgres server on port 5432 
        - move to the project directory 
        - create a virtual environment & activate it
        ```shell
        python3 -m pip install --upgrade pip
        python3 -m venv venv
        source venv/bin/activate
        ```
        - install dependencies & make migrations
        ```shell
        python3 -m pip install -r requirements.txt
        python3 manage.py makemigrations
        python3 manage.py migrate
        ```
        - now run the server finally
        ```shell
        python3 manage.py runserver
        ```
        - now browse the site at http://localhost:8000/ 
        - **N.B.** a facebook login app needs to be set up & its credentials are to be addded into database properly to access login pages.  
          For ease, an app is created & its credentials are provided into a dumped json file which can be loaded into the database using:
        ```shell
        python3 manage.py loaddata data.json
        ```
 - **N.B.** Facebook/Google login may not work properly as those login apps credentials might be outdated now.          
          
          
**Some Basic Functionalities Implemented:**
- User Session Handling
- Third Party Authentication
- Sub-domain Handling
- Shopping Cart Management
- Local Storage Handling
- Online Payment Handling
- Review-Rating Management

Docker Hub Repo: https://hub.docker.com/r/vishwajittidke/foodsquare

***

## Sample Usage:
***Homepage*** ![website_homepage (2)](https://github.com/user-attachments/assets/f7d62664-3b7b-4789-a91e-fb0e66d5f514)


***Browse Cuisines***
![Browse Cuisines](https://github.com/user-attachments/assets/a522dee5-e424-4564-b3bd-fcc5e38fff5e)

***Payment***

<img src="https://raw.githubusercontent.com/Subangkar/Foodsquare-Web-App/master/Foodsquare_Screenshots/bkash.png?token=AHSCFFTSZANDZAQZ5BJ6GUC7HAN5G" alt="Payment" width="500" height="400"/>

***Branch Open***
![Branch Open](https://raw.githubusercontent.com/Subangkar/Foodsquare-Web-App/master/Foodsquare_Screenshots/rest_branch_reg.png?token=AHSCFFSFY4IOR3WV7VFXAJ27HALL4)
***Add Items***
![Add Items](https://raw.githubusercontent.com/Subangkar/Foodsquare-Web-App/master/Foodsquare_Screenshots/additem.png?token=AHSCFFQ2SC7HM7GV5FJBBEC7HALMK)



***Manage and Accept Orders***
![Manage and Accept Orders](https://raw.githubusercontent.com/Subangkar/Foodsquare-Web-App/master/Foodsquare_Screenshots/accept_branch.png?token=AHSCFFUV6AGWFLXQIMFCX427HAMPG)


