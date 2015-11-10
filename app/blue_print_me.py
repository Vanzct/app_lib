# -*- coding:utf-8 -*-
__author__ = 'Van'

from flask import Blueprint, render_template, request
import data_me as data
me = Blueprint('me', __name__, url_prefix='/me', template_folder='me', static_folder='me')


@me.errorhandler(404)
def page_not_found(error):
    return render_template('wx/404.html'), 404


@me.errorhandler(1024)
def something_error(error):
    return render_template('wx/1024.html', error=error), 200


@me.route('/', methods=['GET'])
@me.route('/index', methods=['GET'])
def me_index():
    return render_template("me/me.html", data=data, page_id="index")


@me.route('/experience', methods=['GET'])
def me_experience():
    return render_template("me/experience.html", data=data, page_id="experience")


@me.route('/tech', methods=['GET'])
def me_tech():
    return render_template("me/tech.html", data=data, page_id="tech")


@me.route('/other', methods=['GET'])
def me_other():
    return render_template("me/other.html", data=data, page_id="other")