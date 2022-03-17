from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)

# ========================
# ROOT ROUTE
# ========================
@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("read_all.html", users=users)


# ========================
# CREATE USER PAGE
# ========================

@app.route("/create_user")
def create_user_page():
    return render_template("create.html")


# ========================
# CREATE USER PROCESS
# ========================

@app.route("/create_user_process", methods=['post'])
def create_user_process():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "eml": request.form["eml"]
    }
    User.save(data)
    return redirect('/')







if __name__=="__main__":
    app.run(debug=True, port=5001)
