from keras import backend as K
from keras.models import model_from_json
import numpy as np
from .utils import *
import os

class GenderPrediction:

    model_dir:str = 'gender_by_name/output'

    model: None

    def load(self):
        K.set_learning_phase(0)
        print(os.path)
        with open(os.getcwd() + "/" + self.model_dir + "/" + 'model.json', 'r') as fp:
            self.model = model_from_json(fp.read())        

        self.model.compile(loss='categorical_crossentropy', optimizer='adam',metrics=['accuracy'])
        self.model.load_weights(os.path.join(self.model_dir, 'model.h5'))
        

    def format_out(self, out, dict):
        stringify = np.vectorize(lambda x: '{}: {:0.2f}'.format(dict[x], out[x]))
        return ', '.join(stringify(np.argsort(-out)))
        return ""

    def predict(self, word):
        out = self.model.predict(np.array([word2input(word, 50)]))
        indMax = np.argmax(out[0])
        result = {
            "raw_output": list(map(lambda x: str(x), list(out[0]))),
            "sex": SEX_DICT_REVERSE[indMax]
        }
        return result