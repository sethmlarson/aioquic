from cryptography.hazmat.backends.interfaces import EllipticCurveBackend
from cryptography.hazmat.primitives.asymmetric.padding import AsymmetricPadding
from cryptography.hazmat.primitives.hashes import HashAlgorithm
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    KeySerializationEncryption,
    PrivateFormat,
    PublicFormat,
)

class ECDH: ...

class ECDSA:
    def __init__(self, algorithm: HashAlgorithm): ...

class EllipticCurve: ...
class SECP192R1(EllipticCurve): ...
class SECP224R1(EllipticCurve): ...
class SECP256K1(EllipticCurve): ...
class SECP256R1(EllipticCurve): ...
class SECP384R1(EllipticCurve): ...
class SECP521R1(EllipticCurve): ...

class EllipticCurvePrivateKey:
    def exchange(
        self, algorithm: ECDH, peer_public_key: EllipticCurvePublicKey
    ) -> bytes: ...
    def public_key(self) -> EllipticCurvePublicKey: ...
    def private_bytes(
        self,
        encoding: Encoding,
        format: PrivateFormat,
        encryption_algorithm: KeySerializationEncryption,
    ) -> bytes: ...

class EllipticCurvePublicKey:
    curve: EllipticCurve
    @classmethod
    def from_encoded_point(
        cls, curve: EllipticCurve, data: bytes
    ) -> EllipticCurvePublicKey: ...
    def public_bytes(self, encoding: Encoding, format: PublicFormat) -> bytes: ...
    def sign(
        self, data: bytes, padding: AsymmetricPadding, algorithm: HashAlgorithm
    ) -> bytes: ...
    def verify(
        self,
        signature: bytes,
        data: bytes,
        padding: AsymmetricPadding,
        algorithm: HashAlgorithm,
    ) -> None: ...

def derive_private_key(
    private_value: int, curve: EllipticCurve, backend: EllipticCurveBackend
) -> EllipticCurvePrivateKey: ...
def generate_private_key(
    curve: EllipticCurve, backend: EllipticCurveBackend
) -> EllipticCurvePrivateKey: ...
