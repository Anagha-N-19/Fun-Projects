import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = tk.Tk()
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
window.title("Anagha's text editor")


def opener():
    path_reqd = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if path_reqd is None:
        return
    text_wnd.delete("1.0", tk.END)  # deleting contents of text widget
    with open(path_reqd, "r", encoding="utf-8") as fin:
        text = fin.read()
        text_wnd.insert(tk.END, text)
    window.title(f"Anagha's text editor : {path_reqd}")


def saver():
    path_reqd = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if path_reqd is None:
        return
    with open(path_reqd, "w", encoding="utf-8") as fout:
        text = text_wnd.get("1.0", tk.END)
        fout.write(text)
    window.title(f"Anagha's text editor : {path_reqd}")


text_wnd = tk.Text(window)

req_buttons = tk.Frame(window, relief=tk.GROOVE, bd=3)
open_button = tk.Button(req_buttons, text="Open file", command=opener)
save_as_button = tk.Button(req_buttons, text="Save as",command = saver)
open_button.grid(row=0, column=0, sticky="ew", padx=8, pady=8)
save_as_button.grid(row=1, column=0, sticky="ew", padx=8, pady=10)
req_buttons.grid(row=0, column=0, sticky="ns")
text_wnd.grid(row=0, column=1, sticky="nsew")

window.mainloop()
