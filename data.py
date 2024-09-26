from pymongo import MongoClient
# from pymongo.server_api import ServerApi

MONGODB_USER = 'talavodoi0123'
MONGODB_PASSWORD = '2Fw6co0FMIRlKpnu'

# Kết nối tới MongoDB
uri = f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASSWORD}@myportfolio.yoghy.mongodb.net/?retryWrites=true&w=majority&appName=MyPortfolio"
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

if __name__ == '__main__':
    print(getHeader('vi'))
