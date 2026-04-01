# Handles the Merkle-linked anchors and cryptographic non-repudiation.
import hashlib
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding



class IntentAnchor:
    def __init__(self):
        self._private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.public_key = self._private_key.public_key()
        self.history_hash = "0" * 64 

    def create_anchor(self, agent_id, thought, action):
        payload = f"{self.history_hash}|{agent_id}|{thought}|{action}"
        signature = self._private_key.sign(
            payload.encode(),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        self.history_hash = hashlib.sha256(payload.encode()).hexdigest()
        return {"payload": payload, "signature": signature.hex(), "hash": self.history_hash}

    def verify_anchor(self, anchor, prev_hash):
        if not anchor["payload"].startswith(prev_hash): return False
        try:
            self.public_key.verify(
                bytes.fromhex(anchor["signature"]),
                anchor["payload"].encode(),
                padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
                hashes.SHA256()
            )
            return True
        except: return False
