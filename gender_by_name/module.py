from .predict import GenderPrediction
import json

class GenderByName():

    net = None

    def __init__(self):
        self.net = GenderPrediction()
        self.net.load()

    def handleTextMessage(self, message):
        res = self.net.predict(message.text)
        return json.dumps(res)

    def handleImage(self, image):
        return 'Gender by name does not support images recognition'