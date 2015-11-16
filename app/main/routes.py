# -*- coding: utf-8 -*-
__author__ = 'Van'

from flask import render_template, session, redirect, url_for, current_app, request
from . import main
from ..mongo import get_app_by_name, get_all_apps, add_app, update_introduction

qiuniu_bucket = "http://7s1srd.com1.z0.glb.clouddn.com/"


def get(d, key, default):
    if key in d:
        return d[key]
    else:
        return default


@main.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@main.route('/app/<key>', methods=['GET'])
def show(key=None):

    if key == 'dianyingpiao':
        return render_template("dianyinpiao.html")
    app = get_app_by_name(key)
    data = {"key": app["key"],
            "name": app["name"],
            "download_count": get(app, "download_count", 0),
            "size": get(app, "size", "0M"),
            "introduction": get(app, "introduction", u"赞无"),
            "apk_url": get(app, "apk_url", ""),
            "icon": get(app, "icon", ""),
            "images": get(app, "images", []),
            "short": get(app, "short", ""),
            "bait": get(app, "bait", "")
            }
    return render_template("app.html", app=data, url_prefix=qiuniu_bucket)


@main.route('/info', methods=['GET'])
def info():
    return render_template(
        "app_info.html",
        name=u'一人'
    )


@main.route('/company', methods=['GET'])
def company():
    return render_template("company.html")


@main.route('/us', methods=['GET'])
def us():
    return render_template("us.html")


@main.route('/edit', methods=['GET'])
def edit():
    apps = get_all_apps()
    return render_template("edit.html", apps=apps)


@main.route('/add', methods=['GET'])
def add():
    name = request.args.get("name", "")
    key = request.args.get("key", "")
    app = {"key": key,
           "name": name,
           "download_count": 0,
           "size": "0M",
           "introduction": "赞无",
           "icon": key + "/icon.png",
           "images": []}
    add_app(app)
    return redirect("edit.html")


@main.route('/update', methods=['GET'])
def update():
    key = request.args.get('key', '1234')
    app = get_app_by_name(key)
    data = {"key": app["key"],
            "name": app["name"],
            "download_count": get(app, "download_count", 0),
            "size": get(app, "size", "0M"),
            "introduction": get(app, "introduction", u"赞无"),
            "icon": get(app, "icon", ""),
            "images": get(app, "images", [])}
    # s = data["images"].
    return render_template("update.html", images_count=4, app=data)


@main.route('/update_submit', methods=['GET'])
def update_submit():
    key = request.args.get('key')
    app = get_app_by_name(key)
    data = {"key": request.args.get('key', ""),
            "name": request.args.get('name', ""),
            "download_count": request.args.get('download_count', "0"),
            "size": request.args.get('name', "0M"),
            "introduction": request.args.get("introduction", u"赞无"),
            "icon": app.get('icon', key+"/icon"),
            "images": app.get('images', [])
            }
    return render_template("app.html", app=data, url_prefix=qiuniu_bucket)


@main.route('/update_intro', methods=['GET'])
def update_in():
    update_introduction()
    return "OK"


@main.route('/yirendai.html', methods=['GET'])
def yirendai():
    return show("yirendai")