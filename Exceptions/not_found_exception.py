class NotFoundException(Exception):
    message: str

    def __init__(self, message='Not Found Exception'):
        self.message = message
