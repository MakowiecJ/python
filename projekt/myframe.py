import tkinter as tk
from t9 import T9


class MyFrame(tk.Frame):

    def __init__(self, root, words):
        tk.Frame.__init__(self, root)
        self.t9 = T9(words)
        self.current_node = self.t9.get_root()

        button_frame = tk.Frame(self)

        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)

        button_frame.rowconfigure(0, weight=3)
        button_frame.rowconfigure(1, weight=3)
        button_frame.rowconfigure(2, weight=3)
        button_frame.rowconfigure(3, weight=3)

        self.label1_text = tk.StringVar()
        self.label2_text = tk.StringVar()

        self.label1 = tk.Label(self, textvariable=self.label1_text)
        self.label2 = tk.Label(self, textvariable=self.label2_text)

        self.label1.pack(padx=20, pady=20)
        self.label2.pack(padx=20, pady=20)

        self.ok_button = tk.Button(button_frame, height=4, width=4, text="OK", command=self.ok_clicked)
        self.del_button = tk.Button(button_frame, height=4, width=4, text="DEL", command=self.del_clicked)
        self.reset_button = tk.Button(button_frame, height=4, width=4, text="RESET", command=self.reset_clicked)
        self.change_button = tk.Button(button_frame, height=4, width=4, text="1\nchange", command=self.change_clicked)
        self.b2 = tk.Button(button_frame, height=4, width=4, text="2\nabc", command=self.b2_clicked)
        self.b3 = tk.Button(button_frame, height=4, width=4, text="3\ndef", command=self.b3_clicked)
        self.b4 = tk.Button(button_frame, height=4, width=4, text="4\nghi", command=self.b4_clicked)
        self.b5 = tk.Button(button_frame, height=4, width=4, text="5\njkl", command=self.b5_clicked)
        self.b6 = tk.Button(button_frame, height=4, width=4, text="6\nmno", command=self.b6_clicked)
        self.b7 = tk.Button(button_frame, height=4, width=4, text="7\npqrs", command=self.b7_clicked)
        self.b8 = tk.Button(button_frame, height=4, width=4, text="8\ntuv", command=self.b8_clicked)
        self.b9 = tk.Button(button_frame, height=4, width=4, text="9\nwxyz", command=self.b9_clicked)

        self.orig_color = self.change_button.cget("background")

        self.reset_button.grid(row=0, column=0, sticky=tk.W + tk.E + tk.S)
        self.ok_button.grid(row=0, column=1, sticky=tk.W + tk.E + tk.S)
        self.del_button.grid(row=0, column=2, sticky=tk.W + tk.E + tk.S)
        self.change_button.grid(row=1, column=0, sticky=tk.W + tk.E + tk.S)
        self.b2.grid(row=1, column=1, sticky=tk.W + tk.E + tk.S)
        self.b3.grid(row=1, column=2, sticky=tk.W + tk.E + tk.S)
        self.b4.grid(row=2, column=0, sticky=tk.W + tk.E + tk.S)
        self.b5.grid(row=2, column=1, sticky=tk.W + tk.E + tk.S)
        self.b6.grid(row=2, column=2, sticky=tk.W + tk.E + tk.S)
        self.b7.grid(row=3, column=0, sticky=tk.W + tk.E + tk.S)
        self.b8.grid(row=3, column=1, sticky=tk.W + tk.E + tk.S)
        self.b9.grid(row=3, column=2, sticky=tk.W + tk.E + tk.S)

        button_frame.pack(fill='both', padx=10, pady=10)

    def ok_clicked(self):
        if len(self.current_node.words) > 0:
            self.label2_text.set(self.label2_text.get() + " " + self.label1_text.get())
            self.label1_text.set("")
            self.current_node = self.t9.get_root()
        self.check_words()

    def del_clicked(self):
        self.current_node = self.t9.get_root()
        self.label1_text.set("")
        self.check_words()

    def reset_clicked(self):
        self.current_node = self.t9.get_root()
        self.label1_text.set("")
        self.label2_text.set("")
        self.check_words()

    def change_clicked(self):
        if self.current_node is not None:
            if len(self.current_node.words) > 1:
                self.current_node.words.append(self.current_node.words.pop(0))
                self.label1_text.set(self.current_node.words[0])

    def b2_clicked(self):
        if self.current_node.node_dict["b2"] is None:
            self.label1_text.set("No such word in the dictionary")
            return
        self.current_node = self.current_node.node_dict["b2"]
        if self.current_node.words:
            self.label1_text.set(self.current_node.words[0])
        else:
            self.label1_text.set(self.label1_text.get() + "a")
        self.check_words()

    def b3_clicked(self):
        if self.current_node.node_dict["b3"] is None:
            self.label1_text.set("No such word in the dictionary")
            return
        self.current_node = self.current_node.node_dict["b3"]
        if self.current_node.words:
            self.label1_text.set(self.current_node.words[0])
        else:
            self.label1_text.set(self.label1_text.get() + "d")
        self.check_words()

    def b4_clicked(self):
        if self.current_node.node_dict["b4"] is None:
            self.label1_text.set("No such word in the dictionary")
            return
        self.current_node = self.current_node.node_dict["b4"]
        if self.current_node.words:
            self.label1_text.set(self.current_node.words[0])
        else:
            self.label1_text.set(self.label1_text.get() + "g")
        self.check_words()

    def b5_clicked(self):
        if self.current_node.node_dict["b5"] is None:
            self.label1_text.set("No such word in the dictionary")
            return
        self.current_node = self.current_node.node_dict["b5"]
        if self.current_node.words:
            self.label1_text.set(self.current_node.words[0])
        else:
            self.label1_text.set(self.label1_text.get() + "j")
        self.check_words()

    def b6_clicked(self):
        if self.current_node.node_dict["b6"] is None:
            self.label1_text.set("No such word in the dictionary")
            return
        self.current_node = self.current_node.node_dict["b6"]
        if self.current_node.words:
            self.label1_text.set(self.current_node.words[0])
        else:
            self.label1_text.set(self.label1_text.get() + "m")
        self.check_words()

    def b7_clicked(self):
        if self.current_node.node_dict["b7"] is None:
            self.label1_text.set("No such word in the dictionary")
            return
        self.current_node = self.current_node.node_dict["b7"]
        if self.current_node.words:
            self.label1_text.set(self.current_node.words[0])
        else:
            self.label1_text.set(self.label1_text.get() + "p")
        self.check_words()

    def b8_clicked(self):
        if self.current_node.node_dict["b8"] is None:
            self.label1_text.set("No such word in the dictionary")
            return
        self.current_node = self.current_node.node_dict["b8"]
        if self.current_node.words:
            self.label1_text.set(self.current_node.words[0])
        else:
            self.label1_text.set(self.label1_text.get() + "t")
        self.check_words()

    def b9_clicked(self):
        if self.current_node.node_dict["b9"] is None:
            self.label1_text.set("No such word in the dictionary")
            return
        self.current_node = self.current_node.node_dict["b9"]
        if self.current_node.words:
            self.label1_text.set(self.current_node.words[0])
        else:
            self.label1_text.set(self.label1_text.get() + "w")
        self.check_words()

    def check_words(self):
        if len(self.current_node.words) > 0:
            self.ok_button.configure(bg="green")
        else:
            self.ok_button.configure(bg=self.orig_color)

        if len(self.current_node.words) > 1:
            self.change_button.configure(bg="green")
        else:
            self.change_button.configure(bg=self.orig_color)
