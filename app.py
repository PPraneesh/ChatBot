from flask import Flask,flash,render_template,request,redirect,session
import openai
import pymongo

# mongodb
clientUrl = pymongo.MongoClient("mongodb+srv://todolist.inmadjo.mongodb.net/")
DB = clientUrl["chatbotdatabase"]
col = DB["users"]
# open ai
openai.organization = "# Organization Id #"
openai.api_key = "# Your API_key #"
openai.Model.list()

app = Flask(__name__)
chatMsg = [
   {
  "role": "system",
  "content": "AI Security Chatbot: Crafting an AI Assistant for Cybersecurity Guidance Participants need to create an AI-powered chatbot that offers cybersecurity guidance and answers common security-related questions in real-time. The chatbot should use AI to provide assistance and recommendations on cybersecurity best practices, enhancing user's security awareness. Please note that I respond that 'it is not trained to answer this question' if the question is off-topic."
},{
  "role": "assistant",
  "content": "Hello! How can I assist you today with cybersecurity guidance?"
}

  ]
def call ():
    completion= openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages= chatMsg
    )
    return completion
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/speech',methods=["GET","POST"])
def speech():
    if request.method == "POST" :
        msg = ''
        speech(msg)
@app.route('/chat',methods=["GET","POST"])
def index() :
    if request.method == "GET":
        return render_template('index.html',chat=enumerate(chatMsg))
    elif request.method == "POST" :
        userinput= request.form['userInput']
        chatMsg.append({"role":"user","content":userinput}) 
        AIoutput= call()
        chatMsg.append(AIoutput.choices[0].message)
        return redirect("/chat")
@app.route('/login',methods=["GET","POST"])
def login():
    error= None
    if request.method == "POST" :
        query = { "email": request.form['email']}
        mydoc = col.find(query)
        user_found = False
        for x in mydoc:
            if x is not None :
                session['email'] = request.form['email']
                session['password'] = request.form['password']
                user_found = True
                print("found")
                if x["password"] !=  request.form['password']:
                    error = 'Invalid password. Please try again!'
                    print("wrong password")
                else :
                    return redirect("/chat")
        if user_found == False :
            error = "User not found, try registering"
            print("not found")
    return render_template('login.html',error=error) ######
@app.route('/register',methods=["GET","POST"])
def register():
    if request.method == "POST" :
        newuser={
            "username":request.form['username'],
            "email":request.form['email'],
            "password":request.form['password']
        } 
        col.insert_one(newuser)
        flash('Your account has been created successfully, please login.')
        print("account created")
        return redirect("/login") 
    return render_template('register.html')

app.run(use_reloader=True)
