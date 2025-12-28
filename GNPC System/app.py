# from flask import Flask, render_template, request, redirect, url_for, session
# import sqlite3
# from datetime import datetime

# app = Flask(__name__)
# app.secret_key = "gnpc_secret_key"


# # =========================
# # DATABASE CONNECTION
# # =========================
# def get_db():
#     conn = sqlite3.connect("database.db")
#     conn.row_factory = sqlite3.Row
#     return conn


# # =========================
# # HOME PAGE
# # =========================
# @app.route("/")
# def index():
#     return render_template("index.html")


# # =========================
# # LOGIN
# # =========================
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]

#         users = {
#             "engineer": "Engineer",
#             "manager": "Manager",
#             "admin": "Admin"
#         }

#         if username in users and password == "123":
#             session["user"] = username
#             session["role"] = users[username]
#             return redirect(url_for("dashboard"))

#         return render_template("login.html", error="Invalid credentials")

#     return render_template("login.html")


# # =========================
# # DASHBOARD
# # =========================
# @app.route("/dashboard")
# def dashboard():
#     if "user" not in session:
#         return redirect(url_for("login"))

#     conn = get_db()
#     data = conn.execute("SELECT * FROM operations").fetchall()
#     conn.close()

#     return render_template(
#         "dashboard.html",
#         data=data,
#         user=session["user"],
#         role=session["role"]
#     )


# # =========================
# # OPERATIONS INPUT
# # =========================
# @app.route("/input", methods=["GET", "POST"])
# def input_ops():
#     if "user" not in session:
#         return redirect(url_for("login"))

#     if request.method == "POST":
#         parameter = request.form["parameter"]
#         value = request.form["value"]
#         category = request.form["category"]
#         status = "ALERT" if float(value) > 80 else "NORMAL"
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#         conn = get_db()
#         conn.execute(
#             "INSERT INTO operations (parameter, value, category, status, timestamp) VALUES (?, ?, ?, ?, ?)",
#             (parameter, value, category, status, timestamp)
#         )
#         conn.commit()
#         conn.close()

#         return redirect(url_for("dashboard"))

#     return render_template("input.html")


# # =========================
# # PROJECTS
# # =========================
# @app.route("/projects")
# def projects():
#     if "user" not in session:
#         return redirect(url_for("login"))
#     return render_template("projects.html")


# # =========================
# # SUSTAINABILITY
# # =========================
# @app.route("/sustainability")
# def sustainability():
#     if "user" not in session:
#         return redirect(url_for("login"))
#     return render_template("sustainability.html")


# # =========================
# # HSE
# # =========================
# @app.route("/hse")
# def hse():
#     if "user" not in session:
#         return redirect(url_for("login"))
#     return render_template("hse.html")


# # =========================
# # LOGOUT
# # =========================
# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect(url_for("login"))


# @app.route("/input")
# def input_page():
#     return render_template("input.html")


# # =========================
# # RUN APP
# # =========================
# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "gnpc_secret_key"


# =========================
# DATABASE CONNECTION
# =========================
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# =========================
# LOGIN (HOME PAGE)
# =========================
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        users = {
            "engineer": "Engineer",
            "manager": "Manager",
            "admin": "Admin"
        }

        if username in users and password == "123":
            session["user"] = username
            session["role"] = users[username]
            return redirect(url_for("dashboard"))

        return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


# =========================
# DASHBOARD
# =========================
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    data = conn.execute("SELECT * FROM operations").fetchall()
    conn.close()

    return render_template(
        "dashboard.html",
        data=data,
        user=session["user"],
        role=session["role"]
    )


# =========================
# OPERATIONS INPUT
# =========================
@app.route("/input", methods=["GET", "POST"])
def input_ops():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        parameter = request.form["parameter"]
        value = request.form["value"]
        category = request.form["category"]
        status = "ALERT" if float(value) > 80 else "NORMAL"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conn = get_db()
        conn.execute(
            """
            INSERT INTO operations (parameter, value, category, status, timestamp)
            VALUES (?, ?, ?, ?, ?)
            """,
            (parameter, value, category, status, timestamp)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("dashboard"))

    return render_template("input.html")


# =========================
# PROJECTS
# =========================
@app.route("/projects")
def projects():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("projects.html")


# =========================
# SUSTAINABILITY
# =========================
@app.route("/sustainability")
def sustainability():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("sustainability.html")


# =========================
# HSE
# =========================
@app.route("/hse")
def hse():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("hse.html")


# =========================
# LOGOUT
# =========================
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    app.run(debug=True, port=5001)

