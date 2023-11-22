from flask import Flask, render_template, request
import numpy as np
import pickle


model = pickle.load(open("model.pkl", "rb"))
app = Flask(__name__)

# Set the path to the folder containing static files (images, CSS, etc.)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/predict.html")
def predictpage():
    return render_template("predict.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Your existing code here
    Administrative = request.form["administrative"]
    Administrative_Duration = request.form["adminDuration"]
    Informational = request.form["informational"]
    Informational_Duration = request.form["infoDuration"]
    ProductRelated = request.form["productRelated"]
    ProductRelated_Duration = request.form["productDuration"]
    BounceRates = request.form["bounceRates"]
    ExitRates = request.form["exitRates"]
    PageValues = request.form["pageValues"]
    SpecialDay = request.form["specialDay"]
    Month = request.form["month"]
    OperatingSystems = request.form["os"]
    Browser = request.form["browser"]
    Region = request.form["region"]
    TrafficType = request.form["trafficType"]
    VisitorType = request.form["visitorType"]
    Weekend = request.form["weekend"]

    total = [[int(Administrative), float(Administrative_Duration), int(Informational), float(Informational_Duration),
              int(ProductRelated), float(ProductRelated_Duration), float(BounceRates), float(ExitRates),
              float(PageValues), float(SpecialDay), int(Month), int(OperatingSystems), int(Browser), int(Region),
              int(TrafficType), int(VisitorType), int(Weekend)]]

    print(total)

    # Assuming your 'model' is already defined and loaded
    prediction = model.predict(total)
    print(prediction)

    if prediction == 0:
        text = "The visitor is not interested in buying products."
    else:
        text = "The visitor is interested in buying products."

    return render_template("submit.html", result=text)
@app.route("/submit.html")
def submit():
    return render_template("submit.html")
if __name__ == "__main__":
    app.run(debug=False)
