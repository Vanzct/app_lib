__author__ = 'Van.zx'

from flask import Blueprint, render_template, request
import logging
import hashlib

wx = Blueprint('wx', __name__, url_prefix='/wx', template_folder='wx', static_folder='wx')


@wx.errorhandler(404)
def page_not_found(error):
    return render_template('wx/404.html'), 404


@wx.errorhandler(1024)
def something_error(error):
    return render_template('wx/1024.html', error=error), 200


@wx.route('/receive_msg', methods=['GET'])
def receive_msg():
    try:
        signature = request.args.get("signature")

        timestamp = request.args.get("timestamp")
        nonce = request.args.get("nonce")

        echo_str = request.args.get("echostr")
        logging.info(signature+";"+timestamp+";"+nonce+";"+echo_str)
        token = "TW20150612"
        tem_arr = [token, timestamp, nonce]
        tem_arr.sort()
        temp_str = tem_arr.__str__()
        hash_sha1 = hashlib.sha1(temp_str)
        value = hash_sha1.hexdigest()
        if value == signature:
            return echo_str
        else:
            return "false"
    except TypeError, e:
        return "args error" + e


@wx.route('/', methods=['GET'])
def wx_index():
    return render_template("wx/wx.html")
