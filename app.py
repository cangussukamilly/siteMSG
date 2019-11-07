from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/NovaMensagem')
def NovaMensagem():
    return render_template('Mensagens.html')

if __name__ == '__main__':
    app.run(debug=True)