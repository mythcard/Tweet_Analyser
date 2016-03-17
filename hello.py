# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 02:44:07 2016

@author: mythcard
"""
#!/usr/bin/env python
from flask import Flask, render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form 
from wtforms import RadioField
from wtforms import StringField, SubmitField
import class_update  
import tf_idf_vectorizer
#from wtforms.validators import Required

app = Flask(__name__)
#app.debug = True
app.config['SECRET_KEY'] = 'tweet_det'
manager = Manager(app)
bootstrap = Bootstrap(app)

class NameForm(Form):
    example = RadioField('Label', choices=[('very important','Very Important'),('important','Important'),('ignore','Ignore'),('none','Not Now')])
#    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    
    text = class_update.next_tweet_for_update()   
    total_repo_count = class_update.repo_total_count()
    total_repo_count_classified = class_update.repo_total_count_classified()
    class_pred = tf_idf_vectorizer.get_class_pred()    
    
    if form.validate_on_submit():
        name = form.example.data
        print("Name: ",name)
        if name != 'none':
#            print("Class_pred: ",class_pred)
            class_update.update_status_specific(name,class_pred)
    else:
        print(form.errors)
#    print("Class pred: ",class_pred)
    return render_template('index.html', form=form, name = text, total_repo_count = total_repo_count, total_repo_count_classified = total_repo_count_classified, class_pred = class_pred)
    
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)    

if __name__ == '__main__':
    manager.run()