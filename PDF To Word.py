import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2docx import Converter
import os

def convert_pdf_to_word():
    pdf_file = filedialog.askopenfilename(title="Select PDF File", filetypes=[("PDF Files", "*.pdf")])
    
    if not pdf_file:
        return

    output_file = filedialog.asksaveasfilename(
        defaultextension=".docx",
        filetypes=[("Word Document", "*.docx")],
        title="Save as"
    )

    if not output_file:
        return

    try:
        converter = Converter(pdf_file)
        converter.convert(output_file, start=0, end=None)
        converter.close()
        messagebox.showinfo("Success", f"Conversion successful!\nSaved as:\n{output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

# GUI Setup
root = tk.Tk()
root.title("PDF to Editable Word Converter")
root.geometry("400x200")

label = tk.Label(root, text="PDF to Word Converter", font=("Helvetica", 16))
label.pack(pady=20)

convert_button = tk.Button(root, text="Select PDF & Convert", command=convert_pdf_to_word, font=("Helvetica", 12))
convert_button.pack(pady=10)

root.mainloop()
