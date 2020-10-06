class TooYoung(Exception):
    def __init__(self):
        self.msg = "Too Young for the job exception"


age = int(input('Enter your age: '))
if age > 12:
    print('Your application is accepted')
else:
    raise TooYoung()