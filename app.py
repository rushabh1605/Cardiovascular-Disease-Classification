from flask import Flask, render_template, request

import cvd as cvd


app = Flask(__name__)


@app.route("/", methods=["POST"])
def model():
    if request.method == "POST":
        age = request.form['age']
        gender = request.form['gender']
        height = request.form['height']
        weight = request.form['weight']
        ap_hi = request.form['ap_hi']
        ap_lo = request.form['ap_lo']
        cholesterol = request.form['cholesterol']
        gluc = request.form['gluc']
        smoke = request.form['smoke']
        alco = request.form['alco']
        active = request.form['active']

        cvd_pred = cvd.cvd_prediction(
            age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active)
        print(cvd_pred)

    return render_template("index. html")


if __name__ == "__main__":
    app.run(debug=True)
