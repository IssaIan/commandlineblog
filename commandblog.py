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
                return 'Wrong password'
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

        elif userinput == str("2"):
            comment_id = int(input('Enter comment id:'))
            if not comment_id:
                return "Enter comment id"
            comment = next((comment for comment in comments if comment["comment_id"] == comment_id), False)
            if comment == False:
                    return "No comment found"
            edit = input("Enter your comment here:")
            comment["comment"] = edit
            return comments

        else:
            login()

    
    if user['role'] == "moderator":
        userinput = input("1. create comment \n 2. edit comment \n 3. delete comment \n 4. logout \n ")
        
        if userinput == str("1"):
            comment = input("Enter your comment:")
        
            data = {'comment_id': len(comments) +1,
            'comment': comment,
            'timestamp': datetime.datetime.now() ,
            'created_by': username
            }
            comments.append(data)
            return comments

        elif userinput == str("2"):
            comment_id = int(input('Enter comment id:'))
            if not comment_id:
                return "Enter comment id: "
            comment = next((comment for comment in comments if comment["comment_id"] == comment_id), False)
            if comment == False:
                    return "No comment found"
            edit = input("Enter your comment here:")
            comment["comment"] = edit
            return comments
        elif userinput == str("3"):
            comment_id = int(input('Enter comment id'))
            if not comment_id:
                return 'Enter comment id'
            comment = next((comment for comment in comments if comment["comment_id"] == comment_id), False)
            if comment == False:
                    return "No comment found"
            comments.remove(comment)
            return comments


        else:
            login()



            


print(login())