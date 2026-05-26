import ctypes
import os

def load_caesar_library():
    # Getting the absolute path to the  compiler .so file
    lib_path = os.path.abspath("./libcaesar.so")

    #Loading the shared library
    lib = ctypes.CDLL(lib_path)

    # Explicityly define the input arguments and return type for safety
    # decrypt_caesar(char *text, int shift) -> void
    lib.decrypt_caesar.argtypes = [ctypes.c_char_p, ctypes.c_int]
    lib.decrypt_caesar.restype = None

    return lib

def brute_force_caesar(ciphertext):
    lib = load_caesar_library()

    print(f"[*] Brute-forcing ciphertext: {ciphertext}\n")

    for shift in range(26):
        # converting python string to bytes
        encoded_bytes = ciphertext.encode('utf-8')

        # creating a mutable memory buffer that c can modify safely
        buffer = ctypes.create_string_buffer(encoded_bytes)

        # calling the c function and passing the pointer and shift key
        lib.decrypt_caesar(buffer, shift)

        # extracting the output into the python string
        plaintext = buffer.value.decode('utf-8')

        print(f"Shift {shift:02d}: {plaintext}\n")


if __name__ == "__main__":
    encrypted_input = input("Enter the ciphertext to decode: ")
    brute_force_caesar(encrypted_input)


