from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import GrowersData
from datetime import datetime

# Mock data
growers = [
  {
    "grower_id": "Gr017",
    "citizen_id": "1123455679008",
    "first_name": "Oliver",
    "last_name": "Brown",
    "gender": "male",
    "citizen_id_issue_date": "2017-03-15",
    "citizen_id_expiry_date": "2027-03-15",
    "citizen_birth_date": "1988-04-20",
    "age": 37,
    "phone": "0987111111",
    "email": "oliver.brown@example.com",
    "address": "45 Maple Street",
    "state": "Virginia",
    "city": "Arlington",
    "zip_code": "22201",
    "photo": "/static/oliver.jpeg"
  },
  {
    "grower_id": "Gr018",
    "citizen_id": "1123455679009",
    "first_name": "Sophia",
    "last_name": "Johnson",
    "gender": "female",
    "citizen_id_issue_date": "2019-08-22",
    "citizen_id_expiry_date": "2029-08-22",
    "citizen_birth_date": "1995-09-10",
    "age": 30,
    "phone": "0987222222",
    "email": "sophia.j@example.com",
    "address": "22 Oak Avenue",
    "state": "Texas",
    "city": "Austin",
    "zip_code": "73301",
    "photo": "/static/sophia.jpeg"
  },
  {
    "grower_id": "Gr019",
    "citizen_id": "1123455679010",
    "first_name": "Ethan",
    "last_name": "Davis",
    "gender": "male",
    "citizen_id_issue_date": "2016-12-05",
    "citizen_id_expiry_date": "2026-12-05",
    "citizen_birth_date": "1982-11-12",
    "age": 42,
    "phone": "0987333333",
    "email": "ethan.davis@example.com",
    "address": "12 Pine Lane",
    "state": "Florida",
    "city": "Miami",
    "zip_code": "33101",
    "photo": "/static/ethan.jpeg"
  },
  {
    "grower_id": "Gr020",
    "citizen_id": "1123455679011",
    "first_name": "Amelia",
    "last_name": "Garcia",
    "gender": "female",
    "citizen_id_issue_date": "2020-02-28",
    "citizen_id_expiry_date": "2030-02-28",
    "citizen_birth_date": "1993-01-08",
    "age": 32,
    "phone": "0987444444",
    "email": "amelia.garcia@example.com",
    "address": "89 Cedar Road",
    "state": "California",
    "city": "San Diego",
    "zip_code": "92101",
    "photo": "/static/amelia.jpeg"
  },
  {
    "grower_id": "Gr021",
    "citizen_id": "1123455679012",
    "first_name": "Liam",
    "last_name": "Martinez",
    "gender": "male",
    "citizen_id_issue_date": "2015-06-18",
    "citizen_id_expiry_date": "2025-06-18",
    "citizen_birth_date": "1980-03-05",
    "age": 45,
    "phone": "0987555555",
    "email": "liam.martinez@example.com",
    "address": "301 River Street",
    "state": "New York",
    "city": "Brooklyn",
    "zip_code": "11201",
    "photo": "/static/liam.jpeg"
  },
  {
    "grower_id": "Gr022",
    "citizen_id": "1123455679013",
    "first_name": "Mia",
    "last_name": "Rodriguez",
    "gender": "female",
    "citizen_id_issue_date": "2018-07-09",
    "citizen_id_expiry_date": "2028-07-09",
    "citizen_birth_date": "1991-02-15",
    "age": 34,
    "phone": "0987666667",
    "email": "mia.rod@example.com",
    "address": "15 Willow Court",
    "state": "Illinois",
    "city": "Chicago",
    "zip_code": "60601",
    "photo": "/static/mia.jpeg"
  },
  {
    "grower_id": "Gr023",
    "citizen_id": "1123455679014",
    "first_name": "Noah",
    "last_name": "Wilson",
    "gender": "male",
    "citizen_id_issue_date": "2014-10-02",
    "citizen_id_expiry_date": "2024-10-02",
    "citizen_birth_date": "1979-06-25",
    "age": 46,
    "phone": "0987666668",
    "email": "noah.wilson@example.com",
    "address": "77 Birch Boulevard",
    "state": "Georgia",
    "city": "Atlanta",
    "zip_code": "30301",
    "photo": "/static/noah.jpeg"
  },
  {
    "grower_id": "Gr024",
    "citizen_id": "1123455679015",
    "first_name": "Isabella",
    "last_name": "Anderson",
    "gender": "female",
    "citizen_id_issue_date": "2021-11-11",
    "citizen_id_expiry_date": "2031-11-11",
    "citizen_birth_date": "2000-12-30",
    "age": 24,
    "phone": "0987666669",
    "email": "isabella.anderson@example.com",
    "address": "210 Elm Drive",
    "state": "North Carolina",
    "city": "Charlotte",
    "zip_code": "28201",
    "photo": "/static/isabella.jpeg"
  },
  {
    "grower_id": "Gr025",
    "citizen_id": "1123455679016",
    "first_name": "James",
    "last_name": "Thomas",
    "gender": "male",
    "citizen_id_issue_date": "2013-04-27",
    "citizen_id_expiry_date": "2023-04-27",
    "citizen_birth_date": "1975-08-19",
    "age": 50,
    "phone": "0987666670",
    "email": "james.thomas@example.com",
    "address": "400 Spruce Circle",
    "state": "Ohio",
    "city": "Columbus",
    "zip_code": "43004",
    "photo": "/static/james.jpeg"
  },
  {
    "grower_id": "Gr026",
    "citizen_id": "1123455679017",
    "first_name": "Charlotte",
    "last_name": "Moore",
    "gender": "female",
    "citizen_id_issue_date": "2016-01-19",
    "citizen_id_expiry_date": "2026-01-19",
    "citizen_birth_date": "1987-05-14",
    "age": 38,
    "phone": "0987666671",
    "email": "charlotte.moore@example.com",
    "address": "55 Aspen Way",
    "state": "Colorado",
    "city": "Denver",
    "zip_code": "80201",
    "photo": "/static/charlotte.jpeg"
  }
]



def seed():
    db: Session = SessionLocal()
    for data in growers:
        
        data["citizen_id_issue_date"] = datetime.strptime(data["citizen_id_issue_date"], "%Y-%m-%d").date()
        data["citizen_id_expiry_date"] = datetime.strptime(data["citizen_id_expiry_date"], "%Y-%m-%d").date()
        data["citizen_birth_date"] = datetime.strptime(data["citizen_birth_date"], "%Y-%m-%d").date()
        
        grower = GrowersData(**data)
        db.merge(grower)  # merge prevents duplicate insert if exists
    db.commit()
    db.close()

if __name__ == "__main__":
    seed()
    print("✅ Growers seeded successfully.")
