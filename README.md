# ScraperProject
###### Scrap 500 apartments from reality.cz and display it

# Project Description:
    
The project is all about building a powerful yet simple data-gathering and presentation system. It's designed to fetch valuable real estate information from sreality.cz, one of the Czech Republic's top real estate websites. We're specifically interested in the first 500 items under the "flats for sale" category. Using the Scrapy framework, we scrape these ads, capturing their titles and image URLs.

The collected data is stored in a PostgreSQL database, which helps organize and manage the information efficiently. To make this data accessible and user-friendly, we use Flask and psycopg2 to create a lightweight HTTP server. This server showcases the 500 listings on a straightforward web page, displaying their titles and images. It's all wrapped up neatly in a Docker container, ensuring an easy setup and a seamless way to see the scraped ads. This project streamlines the process of collecting and viewing real estate data, making it a breeze to stay updated with the latest listings.


# How to use:

## Running via Docker
    a) Docker version used is 24.0.6 (ensure compatible docker version)
    
    b) Virtualization is enabled via BIOS/UEFI (For cross-checking, go to Task Manager>Performance>CPU>Virtualisation)
    
    C) Got to the directory (../ScraperProject) and enter the command "docker compose up"
    
    d) Access the scraped ads on http://127.0.0.1:8080
    

## Database PostgreSQL


        System: PostgreSQL
    
        Server: db_task
    
        Username: affan
    
        Password: 2023
    
        Database: sreality_apartments_db
    
    
    

