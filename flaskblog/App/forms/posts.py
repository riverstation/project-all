from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField
from wtforms.validators import DataRequired,Length

class Posts(FlaskForm):
    content = TextAreaField('发表博客',validators=[DataRequired(message='内容不能为空'),Length(min=10,max=1000,message='内容在10～1000个字之间')])
    submit = SubmitField('发表')