from flask import Flask, render_template, request, redirect, render_template, url_for
import csv
app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


# def write_to_file(data):
#    with open("database.txt", mode="a") as database:
#        name = data["name"]
#        email = data["email"]
#        subject = data["subject"]
#        message = data["message"]
#        file = database.write(f"\n{name}, {email}, {subject}, {message}")


def write_to_csv(data):
    with open("database.csv", mode="a", newline="") as database2:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            database2, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect(url_for("thankyou", name=request.form["name"]))
        except:
            return "Did not save to database, please check."
    else:
        return "Something went wrong, please try again."


@app.route("/thankyou")
def thankyou():
    return render_template("/thankyou_form.html", name=request.args["name"])
