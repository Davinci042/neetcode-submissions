import string
from typing import List

class Solution:
      

    def __init__(self):
        characters = (list(string.digits) + 
        list(string.ascii_lowercase) +
        list(string.ascii_uppercase) +
        list(string.punctuation)
        )

        self.encrypt_key = {
                char : characters[(i + 15) % len(characters)]
                for i, char in enumerate(characters)
            }  
        self.decrypt_key = {
            value: key for key, value in self.encrypt_key.items()
        }
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            encrypted_word = ''.join(self.encrypt_key.get(char, char) for char in word)
            encoded.append(f"{len(encrypted_word)}:{encrypted_word}")
    
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0
        while i < len(s):
            j = s.find(":", i)
            length_word = int(s[i:j])
            start_word = j + 1
            end_word = start_word + length_word

            decrypt_chunk = s[start_word:end_word]
            decrypted_word = ''.join(self.decrypt_key.get(char, char) for char in decrypt_chunk)

            decoded.append(decrypted_word)

            i = end_word

        return decoded
