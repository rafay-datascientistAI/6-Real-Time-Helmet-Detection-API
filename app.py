from flask import Flask, render_template, request
import os
from model import detect_helmet , detect_helmet_video

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "uploads"

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/" , methods=['GET' , 'POST'])
def index():
    result = ""
    filename = ""
    if request.method == 'POST':

        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No file selected"
        filename = file.filename
        filepath = os.path.join("static/uploads", file.filename)
        file.save(filepath)

        # check file type
        if filename.lower().endswith(('.png' , '.jpg' , '.jpeg')):
            result = detect_helmet(filepath)
            filetype = "image"
        elif filename.lower().endswith(('.mp4' , '.avi' , '.mov')):
            output_video = detect_helmet_video(filepath)
            result = "Video Processed"
            filetype = "video"
            filename = os.path.basename(output_video)
        else:
            return "Unsupported File type"
        return render_template('index.html' , result=result , filename=file.filename , filetype=filetype)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(host="0.0.0.0" , port=10000 , debug=False )