
from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = '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'
model_name = 'gpt-3.5-turbo'


conditions = ['Fever', 'Cough', 'Headache','Cancer']
severity_levels = ['Low', 'Medium', 'High']

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        condition = request.form['condition']
        severity = request.form['severity']
      
        prompt =f"Health Condition: {condition} Severity of Condition: {severity}"
        try:
        
            response = openai.Completion.create(
            engine='text-davinci-002',
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7
            )


            reply = response.choices[0].text.strip()

            return render_template('index.html', conditions=conditions, severity_levels=severity_levels, reply=reply)
        except openai.error.OpenAiError as e:
            print(e)
    else:
        return render_template('index.html', conditions=conditions, severity_levels=severity_levels)

if __name__ == '__main__':
    app.run(debug=True)
