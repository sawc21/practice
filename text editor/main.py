import tkinter as tk
from tkinter import ttk

class TextEditor(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        root = self.master

        # Layout config
        self.grid(sticky='nsew', padx=10, pady=10)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)  # Make row 1 (Text widget) expand

        # Top bar
        ttk.Label(self, text="Text Editor").grid(column=0, row=0, sticky='w')
        ttk.Button(self, text="Quit", command=root.destroy).grid(column=1, row=0, sticky='e')

        # Text widget
        widget = tk.Text(self, wrap="word")
        widget.grid(row=1, column=0, columnspan=2, sticky="nsew")  # Span two columns


        #scroll bar
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=widget.yview)
        scrollbar.grid(row=1, column=2, sticky="ns")
        widget.configure(yscrollcommand=scrollbar.set)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Text Editor")
    root.geometry("300x100")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    app = TextEditor(root)
    root.mainloop()
