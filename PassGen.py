import random
import string
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import tkinter.font as font
import pyperclip

def generate_passphrase(num_words, separator, capitalize=False, digits=False):
    with open('words.txt', 'r') as f:
        word_list = f.readlines()
    word_list = [word.strip() for word in word_list]
    words = random.choices(word_list, k=num_words)
    if capitalize:
        words = [word.capitalize() for word in words]
    if digits:
        digit = random.randint(0, 9)
        words.append(str(digit))
    passphrase = separator.join(words)
    return passphrase

def generate_password(length, digits=True, symbols=True):
    characters = string.ascii_letters
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

def generate():
    global generated_label
    global generated_product
    global copy_button
    generated_product = ""
    if choice.get() == 0:
        num_words = int(entry.get())
        separator = separator_entry.get()
        capitalize = capitalize_check.get()
        digits = digits_check.get()
        generated_product = generate_passphrase(num_words, separator, capitalize=capitalize, digits=digits)
    elif choice.get() == 1:
        length = int(entry.get())
        digits = digits_check.get()
        symbols = symbols_check.get()
        generated_product = generate_password(length, digits=digits, symbols=symbols)
    generated_label.config(text="Generated: " + "*"*len(generated_product))
    copy_button.config(state="normal")

def reveal():
    global generated_label
    global generated_product
    if generated_label.cget('text') == 'Generated: ' + '*'*len(generated_product):
        generated_label.config(text="Generated: " + generated_product)
    else:
        generated_label.config(text="Generated: " + '*'*len(generated_product))


def copy_to_clipboard():
    global generated_product
    pyperclip.copy(generated_product)

root = tk.Tk()
root.title("Password/Passphrase Generator")
root.geometry("400x300")

frame = tk.Frame(root)
frame.pack(pady=10)

choice = tk.IntVar()
passphrase_button = ttk.Button(frame, text="Passphrase", command=lambda: choice.set(0))
password_button = ttk.Button(frame, text="Password", command=lambda: choice.set(1))
passphrase_button.grid(row=0, column=0, padx=5)
password_button.grid(row=0, column=1, padx=5)

entry_label = tk.Label(frame, text="Number of words/Length:")
entry_label.grid(row=1, column=0, pady=5)

entry = tk.Entry(frame)
entry.grid(row=1, column=1, pady=5)

separator_label = tk.Label(frame, text="Separator:\n(Fill out for passphrases only)")
separator_label.grid(row=2, column=0, pady=5)

separator_entry = tk.Entry(frame)
separator_entry.grid(row=2, column=1, pady=5)

capitalize_check = tk.BooleanVar()
capitalize_check.set(False)
capitalize_box = tk.Checkbutton(frame, text="Capitalize first letter of each word", variable=capitalize_check)
capitalize_box.grid(row=3, column=0, columnspan=2)

digits_check = tk.BooleanVar()
digits_check.set(False)
digits_box = tk.Checkbutton(frame, text="Include digits", variable=digits_check)
digits_box.grid(row=4, column=0, columnspan=2)

symbols_check = tk.BooleanVar()
symbols_check.set(False)
symbols_box = tk.Checkbutton(frame, text="Include symbols", variable=symbols_check)
symbols_box.grid(row=5, column=0, columnspan=2)

generate_button = ttk.Button(frame, text="Generate", command=generate)
generate_button.grid(row=6, column=0, columnspan=2, pady=10)

generated_label = tk.Label(frame, text="Generated: ")
generated_label.grid(row=7, column=0, columnspan=2)

reveal_button = ttk.Button(frame, text="Reveal", command=reveal)
reveal_button.grid(row=8, column=0, padx=5)

copy_button = ttk.Button(frame, text="Copy to clipboard", command=copy_to_clipboard, state="disabled")
copy_button.grid(row=8, column=1, padx=5)

root.mainloop()