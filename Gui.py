import tkinter as tk
from compressionmodule import compress, decompress


def compression(i, o):
    compress(i, o)


window = tk.Tk()
window.title("Compression Engine")
window.geometry("600x400")

input_entry = tk.Entry(window)
output_entry = tk.Entry(window)

input_label = tk.Label(window, text='File to be compressed')
input_label.grid(row=0, column=0)
input_entry.grid(row=0, column=1)

output_label = tk.Label(window, text='Name of the compressed file')
output_label.grid(row=0, column=0)
output_entry.grid(row=1, column=0)

compress_button = tk.Button(window, text='COMPRESS')
compress_button.grid(row=2, column=1)

window.mainloop()
