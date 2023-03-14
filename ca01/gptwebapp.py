'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import request,redirect,url_for,Flask
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

@app.route('/')
def home():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1>GPT Demo</h1>
        <a href="{url_for('gptdemo')}">Ask questions to GPT</a>
        <h1>About</h1>
        <a href="{url_for('about')}">About Page</a>
        <h1>Team</h1>
        <h4>The link below will show each of our team member's role in this app.</h4>
        <a href="{url_for('teamBohan')}">Bohan Lin</a><br />
        <a href="{url_for('teamAochan')}">Ao Chan</a>
        <h1>Index</h1>
        <h4>The link below will direct to each of our team member's page.</h4>
        <a href="{url_for('indexBohan')}">Bohan Lin</a>
        <h1>Form</h1>
        <a href="{url_for('fixMistakes')}">Fix Mistake Demo</a><br />
        <a href="{url_for('translateToChinese')}">Translate To Chinese Demo</a>

    '''


@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemo')}> make another query</a>
        '''
    else:
        return '''
        <h1>GPT Demo App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
    

@app.route('/about')
def about():
    print('processing /about route')
    return f'''
    <h1> Fix Mistake Demo</h1>
    <p> This demo can get a prompt from the user and then 
            send to the GPT to fix the spelling mistake and send it back.</p>
    <h1> Translate to Chinese Demo</h1>
    <p> This demo can translate the input to Chinese from any
            language and send it back.</p>

    '''

@app.route('/team/bohan')
def teamBohan():
    print('processing /team/bohan route')
    return f'''
    <h1> Bohan Lin</h1>
    <p> In charge of the "Fix Mistake Demo" in this app and also directing the route in flask app</p>
    '''
@app.route('/team/aochan')
def teamAochan():
    print('processing /team/aochan route')
    return f'''
    <h1> Ao Chan</h1>
    <p> Responsible for the method of 'translate to Chinense'</p>
    '''

@app.route('/index/bohan')
def indexBohan():
    print('processing index/bohan route')
    return f'''
        <div>
            <h1 style="text-align: center;">Hi, 你好! </h1>
            <p style="text-align: center;">I'm Bohan Lin, currentyly a computer science major student 
                in Brandeis Univerisy. This is my last semester and I really enjoy studying here.</p>
        </div>
        <div style="text-align: center;">
            <a href="https://github.com/bohan0lin">github link</a><br />
            <a href="{url_for('home')}">home</a>
        </div>
    '''

@app.route('/fixMistakes', methods = ['GET', 'POST'])
def fixMistakes():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.fixMistakes(prompt)
        return f'''
        <h1>Fix Mistake Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('fixMistakes')}> make another query</a>
        '''
    else:
        return '''
        <h1>Fix Mistake Demo App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
    
@app.route('/translateToChinese', methods = ['GET', 'POST'])
def translateToChinese():
    ''' translate a prompt in any language to Chinese
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.translateToChinese(prompt)
        return f'''
        <h1>Translate To Chinese Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('translateToChinese')}> make another query</a>
        '''
    else:
        return '''
        <h1>Translate To Chinese Demo App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)