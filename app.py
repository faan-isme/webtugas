from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')
@app.route('/skill')
def Skill():
   return render_template('skill.html')
@app.route('/project')
def Project():
   return render_template('project.html')

if __name__ == '__main__':  
    app.run('0.0.0.0',port=5000,debug=True)
    



