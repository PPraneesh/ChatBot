# CYBER-SECURITY CHATBOT

This is a simple web-based chatbot for providing cybersecurity guidance and answering security-related questions in real-time. It uses the GPT-3.5 Turbo model from OpenAI to generate responses to user inputs.

## Table of Contents

- Project Description
- Features
- Getting Started
  - Prerequisites
  - Installation
- Usage
- License

## Project Description

This project is a web application built with Flask, OpenAI, and MongoDB. It allows users to interact with a chatbot to receive cybersecurity guidance and information. The chatbot is powered by the GPT-3.5 Turbo model from OpenAI and can respond to user messages. Users can also register and log in to have personalized chat sessions.

## Features
- User registration and login system.
- Real-time chat with a cybersecurity chatbot powered by OpenAI.
- User-friendly web interface.
- Responses to common cybersecurity questions and guidance.

## Getting Started

Follow these instructions to set up the project on your local machine.

### Prerequisites
- Python 3.x
- To set up this project locally you need mongodb installed in your laptop.
- To set up mongodb follow this [youtube video](https://youtu.be/6DoLxeMlVTI?si=W3wnE1R1YssTxu6f)
- You will also need Openai's api key and organization id
- Click here to find your [organization id](https://platform.openai.com/account/org-settings)
- Click here to find your [api keys](https://platform.openai.com/account/api-keys)
  - After going to the website, just click on create new secret key
  - Then copy the secret key and save it somewhere (ideally in notepad)
### Setting up this project locally
- First create a folder (say Python)
- Then open command prompt, navigate to Python folder
- the run thess following commands
  - `pip install virtualenv`
  - `virtualenv chatbot`
  - `.\chatbot\Scripts\activate`
  - `pip install Flask, openai, pymongo`
  - `cd chatbot`
- Now, you need to download the zip file of this repo and extract it and save it in python\chatbot folder
- This is the file structure <br>
  ![image](https://github.com/PPraneesh/ChatBot/assets/125351602/faa766f0-4cf8-4d78-a750-47dcad984003)
- now run this following command
  - `cd ChatBot-main`
- now in app.py replace
  -   '# Organization Id#' with your organization id
  -  '# Your API_key #' with your api key
  -  '# mongodb uri #' with your mongodb uri, it is generally mongodb://localhost:27017/
- now run this following command
  - `python app.py`
- if you followed this procedure correctly you will get this following in your command prompt <br>
![image](https://github.com/PPraneesh/ChatBot/assets/125351602/c1d0eb48-6d2d-4a43-a8ad-1c92dc515914)
- At the following http://127.0.0.1:5000/ can see your project locally.
## Usage
- Visit http://localhost:5000 in your web browser to access the chatbot interface.
- You can start a chat session, ask questions related to cybersecurity, and receive responses from the chatbot.
- You can also register an account or log in to have personalized chat sessions.
## License
This project is licensed under the MIT License.
## Contact me
If you face any issue while setting up the project locally you can always contact me, <br>
I'm ready to help you out.
