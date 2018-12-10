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
        "name": "stev",
        "password": "1234",
        "role": "normal"
    }
]


def login():
    username = input("please input username: ")
    password = input("please input password: ")

    if not username:
        print('please input username !!!')
        return "please input username!!!"
    if not password:
        print('please input password !!!')
        return "please input password!!!"
    user = next((user for user in users if user["name"] == username), False)

    if user == False:
        print('No user with that username exists')
        return 'No user with that username exists'

    if user['password'] != password:
        print('wrong password')
        return "wrong password"
    user["lastLoginAt"] = datetime.datetime.now()

    if user['role'] == "normal":
        userinput = input("1. create comment \n 2.Edit comment \n  3. logout ")

        if userinput == str("1"):
            comment = input("Enter your comment:")

            data = {'comment_id': len(comments) + 1,
                    'comment': comment,
                    'timestamp': datetime.datetime.now(),
                    'created_by': username
                    }
            comments.append(data)
            print(comments)
            

        elif userinput == str("2"):
            comment_id = int(input('Enter comment id:'))
            if not comment_id:
                return "Enter comment id"
            comment = next(
                (comment for comment in comments if comment["comment_id"] == comment_id), False)
            if comment == False:
                return "No comment found"
            edit = input("Enter your comment here:")
            comment["comment"] = edit
            print(comments)

        else:
            login()

    if user['role'] == "moderator":
        userinput = input(
            "1. create comment \n 2. edit comment \n 3. delete comment \n 4. logout \n ")

        if userinput == str("1"):
            comment = input("Enter your comment:")

            data = {'comment_id': len(comments) + 1,
                    'comment': comment,
                    'timestamp': datetime.datetime.now(),
                    'created_by': username
                    }
            comments.append(data)
            print(comments)

        elif userinput == str("2"):
            comment_id = int(input('Enter comment id:'))
            if not comment_id:
                print("Enter comment id: ")
            comment = next(
                (comment for comment in comments if comment["comment_id"] == comment_id), False)
            if comment == False:
                print("No comment found")
            edit = input("Enter your comment here:")
            comment["comment"] = edit
            print(comments)
       
        elif userinput == str("3"):
            comment_id = int(input("Enter the comment id to delete:")) 
            if not comment_id:
                print('You must enter the comment id')
            comment = next((comment for comment in comments if comment["comment_id"] == comment_id), False)

            if comment == False:
                print('Comment not found!')
            comments.remove(comment)
            print(comments)

        else:
            login()


if __name__ == "__main__":

    choice = 'y'

    while choice is not 'n':

        login()

        choice = input('Continue?')
