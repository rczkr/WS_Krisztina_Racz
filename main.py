import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# ---------------------------------------------------------
# ROUTEN FÜR DIE UNTERSEITEN
# ---------------------------------------------------------

@app.route('/')
def home():
    """Startseite: Cyber-Hero & Interaktiver Lebenslauf"""
    return render_template('index.html')

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

# ---------------------------------------------------------
# DOWNLOAD ROUTE FÜR DEN LEBENSLAUF (PDF)
# ---------------------------------------------------------

@app.route('/download-cv')
def download_cv():
    """
    Lädt die Datei Lebenslauf_Krisztina_Racz_FIAE.pdf
    aus dem Ordner static/docs/ herunter.
    """
    docs_dir = os.path.join(app.root_path, 'static', 'docs')
    return send_from_directory(
        docs_dir,
        'Lebenslauf_Krisztina_Racz_FIAE.pdf',
        as_attachment=True
    )

# ---------------------------------------------------------
# LOCAL SERVER START
# ---------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)

