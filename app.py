from src.gui.VideoStreamer import VideoStreamer
from src.camera.Camera import Camera
from threading import Thread
import time

from src.utils.injection.decorator import inject
from src.utils.PubSub import PubSub

Camera(0)

server = VideoStreamer()
server.run(host="0.0.0.0", threaded=True)

#thread = Thread(target=server.run, kwargs={"host": "0.0.0.0", "threaded": True})
# thread.start()
