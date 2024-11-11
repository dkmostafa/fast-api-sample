class GenericException(Exception):
    message: str

    def __init__(self, message='Generic Exception'):
        self.message = message
