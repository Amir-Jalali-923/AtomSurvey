from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from helpers import *
import json

def init_admin_routes(app):
    @app.route('/admin/', methods=['GET', 'POST'])
    def admin():
        if request.method == 'GET':
            return render_template('adminLogin.html')
        else:
            data = {}
            with open('admins.json', 'r') as f:
                data = json.load(f)
            print(data)
            print(request.form.get('user'))
            print(request.form.get('pass'))
            print(hash(request.form.get('pass')))
            if(request.form.get('user') == data['user'] and hash(request.form.get('pass')) == data['pass']):
                session['admin'] = True
                return redirect('/showStats?qn=1')
            return render_template('error.html', errtext='نام کاربری یا رمز ورود نادرست است', errcode=400), 400
        

    @app.route('/showStats')
    def showStats():
        if not session['admin']:
            return redirect('/admin')
        try:
            qn = request.args.get('qn')
            title = get_question('data/questions.csv', int(qn))['title']
            stats = read_stats('data/answers.json')[qn]
            return render_template('AdminPage.html', title=title, data=list(stats.values()), labels=list(stats.keys()), qn=int(qn))
        except:
            return render_template('error.html', errtext='اظلاعات یافت نشد', errcode=500), 500
            