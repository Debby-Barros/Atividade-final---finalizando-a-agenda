from flask import render_template 
import connexion
import user, event


app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")


@app.route("/")
def home():
    _user = user.read_all()
    _event = event.read_all()
    return render_template("home.html", user=_user, event=_event)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)