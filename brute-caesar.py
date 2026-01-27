import string
import sys

def decrypt_caesar(text: str, key: int) -> str:
    """Decrypt a Caesar cipher text with the given key (shift backward). Preserves case and non-letter characters."""
    result = []
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    for char in text:
        if char in lower:
            pos = lower.index(char)
            new_pos = (pos - key) % 26
            result.append(lower[new_pos])
        elif char in upper:
            pos = upper.index(char)
            new_pos = (pos - key) % 26
            result.append(upper[new_pos])
        else:
            result.append(char)
    return '' .join(result)

def is_likely_english(text: str) -> bool:
    """
    Simple heuristic: check for common English words/phrases | Helps spot the correct decryption quickly.
    """
    lower_text = text.lower()
    common = ["the","and","is","to","in","of","that","it","hello"]
    return any(word in lower_text for word in common)

def brute_force_caeser(cipertext: str):
    """
    Try all 26 possible keys and print the results. Highlights lines that look like English.
    """
    print(f"\nBrute-forcing Caesar cipher on:\n")
    print("key | Decrypted text" +" " * 30 + "Likely English?")
    print("-" * 70)

    for key in range(26):
        decrypted = decrypt_caesar(cipertext, key)
        likely = "YES " if is_likely_english(decrypted) else "  "
        print(f"{key:2d}  | {decrypted:<50} {likely}")


def main():
    if len(sys.argv) > 1:
        cipertext = ' '.join(sys.argv[1: ])
    else:
        cipertext = input("Enter the encrypted text: ").strip()
    if not cipertext:
        print("No text provided. Exiting.")
        return

    brute_force_caeser(cipertext)

if __name__ == "__main__":
    main()                       
