# Caesar Cipher Decoder (Python + C Hybrid)

A fast Caesar cipher brute-force decoder that combines **Python** for the user interface with **C** for high-performance decryption.

## Features

- **Hybrid Implementation**: Core decryption logic in optimized C, wrapped with Python using `ctypes`
- **Brute-force Attack**: Automatically tries all 26 possible shifts
- **In-place Decryption**: Efficient memory manipulation directly in C
- **Simple CLI**: Easy to use command-line interface

## How It Works

The C function modifies the text buffer directly for each possible shift. Python handles input/output and automation via `ctypes`.

## Repository Structure
```
caesar-decoder-py/
|----src/
|  |---- caesar.c  # Core decryption logic in C
|  |---- decoder.py  # Python wrapper and brute-force script
|  |____ .gitignore
|---- libcaesar.so  # Compiled shared library
|____ README.md
```


## Usage

1. **Compile the C code** into a shared library:

```bash
cd src
gcc -shared -o libcaesar.so -fPIC caesar.c
python3 decoder.py
```
## Example
```
Enter the ciphertext to decode: Khoor Zruog
Shift 00: Khoor Zruog
Shift 01: Jgnnq Yqtnf
Shift 03: Hello World   ← Correct decryption
```
This README.md file is created by AI



