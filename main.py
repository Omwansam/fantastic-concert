from concertbase import session
from models import Band, Venue, Concert


def add_concert(band_name, hometown, venue_name, city, concert_date):
    # Check if the band already exists
    band = session.query(Band).filter_by(name=band_name, hometown=hometown).first()
    if not band:
        band = Band(name=band_name, hometown=hometown)
        session.add(band)
        session.flush()  # Ensure the band is visible in the session
    
    # Check if the venue already exists
    venue = session.query(Venue).filter_by(name=venue_name, city=city).first()
    if not venue:
        venue = Venue(name=venue_name, city=city)
        session.add(venue)
        session.flush()  # Ensure the venue is visible in the session
    
    # Check if the concert already exists
    concert = session.query(Concert).filter_by(band=band, venue=venue, date=concert_date).first()
    if not concert:
        concert = Concert(band=band, venue=venue, date=concert_date)
        session.add(concert)
    
    return concert



add_concert('Maroon 5', 'United Kingdom', 'Wembley Stadium', 'London', '2023-10-1')
add_concert('Chainsmokers', 'USA', 'Mercedes Stadium', 'Chicago', '2024-10-24')
session.commit()

print("Concerts added successfully.")

first_band = session.query(Band).first()
if first_band:
    print(first_band.venues())
    print(first_band.all_introductions())
    
    if first_band.concerts:
        print(first_band.concerts[0].introduction())
    else:
        print("No concerts found .")
else:
    print("No bands found in the database.")

