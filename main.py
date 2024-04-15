import tkinter as tk
from PIL import Image, ImageTk
import os

class ImageQuestionApp:
    def __init__(self, root, image_folder):
        self.organized = {}
        self.organized["subject_present"] = []
        self.organized["no_subject"] = []

        self.root = root
        self.image_folder = image_folder
        self.image_list = os.listdir(image_folder)
        self.current_index = 0

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.display_image()

        self.question_label = tk.Label(root, text="Is there a subject in this image?")
        self.question_label.pack()

        self.question_label = tk.Label(root, text="Left arrow for yes right arrow for no")
        self.question_label.pack()

        self.root.bind("<Left>", lambda event: self.next_image(event, choice=1))
        self.root.bind("<Right>", lambda event: self.next_image(event, choice=0))
        self.root.bind("<Up>", self.stop)

    def display_image(self):
        image_path = os.path.join(self.image_folder, self.image_list[self.current_index])
        image = Image.open(image_path)
        image.thumbnail((400, 400))
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(200, 200, image=self.photo)

    def prev_image(self, event):
        self.current_index = (self.current_index - 1) % len(self.image_list)
        self.canvas.delete("all")
        self.display_image()

    def next_image(self, event, choice):
        if choice == 1:
            self.organized["subject_present"].append(self.image_list[self.current_index])
        else:
            self.organized["no_subject"].append(self.image_list[self.current_index])
        self.current_index = (self.current_index + 1) % len(self.image_list)
        self.canvas.delete("all")
        self.display_image()

    def stop(self, event):
        print(self.organized)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageQuestionApp(root, "/Users/amoghpanhale/Downloads/data/training_images/")
    root.mainloop()
