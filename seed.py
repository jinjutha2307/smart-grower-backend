import csv
from sqlalchemy.orm import Session
from database import engine
from models import State, City, Zipcode

session = Session(bind=engine)

with open("geographic_data.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    states = {} #cache states to avoid duplicates
    cities = {} #cache cities to avoid duplicates

    for row in reader:
        state_name = row['state']
        city_name = row['city']
        zipcode_value = row['zipcode']

        if state_name not in states:
            state = State(name=state_name)
            session.add(state)
            session.flush() # ensure state.id is generated
            states[state_name] = state
        else:
            state = states[state_name]

        city_key = (state.id, city_name)
        if city_key not in cities:
            city = City(name=city_name, state_id=state.id)
            session.add(city)
            session.flush() # ensure city.id is generated
            cities[city_key] = city
        else:
            city = cities[city_key]
        
        zipcode = Zipcode(code=zipcode_value, city_id=city.id)
        session.add(zipcode)

session.commit()
session.close()
print("Database seeded successfully.")
    
