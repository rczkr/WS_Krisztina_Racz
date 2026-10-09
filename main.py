from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lebenslauf')
def cv():
    return render_template('cv.html')

@app.route('/anschreiben')
def anschreiben():
    return render_template('anschreiben.html')

@app.route('/projekte/kopf-fit')
def kopf_fit():
    return render_template('kopffit.html')

@app.route('/projekte/jumpnova')
def jumpnova():
    return render_template('jumpnova.html')

@app.route('/warum-ihr-unternehmen')
def warum_ihr():
    return render_template('warum_firma.html')

@app.route('/impressum')
def impressum():
    return render_template('impressum.html')

@app.route('/datenschutz')
def datenschutz():
    return render_template('datenschutz.html')

@app.route('/berry')
def berry():
    return render_template('berry.html')

if __name__ == '__main__':
    app.run(debug=True)