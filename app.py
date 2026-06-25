from flask import Flask,render_template,url_for,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template ("about.html")
@app.route("/history")
def history():
    return render_template ("history.html")
@app.route("/contact")
def contact():
    return render_template ("contact.html")
# @app.route('/project')
# def predict():
# data=["Age","Gender","BMI","BloodPressure","GlucoseLevel","Cholesterol","HeartRate","Smoking","Alcohol","PhysicalActivity","FamilyHistory"]
#     return render_template ("project.html")
if __name__=="__main__":
    app.run()
