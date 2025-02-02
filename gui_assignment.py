import tkinter as tk
from tkinter import font as tkfont


class mainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PredictURL, PastPredict):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Phisherman's Enemy", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Predict a URL", command=lambda: controller.show_frame("PredictURL"))
        button2 = tk.Button(self, text="Show Past Predictions", command=lambda: controller.show_frame("PastPredict"))
        button1.pack()
        button2.pack()


class PredictURL(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Prints out the wording title in the application
        label = tk.Label(self, text="Enter a URL to predict if its a phishing site:", font=controller.title_font)
        label1 = tk.Label(self, text="", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1.pack(side="top", fill="x", pady=10)
        tk.Label(self, text="URL")

        # Creates a variable val to store the radio btn value 1/2/3 which user selects
        val = tk.StringVar(self, "1")

        values = {"Gradient Boosting Classifier": "1",
                  "XGB Classifier": "2",
                  "Random Forest Classifier": "3"}

        # Loops through the dictionary and create the radio buttons
        for (text, value) in values.items():
            tk.Radiobutton(self, text=text, variable=val, value=value).pack(side=tk.TOP, ipady=10)
        entry_user = tk.Entry(self, width=20, cursor="xterm")
        entry_user.pack()

        button3 = tk.Button(self, text='Predict', command=lambda: getpredict())
        button4 = tk.Button(self, text="Back to main", command=lambda: controller.show_frame("StartPage"))
        button3.pack()
        button4.pack()

        # Place in the code for predict function
        def getpredict():
            entry1 = entry_user.get()
            model = val.get()
            print(entry1)
            print(model)
            # Only if predict function return a value
            label1.config(text="Predicted Please proceed to view it via pastPredictions")


class PastPredict(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Past Predictions", font=controller.title_font)
        label1 = tk.Label(self, text="", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text='Load Server', command=lambda: loadServer())
        button2 = tk.Button(self, text="Back to main", command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        button2.pack()

        # Place in the code for predict function
        def loadServer():
            print("Call for load server function")
            label1.config(text="Go to http://127.0.0.1/test to view the report")


if __name__ == "__main__":
    app = mainApp()
    app.title("Phisherman's Enemy")
    app.mainloop()


