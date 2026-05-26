```
# Caesar Cipher Decoder (Hybrid Python/C Implementation)

A high-performance Caesar cipher brute-force utility built using a hybrid architecture. The core cryptographic decryption routine is written in low-level **C** for raw execution speed and direct memory manipulation, while the interface and automation wrapper are written in **Python**. 

The two environments interface seamlessly using Python's standard `ctypes` library, passing memory pointers directly to a compiled shared object (`.so`) file.

## 🚀 Features
* **In-Place Decryption:** The C implementation modifies character buffers directly in memory via pointers (`char *`), avoiding allocations and keeping overhead minimal.
* **Brute-Force Engine:** Automatically iterations through all 26 possible shift keys.
* **Cross-Language Bindings:** Demonstrates how to use Python's `ctypes` to bridge high-level scripts with compiled binaries.

## 📁 Repository Structure
```text
caesar-decoder-py
|_____
|     ├── caesar.c          # Core decryption logic in C
|     ├── decoder.py        # Python brute-force automation script
└── README.md         # Documentation
```
