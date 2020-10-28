def decor(func):
    def inner(name):
        if name == 'Vamsi':
            func(name)
        else:
            print('Hello', name, 'Good evening')
    return inner

@decor
def wish(name):
    print('Hello', name, 'Good morning')

wish('Vamsi')
wish('Kamal')