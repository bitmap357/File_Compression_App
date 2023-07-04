import tkinter as tk
from compressionmodule import compress, decompress


def compression(i, o):
    compress(i, o)


window = tk.Tk()
window.title("Compression Engine")
window.geometry("600x400")


window.mainloop()
