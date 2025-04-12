import os

folder = "./"
files = sorted(f for f in os.listdir(folder) if f.endswith('.mp3'))

for i, filename in enumerate(files, start=1):
    new_name = f"{i}.mp3"
    os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))