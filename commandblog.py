comments = []
users = [
    {
        "name": "kenn",
        "password": "1234",
        "role": "admin"
    },
    {
        "name": "issa",
        "password": "1234",
        "role": "moderator"
    },    
    {
        "name": "eric",
        "password": "1234",
        "role": "normal"
    },    
    {
        "name": "steve",
        "password": "1234",
        "role": "normal"
    }
]


class MyClass:
    def __init__(self):
        self.user = users  
    
    def login(self):
        x = input("Enter your name.")
        for user in users:
            if user['name'] == x:
                return user['password']
            y = input('Enter your password: ')
            if user['password'] == y:
                print('You are now logged in!')
            else:
                print('wrong password!')
            break

myclass = MyClass()
myclass.login()
