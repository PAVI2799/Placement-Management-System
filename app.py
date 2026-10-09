from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        # ipo ku terminal la mattum print pannum
        print(f"New Register: {name} - {email}")
        return f"<h2 style='text-align:center; margin-top:50px;'>Thanks {name}, you registered successfully! ✅</h2><center><a href='/login'>Go to Login</a></center>"
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        return f"<h2 style='text-align:center; margin-top:50px;'>Welcome {email}! Login Success ✅</h2><center><a href='/jobs'>View Jobs</a></center>"
    return render_template("login.html")

@app.route("/jobs")
def jobs():
    return render_template("jobs.html")

@app.route("/apply/<job_title>")
def apply(job_title):
    return f"<h2 style='text-align:center; margin-top:50px;'>You applied for {job_title} Successfully! ✅</h2><center><a href='/jobs'>Back to Jobs</a> | <a href='/'>Home</a></center>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)