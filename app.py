from flask import Flask,flash,render_template,request,redirect,session
# GEMINI
import pathlib
import textwrap
import google.generativeai as genai
GOOGLE_API_KEY="##  API-KEY  ##"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

app = Flask(__name__)
app.secret_key = 'your_secret_key'
chatMsg = []

def call ():
    response = model.generate_content(chatMsg)
    return response

@app.route('/',methods=["GET","POST"])
def index() :
    if request.method == "GET":
        return render_template('index.html',chat=enumerate(chatMsg))
    elif request.method == "POST" :
        userinput= request.form['userInput']
        chatMsg.append({'role':'user','parts':[userinput]}) 
        AIoutput= call().text
        chatMsg.append({
            'role':'model',
            'parts':[AIoutput]
        })
        return redirect("/")
@app.route('/clear')
def clear():
    chatMsg.clear()
    return redirect("/")
if __name__ == "__main__":
    app.run()
