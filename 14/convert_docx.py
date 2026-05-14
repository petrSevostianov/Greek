import mammoth
import sys

docx_path = r"d:\Greek\14\10_01. Группа B. Простое будущее и прошлое (1).docx"
md_path = r"d:\Greek\14\10_01_Группа_B_Простое_будущее_и_прошлое.md"

try:
    with open(docx_path, "rb") as docx_file:
        result = mammoth.convert_to_markdown(docx_file)
        markdown = result.value
        
    with open(md_path, "w", encoding="utf-8") as md_file:
        md_file.write(markdown)
    
    print(f"Успешно конвертирован в {md_path}")
    
    if result.messages:
        print("\nПредупреждения:")
        for message in result.messages:
            print(f"  {message}")
            
except Exception as e:
    print(f"Ошибка: {e}")
    sys.exit(1)
