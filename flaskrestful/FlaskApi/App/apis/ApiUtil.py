from flask import request
from flask_restful import Resource

from App.ext import cache
from App.models import User


class BaseResource(Resource):

    def get(self):

        token = request.args.get("token")

        if token:

            u_id = cache.get(token)

            if u_id:

                user = User.query.get(u_id)

                if user:

                    if not user.is_delete:

                        return self.get_data()

                    else:
                        data = {
                            "msg": "user deleted"
                        }
                        return data

                else:

                    data = {
                        "msg": "user not exist"
                    }

                    return data

            else:
                data = {
                    "msg": "user not available"
                }

                return data

        else:

            data = {
                "msg": "user not login"
            }

            return data

    def get_data(self):

        raise NotImplementedError()

