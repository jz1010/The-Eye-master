from flask import Blueprint, render_template, session, request, flash, redirect, json

import os
# import editjson file
from werkzeug.datastructures import MultiDict

from website import editjson

views = Blueprint('views', __name__)


@views.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')

    else:
        return render_template('home.html')


@views.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'Gecko1' and request.form['username'] == 'pi':
        session['logged_in'] = True
        return redirect('/')

    else:
        flash('wrong password!')
        return home()


# create new view for playa mode
@views.route('/playa')
def playa():
    if not session.get('logged_in'):
        return redirect('/')

    else:
        return render_template('playa.html')


# create new view for dev mode
@views.route('/dev_settings', methods=['GET','POST'])
def dev_settings():
    if not session.get('logged_in'):
        return redirect('/')

    else:
        cur_path = os.path.dirname(__file__)
        file_path = os.path.join(cur_path, '..\\settings\\settings_template.json')
        with open(file_path) as json_file:
            data = json.load(json_file)
        print(data)
        if request.method == 'POST':
            result=MultiDict(request.form)
            print(result)
            result=list(result.lists())
            print(result)
            #for num in list length
            for num, item in enumerate(result[:]):
                if(item[1]==['']):
                    result.remove(item)

                #if item[1] has only one item get rid of the list
            for num, item in enumerate(result[:]):
                if(len(item[1])==1):
                    result[num]=(item[0], item[1][0])

                #if item[1] is an int convert to int
            for num, item in enumerate(result[:]):
                if item[1].isdigit():
                    result[num]=(item[0], int(item[1]))

                 #result[num][1]=int(value)
                elif item[1].replace('.','',1).isdigit():
                    result[num]=(item[0], float(item[1]))

                if (item[1] == 'True'):
                    result[num] = (item[0], True)
                elif (item[1] == 'False'):
                    result[num] = (item[0], False)

                if (item[1] == 'None'):
                    result[num] = (item[0], None)

            print(result)

            di=(dict(result))
            print(di)

        #print(data)

        return render_template('dev_settings.html', data=data)

@views.route('/dev_custom', methods=['GET','POST'])
def dev_custom():
    if not session.get('logged_in'):
        return redirect('/')
    else:
        cur_path = os.path.dirname(__file__)
        file_path = os.path.join(cur_path, '..\\settings\\settings_template.json')
        with open(file_path) as json_file:
            data = json.load(json_file)
        print(data)
        print(data["hack"])
        return render_template('dev_custom.html',
                               data=data,
                               cur_eye_shape=data["hack"][0]["eye.shape"],
                               cur_iris_art=data["hack"][0]["iris.art"],
                               cur_lid_art=data["hack"][0]["lid.art"],
                               cur_sclera_art=data["hack"][0]["sclera.art"])
