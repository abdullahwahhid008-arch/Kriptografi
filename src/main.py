"""Demonstrasi ringkas enkripsi dan dekripsi AES-256-GCM."""

from __future__ import annotations

from . import aesgcm_lab as lab

PLAINTEXT = "ABDULLAH WAHID - UTS KRIPTOGRAFI"


def main() -> int:
    key = lab.new_key()
    plaintext_bytes = PLAINTEXT.encode("utf-8")
    sealed = lab.seal_text(key, PLAINTEXT)
    decrypted = lab.unseal_text(key, sealed)
    matched = decrypted == PLAINTEXT
    separator = "=" * 66

    print(separator)
    print("              AES-256-GCM ENCRYPTION & DECRYPTION")
    print(separator)
    print()
    print("[1] PLAINTEXT")
    print(f"Text : {PLAINTEXT}")
    print(f"Bytes: {plaintext_bytes.hex()}")
    print()
    print("[2] KEY INFORMATION")
    print("Algorithm  : AES-256-GCM")
    print(f"Key size   : {lab.KEY_LEN * 8} bits")
    print(f"Nonce size : {lab.NONCE_LEN * 8} bits")
    print(f"Tag size   : {lab.TAG_LEN * 8} bits")
    print()
    print("[3] ENCRYPTION RESULT")
    print(f"Nonce     : {sealed.nonce.hex().upper()}")
    print(f"Ciphertext: {sealed.ciphertext.hex().upper()}")
    print(f"Auth Tag  : {sealed.tag.hex().upper()}")
    print()
    print("[4] DECRYPTION RESULT")
    print(f"Decrypted : {decrypted}")
    print()
    print("[5] VERIFICATION")
    print(f"Status      : {'SUCCESS' if matched else 'FAILED'}")
    print(f"Verification: {'PLAINTEXT MATCH' if matched else 'PLAINTEXT MISMATCH'}")
    print()
    print(separator)
    return 0 if matched else 1


if __name__ == "__main__":
    raise SystemExit(main())
