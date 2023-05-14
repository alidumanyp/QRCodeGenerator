import tkinter as tk
import qrcode
from PIL import ImageTk


class QRCodeGenerator(tk.Frame):
    def __init__(self, window=None):
        super().__init__(window)
        self.window = window
        self.window.title("QR Code Generator")
        self.pack()
        self.qrcode_label = None
        self.generate_button = None
        self.link_entry = None
        self.link_label = None

        self.create_widgets()

    def create_widgets(self):
        self.link_label = tk.Label(self, text="Link:")
        self.link_label.pack(side="left", )

        self.link_entry = tk.Entry(self, width=50)
        self.link_entry.pack(side="left")

        self.generate_button = tk.Button(self, text="generate", command=self.generate_qrcode)
        self.generate_button.pack(side="right")

        self.qrcode_label = tk.Label(self)
        self.qrcode_label.pack()

    def generate_qrcode(self):
        link = self.link_entry.get()
        img_qr = qrcode.make(link)
        img_display = ImageTk.PhotoImage(img_qr)

        self.qrcode_label.config(image=img_display)
        self.qrcode_label.image = img_display


if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGenerator(window=root)
    app.mainloop()
