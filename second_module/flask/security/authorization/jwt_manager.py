import jwt


class JWT_Manager:
    """Supports HS256 (single secret) or RS256 (private key to sign, public key to verify)."""

    def __init__(self, private_key, public_key=None, algorithm="RS256"):
        self.private_key = private_key
        self.public_key = public_key if public_key is not None else private_key
        self.algorithm = algorithm

    def encode(self, data):
        try:
            key = self.private_key
            encoded = jwt.encode(data, key, algorithm=self.algorithm)
            return encoded
        except Exception as e:
            print(e)
            return None

    def decode(self, token):
        try:
            key = self.public_key
            decoded = jwt.decode(token, key, algorithms=[self.algorithm])
            return decoded
        except Exception as e:
            print(e)
            return None
