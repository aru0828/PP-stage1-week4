from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin', methods=["POST"])
def signin():
    #測試用帳號
    test={
        'account':'test',
        'password':'test'
    }
    #取得使用者輸入的帳號密碼 
    userAccount = request.form["account"]
    userPassword = request.form["password"]
    
    #判斷帳號密碼是否正確
    if userAccount == test["account"] and userPassword == test["password"]:
        #成功登入後 將帳號儲存到session 驗證登入ing
        session['uid'] = userAccount
        return redirect(url_for('member'))
    else:
        return redirect(url_for('error'))

@app.route('/member/')
def member():
    #進入member後 取得session中的uid 驗證是否登入中
    uid = session.get('uid')
    if uid:
        return render_template('member.html')
    else:
        return redirect(url_for('index'))

@app.route('/error/')
def error():
    return render_template('error.html')

@app.route('/signout')
def signout():
    #清空session uid
    session["uid"] = False
    return redirect(url_for('index'))

app.run(port=3000)