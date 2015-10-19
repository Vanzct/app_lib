# -*- coding:utf-8 -*-
__author__ = 'Van'
import os
import pymongo
from bson import ObjectId

mongodb_host = os.getenv("MONGODB_HOST", '127.0.0.1')
mongodb_post = 27017

mongodb_client = pymongo.MongoClient(mongodb_host, mongodb_post)


def get_app_by_name(key):
    return mongodb_client.applib.apps.find({"key": key})[0]


def get_all_apps():
    return mongodb_client.applib.apps.find()


def add_app(app_json):
    mongodb_client.applib.apps.insert(app_json)


def update_introduction():
    s = "宜人贷借款”APP是国内首款借款服务应用，为有借款需求的用户精心打造了两种在线借款方式，" \
        "即极速申请模式与普通申请模式。<br>" \
        "极速模式是宜人贷全新打造的在线秒批信用借款产品，1分钟申请，10分钟审核，最快当天即可放款。<br>" \
        "普通模式是宜人贷首款无抵押无担保的信用借款款产品，持有信用卡或税后月薪4千即可申请，借款金额最高可达50万。<br>" \
        "【手机端优势】<br>" \
        "-独有极速模式借款 <br>" \
        "-享vip借款通道 <br>" \
        "-借款资料随拍随传 <br>" \
        "-借款状态变化随时知晓 <br>" \
        "-一键快捷还款，支付更大额更便捷 <br>" \
        "【宜人贷介绍】<br>" \
        "宜人贷是2012年由全球成交量最大的P2P公司宜信推出的个人对个人信用借款与理财咨询服务平台。" \
        "宜人贷秉持“让信用变价值”的理念，依托宜信9年风控经验，采用反欺诈系统交叉验证，" \
        "及移动互联网和大数据创新技术风控，坚持科技驱动金融创新，领航移动互联网金融布局，" \
        "为大众信用价值的建立、释放和传递搭建了一个轻松、便捷、安全、透明的网络平台。"
    mongodb_client.applib.apps.update({"key": "1234"}, {"$set": {"introduction": s}})
