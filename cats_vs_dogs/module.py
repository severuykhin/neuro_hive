from .Model import Model

class CatsVsDogs():

    model = None

    def __init__(self):
        self.model = Model()
        self.model.configure()
        self.model.load_weights()

    def handleTextMessage(self, message):
        return 'Cats vs dogs does not support text messages'

    def handleImage(self, image):
        response = self.model.predict(image)
        result = 'Это собака' if response == 1 else 'Это кошка'
        return result
    