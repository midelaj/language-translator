from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('translate.html')  # Use the new template

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    target_language = request.form['language']
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    translated_text = translated.text
    return render_template('translate.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
