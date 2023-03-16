'''
Demo code for interacting with GPT-3 in Python.

To run this you need to 
* first visit openai.com and get an APIkey, 
* which you export into the environment as shown in the shell code below.
* next create a folder and put this file in the folder as gpt.py
* finally run the following commands in that folder

On Mac
% pip3 install openai
% export APIKEY="......."  # in bash
% python3 gpt.py

On Windows:
% pip install openai
% $env:APIKEY="....." # in powershell
% python gpt.py
'''
import openai


class GPT():
    ''' make queries to gpt from a given API '''
    def __init__(self,apikey):
        ''' store the apikey in an instance variable '''
        self.apikey=apikey
        # Set up the OpenAI API client
        openai.api_key = apikey #os.environ.get('APIKEY')

        # Set up the model and prompt
        self.model_engine = "text-davinci-003"

    def getResponse(self,prompt):
        ''' Generate a GPT response '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )    
        response = completion.choices[0].text
        return response

    def fixMistakes(self,prompt):
        ''' This method can get a prompt from the user and then 
            send to the gpt to fix the spelling mistake and send it back.   --Bohan Lin'''
        edit = openai.Edit.create(
            model = "text-davinci-edit-001",
            input = prompt,
            instruction = "Fix the spelling mistakes"
        )
        response = edit.choices[0].text
        return response

    def translateToChinese(self,prompt):
        '''This method can translate the prompt into Chinese no matter what
           language the prompt is and return it back.   --Ao Chan'''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt = "Translate the following to Chinese:"+prompt,
            n=1,
            temperature=0.8,
        )
        response = completion.choices[0].text
        return response
    
    def comment_f(self,prompt):
        '''This method asks ChatGPT to comment a python function --Ziming Xu'''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt = "Comment the following python function"+prompt,
            n=1,
            temperature=0.8,
            stop = None,
            max_tokens = 1024
        )
        response = completion.choices[0].text
        return response
    
     def simplifycode(self,prompt):
        ''' This method will ask ChatGPT to simpify a code   -Zijun Wang'''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt="simplify this code:"+ prompt,
            n=1,
            temperature=0.8,
        )    
        response = completion.choices[0].text
        return response
    
if __name__=='__main__':
    '''
    '''
    import os
    g = GPT(os.environ.get("APIKEY"))
    # print(g.getResponse("what does openai GPT stand for?"))

    print(g.comment_f(input('Enter a python function that you want to comment:')))
    #print(g.translateToChinese(input("Enter a sentence to translate to Chinese:")))
    # print(g.fixMistakes(input('Enter a sentence: ')))
