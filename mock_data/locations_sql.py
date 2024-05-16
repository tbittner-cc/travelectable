import json
from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

# Create an engine that stores data in a local SQLite file
engine = create_engine('sqlite:///travel_data.db')

class USMetroArea(Base):
    __tablename__ = 'us_metro_areas'

    id = Column(Integer, primary_key=True)
    metro_area = Column(String)
    population = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    description = Column(String)
    points_of_interest = Column(String)

class USLocations(Base):
    __tablename__ = 'us_locations'

    id = Column(Integer, primary_key=True)
    location = Column(String)
    state = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    nearest_metro_area = Column(String)
    country = Column(String)
    description = Column(String)
    points_of_interest = Column(String)

class IntlDestinations(Base):
    __tablename__ = 'intl_destinations'

    id = Column(Integer, primary_key=True)
    location = Column(String)
    country = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    travel_advisory_level = Column(Enum('Exercise Normal Precautions', 
                                        'Exercise Increased Precautions', 
                                        'Reconsider Travel', 
                                        'Do Not Travel'))
    description = Column(String)
    points_of_interest = Column(String)

# Create all tables in the engine
Base.metadata.create_all(engine)

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

with open('us_cities.txt') as f:
    data = f.read()
    us_cities = json.loads(data)
for city in us_cities:
    session.add(USMetroArea(**city))

with open('us_dests.txt') as f:
    data = f.read()
    us_dests = json.loads(data)
for dest in us_dests:
    session.add(USLocations(**dest))

with open('intl_dests.txt') as f:
    data = f.read()
    intl_dests = json.loads(data)
for dest in intl_dests:
    session.add(IntlDestinations(**dest))

session.commit()
session.close()
