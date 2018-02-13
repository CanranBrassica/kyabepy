# error

class KyabeError(Exception):
    def __init__(self):
        pass
    def what(self):
        pass

class TwitterRequestError(KyabeError):
    def __init__(self, status_code):
        self.status_code = status_code
    def what(self):
        print("TwitterRequestError: " + str(self.status_code))

'''
class TwitterAPINameTypeError(KyabeError):
    def __init__(self, api_name):
        self.api_name = api_name
    def what(self):
        print("TwitterAPINameTypeError: " + type(self.api_name))
'''
