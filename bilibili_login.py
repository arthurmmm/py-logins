#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'arthur_mao@live.com'
__date__ = '2017-01-29'

import os
import requests
from requests.utils import dict_from_cookiejar
import rsa
import json
import base64
from getpass import getpass

def testLogin(cookies=None, cookies_file=None):
    ''' Access a page that require a login status to validate if we login successfully.
    cookies: cookies dict
    cookies_file: a file that contains cookie dict, with JSON format.
    
    return: test result (true/false)
    '''
    return False

def login(username, password, captcha_file=None, cookies_file=None):
    ''' Perform login with given arguments
    username: Your username
    password: Your password
    captcha_file: Path to store captcha image
    cookies_file: Path to persist cookies dict. Optional.
    
    return: cookies dict or None.
    '''
    
    # step0 - start session for cookies
    session = requests.Session()
    session.get('https://passport.bilibili.com/ajax/miniLogin/minilogin')
    
    # step1 - get captcha
    while True:
        res = session.get('https://passport.bilibili.com/captcha')
        with open('/root/git/nginx-sh1/html/captcha.png', 'wb') as f:
            f.write(res.content)
        captcha = input('Please type captcha, type "retry" if need refresh: ')
        if captcha == 'retry':
            continue
        else:
            break
        
    # step2 - get HASH and RSA pubkey
    print('get HASH and RSA pubkey')
    res = session.get('https://passport.bilibili.com/login?act=getkey')
    hash, pubkey = res.json()['hash'], res.json()['key']
    print('hash: %s, pubkey: %s' % (hash, pubkey))
    
    # step3 - encrypt password (RSA+base64)
    pwd = hash + password
    pwd = pwd.encode('utf-8')
    pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(pubkey.encode('utf-8'))
    pwd = rsa.encrypt(pwd, pubkey)
    print('pwd[RSA]: %s' % (pwd))
    pwd = base64.b64encode(pwd)
    print('pwd[BASE64]: %s' % (pwd))
    
    # step4 - login
    res = session.post('https://passport.bilibili.com/ajax/miniLogin/login', data={
        'userid': username,
        'pwd': pwd,
        'captcha': captcha,
        'keep': 1,
    })
    res = res.json()
    if res['status']:
        url = res['data']['crossDomain']
    else:
        print('Login Failed! status: %s, reason: %s')
    
    print(res.text)
    cookie = dict_from_cookiejar(session.cookies)
    print(cookie)
    with open('/var/tmp/cookies.json', 'w') as f:
        f.write(json.dumps(cookie))

def main():
    username = input('Username: ')
    password = getpass('Password: ')
    cookies = login(username, password, '/var/tmp/bilibili_login.json')
    if testLogin(cookie_file='/var/tmp/bilibili_login.json'):
        print('Login Test pass')
    else:
        print('Login Test failed')
        
if __name__ = '__main__':
    main()