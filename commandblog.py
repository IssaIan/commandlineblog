import datetime

comments = []
users = [
    {
        "name": "kenn",
        "password": "1234",
        "role": "admin",
        "lastLoginAt": ""

    },
    {
        "name": "issa",
        "password": "1234",
        "role": "moderator",
        "lastLoginAt": ""
    },
    {
        "name": "eric",
        "password": "1234",
        "role": "normal",
        "lastLoginAt": ""
    },
    {
        "name": "steve",
        "password": "1234",
        "role": "normal"
    }
]

def login():
    username = input("please input username: ")

    for user in users:
        if user['name'] == username:
            # return user['password']
            password = input("please input password: ")
            if user['password'] != password:
                print('Wrong password')
            user["lastLoginAt"] = datetime.datetime.now()

    if user['role'] == "normal":
        userinput = input("1. create comment \n 2.Edit comment \n  3. logout ")
        
        if userinput == str("1"):
            comment = input("Enter your comment:")
        
        data = {'comment_id': len(comments) +1,
            'comment': comment,
            'timestamp': datetime.datetime.now() ,
            'created_by': username
            }
        comments.append(data)
        return comments

        


print(login())