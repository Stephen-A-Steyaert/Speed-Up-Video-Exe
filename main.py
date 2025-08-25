import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from moviepy import VideoFileClip, vfx
import os

def main():
    root = tk.Tk()
    root.withdraw()  # hide root window

    # Step 1: Ask for video file
    filepath = filedialog.askopenfilename(
        title="Select Video to Speed Up",
        initialdir="~",
        filetypes=(("Video Files", "*.mp4 *.avi *.mov *.mkv"), ("All Files", "*.*"))
    )

    if not filepath:
        messagebox.showinfo("Canceled", "No file selected.")
        return

    # Step 2: Ask for speed multiplier
    speed = simpledialog.askfloat(
        "Speed Input",
        "Enter speed multiplier (e.g., 1.5 for 1.5x speed):",
        minvalue=0.1,
        maxvalue=10.0
    )

    if speed is None:
        messagebox.showinfo("Canceled", "No speed entered.")
        return

    # Step 3: Build output path in Downloads
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    if not os.path.exists(downloads_folder):
        os.makedirs(downloads_folder)

    base = os.path.splitext(os.path.basename(filepath))[0]
    ext = os.path.splitext(filepath)[1]
    output_path = os.path.join(downloads_folder, f"{base}_spedup{ext}")

    # Step 4: Ask user for permission to save in Downloads
    confirm = messagebox.askyesno(
        "Allow Write Access",
        f"This program will save the sped-up video to your Downloads folder:\n\n{output_path}\n\nDo you allow this?"
    )

    if not confirm:
        messagebox.showinfo("Canceled", "Write access not granted. Operation canceled.")
        return

    # Step 5: Process video with speedx
    messagebox.showinfo("Processing", f"Processing video at {speed}x speed...\nPlease wait.")
    clip = VideoFileClip(filepath)
    new_clip = clip.fx(vfx.speedx, factor=speed)
    new_clip.write_videofile(output_path)

    messagebox.showinfo("Done", f"Video saved to:\n{output_path}")

if __name__ == "__main__":
    main()
