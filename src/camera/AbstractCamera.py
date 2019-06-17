import numpy as np

class AbstractCamera:

    def __init__(self, name: str = 'GenericCamera'):
        self.name = name

    def read(self) -> np.ndarray:
        raise NotImplementedError

    def check(self) -> bool:
        raise NotImplementedError

    
