from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from App.models import User  # 导入User类
from flask_wtf.file import FileAllowed,FileField,FileRequired #导入文件上传需要的字段 验证器
from App.extensions import file


class Register(FlaskForm):
    username = StringField('用户名',
                           validators=[DataRequired(message='用户名不能为空'), Length(min=6, max=12, message='用户名长度为6～12位')],
                           render_kw={'placeholder': '请输入用户名', 'maxlength': 12})
    userpass = PasswordField('密码',
                             validators=[DataRequired(message='密码不能为空'), Length(min=6, max=16, message='密码长度为6~16位')],
                             render_kw={'placeholder': '输入密码', 'maxlength': 16})
    confirm = PasswordField('确认密码',
                            validators=[DataRequired(message='确认密码不能为空'), Length(min=6, max=16, message='密码长度为6~16位'),
                                        EqualTo('userpass', message='俩次输入的密码不一致!')],
                            render_kw={'placeholder': '输入确认密码', 'maxlength': 16})
    email = StringField('激活邮箱', validators=[Email(message='请输入正确的邮箱地址'), DataRequired(message='邮箱不能为空')],
                        render_kw={"placeholder": "请输入激活邮箱", 'maxlength': 40})
    submit = SubmitField('注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户已注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已存在')


# https://www.cnblogs.com/ckf1988/p/5619337.html

# 账户激活的表单
class AccountActivate(FlaskForm):
    username = StringField('用户名',
                           validators=[DataRequired(message='用户名不能为空'), Length(min=6, max=12, message='用户名长度为6～12位')],
                           render_kw={'placeholder': '请输入用户名', 'maxlength': 12})
    userpass = PasswordField('密码',
                             validators=[DataRequired(message='密码不能为空'), Length(min=6, max=16, message='密码长度为6~16位')],
                             render_kw={'placeholder': '输入密码', 'maxlength': 16})

    email = StringField('激活邮箱', validators=[Email(message='请输入正确的邮箱地址'), DataRequired(message='邮箱不能为空')],
                        render_kw={"placeholder": "请输入激活邮箱", 'maxlength': 40})
    submit = SubmitField('激活')


#登录的表单
class Login(FlaskForm):
    username = StringField('用户名',
                           validators=[DataRequired(message='用户名不能为空'), Length(min=6, max=12, message='用户名长度为6～12位')],
                           render_kw={'placeholder': '请输入用户名', 'maxlength': 12})
    userpass = PasswordField('密码',
                             validators=[DataRequired(message='密码不能为空'), Length(min=6, max=16, message='密码长度为6~16位')],
                             render_kw={'placeholder': '输入密码', 'maxlength': 16})
    submit = SubmitField('登录')



#修改头像表单
class Icon(FlaskForm):
    icon = FileField('上传头像',validators=[FileRequired(message='您还没有选择文件'),FileAllowed(file,message='该类型文件不允许上传')])
    submit = SubmitField('上传')