from flask import Flask, redirect, url_for, render_template, request, session, flash
from blog import app
from flask_mail import Mail, Message
from datetime import timedelta

app.permanent_session_lifetime = timedelta(days=5)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'lyantung0822@gmail.com'
app.config['MAIL_PASSWORD'] = 'trdiluydmcstmuhu'
app.config['MAIL_DEFAULT_SENDER'] = 'lyantung0822@gamil.com'
mail = Mail(app)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/send-contact", methods=["POST"])
def process_email():
    if request.method == "POST":
        user = request.form["user_name"]
        email = request.form["user_email"]
        message = request.form["user_message"]

        # Email to notice me
        msg = Message("Jess, %s left you a message!" % (user), sender='lyantung0822@gmail.com', recipients=['jesslam321@gmail.com'])
        msg.body = """
        Hey Jess, looks like some left you a message on your website.

        Name: %s
        Email: %s
        Message: %s
        """ % (user, email, message)

        mail.send(msg)
        return redirect(url_for("contact"))
    else:
        return render_template("contact.html")