from flask import Flask, jsonify, request
from http import HTTPStatus


  
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










#session 3 path parameters
# Path Parameters allow us to capture values from the URL itself.
@app.route("/greet/<string:name>")
def greet(name):
    return  f" Ey Hello, {name}!"

students_names =["Eric", "Jeuan", "Brant", "Micah", "Matt"]

@app.route("/students", methods=["POST"])
def add_student():
    students_names.append("Leo")
    return students_names



products = [
    {
        "_id": 1,
        "title": "Nintendo Switch",
        "price": 299.99,
        "category": "Entertainment",
        "image": "https://picsum.photos/seed/1/300/300"
    },
    {
        "_id": 2,
        "title": "Smart Refrigerator",
        "price": 999.99,
        "category": "Kitchen",
        "image": "https://picsum.photos/seed/2/300/300"
    },
    {
        "_id": 3,
        "title": "Bluetooth Speaker",
        "price": 79.99,
        "category": "Electronics",
        "image": "https://picsum.photos/seed/3/300/300"
    }
]
# GET /api/products endpoint to return all products
@app.route("/api/products", methods=["GET"])
def get_products():
    """Returns a list of all products"""
    return jsonify({
        "success": True,
        "message": "Products retrieved successfully",
        "data": products
    }), HTTPStatus.OK # 200


@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    print(product_id)
    for product in products:
        if product["_id"] == product_id:
            return jsonify({
                "success": True,
                "message": "Product retrieved successfully",
                "data": product
            })
    return jsonify({
        "success": False,
        "message": "Product not found"
    }), HTTPStatus.NOT_FOUND # 404  


# POST /api/products to add a new product
@app.route("/api/products", methods=["POST"])
def create_product():
    """Create a new product. If the client doesn't provide an `_id`,
    assign one automatically (max existing _id + 1).
    """
    new_product = request.get_json() or {}

    # Compute a new id if not provided
   
    new_product["_id"] = len(products) + 1

    # Minimal validation: ensure at least a title exists
    if "title" not in new_product:
        return jsonify({
            "success": False,
            "message": "Missing required field: title"
        }), HTTPStatus.BAD_REQUEST

    products.append(new_product)
    print(f"Created product: {new_product}")

    return jsonify({
        "success": True,
        "message": "Product created successfully",
        "data": new_product
    }), HTTPStatus.CREATED # 201

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
    return jsonify({"coupons": coupons})

@app.route("/api/coupons/count", methods=["GET"])
def get_coupons_count():
    """Returns the number of coupons in the system"""
    return jsonify({"count": len(coupons)})



# Assignment 3 add a coupon and create a coupons
@app.route("/api/coupons", methods=["POST"])
def create_coupon():
    """Create a new coupon"""
    new_coupon = request.get_json() or {}
    new_coupon["_id"] = len(coupons) + 1
    coupons.append(new_coupon)
    return jsonify({
        "success": True,
        "message": "Coupon created successfully",
        "data": new_coupon
    }), HTTPStatus.CREATED # 201

if __name__ == "__main__":
    app.run(debug=True)


# ---Mini Challenge---
# Create a user/endpoint
# return a dictionary with the follwing keys: Name, role, is_active, and favorite_technologies
# Test it by visiting http://127.0.0.1:5000/user