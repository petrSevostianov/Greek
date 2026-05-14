text1 = "αγαπήσαμε"  # первое слово
text2 = "αγαπήσαμε"  # второе слово

print("Сравнение слов:")
print(f"Слово 1: {text1}")
print(f"Слово 2: {text2}")
print(f"\nОдинаковые? {text1 == text2}")
print(f"\nДлина 1: {len(text1)}, Длина 2: {len(text2)}")

print("\n--- Unicode символы слова 1 ---")
for i, char in enumerate(text1):
    print(f"{i}: '{char}' = U+{ord(char):04X} ({ord(char)})")

print("\n--- Unicode символы слова 2 ---")
for i, char in enumerate(text2):
    print(f"{i}: '{char}' = U+{ord(char):04X} ({ord(char)})")

if text1 != text2:
    print("\n--- РАЗЛИЧИЯ ---")
    max_len = max(len(text1), len(text2))
    for i in range(max_len):
        if i < len(text1) and i < len(text2):
            if text1[i] != text2[i]:
                print(f"Позиция {i}: '{text1[i]}' (U+{ord(text1[i]):04X}) != '{text2[i]}' (U+{ord(text2[i]):04X})")
        elif i >= len(text1):
            print(f"Позиция {i}: слово 1 короче, в слове 2: '{text2[i]}' (U+{ord(text2[i]):04X})")
        else:
            print(f"Позиция {i}: слово 2 короче, в слове 1: '{text1[i]}' (U+{ord(text1[i]):04X})")
