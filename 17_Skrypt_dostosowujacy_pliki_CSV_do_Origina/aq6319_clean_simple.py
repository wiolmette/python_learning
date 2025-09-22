import os
import re
import argparse
import pandas as pd

# wzorzec: "liczba,liczba" (także w notacji naukowej, np. 1.23E-07)
num_line_re = re.compile(
    r'^\s*[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[Ee][+-]?\d+)?\s*,\s*[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[Ee][+-]?\d+)?\s*$'
)

def find_data_start(lines):
    for i, ln in enumerate(lines):
        if num_line_re.match(ln):
            return i
    raise ValueError("Nie znaleziono linii z danymi numerycznymi")

def clean_file(src_path, dst_path):
    with open(src_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    start = find_data_start(lines)
    cleaned = [re.sub(r'\s*,\s*', ',', ln.strip()) for ln in lines[start:] if ln.strip()]

    # Walidacja przez pandas
    from io import StringIO
    df = pd.read_csv(StringIO("\n".join(cleaned)), header=None)
    df = df.dropna()

    # Zapis: same liczby, przecinek, brak nagłówka
    df.to_csv(dst_path, index=False, header=False, sep=",", lineterminator="\r\n")

def main():
    ap = argparse.ArgumentParser(description="Czyszczenie plików CSV z AQ6319 (same liczby, przecinek).")
    ap.add_argument("source", help="Plik lub folder z plikami")
    ap.add_argument("-o", "--output", default="clean", help="Folder wyjściowy (domyślnie: clean)")
    ap.add_argument("--ext", default=".csv", help="Rozszerzenie plików wejściowych (domyślnie .csv)")
    ap.add_argument("--name-suffix", default="_clean", help="Sufiks dla wynikowych plików (domyślnie _clean)")
    args = ap.parse_args()

    src = args.source
    os.makedirs(args.output, exist_ok=True)

    def process_file(path):
        base = os.path.basename(path)
        name, _ = os.path.splitext(base)
        if name.endswith(args.name_suffix):
            print(f"SKIP: {path} (już wyczyszczony)")
            return
        dst = os.path.join(args.output, f"{name}{args.name_suffix}.csv")
        clean_file(path, dst)
        print(f"OK  : {path} -> {dst}")

    if os.path.isfile(src):
        process_file(src)
    else:
        for root, _, files in os.walk(src):
            for fn in files:
                if fn.lower().endswith(args.ext.lower()):
                    process_file(os.path.join(root, fn))

if __name__ == "__main__":
    main()