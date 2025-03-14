# coding:utf-8
# author:ila
import re
from flask import request, jsonify, session
from utils.jwt_auth import Auth
from utils.codes import *
from . import main_bp
import time
from utils.log_util import printLog

@main_bp.before_request
def before_request():
    # 在请求到达视图函数之前记录开始时间
    request.start_time = int(time.time()*1000)
    request__url = session.get('request__url')
    if request.method == 'GET':
        get_list = [
            "/",
            "/apidocs/",
             "/python1p21sd8o/examusers/login" ,
            "/python1p21sd8o/examusers/register",
            '/python1p21sd8o/defaultuser/login',
            '/python1p21sd8o/users/login',
        ]  # 免认证list

        # 重置密码时获取验证码不检测token。
        if request__url not in get_list and "/notify" not in request__url and "/static/" not in request__url and "/js/" not in request__url  and "/css/" not in request__url and "/img/" not in request__url  and "/fonts/" not in request__url   and  "detail" not in request__url   and "templates" not in request__url and "/forum/flist" not in request__url and "/forum/list" not in request__url and "/upload/" not in request__url and "/examusers/login" not in request__url and "/examusers/register" not in request__url and  request__url[-5:]!="/list" and "/login" not in request__url  and "/dist" not in request__url and "/admin" not in request__url and "/autoSort" not in request__url and '/option' not in request__url and '/security' not in request__url and '/sendemail' not in request__url and '/updateBrowseDuration' not in request__url and '/sendsms' not in request__url or "autoSort2" in request__url:
            result = Auth.identify(Auth, request)

            if result.get('code') != normal_code:
                print('jwt auth success')
                return jsonify(result)

    elif request.method == 'POST':
        post_list = [
            '/python1p21sd8o/defaultuser/register',
            '/python1p21sd8o/defaultuser/login',
            '/python1p21sd8o/users/register',
            '/python1p21sd8o/users/login',
            "/python1p21sd8o/examusers/login" ,
            "/python1p21sd8o/examusers/register"
        ]  # 免认证list
        if request__url not in post_list and "register" not in request__url and "login" not in request__url and "faceLogin" not in request__url and '/file/upload' not in request__url and '/update' not in request__url:  # 注册时不检测token。
            result = Auth.identify(Auth, request)
            if result.get('code') != normal_code:
                print('jwt auth fail')
                return jsonify(result)

@main_bp.after_request
def after_request(response):
    # 在响应返回给客户端之前计算请求时间并打印
    request.request_time = int(time.time()*1000) - request.start_time
    printLog(request)
    return response
