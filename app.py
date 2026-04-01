from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "secret123"

# ===================== DB CONNECTION =====================
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="A*durgabhavani07",
    database="glow_beauty"
)
cursor = db.cursor()

# ===================== SERVICES (40+) =====================
services = [
{"name":"Bridal Makeup","price":5000},
{"name":"Party Makeup","price":2000},
{"name":"Engagement Makeup","price":4000},
{"name":"Reception Makeup","price":4500},
{"name":"Haldi Makeup","price":1500},
{"name":"HD Makeup","price":6000},
{"name":"Airbrush Makeup","price":7000},
{"name":"Eye Makeup","price":1000},

{"name":"Hair Styling","price":1500},
{"name":"Hair Cut","price":600},
{"name":"Hair Wash","price":200},
{"name":"Hair Coloring","price":3000},
{"name":"Hair Straightening","price":3000},
{"name":"Hair Smoothening","price":3500},
{"name":"Hair Spa","price":1500},
{"name":"Hair Rebonding","price":6000},
{"name":"Hair Extensions","price":4000},
{"name":"Scalp Treatment","price":1500},

{"name":"Facial","price":1200},
{"name":"Gold Facial","price":1500},
{"name":"Diamond Facial","price":1800},
{"name":"Anti-Aging Facial","price":2200},
{"name":"Acne Treatment Facial","price":1800},
{"name":"De-Tan Treatment","price":800},
{"name":"Bleach","price":300},
{"name":"Skin Polishing","price":2500},
{"name":"Body Polishing","price":2500},

{"name":"Manicure","price":700},
{"name":"Pedicure","price":900},
{"name":"Nail Art","price":800},
{"name":"Hand Spa","price":700},
{"name":"Foot Spa","price":900},

{"name":"Threading","price":200},
{"name":"Eyebrow Threading","price":50},
{"name":"Upper Lip Threading","price":20},

{"name":"Waxing","price":1000},
{"name":"Underarm Waxing","price":300},
{"name":"Full Body Waxing","price":2500},

{"name":"Mehendi Full Hand","price":2500},
{"name":"Saree Draping","price":800},

{"name":"Pre-Bridal Package","price":8000},
{"name":"Post-Bridal Care","price":5000},
{"name":"Bridal Trial Makeup","price":2000},
{"name":"Party Combo Package","price":3500}
]

# ===================== PRODUCTS (40+) =====================
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
{"id":20,"name":"Nivea Moisturizer","price":300},

{"id":21,"name":"Lakme Sunscreen SPF 50","price":450},
{"id":22,"name":"Maybelline Fit Me Foundation","price":650},
{"id":23,"name":"Lakme Liquid Foundation","price":550},
{"id":24,"name":"Maybelline Concealer","price":400},
{"id":25,"name":"Lakme Compact Powder","price":350},
{"id":26,"name":"Huda Beauty Foundation","price":2500},
{"id":27,"name":"MAC Studio Fix Foundation","price":3000},
{"id":28,"name":"Nykaa Matte Lipstick","price":500},
{"id":29,"name":"Maybelline Matte Lipstick","price":450},
{"id":30,"name":"Lakme Lip Gloss","price":300},

{"id":31,"name":"Sugar Matte Lipstick","price":600},
{"id":32,"name":"Maybelline Kajal","price":300},
{"id":33,"name":"Lakme Eyeliner","price":250},
{"id":34,"name":"Faces Canada Eyeliner","price":350},
{"id":35,"name":"Swiss Beauty Highlighter","price":400},
{"id":36,"name":"Nykaa Primer","price":600},
{"id":37,"name":"Colorbar Primer","price":800},
{"id":38,"name":"Vitamin C Serum","price":599},
{"id":39,"name":"Niacinamide Serum","price":549},
{"id":40,"name":"Face Pack","price":250}
]

cart = []

# ===================== ROUTES =====================
@app.route("/")
def home():
    return render_template("home.html", services=services, products=products)

@app.route("/services")
def services_page():
    return render_template("services.html", services=services)

@app.route("/products")
def products_page():
    return render_template("products.html", products=products)

@app.route("/cart")
def view_cart():
    return render_template("cart.html", cart=cart)

# ===================== BOOKING (MYSQL) =====================
@app.route("/booking", methods=["GET", "POST"])
def booking():
    success = False

    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        service = request.form.get("service")
        date = request.form.get("date")

        sql = "INSERT INTO bookings (name, phone, service, date) VALUES (%s, %s, %s, %s)"
        values = (name, phone, service, date)

        cursor.execute(sql, values)
        db.commit()

        success = True

    # FETCH DATA
    cursor.execute("SELECT name, phone, service, date FROM bookings")
    data = cursor.fetchall()

    bookings = []
    for row in data:
        bookings.append({
            "name": row[0],
            "phone": row[1],
            "service": row[2],
            "date": row[3]
        })

    return render_template("booking.html", success=success, bookings=bookings)

# ===================== RUN =====================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)