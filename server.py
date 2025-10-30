from flask import Flask
  
app = Flask(__name__) # instance of Flask application

@app.route("/", methods=["GET"])
def index():
        
        return "Welcome to Flask Framework!"



@app.route("/cohort-61", methods=["GET"])
def cohort_61():
    students_list= ["Eric", "Jeuan", "Brant", "Micah", "Matt"]
    return students_list


@app.route("/cohort-100", methods=["GET"])
def cohort_100():
    students_list = ["Pam", "John", "Dwight", "Michael", "Oscar"]
    return students_list


@app.route("/contact", methods=["GET"])
def contact():
    information ={"email": "jeuan.mitchell@gmail.com", "phone": "123-456-7890"}
    
    return information

@app.route("/course", methods=["GET"])
def course():
    course_info = {
        "title": "Introductory Web API Flask",
        "duration": "4 sessions",
        "level": "Beginner"
    }
    return course_info


@app.route("/user", methods=["GET"])
def user():
    user_info = {
        "name": "Jeuan Mitchell",
        "role": "Hacker",
        "is_active": True,
        "favorite_technologies": ["Flask", "Django", "FastAPI"]
    }
    return user_info

#--- COUPONS ---
# Coupons data
coupons = [
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2, "code": "SPOOKY25", "discount": 25},
    {"_id": 3, "code": "VIP50", "discount": 50}
]

@app.route("/api/coupons", methods=["GET"])
def get_coupons():
    """Returns a list of all coupons"""
    return coupons

@app.route("/api/coupons/count", methods=["GET"])
def get_coupons_count():
    """Returns the number of coupons in the system"""
    return {"count": len(coupons)}

if __name__ == "__main__":
    app.run(debug=True)

# ---Mini Challenge---
# Create a user/endpoint
# return a dictionary with the follwing keys: Name, role, is_active, and favorite_technologies
# Test it by visiting http://127.0.0.1:5000/user