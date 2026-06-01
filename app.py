from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "studenttoolkit"

CAR_PARTS = {
    "tyre": 5500,
    "battery": 6500,
    "brake pad": 1800,
    "air filter": 600,
    "engine oil": 2500,
    "spark plug": 450
}

@app.route("/", methods=["GET", "POST"])
def home():

    percentage = None
    cgpa = None
    fuel_cost = None
    part_price = None
    bot_reply = None

    if request.method == "POST":

        action = request.form.get("action")

        try:

            if action == "percentage":

                obtained = float(request.form["obtained"])
                total = float(request.form["total"])

                percentage = round((obtained / total) * 100, 2)

            elif action == "cgpa":

                marks = float(request.form["marks"])
                cgpa = round(marks / 9.5, 2)

            elif action == "fuel":

                distance = float(request.form["distance"])
                mileage = float(request.form["mileage"])
                petrol = float(request.form["petrol"])

                fuel_cost = round(
                    (distance / mileage) * petrol,
                    2
                )

            elif action == "part":

                part = request.form["part"].lower()

                part_price = CAR_PARTS.get(
                    part,
                    "Part not found"
                )

            elif action == "chat":

                msg = request.form["msg"].lower()

                if "study" in msg:
                    bot_reply = "Create a daily study timetable and revise regularly."

                elif "python" in msg:
                    bot_reply = "Python is excellent for AI, websites and automation."

                elif "exam" in msg:
                    bot_reply = "Practice previous-year questions and mock tests."

                else:
                    bot_reply = "I am still learning. Try asking about study, exams or Python."

        except:
            bot_reply = "Please enter valid values."

    return render_template(
        "home.html",
        percentage=percentage,
        cgpa=cgpa,
        fuel_cost=fuel_cost,
        part_price=part_price,
        bot_reply=bot_reply
    )
@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "123":

            session["admin"] = True

            return redirect("/admin")

    return render_template("login.html")

@app.route("/admin")
def admin():

    if not session.get("admin"):
        return redirect("/login")

    return render_template("admin.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)