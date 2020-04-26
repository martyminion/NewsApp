from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class SearchForm(FlaskForm):

    search_item = StringField('What would like to see today',validators=[Required()])
    submit = SubmitField('Search')