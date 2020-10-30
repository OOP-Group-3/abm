class BasePlotter:
    def __init__(self, space):
        self.space = space

    def plot(self):
        raise NotImplementedError
