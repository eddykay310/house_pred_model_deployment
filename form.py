#import modules and classes that are needed to create the Presiction class to use in webapp
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired 

#creating the class Prediction, a form for accepting input
class Prediction(FlaskForm):
    bedrooms = IntegerField('Number of Bedrooms',validators=[DataRequired()])
    bathrooms = IntegerField('Number of Bathrooms',validators=[DataRequired()])
    sqft_living = IntegerField('sqft_living',validators=[DataRequired()])
    sqft_lot = IntegerField('sqft_lot',validators=[DataRequired()]) 
    floors = DecimalField('floors',validators=[DataRequired()])
    # waterfront = IntegerField('waterfront',validators=[DataRequired()])
    # view = IntegerField('view',validators=[DataRequired()])
    condition = IntegerField('condition',validators=[DataRequired()])
    # grade = IntegerField('grade',validators=[DataRequired()])
    sqft_above = IntegerField('sqft_above',validators=[DataRequired()])
    # sqft_basement = IntegerField('sqft_basement',validators=[DataRequired()])
    yr_built = IntegerField('yr_built',validators=[DataRequired()])
    # yr_renovated = IntegerField('yr_renovated',validators=[DataRequired()])
    # lat = DecimalField('lat',validators=[DataRequired()])
    # lng = DecimalField('long',validators=[DataRequired()])
    # sqft_living15 = IntegerField('sqft_living15',validators=[DataRequired()])
    sqft_lot15 = IntegerField('sqft_lot15',validators=[DataRequired()])
    zipcode = IntegerField('zipcode',validators=[DataRequired()])
    submit = SubmitField('Predict')

    