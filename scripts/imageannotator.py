import os
import sys
import tkinter as tk
from PIL import Image, ImageTk
from tesserocr import PyTessBaseAPI


class TextExtractor:
    def __init__(self, master, folder_path):
        self.master = master
        self.master.title("Image Text Extractor")

        self.label = tk.Label(master, text="Enter the text from the image:")
        self.label.pack()

        self.text_entry = tk.Entry(master, width=50)
        self.text_entry.pack()
        self.text_entry.bind("<Return>", self.save_text)

        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack()

        self.images = []
        self.current_image = None
        self.current_image_index = 0

        self.folder_path = folder_path

        # Bind Escape key to close the program
        self.master.bind("<Escape>", lambda event: self.master.quit())

        # self.api = PyTessBaseAPI(
        #     path="/Users/roy_shilkrot/Downloads/scoresight/tesseract/tessdata",
        #     lang="daktronics",
        # )
        # # single word PSM
        # self.api.SetPageSegMode(8)

        master.after(100, self.load_images)

    def display_image(self, image_path):
        img = Image.open(image_path)
        img.thumbnail((500, 500), Image.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(img)
        self.canvas.create_image(250, 250, image=self.tk_image)
        self.master.title(
            f"Image Text Extractor - Image {self.current_image_index + 1}/{len(self.images)}"
        )

    def save_text(self, event=None):
        text = self.text_entry.get()
        if text and self.current_image:
            base_name = os.path.splitext(self.current_image)[0]
            with open(base_name + ".gt.txt", "w") as file:
                file.write(text)
            self.next_image()

    def next_image(self):
        self.current_image_index += 1
        if self.current_image_index < len(self.images):
            self.current_image = self.images[self.current_image_index]
            self.display_image(self.current_image)
        else:
            self.master.quit()

    def load_images(self):
        for file in os.listdir(self.folder_path):
            if file.lower().endswith((".png", ".jpg", ".jpeg")):
                # check there isn't a ".gt.txt" file for this image
                base_name = os.path.splitext(file)[0]
                if not os.path.exists(
                    os.path.join(self.folder_path, base_name + ".gt.txt")
                ):
                    self.images.append(os.path.join(self.folder_path, file))
        # sort the images by creation time
        self.images.sort(key=lambda x: os.path.getctime(x))
        if self.images:
            self.current_image = self.images[0]
            self.display_image(self.images[0])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the folder path as a command line argument.")
        sys.exit(1)

    folder_path = sys.argv[1]

    root = tk.Tk()
    app = TextExtractor(root, folder_path)
    root.mainloop()
