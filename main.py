from flask import Flask, render_template, request, redirect, url_for, flash,

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('base.html')
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)