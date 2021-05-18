from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from datetime import datetime

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired()])
    content = TextAreaField('내용', validators=[DataRequired()])

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])
    name = StringField('이름', validators=[DataRequired(), Length(min=2, max=25)])
    sex = StringField('성별', validators=[DataRequired(), Length(min=1, max=25)])
    create_date = datetime.now()

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])


class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired()])
    content = TextAreaField('내용', validators=[DataRequired()])


#class ImageUploadForm(FlaskForm):
#    tag1 = StringField('태그1', validators=[DataRequired()])
#    tag2 = StringField('태그2', validators=[DataRequired()])
#    tag3 = StringField('태그3', validators=[DataRequired()])