from .Model import Model

class EyeGlasses():

    model = None

    def __init__(self):
        self.model = Model()
        self.model.configure()
        self.model.load_weights()

    def handleTextMessage(self, message):
        return 'eye_glasses does not support text messages'

    def handleImage(self, image):
        response = self.model.predict(image)
        result = 'Это собака' if response == 1 else 'Это кошка'
        return result
    