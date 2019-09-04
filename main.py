from flask import Flask, render_template, redirect, flash, url_for
from form import Prediction #import the Prediction class in the main
from joblib import load

#init a class as app from Flask allowing the webapp run on the websever
app = Flask(__name__) 
app.config['SECRET_KEY'] = 'd2877d7c60a388cbc75b8cf341364b09'

#declaring app route
@app.route('/',methods=['GET','POST']) #add POST request cos default is GET
def home():
    form = Prediction() # declaring form in the main webpage
    result = ''
    if form.validate_on_submit():
        
        data = [form.bedrooms.data,form.bathrooms.data,form.sqft_living.data,form.sqft_lot.data,
                form.floors.data,form.sqft_above.data,form.sqft_lot15.data,form.yr_built.data,form.condition.data,
                form.zipcode.data]
#form.waterfront.data,form.view.data,form.sqft_basement.data,form.grade.data,form.lat.data,form.lng.data,form.sqft_living15.data
#form.yr_renovated.data,

        model = load('model.joblib')
        result = model.predict([data])
        result = str(result).strip('[]')
        flash('The price of the house is $' + result)
        return redirect(url_for('home'))
    return render_template('home.html',myform=form) #returning the home.html created in templates(that is what flask recognizes for htmls)

@app.route('/about') #another app route for the about page
def about():
    return render_template('about.html') #returning the about.html created in templates

if __name__ == '__main__':
    app.run(debug=True) #call the main.py file to start serving
