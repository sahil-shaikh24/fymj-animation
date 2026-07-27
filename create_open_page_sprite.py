import os
import glob
from PIL import Image

folder_path = 'For coding/open page'
output_file = 'open_page_sprite_grid.png'
frame_width = 960
frame_height = 540
columns = 14

print(f"Processing folder: {folder_path}...")
images = sorted(glob.glob(os.path.join(folder_path, '*.png')))
total_frames = len(images)

if total_frames == 0:
    print("No PNG images found. Exiting.")
    exit(1)

print(f"Found {total_frames} frames. Resizing to {frame_width}x{frame_height} (16:9 ratio)...")

rows = (total_frames + columns - 1) // columns
sprite_width = columns * frame_width
sprite_height = rows * frame_height

sprite = Image.new('RGBA', (sprite_width, sprite_height), (0,0,0,0))

for i, img_path in enumerate(images):
    with Image.open(img_path) as img:
        img_resized = img.resize((frame_width, frame_height), Image.Resampling.LANCZOS)
        row = i // columns
        col = i % columns
        x = col * frame_width
        y = row * frame_height
        sprite.paste(img_resized, (x, y))
        
sprite.save(output_file)
print(f"Successfully saved {output_file}! (Grid: {columns}x{rows}, Size: {sprite_width}x{sprite_height})")
