__author__ = 'Van'
import os
import pymongo

mongodb_host = os.getenv("MONGODB_HOST", '127.0.0.1')
mongodb_post = 27017

mongodb_client = pymongo.MongoClient(mongodb_host, mongodb_post)


def get_app_by_name(key):
    return mongodb_client.applib.apps.find({"key": key})[0]


def get_all_apps():
    return mongodb_client.applib.apps.find()


def add_app(app_json):
    mongodb_client.applib.apps.insert(app_json)
