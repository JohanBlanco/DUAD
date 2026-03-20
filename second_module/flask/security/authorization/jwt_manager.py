import os

import jwt

_KEYS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "keys")


def _load_pem_file(name: str):
    path = os.path.join(_KEYS_DIR, name)
    if not os.path.isfile(path):
        return None
    with open(path, "rb") as f:
        return f.read()


class JWT_Manager:
    """Supports HS256 (single secret) or RS256 (PEM private/public keys)."""

    __jwt_manager = None

    @classmethod
    def get_instance(cls):
        if cls.__jwt_manager is None:
            algorithm = os.getenv("JWT_ALGORITHM", "HS256")
            algo_upper = algorithm.upper()
            if algo_upper.startswith("HS"):
                secret = os.getenv("JWT_PRIVATE_KEY", "trespatitos")
                public = os.getenv("JWT_PUBLIC_KEY") or secret
                cls.__jwt_manager = JWT_Manager(
                    private_key=secret,
                    public_key=public,
                    algorithm=algorithm,
                )
            else:
                private = os.getenv("JWT_PRIVATE_KEY")
                public = os.getenv("JWT_PUBLIC_KEY")
                if not private:
                    private = _load_pem_file("jwt_private.pem")
                if not public:
                    public = _load_pem_file("jwt_public.pem")
                if not private or not public:
                    raise ValueError(
                        "RS256 requires JWT_PRIVATE_KEY and JWT_PUBLIC_KEY (PEM) "
                        "or keys/jwt_private.pem and keys/jwt_public.pem"
                    )
                cls.__jwt_manager = JWT_Manager(
                    private_key=private,
                    public_key=public,
                    algorithm=algorithm,
                )
        return cls.__jwt_manager

    def __init__(self, private_key, public_key=None, algorithm="HS256"):
        self.private_key = private_key
        self.public_key = public_key if public_key is not None else private_key
        self.algorithm = algorithm

    def encode(self, data):
        try:
            return jwt.encode(data, self.private_key, algorithm=self.algorithm)
        except Exception as e:
            print(e)
            return None

    def decode(self, token):
        try:
            return jwt.decode(
                token, self.public_key, algorithms=[self.algorithm]
            )
        except Exception as e:
            print(e)
            return None
