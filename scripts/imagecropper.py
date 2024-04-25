import os
import tkinter as tk
from PIL import Image, ImageTk
import sys
import uuid
import sys


class ImageCropper:
    def __init__(self, master):
        self.master = master
        self.master.focus_force()  # Add this line to give focus to the window
        self.canvas = tk.Canvas(master, cursor="cross")
        self.canvas.pack(fill="both", expand=True)

        self.images = []
        self.current_image = None
        self.start_x = None
        self.start_y = None
        self.rect = None
        master.after(100, self.load_images, sys.argv[1])
        self.current_image_index = 0

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        master.bind("<Right>", self.next_image)
        master.bind("n", self.next_image)
        master.bind("<Left>", self.previous_image)
        master.bind("p", self.previous_image)
        master.bind("<Configure>", self.on_window_resize)

        # Set the default window width to 640
        master.geometry("640x480")
        master.bind("q", self.close_program)

        master.bind("<Escape>", self.cancel_rect)

    def cancel_rect(self, event):
        if self.rect:
            self.canvas.delete(self.rect)
            self.rect = None

    def close_program(self, event):
        self.master.destroy()

    def on_window_resize(self, event=None):
        if self.current_image_index is not None:
            self.display_image(self.current_image_index)

    def load_images(self, folder_path):
        if not os.path.exists(folder_path):
            raise ValueError("The specified folder does not exist.")

        for file in os.listdir(folder_path):
            if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
                self.images.append(Image.open(os.path.join(folder_path, file)))

        if self.images:
            self.display_image(0)

    def display_image(self, index):
        if 0 <= index < len(self.images):
            self.current_image_index = index
            self.current_image = self.images[index]
            original_image = self.images[index]

            window_width = self.master.winfo_width()
            window_height = self.master.winfo_height()
            if window_width > 1 and window_height > 1:
                img_width, img_height = original_image.size
                scale_width = window_width / img_width
                scale_height = window_height / img_height
                scale = min(scale_width, scale_height)
                new_size = (int(img_width * scale), int(img_height * scale))

                resized_image = original_image.resize(new_size, Image.LANCZOS)
                self.tk_image = ImageTk.PhotoImage(resized_image)
                self.canvas.create_image(0, 0, image=self.tk_image, anchor="nw")
                self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def on_button_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        if not self.rect:
            self.rect = self.canvas.create_rectangle(
                self.start_x, self.start_y, 1, 1, outline="red"
            )

    def on_move_press(self, event):
        curX, curY = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)

    def on_button_release(self, event):
        end_x, end_y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
        self.save_crop(self.start_x, self.start_y, end_x, end_y)
        self.start_x = None
        self.start_y = None
        self.rect = None

    def canvas_to_image_coords(self, x, y):
        img_width, img_height = self.current_image.size
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        # Calculate the scaling factor
        scale = max(img_width / canvas_width, img_height / canvas_height)

        # Convert the coordinates from canvas to image
        image_x = int(x * scale)
        image_y = int(y * scale)

        return image_x, image_y

    def save_crop(self, x1, y1, x2, y2):
        if self.current_image is not None:
            # Normalize the coordinates to ensure they are within the image bounds
            img_width, img_height = self.current_image.size
            # transform to image coordinates
            x1, y1 = self.canvas_to_image_coords(x1, y1)
            x2, y2 = self.canvas_to_image_coords(x2, y2)
            # make sure x1,y1 is top left and x2,y2 is bottom right
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            # make sure the coordinates are within the image bounds
            x1, y1 = max(0, x1), max(0, y1)
            x2, y2 = min(img_width, x2), min(img_height, y2)

            # Ensure valid crop area
            if x2 > x1 and y2 > y1:
                cropped = self.current_image.crop((x1, y1, x2, y2))
                unique_id = str(uuid.uuid4())[:8]  # Generate a unique ID
                folder_path = os.path.dirname(self.current_image.filename)
                out_folder_path = os.path.join(folder_path, "out")
                os.makedirs(out_folder_path, exist_ok=True)
                save_path = os.path.join(out_folder_path, f"cropped_{unique_id}.png")
                cropped.save(save_path)

    def next_image(self, event):
        if self.current_image_index < len(self.images) - 1:
            self.display_image(self.current_image_index + 1)

    def previous_image(self, event):
        if self.current_image_index > 0:
            self.display_image(self.current_image_index - 1)


if len(sys.argv) < 2:
    print("Please provide the input folder as the first argument.")
    sys.exit(1)

root = tk.Tk()
app = ImageCropper(root)
root.mainloop()
