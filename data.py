from pymongo import MongoClient
import os
from dotenv import load_dotenv
# from pymongo.server_api import ServerApi

load_dotenv()

user = os.getenv('MONGODB_USER')
password = os.getenv('MONGODB_PASSWORD')
# Kết nối tới MongoDB
uri = f"mongodb+srv://{user}:{password}@myportfolio.yoghy.mongodb.net/?retryWrites=true&w=majority&appName=MyPortfolio"
# Lấy database
client = MongoClient(uri)

# Kiểm tra kết nối
db = client['testDatabase']

def getFamiliarWith():
    data = db['familiarWith']
    return [i for i in data.find({}, {'_id': 0})]


def getHeader(language):
    data = db['languages']
    return [i for i in data.find({}, {f"{language}.header": 1, '_id': 0})][0].get(f'{language}').get('header')

def overAllData():
    data = db['languages']
    dataPicMedia = db['overAll']
    return {
        'en': data.find()[0]['en'],
        'vi': data.find()[0]['vi'],
        'overall': {
            'profilePicture': dataPicMedia.find()[0]['profilePicture'],
            'socialMedia': dataPicMedia.find()[0]['socialMedia']
        }
    }

if __name__ == '__main__':
    print(user, password)
