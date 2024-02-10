# from rembg import remove

# input_p = 'nameLogo.png'
# output_p = 'output1.png'

# with open(input_p, 'rb') as input_r:
#     with open(output_p, 'wb') as output_w:
#         input = input_r.read()
#         output = remove(input)
#         output_w.write(output)
#!/usr/bin/env python3

import io
import os
from tkinter import *
from tkinter import filedialog, ttk

import numpy as np
from PIL import Image
from rembg.bg import remove


class BackJackr:
    def __init__(self, root):
        root.title("BackJackr")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Label(mainframe, text='Input Image').grid(column=1, row=1, sticky=(N, E))

        self.input_path = StringVar()
        ttk.Button(mainframe, text="Select", command=self.get_inputfilename).grid(column=2, row=1, sticky=(N, E))

        ttk.Label(mainframe, text='Output Image').grid(column=1, row=2, sticky=(N, E))

        self.output_path = StringVar()
        ttk.Button(mainframe, text="Select", command=self.get_outputfilename).grid(column=2, row=2, sticky=(N, E))

        ttk.Button(mainframe, text="Process", command=self.process).grid(column=2, row=3, sticky=(N, E))

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        root.bind("<Return>", self.process)

    def get_inputfilename(self, *args):
        self.input_path.set(filedialog.askopenfilename())

    def get_outputfilename(self, *args):
        self.output_path.set(filedialog.asksaveasfilename())

    def generate_default_output_filename(self):
        input_file_path = self.input_path.get()
        if input_file_path:
            input_file_name = os.path.basename(input_file_path)
            root, ext = os.path.splitext(input_file_name)
            default_output_file_name = f"{root}_output.png"
            self.output_path.set(os.path.join(os.path.dirname(input_file_path), default_output_file_name))
    
    def process(self, *args):
        try:
            print(self.input_path.get())
            # print(self.output_path.get())
            f = np.fromfile(self.input_path.get())
            result = remove(f)
            img = Image.open(io.BytesIO(result)).convert("RGBA")
            img.save(self.output_path.get())
        except Exception: 
            pass

root = Tk()
BackJackr(root)
root.mainloop()