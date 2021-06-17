from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 코딩 시작

# insert 데이터 넣기
# find 데이터 찾기
# update / delete

same_ages = list(db.users.find({'age':21},{'_id':False})) #깔끔한 출력
# same_ages = list(db.users.find({},{'_id':False})) #보통은 이렇게
print(same_ages)

for i in same_ages:
    print(i)
#특정 값만 가져오기
user = db.users.find_one({'name': 'bobby'})
print(user)
#update
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
#delete
db.users.delete_one({'name':'bobby'})


# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})