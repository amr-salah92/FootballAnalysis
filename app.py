from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from core.analysis.advanced_detection import AdvancedAnalyzer
from core.utils.export import DataExporter

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

analyzer = AdvancedAnalyzer()

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_video():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            analysis_results = analyzer.analyze_video(filepath)
            # Process analysis results and store them
            return redirect(url_for('video_analysis', filename=filename))
    return render_template('upload.html')

@app.route('/video_analysis/<filename>')
def video_analysis(filename):
    # Retrieve analysis results for the video
    # analysis_results = ...
    return render_template('video_analysis.html', filename=filename, analysis_results=analysis_results)

@app.route('/export/<format>')
def export_data(format):
    # Implement export functionality
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)