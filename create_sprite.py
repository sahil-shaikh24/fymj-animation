import os
import glob
from PIL import Image

base_dir = 'For coding'
frame_size = 300
columns = 14

print(f"Scanning {base_dir} for folders...")

for folder_name in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder_name)
    
    # Skip if not a directory or if it's "Page 2"
    if not os.path.isdir(folder_path) or folder_name == 'Page 2':
        continue
        
    output_file = f"{folder_name.replace(' ', '_')}_sprite_grid.png"
    
    print(f"\n--- Processing folder: {folder_name} ---")
    images = sorted(glob.glob(os.path.join(folder_path, '*.png')))
    total_frames = len(images)
    
    if total_frames == 0:
        print(f"No PNG images found in {folder_name}. Skipping.")
        continue
        
    print(f"Found {total_frames} frames. Resizing and stitching...")
    
    rows = (total_frames + columns - 1) // columns
    sprite_width = columns * frame_size
    sprite_height = rows * frame_size

    sprite = Image.new('RGBA', (sprite_width, sprite_height), (0,0,0,0))

    for i, img_path in enumerate(images):
        with Image.open(img_path) as img:
            # Resize to 300x300 with high quality resampling
            img_resized = img.resize((frame_size, frame_size), Image.Resampling.LANCZOS)
            
            # Calculate grid position
            row = i // columns
            col = i % columns
            x = col * frame_size
            y = row * frame_size
            
            # Paste into sprite sheet
            sprite.paste(img_resized, (x, y))
            
    sprite.save(output_file)
    print(f"Successfully saved {output_file}! (Grid: {columns}x{rows}, Size: {sprite_width}x{sprite_height})")

print("\nAll folders processed successfully!")
