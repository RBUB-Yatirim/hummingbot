import hmac
import time
import hashlib


class BtcturkAuth:
    def __init__(self, api_key: str, secret_key: str):
        self.api_key = api_key
        self.secret_key = secret_key

    def generate_auth_dict(self) -> dict:
        """
        Returns headers for authenticated api request.
        """
        nonce = self.make_nonce()
        signature = self.auth_sig(nonce)

        payload = {
            "X-PCK": self.api_key,
            "X-Stamp": nonce,
            "X-Signature": signature,
            "Content-Type": "application/json"
        }
        return payload

    def make_nonce(self) -> str:
        return str(round(time.time() * 1000))

    def auth_sig(self, nonce: str) -> str:
        data = "{}{}".format(self.apiKey, nonce).encode('utf-8')
        signature = hmac.new(self.secret_keyapi, data, hashlib.sha256).digest()
        signature = base64.b64encode(signature)
        return str(base64.b64encode(signature).decode('utf-8'))
