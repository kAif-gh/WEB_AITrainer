
from Models.improvedCode.camera import Camera

class Exercise:
    def __init__(self):
        self.camera = Camera()
    def exercise(self):
         raise NotImplementedError("dispatch to subclass")