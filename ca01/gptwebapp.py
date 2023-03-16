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
        <a href="{url_for('teamAochan')}">Ao Chan</a><br />
        <a href="{url_for('teamHangliao')}">Hang Liao</a><br />
        <a href="{url_for('teamZijun')}">Zijun Wang</a><br />
        <a href="{url_for('teamZiming')}">Ziming Xu</a>
        <h1>Index</h1>
        <h4>The link below will direct to each of our team member's page.</h4>
        <a href="{url_for('indexBohan')}">Bohan Lin</a><br />
        <a href="https://srautogroupma.com/">Ao Chan</a><br />
        <a href="{url_for('indexHangliao')}">Hang Liao</a><br />
        <a href="{url_for('indexZijun')}">Zijun Wang</a><br />
        <a href="{url_for('indexZiming')}">Ziming Xu</a>
        <h1>Form</h1>
        <a href="{url_for('fixMistakes')}">Fix Mistake Demo</a><br />
        <a href="{url_for('translateToChinese')}">Translate To Chinese Demo</a><br />
        <a href="{url_for('summarize_text')}">Summarize Text Demo</a><br />
        <a href="{url_for('simplifycode')}">Simplify Code Demo</a><br />
        <a href="{url_for('comment_function')}">Comment a simple python function Demo</a>

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
    <h1> Comment Function Demo </h1>
    <p> This demo can comment a given python function. </p>
    <h1> Simplify Code Demo </h1>
    <p> This demo can help to simplify your code. </p>
    <h1> Summarize Text Demo </h1>
    <p> This demo can help to summarize a paragraph. </p> 
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

@app.route('/team/hangliao')
def teamHangliao():
    print('processing /team/Hangliao route')
    return f'''
    <h1> Hang Liao</h1>
    <p> Write and add the method 'summarize_text</p>
    '''

@app.route('/team/Ziming')
def teamZiming():
    print('processing /team/Ziming route')
    return f'''
    <h1> Ziming Xu</h1>
    <p> Responsible for the method of 'Comment python function'</p>
    '''
@app.route('/team/Zijun')
def teamZijun():
    print('processing /team/Zijun route')
    return f'''
    <h1> Zijun Wang</h1>
    <p> Responsible for the method of 'Simplify Code'</p>
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


@app.route('/index/hangliao')
def indexHangliao():
    print('processing index/hangliao route')
    return f'''
        <div>
            <h1 style="text-align: center;">Hiiiiii! </h1>
            <p style="text-align: center;">I'm Hang Liao, currentyly a Econ major & Computer Science major student 
                in Brandeis Univerisy. I am a junior.</p>
        </div>
        <div style="text-align: center;">
            <a href="https://github.com/heathlh">github link</a><br />
            <a href="https://www.linkedin.com/in/hang-liao-3a6ab9224/">linkedin page</a><br />
            <a href="{url_for('home')}">home</a>
        </div>
    '''

@app.route('/index/Ziming')
def indexZiming():
    print('processing index/Ziming route')
    return f'''
    <h1 style="text-align: center;">Hi, </h1>
    <p style="text-align: center;"> My name is Ziming Xu, and I am a senior minoring in computer science. 
    I learned a lot of useful tools in this class :) </p>
    <div style="text-align: center;">
        <a href="https://github.com/JamesXu125">Github Link</a>
        <br/>
        <a href="{url_for('home')}">Back to Home</a>
    </div>
    '''

@app.route('/index/zijun')
def indexZijun():
    print('processing index/zijun route')
    return f'''
        <div>
            <h1 style="text-align: center;">Hi :D </h1>
            <p style="text-align: center;">I'm Zijun Wang, and I'm a sophomore, prearing to declare CS major</p>
        </div>
        <div style="text-align: center;">
            <a href="https://github.com/zijunwang20">my github link</a><br />
            <a href="{url_for('home')}">back to home</a>
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

@app.route('/summarize_text', methods = ['GET', 'POST'])
def summarize_text():
    ''' Handle GET requests by sending a form and POST requests by returning a summary of the input text '''
    if request.method == 'POST':
        input_text = request.form['input_text']
        summary = gptAPI.summarize(input_text)
        return f'''
        <h1>Text Summarizer</h1>
        <h3>Original Text</h3>
        <pre style="bgcolor:yellow">{input_text}</pre>
        <hr>
        <h3>Summary</h3>
        <div style="border:thin solid black">{summary}</div>
        <a href={url_for('summarize_text')}> Summarize Another Text</a>
        '''
    else:
        return '''
        <h1>Text Summarizer</h1>
        Enter your text below
        <form method="post">
            <textarea name="input_text"></textarea>
            <p><input type=submit value="Summarize">
        </form>
        '''

@app.route('/comment_function', methods = ['GET', 'POST'])
def comment_function():
    ''' Comment a given python function
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.comment_f(prompt)
        return f'''
        <h1>Comment a Python function Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('comment_function')}> Comment another function</a>
        '''
    else:
        return '''
        <h1>Comment a Python function App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
@app.route('/simplifycode', methods = ['GET', 'POST'])
def simplifycode():
    ''' simplifycode the input code
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.simplifycode(prompt)
        return f'''
        <h1>simplifycode</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('simplifycode')}> make another query</a>
        '''
    else:
        return '''
        <h1>simplify a code</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
    
    
if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)
    
