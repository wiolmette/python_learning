import os
from PIL import Image, ImageOps
import csv

# Ścieżki
SOURCE_ROOT = r"E:\Zdjęcia"
TARGET_ROOT = r"E:\Zdjęcia_Zmienione"
YEARS = ["2023", "2024", "2025"]
OUTPUT_CSV = os.path.join(TARGET_ROOT, "raport_zmian.csv")

# Docelowe stosunki boków
RATIO_10x13 = 10 / 13
RATIO_13x10 = 13 / 10
TOLERANCE = 0.01

# Przygotowanie folderu docelowego
os.makedirs(TARGET_ROOT, exist_ok=True)
report_data = [("Ścieżka", "Oryginalny rozmiar", "Nowy rozmiar", "Docelowy format")]

def determine_target_format(w, h):
    """Określa do jakiej proporcji przyporządkować zdjęcie."""
    ratio = w / h
    if abs(ratio - RATIO_10x13) < TOLERANCE:
        return "10x13"
    elif abs(ratio - RATIO_13x10) < TOLERANCE:
        return "13x10"
    else:
        return "błąd"

def needs_adjustment(w, h):
    """Sprawdza, czy zdjęcie wymaga korekty proporcji."""
    return determine_target_format(w, h) == "błąd"

def get_target_canvas_size(w, h):
    """Oblicza wymiary płótna o proporcjach 10x13 lub 13x10, większe lub równe oryginalnym."""
    img_ratio = w / h
    if img_ratio > 1:  # poziom
        target_ratio = RATIO_13x10
    else:              # pion
        target_ratio = RATIO_10x13

    # Dostosuj wymiary tak, żeby zmieścić całe zdjęcie
    if img_ratio > target_ratio:
        new_w = w
        new_h = int(w / target_ratio)
    else:
        new_h = h
        new_w = int(h * target_ratio)

    return new_w, new_h, "13x10" if target_ratio == RATIO_13x10 else "10x13"

def pad_image(img):
    """Dodaje białe tło, by uzyskać docelowe proporcje."""
    orig_w, orig_h = img.size
    canvas_w, canvas_h, target_format = get_target_canvas_size(orig_w, orig_h)

    new_img = Image.new("RGB", (canvas_w, canvas_h), (255, 255, 255))
    offset = ((canvas_w - orig_w) // 2, (canvas_h - orig_h) // 2)
    new_img.paste(img, offset)
    return new_img, (orig_w, orig_h), (canvas_w, canvas_h), target_format

# Przetwarzanie zdjęć
for year in YEARS:
    src_path = os.path.join(SOURCE_ROOT, year)
    for root, _, files in os.walk(src_path):
        relative_path = os.path.relpath(root, SOURCE_ROOT)
        dest_dir = os.path.join(TARGET_ROOT, relative_path)
        os.makedirs(dest_dir, exist_ok=True)

        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_dir, file)

                try:
                    with Image.open(src_file) as img:
                        w, h = img.size
                        if needs_adjustment(w, h):
                            padded_img, orig_size, new_size, format_str = pad_image(img)
                            padded_img.save(dest_file)
                            report_data.append((src_file, f"{orig_size[0]}x{orig_size[1]}", f"{new_size[0]}x{new_size[1]}", format_str))
                        else:
                            format_str = determine_target_format(w, h)
                            report_data.append((src_file, f"{w}x{h}", "bez zmian", format_str))
                except Exception as e:
                    print(f"❌ Błąd przy pliku {src_file}: {e}")

# Zapis raportu CSV
with open(OUTPUT_CSV, "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(report_data)

print("✅ Gotowe. Raport znajduje się tutaj:", OUTPUT_CSV)