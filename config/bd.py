from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv
load_dotenv()


class BaseData():
    def __init__(self):

        self.__conn = MongoClient(
            "mongodb+srv://yess:"+getenv('ACCESS_TOKEN')+"@cluster0.wdzh1o3.mongodb.net/?retryWrites=true&w=majority")[getenv('DATABASE')]
        self.__dictGet = {}

    def sendData(self, data):
        self.__conn['Variables'].insert_one(data)

    def readData(self, **kwargs):
        '''
        parameters:
        limit: limit of data
        type_limit: int'''

        if len(kwargs) > 0:
            # for key, value in kwargs.items():
            #     self.__dictGet[key] = value
            return self.__conn['Variables'].find()
        else:
            return self.__conn['Variables'].find()

    def sendUser(self, data):
        insert = {
            '_id': data['email'], 'username': data['username'], 'password': data['password']}
        try:
            insertOut = self.__conn['Users'].insert_one(insert)
            return str(insertOut.inserted_id)
        except:
            return None

    def sendClient(self, data):
        self.__conn['Clients'].insert_one(data)

    def readUser(self, **kwargs):
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    key = '_id'
                self.__dictGet[key] = value
            return self.__conn['Users'].find(self.__dictGet)
        else:
            return self.__conn['Users'].find()

    def readDataData(self):
        return self.__conn['Data'].find()


dataBase = BaseData()
