import pylast

class Credentials:
    def __init__(self, api_key, api_secret, username, password):
        self.api_key = api_key
        self.api_secret = api_secret
        self.username = username
        self.password_md5 = pylast.md5(password)

    @staticmethod
    def load(path=None):
        path = path or "./credentials.json"
        import json
        with open(path) as f:
            return Credentials(**json.load(f))

    def __str__(self):
        return "Credentials("+str({k: getattr(self, k) for k in ["api_key", "api_secret", "username", "password_md5"]})+")"

def main(*args, **kwargs):
    print(Credentials.load())