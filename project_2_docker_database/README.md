# Project 2 - Docker Infrastructure

## Objective

Congratulations, you have been assigned as the lead engineer
to build our data analysts a website and dashboard to input and identify potential clients that are within 100km of our office.

The website would need to contain a way for our data analysts to:
1. Input clients location (coordinates or address)
2. Display a dashboard view of clients that are within 100km of our office (use the following coordinates for NASA's JPL [34.2013° N, 118.1714° W] )
3. Automatically assign a UUID, and provide a way to modify an existing client's location
4. Provide a downloadable report (.csv) of the full client list for audit purposes

## Methodology

After talking with your team on approach and having a proposal written up, you and your team settled on the following:

1. Create a Docker container to act as your serving layer
2. Have your website be created via the Pyramid framework
3. Have a database of your choice (MySQL or Postgres) to store client information
4. Create a Docker compose file to enable local testing, and ease-of-use to deploy to the web.

## Goal for this project

1. Be able to create a Docker container that packages itself as a full website - frontend, middleware, and backend
2. Create a database from scratch and allows for modification of said database
3. Query the database for data display
4. Introduction to full stack development
