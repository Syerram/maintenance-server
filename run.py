#!/usr/bin/env python
import os
from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


@app.route('/')
def home():
  return redirect(url_for('maintenance'))

@app.route('/maintenance')
def maintenance():
  return render_template('maintenance.html'), 503 

if __name__ == '__main__':
  release = os.environ.get('RELEASE', 'DEV')
  debug = release == 'DEV'
  print 'running in debug mode? %s' % debug
  app.run(host='0.0.0.0', port=8040, debug=debug)

