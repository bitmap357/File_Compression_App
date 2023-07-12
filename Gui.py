import tkinter as tk
from compressionmodule import compress, decompress
from tkinter import filedialog


def open_file():
    filename = filedialog.askopenfilename(title='Select a file to compress')
    print(filename)
    return filename


def compression(i, o):
    compress(i, o)


def decompression(i, o):
    decompress(i, o)


window = tk.Tk()
window.title("Compression Engine")
window.geometry("600x400")

# input_entry = tk.Entry(window)
# output_entry = tk.Entry(window)
#
input_label = tk.Label(window, text='File Compression Engine')
input_label.grid(row=0, column=0)
#
# output_label = tk.Label(window, text='Name of the compressed file')
# output_label.grid(row=0, column=0)
# output_entry.grid(row=1, column=0)

compress_button = tk.Button(window, text='COMPRESS A FILE',
                            command=lambda: compression(open_file(), 'compressed_output2.txt'))
compress_button.grid(row=1, column=1)

decompress_button = tk.Button(window, text='DECOMPRESS A FILE',
                              command=lambda: decompression(open_file(), 'decompressed_output2.txt'))
decompress_button.grid(row=2, column=1)


window.mainloop()
