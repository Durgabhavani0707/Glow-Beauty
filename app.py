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
{"name":"Skin Polishing","price":2500},
{"name":"Eyebrow threading","price":50},
{"name":"Upper lip threading","price":20},
{"name":"Gold Facial","price":1200},
{"name":"Diamond Facial","price":1800},
{"name":"De-Tan Treatment","price":800},
{"name":"Bleach","price":300},
{"name":"Head Massage","price":400},
{"name":"Hair Cut","price":600},
{"name":"Hair Wash","price":200},
{"name":"Hair Straightening","price":3000},
{"name":"Hair Smoothening","price":3500},
{"name":"Body Polishing","price":2500},
{"name":"Bridal Package","price":10000},
{"name":"Party Hairstyle","price":1200},
{"name":"Saree Draping","price":800},
{"name":"Basic Cleanup","price":400}
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
{"id":21,"name":"Nivea Moisturizer","price":300},
{"id":22,"name":"Lakme Sunscreen SPF 50","price":450},
{"id":23,"name":"Maybelline Fit Me Foundation","price":650},
{"id":24,"name":"Lakme Liquid Foundation","price":550},
{"id":26,"name":"Maybelline Concealer","price":400},
{"id":27,"name":"Lakme Compact Powder","price":350},
{"id":28,"name":"Huda Beauty Foundation","price":2500},
{"id":29,"name":"MAC Studio Fix Foundation","price":3000},
{"id":30,"name":"Nykaa Matte Lipstick","price":500},
{"id":31,"name":"Maybelline Matte Lipstick","price":450},
{"id":32,"name":"Lakme Lip Gloss","price":300},
{"id":33,"name":"Sugar Matte Lipstick","price":600},
{"id":34,"name":"Maybelline Kajal","price":300},
{"id":35,"name":"Lakme Eyeliner","price":250},
{"id":36,"name":"Faces Canada Eyeliner","price":350},
{"id":37,"name":"Swiss Beauty Highlighter","price":400},
{"id":38,"name":"Lakme Blush","price":450},
{"id":39,"name":"Nykaa Primer","price":600},
{"id":40,"name":"Colorbar Primer","price":800}
]

cart = []
bookings = []

# HOME
@app.route("/")
def home():
    return render_template("home.html", services=services, products=products)

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