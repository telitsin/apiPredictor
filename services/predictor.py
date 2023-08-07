import random


class LoadModel:
    """This class emulates the model. Load real model in app.py"""

    def __int__(self):
        print("load model")

    def predict(self, **args) -> int:
        for arg, value in args.items():
            print(f"{arg}: {value}")
        return random.getrandbits(1)