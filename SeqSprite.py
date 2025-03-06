import os
import glob
from tkinter import Tk, filedialog, Button, Label, messagebox
from PIL import Image, ImageTk

# Function to find bounding box of non-transparent pixels
def find_bounding_box(image):
    return image.getbbox()

def create_sprite_sheet(input_folder, output_file):
    images = sorted(glob.glob(os.path.join(input_folder, '*.png')))
    if not images:
        messagebox.showerror('Error', 'No PNG images found in selected folder')
        return

    # Open first image to get dimensions
    first_img = Image.open(images[0])
    img_width, img_height = first_img.size

    # Calculate sprite sheet dimensions
    spacing = 1
    num_frames = len(images)
    sheet_width = img_width + 2 * spacing
    sheet_height = num_frames * (img_height + spacing)

    # Create sprite sheet
    sprite_sheet = Image.new('RGBA', (sheet_width, sheet_height), (0, 0, 0, 0))

    # Paste images with spacing
    for i, img_path in enumerate(images):
        img = Image.open(img_path)
        x = spacing
        y = i * (img_height + spacing) + spacing
        sprite_sheet.paste(img, (x, y))

    # Save and show success message
    sprite_sheet.save(output_file)
    messagebox.showinfo('Success', f'Sprite sheet created successfully with {num_frames} frames!')

# GUI App
class SpriteSheetApp:
    def __init__(self, master):
        self.master = master
        master.title("Sprite Sheet Maker")
        master.geometry("300x150")

        self.label = Label(master, text="Select your PNG sequence folder.")
        self.label.pack(pady=10)

        self.select_folder_btn = Button(master, text="Select Folder", command=self.select_folder)
        self.select_folder_btn.pack(pady=5)

        self.create_sprite_btn = Button(master, text="Create Sprite Sheet", command=self.create_sprite_sheet)
        self.create_sprite_btn.pack(pady=5)

    def select_folder(self):
        global input_folder
        input_folder = filedialog.askdirectory()
        print("Selected Folder:", input_folder)

    def create_sprite_sheet(self):
        output_file = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[('PNG Files', '*.png')])
        if output_file:
            if 'input_folder' in globals():
                create_sprite_sheet(input_folder, output_file)

# Run App
root = Tk()
root.title("Sprite Sheet Maker")
app = SpriteSheetApp(root)
root.mainloop()
