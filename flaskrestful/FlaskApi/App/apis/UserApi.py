import hashlib
import uuid

from flask_restful import Resource, reqparse, fields, marshal_with, marshal

from App.ext import cache
from App.models import User

parser = reqparse.RequestParser()
parser.add_argument("u_name", required=True, help="请提供用户名")
parser.add_argument("u_password", required=True, help="请输入密码")
#  比较常见的位置直接放在   ?action=login, register
parser.add_argument("action", required=True, help="请提供具体操作")

user_fields = {
    "u_name": fields.String,
    "u_permission": fields.Integer
}

response_user_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(user_fields)
}


response_user_token_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "token": fields.String,
    "data": fields.Nested(user_fields)
}


class UsersResource(Resource):

    # @marshal_with(response_user_fields)
    def post(self):

        args = parser.parse_args()

        action = args.get("action")

        u_name = args.get("u_name")
        u_password = args.get("u_password")

        data = {
            "status": 201,
            "msg": "ok",
        }

        if action == "login":

            user = User.query.filter(User.u_name.__eq__(u_name)).one_or_none()

            if user:
                if not user.verify_password(u_password):

                    data["status"] = 406
                    data["msg"] = "密码错误"

                    return data
                elif user.is_delete:

                    data["status"] = 900
                    data["msg"] = "user not available"

                    return data
                else:
                    data["data"] = user

                    token = str(uuid.uuid4())
                    # 将用户的token存储缓存中，key使用token， 值 使用 id
                    cache.set(token, user.u_id, timeout=60*60*24*7)

                    data["token"] = token

                    return marshal(data, response_user_token_fields)
            else:
                data["status"] = 406
                data["msg"] = "用户不存在"
                return data

        elif action == "register":

            user = User()
            user.u_name = u_name

            # md5 = hashlib.md5()
            # md5.update(u_password.encode("utf-8"))
            # u_password = md5.hexdigest()

            # user.set_password(u_password)
            user.u_password = u_password

            user.save()

            data["data"] = user

            return marshal(data, response_user_fields)


parser_user = reqparse.RequestParser()
parser_user.add_argument("u_password", required=True, help="请提供密码")


class UserResource(Resource):

    @marshal_with(response_user_fields)
    def get(self, id):

        user = User.query.get(id)

        data = {
            "status": 200,
            "msg": "ok",
            "data": user
        }

        return data

    @marshal_with(response_user_fields)
    def post(self, id):
        user = User.query.get(id)

        args = parser_user.parse_args()

        u_password = args.get("u_password")

        user.u_password = u_password

        user.save()

        data = {
            "status": 200,
            "msg": "ok",
            "data": user
        }

        return data

    def delete(self, id):
        user = User.query.get(id)

        user.is_delete = True
        user.save()

        data = {
            "status": 204,
            "msg": "delete success"
        }

        return data