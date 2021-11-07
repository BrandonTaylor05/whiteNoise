from pydub import AudioSegment
from pydub.playback import play
from flask import Flask, render_template, url_for, request
## from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    file = request.files["fileName"]
    fileName = file.filename
    file.save(os.path.join(os.getcwd(), "uploads", fileName))

    #Load an audio file
    myAudioFile = "uploads/" + fileName
    sound1 = AudioSegment.from_file(myAudioFile, format="wav")

    #Invert phase of audio file
    sound2 = sound1.invert_phase()

    #sound2.export("invertedAudio.wav", format="wav")

    Pan1 = sound2.pan(-1)
    Pan2 = sound1.pan(1)

    #Merge two audio files
    combined = Pan1.overlay(Pan2)

    #Export merged audio file
    combined.export(os.getcwd()+"/static/combined.wav", format="wav")

    return render_template('audio.html')

if __name__ == "__main__":
    app.run(debug=True)




