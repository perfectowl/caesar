import tkinter as tk
from tkinter import ttk
from collections import Counter

def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():  # Только буквы
            start = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - start + shift) % 26 + start))
        else:
            result.append(char)
    return ''.join(result)

def break_best(text):
    english_letter_frequencies = {
        'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
        'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
        'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
        'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15,
        'Q': 0.10, 'Z': 0.07
    }
    filtered_text = ''.join(filter(str.isalpha, text))

    if not filtered_text:
        return "Текста для обработки нет >:(", None

    best_shift = 0
    best_score = 0
    best_decryption = ""

    for shift in range(26):
        decrypted_text = caesar_cipher(filtered_text, -shift)
        letter_counts = Counter(decrypted_text.upper())
        total_letters = sum(letter_counts.values())

        # Вычисляем частотное соответствие
        score = 0
        for letter, count in letter_counts.items():
            frequency = (count / total_letters) * 100
            score += frequency * english_letter_frequencies.get(letter, 0)

        if score > best_score:
            best_score = score
            best_shift = shift
            best_decryption = ''.join(
                caesar_cipher(text, -shift)  # Декодируем исходный текст
            )

    return best_decryption, best_shift

def encrypt_message():
    text = message_input.get("1.0", tk.END).strip()
    try:
        shift = int(shift_input.get())
    except ValueError:
        result_output.set("Неверное значение шага!")
        return
    encrypted_text = caesar_cipher(text, shift)
    result_output.set(encrypted_text)

def decrypt_message():
    text = encrypted_input.get("1.0", tk.END).strip()
    try:
        shift = int(shift_input.get())
    except ValueError:
        decrypted_output.set("Неверное значение шага!")
        return
    decrypted_text = caesar_cipher(text, -shift)
    decrypted_output.set(decrypted_text)

def break_from_message():
    text = message_input.get("1.0", tk.END).strip()
    if not text:
        break_output.set("Введите сообщение для взлома!")
        return
    best_decryption, best_shift = break_best(text)
    if best_shift is not None:
        break_output.set(f"Лучший вариант (Шаг {best_shift}):\n{best_decryption}")
    else:
        break_output.set("Подходящий вариант не найден. :(")

# def break_from_result():
#     """Взлом шифра из зашифрованного текста."""
#     text = result_output.get()
#     if not text:
#         break_output.set("Нет текста для взлома!")
#         return
#     best_decryption, best_shift = break_best(text)
#     if best_shift is not None:
#         break_output.set(f"Лучший вариант (Шаг {best_shift}):\n{best_decryption}")
#     else:
#         break_output.set("Подходящий вариант не найден. :(")

def copy(content):
    root.clipboard_clear()
    root.clipboard_append(content)
    root.update()

def paste(entry):
    entry.delete("1.0", tk.END)
    entry.insert("1.0", root.clipboard_get())

# Создание окна приложения
root = tk.Tk()
root.title("Шифр Цезаря")
root.geometry("600x700")

# Ввод сообщения
message_frame = ttk.Frame(root)
message_frame.pack(pady=5, fill=tk.X)
ttk.Label(message_frame, text="Введите сообщение для шифрования/взлома:").pack(anchor=tk.W)
message_input = tk.Text(message_frame, height=4, wrap=tk.WORD)
message_input.pack(fill=tk.BOTH, padx=5, expand=True)
ttk.Button(message_frame, text="Копировать", command=lambda: copy(message_input.get("1.0", tk.END).strip())).pack(side=tk.LEFT, padx=2)
ttk.Button(message_frame, text="Вставить", command=lambda: paste(message_input)).pack(side=tk.LEFT, padx=2)

# Ввод значения сдвига
ttk.Label(root, text="Введите длину шага:").pack(pady=5)
shift_input = ttk.Entry(root, width=10)
shift_input.pack(pady=5)

# Кнопка для шифрования
encrypt_button = ttk.Button(root, text="Зашифровать!!", command=encrypt_message)
encrypt_button.pack(pady=5)

# Поле для вывода зашифрованного текста
result_frame = ttk.Frame(root)
result_frame.pack(pady=5, fill=tk.X)
result_output = tk.StringVar()
result_label = ttk.Label(result_frame, textvariable=result_output, foreground="blue", wraplength=550, anchor=tk.W, justify=tk.LEFT)
result_label.pack(fill=tk.BOTH, padx=5, expand=True)
ttk.Button(result_frame, text="Копировать", command=lambda: copy(result_output.get())).pack(side=tk.LEFT, padx=5)

# Ввод зашифрованного сообщения
encrypted_frame = ttk.Frame(root)
encrypted_frame.pack(pady=5, fill=tk.X)
ttk.Label(encrypted_frame, text="Введите сообщение для дешифрования:").pack(anchor=tk.W)
encrypted_input = tk.Text(encrypted_frame, height=4, wrap=tk.WORD)
encrypted_input.pack(fill=tk.BOTH, padx=5, expand=True)
ttk.Button(encrypted_frame, text="Копировать", command=lambda: copy(encrypted_input.get("1.0", tk.END).strip())).pack(side=tk.LEFT, padx=2)
ttk.Button(encrypted_frame, text="Вставить", command=lambda: paste(encrypted_input)).pack(side=tk.LEFT, padx=2)

# Кнопка для дешифрования
decrypt_button = ttk.Button(root, text="Расшифровать!!1", command=decrypt_message)
decrypt_button.pack(pady=5)

# Поле для вывода расшифрованного текста
decrypted_output = tk.StringVar()
decrypted_label = ttk.Label(root, textvariable=decrypted_output, foreground="green", wraplength=550, anchor=tk.W, justify=tk.LEFT)
decrypted_label.pack(fill=tk.BOTH, padx=5, expand=True)

# Кнопки для взлома шифра
break_button_message = ttk.Button(root, text="Взломать текст из первого поля ввода", command=break_from_message)
break_button_message.pack(pady=5)

# break_button_result = ttk.Button(root, text="Взломать текст из поля вывода", command=break_from_result)
# break_button_result.pack(pady=5)

# Поле для вывода результата взлома
break_output = tk.StringVar()
break_label = ttk.Label(root, textvariable=break_output, justify="left", foreground="blue", wraplength=550, anchor=tk.W)
break_label.pack(fill=tk.BOTH, padx=5, expand=True)

# Запуск приложения
root.mainloop()
