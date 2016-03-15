

import sys
# import os.path

# sys.path.append(os.path.join(os.path.dirname('Models'), '..'))

import sys
sys.path.append('Brother/ReStartLearn/flaskDir')
from Models import User

print(sys.path)

# from User import Module

user = User(19, 'zhang')

# print(user.id)
# print(user.name)


print(user.user_name)
print(user.user_id)

