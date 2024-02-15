import os
import shutil

# Create folders if they don't exist
for folder in ["Documents", "Video", "Audio", "Pictures", "Others"]:
    if not os.path.exists(folder):
        os.mkdir(folder)

audio = ["mp3", "wav"]
video = ["mp4", "mov"]
documents = ["docx", "pptx", "txt"]
pictures = ["png", "jpg", "jpeg", "webp"]

for file in os.listdir():
    name, ext = os.path.splitext(file)
    ext_lower = ext.lower()

    if ext_lower in audio:
        shutil.move(file, os.path.join("Audio", file))
    elif ext_lower in video:
        shutil.move(file, os.path.join("Video", file))
    elif ext_lower in documents:
        shutil.move(file, os.path.join("Documents", file))
    elif ext_lower in pictures:
        shutil.move(file, os.path.join("Pictures", file))
    elif file != "Others":  # Check if the file is not already in the "Others" directory
        shutil.move(file, os.path.join("Others", file))

print("All files are arranged.")
