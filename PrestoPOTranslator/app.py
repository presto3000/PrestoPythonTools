import csv
import os
import polib
import tkinter as tk
from tkinter import messagebox

PO_FILE = "Game.po"
CSV_FOLDER = "TranslationData"

LANG_MAP = {
    "Polish": "Polish (pl)",
    "French": "French (fr)",
    "German": "German (de)",
    "Spanish": "Spanish (es)",
    "Italian": "Italian (it)"
}


def load_translations(folder_path, language_column):
    translations = {}

    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, encoding="utf-8") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    key = row.get("Key", "").strip()
                    value = row.get(language_column, "").strip()

                    if key and value:
                        translations[key] = value

    return translations


def translate(language_column):
    try:
        translations = load_translations(CSV_FOLDER, language_column)

        po = polib.pofile(PO_FILE)

        updated = 0

        for entry in po:
            if entry.msgctxt:
                key = entry.msgctxt.split(",")[-1]

                if key in translations:
                    if entry.msgstr != translations[key]:
                        entry.msgstr = translations[key]
                        updated += 1

        po.save(PO_FILE)

        messagebox.showinfo("Done", f"Updated {updated} entries!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("PrestoPO Translator ver 0.0.1")
root.geometry("300x300")

tk.Label(root, text="Select Language", font=("Arial", 14)).pack(pady=10)

for lang, column in LANG_MAP.items():
    tk.Button(
        root,
        text=lang,
        width=20,
        command=lambda c=column: translate(c)
    ).pack(pady=5)

root.mainloop()