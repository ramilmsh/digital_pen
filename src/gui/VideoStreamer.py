from flask import Flask, render_template, Response
import os

from src.camera.BaseCamera import BaseCamera

class VideoStreamer(Flask):
    DIRECTORY = os.path.dirname(os.path.realpath(__file__))


    def __init__(self, camera: BaseCamera):
        super().__init__("GUI", template_folder=VideoStreamer.DIRECTORY+"/templates",
                                static_folder=VideoStreamer.DIRECTORY+"/static")
    
        self.camera = camera
        print(camera)

        self.add_url_rule('/', view_func=self.index)
        self.add_url_rule('/stream', view_func=self.stream)

    def index(self):
        return render_template('index.html', context={"title":"Title"})

    def stream(self):
        return Response(self._generate_message(), mimetype='multipart/x-mixed-replace; boundary=frame')

    def _generate_message(self):
        while True:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + self.camera.read() + b'\r\n')
