from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"

# DATA
services = [
{"name":"Bridal Makeup","price":5000},
{"name":"Party Makeup","price":2000},
{"name":"Mehendi Full Hand","price":2500},
{"name":"Hair Styling","price":1500},
{"name":"Facial","price":1200},
{"name":"Nail Art","price":800},
{"name":"Engagement Makeup","price":4000},
{"name":"Reception Makeup","price":4500},
{"name":"Haldi Makeup","price":1500},
{"name":"Eye Makeup","price":1000},
{"name":"Hair Coloring","price":3000},
{"name":"Keratin Treatment","price":3500},
{"name":"Pedicure","price":900},
{"name":"Manicure","price":700},
{"name":"Threading","price":200},
{"name":"Waxing","price":1000},
{"name":"HD Makeup","price":6000},
{"name":"Airbrush Makeup","price":7000},
{"name":"Hair Spa","price":1500},
{"name":"Skin Polishing","price":2500}
]

products = [
{"id":1,"name":"Lakme Lipstick","price":500},
{"id":2,"name":"Maybelline Foundation","price":700},
{"id":3,"name":"MAC Compact Powder","price":1200},
{"id":4,"name":"L'Oreal Kajal","price":300},
{"id":5,"name":"Huda Beauty Eyeshadow","price":2500},
{"id":6,"name":"Nykaa Nail Polish","price":200},
{"id":7,"name":"Mamaearth Face Wash","price":350},
{"id":8,"name":"Lotus Sunscreen","price":400},
{"id":9,"name":"Colorbar Lip Gloss","price":600},
{"id":10,"name":"Sugar Eyeliner","price":500},
{"id":11,"name":"Maybelline Mascara","price":650},
{"id":12,"name":"Lakme Blush","price":450},
{"id":13,"name":"Faces Canada Primer","price":800},
{"id":14,"name":"Insight Highlighter","price":300},
{"id":15,"name":"Swiss Beauty Concealer","price":350},
{"id":16,"name":"Elle 18 Lipstick","price":150},
{"id":17,"name":"Revlon Foundation","price":900},
{"id":18,"name":"Blue Heaven Compact","price":250},
{"id":19,"name":"Wet n Wild Palette","price":700},
{"id":20,"name":"Nykaa Perfume","price":1200}
]

cart = []
bookings = []

# HOME
@app.route("/")
def home():
    return render_template("home.html")

# SERVICES
@app.route("/services")
def services_page():
    return render_template("services.html", services=services)

# PRODUCTS
@app.route("/products")
def products_page():
    return render_template("products.html", products=products)

# ADD TO CART
@app.route("/add_to_cart/<int:id>")
def add_to_cart(id):
    for p in products:
        if p["id"] == id:
            cart.append(p)
    return redirect("/products")

# CART
@app.route("/cart")
def view_cart():
    return render_template("cart.html", cart=cart)

# ✅ BOOKING (ONLY ONE ROUTE)
@app.route("/booking", methods=["GET", "POST"])
def booking():
    success = False

    if request.method == "POST":
        print("POST WORKING ✅")

        name = request.form.get("name")
        service = request.form.get("service")

        bookings.append({"name": name, "service": service})
        success = True

    return render_template("booking.html", success=success)

# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "1234":
            session["user"] = username
            return redirect("/")
    return render_template("login.html")

# RUN
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)