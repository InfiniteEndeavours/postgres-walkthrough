from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


class HolidayDestination(base):
    __tablename__ = " HolidayDestination"
    id = Column(Integer, primary_key=True)
    city = Column(String)
    country = Column(String)
    population = Column(Integer)


# Instead of connecting to the database directly, we will ask for a session
# Create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# Opens an actual session by calling the Session() subclass defined above
session = Session()

# Creating the database using declartive_base subclass
base.metadata.create_all(db)

# Create class-based objects

# merthyr_tydfil = HolidayDestination(
#     city="Merthyr Tydfil",
#     country="Wales",
#     population=60000
# )


# cardiff = HolidayDestination(
#     city="Cardiff",
#     country="Wales",
#     population=300000
# )


# london = HolidayDestination(
#     city="London",
#     country="England",
#     population=5000000
# )


# # Add objects to session
# session.add(merthyr_tydfil)
# session.add(cardiff)
# session.add(london)

# # Commit session to DB
# session.commit()

# Update record (single)
# place = session.query(HolidayDestination).filter_by(
#     city="Merthyr Tydfil").first()
# place.population = 58866
# session.commit()

# Delete record
city_name = input("Please type the city name: ")
place = session.query(HolidayDestination).filter_by(
    city=city_name).first()

# if loop to prevent accidental deletion of record
if place is not None:
    print(
        "City " + place.city + " found!"
    )
    confirmation = input("Do you really want to delete this record? (y/n)")
    if confirmation.lower() == "y":
        session.delete(place)
        session.commit()
        print("Record has been deleted.")
    else:
        print("Record not deleted.")
else:
    print("City not found.")

places = session.query(HolidayDestination)
for place in places:
    print(
        place.city,
        place.country,
        place.population,
        sep=" | "
    )
