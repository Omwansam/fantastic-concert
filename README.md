 #The concert app


The Concert App is a project designed to model a domain where Bands perform at different Venues, with Concerts representing the events that link these two entities together. The application uses SQLAlchemy as the ORM for managing database interactions and Alembic for handling migrations. The project is structured with models for Band, Venue, and Concert, which define their relationships and enable querying and data management.

To set up the project, you'll first need to clone the repository and create a Python virtual environment. After that, you can install the required dependencies listed in the requirements.txt file. Once everything is set up, you'll initialize Alembic for managing database migrations and apply the necessary migrations to set up the database tables. After this, you can run the main application to test and interact with the models.


Models
Band
name: Name of the band (String)
hometown: Hometown of the band (String)
Venue
title: Name of the venue (String)
city: City where the venue is located (String)
Concert
band_id: Foreign key referencing the band (Integer)
venue_id: Foreign key referencing the venue (Integer)
date: Date of the concert (String)
Available Methods
Band
concerts(): Returns all concerts played by the band.
venues(): Returns all venues where the band has performed.
play_in_venue(venue, date): Schedules a concert for the band at a specific venue on a given date.
all_introductions(): Returns all concert introductions for the band.
most_performances(): Class method that returns the band with the most concerts.
Venue
concerts(): Returns all concerts held at the venue.
bands(): Returns all bands that have performed at the venue.
concert_on(date): Finds the concert on a specific date at the venue.
most_frequent_band(): Returns the band that has performed the most at the venue.
Concert
band(): Returns the band for the concert.
venue(): Returns the venue for the concert.
hometown_show(): Returns True if the concert is in the band's hometown, False otherwise.
introduction(): Returns a string introduction for the band at the concert.
