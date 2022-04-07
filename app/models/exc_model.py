class CPFError(Exception): ...

class TypeDataError(Exception):
    def __init__(self, key) -> None:
        self.message = f'chave <{key}> possui tipo diferente de string'

class KeyDataError(Exception):
    def __init__(self, expected_key, received_key) -> None:
        self.message = {
            "expected": list(expected_key),
            "received": list(received_key),
        }