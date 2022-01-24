# from pymongo.database import Database
# from alloff_backoffice_server.settings import SERVICE_ENV_IS_DEV
# from pymongo import MongoClient
# from bson.json_util import dumps

# class _Singleton:
#     __instance = None

#     @classmethod
#     def __get_instance(cls):
#         return cls.__instance

#     @classmethod
#     def instance(cls, *args, **kargs):
#         cls.__instance = cls(*args, **kargs)
#         cls.instance = cls.__get_instance
#         return cls.__instance


# class Mongo(_Singleton):
#     __conn: Database = None

#     def __init__(self) -> None:
#         self.__conn = self.__get_database()

#     def __get_database(self):
#         CONNECTION_STRING = "mongodb://root:2morebutter@db.lessbutter.co:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false"
#         client = MongoClient(CONNECTION_STRING)
#         return client["outlet_dev" if SERVICE_ENV_IS_DEV else "outlet"]

#     def list_orders(self):
#         return [dumps(x) for x in self.__conn["orders"].find()]