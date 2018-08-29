# -*- coding: utf-8 -*-
import pingpp
import os

# 全局配置
pingpp.api_key = 'sk_test_mr9enPHSK0KG480aX15OmDiT'
app_id = 'app_nHWbzP4GyPq1TGaL'
pingpp.app_id = app_id
pingpp.private_key_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'your_rsa_private_key.pem')

# log开启
# pingpp.log = "debug"


# API测试
class PingAPI(object):
    @staticmethod
    def create_user():
        # 创建账户
        params = {
            "id": "user_002",  # id 唯一
            "address": "address_1",
            "avatar": None,
            "email": None,
            "gender": "MALE",
            "metadata": {},
            "mobile": None,
            "name": "abc"
        }
        pingpp.User.create(app=app_id, **params)
        return "ok"

    @staticmethod
    def user_list():
        params = {
            "page": 1,
            "per_page": 3,
        }
        list = pingpp.User.list(app=app_id, **params)
        print(list["data"])
        return list


p = PingAPI()
p.user_list()
