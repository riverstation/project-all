from App.apis.ApiUtil import BaseResource


class BookResource(BaseResource):

   def get_data(self):

       data = {
           "status": 200,
           "msg": "666"
       }

       return data