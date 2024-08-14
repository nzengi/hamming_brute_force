import hashlib
import random
import binascii

# Bitcoin adresini oluşturmak için gerekli işlevler
def private_key_to_wif(private_key: int) -> str:
    return binascii.hexlify(private_key.to_bytes(32, 'big')).decode()

def wif_to_public_key(private_key_wif: str) -> str:
    private_key_bytes = binascii.unhexlify(private_key_wif)
    return hashlib.sha256(private_key_bytes).hexdigest()

def public_key_to_address(public_key: str) -> str:
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(hashlib.sha256(binascii.unhexlify(public_key)).digest())
    return ripemd160.hexdigest()

def hamming_distance(a: str, b: str) -> int:
    return sum(el1 != el2 for el1, el2 in zip(a, b))

# Hedef adres ve hedef hamming mesafesi
target_address = "13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so"
target_hamming_distance = 50  # Hedeflenen Hamming mesafesi

# Brute-force arama
def brute_force_hamming_search(target_address: str, target_hamming_distance: int, start_range: int, end_range: int):
    for i in range(start_range, end_range):
        private_key = i
        wif = private_key_to_wif(private_key)
        public_key = wif_to_public_key(wif)
        address = public_key_to_address(public_key)

        hamming_dist = hamming_distance(target_address, address)
        if hamming_dist <= target_hamming_distance:
            print(f"Uygun private key bulundu: {private_key}")
            print(f"Bitcoin adresi: {address}")
            print(f"Hamming mesafesi: {hamming_dist}")
            return private_key, address, hamming_dist

    print("Uygun private key bulunamadı.")
    return None

# Arama işlemini başlat
start_range = 0x2d0ffffffffffffff
end_range = 0x2dfffffffffffffff

brute_force_hamming_search(target_address, target_hamming_distance, start_range, end_range)
