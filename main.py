import os
from flask import Flask, render_template

app = Flask(__name__)

# ---------------------------------------------------------
# ROUTEN FÜR DIE SEITEN
# ---------------------------------------------------------

@app.route('/')
def home():
    """Startseite: Cyber-Hero & Interaktiver Lebenslauf"""
    return render_template('index.html')

@app.route('/lebenslauf')
def cv():
    """HTML Lebenslauf-Seite"""
    return render_template('cv.html')

@app.route('/anschreiben')
def anschreiben():
    """HTML Anschreiben-Seite"""
    return render_template('anschreiben.html')

@app.route('/projekte/kopf-fit')
def kopf_fit():
    """Detailseite für das Quiz-Projekt KopfFit"""
    return render_template('kopffit.html')

@app.route('/projekte/jumpnova')
def projekt_zwei():
    """Detailseite für das Workout-Projekt JumpNova"""
    return render_template('projekt2.html')

@app.route('/warum-ihr-unternehmen')
def warum_ihr():
    """Spezielle Motivationsseite für deine Bewerbung"""
    return render_template('warum_firma.html')
import os
from flask import Flask, render_template, send_from_directory



# ... (deine bisherigen Routen) ...

@app.route('/download-cv')
def download_cv():
    """Lädt den Lebenslauf als PDF herunter"""
    docs_dir = os.path.join(app.root_path, 'static', 'docs')
    return send_from_directory(
        docs_dir,
        'Lebenslauf_Krisztina_Racz_FIAE.pdf',
        as_attachment=True
    )

@app.route('/download-anschreiben')
def download_anschreiben():
    """Lädt das Anschreiben als PDF herunter"""
    docs_dir = os.path.join(app.root_path, 'static', 'docs')
    return send_from_directory(
        docs_dir,
        'Anschreiben_Krisztina_Racz.pdf',
        as_attachment=True
    )
# ---------------------------------------------------------
# LOCAL SERVER START
# ---------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)