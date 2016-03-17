# from app import app
#
# from app.D111.D222.User import User
#
# # print(User().name)
#
# if __name__ == '__main__':
#     app.run(debug=True, port=5003)

from app import app

if __name__ == "__main__":

    # app.secret_key = 'super secret key'  # 使用这个key flask 会对消息进行加密

    app.run(debug=True)




