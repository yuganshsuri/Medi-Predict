from flask import Flask,render_template,url_for,request
import joblib
app=Flask(__name__)
model=joblib.load(r"/Users/yuganshsuri/Desktop/disease prediction/model/decision_tree.lb")
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

@app.route('/project', methods=['GET','POST'])
def predict():
    prediction_label = None
    if request.method == 'POST':
        Age = int(request.form.get('Age', 0))
        Gender = int(request.form.get('Gender', 0))
        BMI = float(request.form.get('BMI', 0.0))
        BloodPressure = int(request.form.get('BloodPressure', 0))
        GlucoseLevel = int(request.form.get('GlucoseLevel', 0))
        Cholesterol = int(request.form.get('Cholesterol', 0))
        HeartRate = int(request.form.get('HeartRate', 0))
        Smoking = int(request.form.get('Smoking', 0))
        Alcohol = int(request.form.get('Alcohol', 0))
        PhysicalActivity = int(request.form.get('PhysicalActivity', 0))
        FamilyHistory = int(request.form.get('FamilyHistory', 0))
        print (Smoking)

        feature_vector = [[
            Age,
            Gender,
            BMI,
            BloodPressure,
            GlucoseLevel,
            Cholesterol,
            HeartRate,
            Smoking,
            Alcohol,
            PhysicalActivity,
            FamilyHistory,
        ]]

        prediction = model.predict(feature_vector)[0]
        label_map = {
            0: 'Healthy',
            1: 'Pre-Diabetes',
            2: 'Hypertension',
            3: 'Heart Disease',
            4: 'Diabetes',
        }
        prediction_label = label_map.get(prediction, 'Unknown')

    return render_template('project.html', prediction_label=prediction_label)

if __name__ == '__main__':
    app.run(debug=True)
