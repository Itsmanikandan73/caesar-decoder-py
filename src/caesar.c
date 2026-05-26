#include <stdio.h>
#include <ctype.h>

// Modifying the string  buffer directly
void decrypt_caesar(char *text, int shift) {
  for (int i = 0; text[i] != '\0'; i++) {
    char c = text[i];

    if (isalpha(c)) {
      char base = isupper(c) ? 'A' : 'a';

      // Calculate the backward shift
      int shifted = (c - base - shift) % 26;

      // Handling negative modulo in c
      if (shifted < 0) {
        shifted += 26;
      }

      text[i] = (char)(base + shifted);
    }
  }
}

