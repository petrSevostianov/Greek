import re

file_path = r"d:\Greek\14\10_01_Группа_B_Простое_будущее_и_прошлое.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Исправляем αυτος -> αυτός
content = content.replace("αυτος τηλεφώνησε", "αυτός τηλεφώνησε")

# Исправляем εσεις -> εσείς  
content = content.replace("εσεις ->", "εσείς ->")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Ударения исправлены:")
print("- αυτος → αυτός")
print("- εσεις → εσείς")
