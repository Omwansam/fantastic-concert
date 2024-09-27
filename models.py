from sqlalchemy import Column,Integer,String,ForeignKey
from concertbase import session
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Concert(Base):
  __tablename__= 'concerts'

 
  id = Column(Integer,primary_key=True)
  band_id = Column(Integer,ForeignKey('bands.id'))
  venue_id = Column(Integer,ForeignKey('venues.id'))
  date = Column(String)


  band = relationship("Band",back_populates="concerts")
  venue = relationship("Venue",back_populates="concerts")

  def hometown_show(self):
    return self.venue.city == self.band.hometown
  
  def introduction(self):
    return f"Hello {self.venue.city}!!! We are {self.band.name} and we're from {self.band.hometown}"
  
class Band(Base):
    __tablename__= 'bands'
    id = Column(Integer, primary_key=True)
   
    name = Column(String)
   
    hometown = Column(String)
    #Relationship to concerts, back_populates allows us to access concerts from band
    concerts = relationship("Concert", back_populates='band')

 #This function is for adding a new concert to the band's concerts table
    def play_in_venue(self, venue, date):
        new_concert = Concert(band=self, venue=venue, date=date)
        session.add(new_concert)#Adding a new concert
        session.commit()

   #This funtion is for gettin a list of introduction messages for all concerts
    def all_introductions(self):  
        return [concert.introduction() for concert in self.concerts]
    
    #This function returns a list of all venues the band has played in
    def venues(self):
        return [concert.venue for concert in self.concerts]
    
    @classmethod
   
    def most_performances(cls):
        return max(session.query(cls).all(), key=lambda b: len(b.concerts))

class Venue(Base):
   __tablename__ = 'venues'

   id = Column(Integer,primary_key=True)
   name = Column(String)
   city = Column(String)

   #Relationship to concerts, back_populates allows us to access concerts from venue
   concerts = relationship("Concert",back_populates="venue")

   def concert_on(self,date):
      return next((concert for concert in self.concerts if concert.date == date),None)
   
   def most_frequent_band(self):
      band_count={}
      for concert in self.concerts:
        
         band_count[concert.band] = band_count.get(concert.band,0) + 1
      return max(band_count,key=band_count.get)