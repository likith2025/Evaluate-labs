import os
from PIL import Image

# User settings
input_folder = "C:\Users\nagar\OneDrive\Desktop\img\venkateshwara-swamy-3840x2160-14468.png"           # Change to your image folder name
output_folder = "C:\Users\nagar\OneDrive\Desktop\img\venkateshwara-swamy-3840x2160-14468.png"            # Folder to save resized images
resize_size = (800, 600)                    # (width, height) in pixels
output_format = "JPEG"                      # Change to "PNG" if needed

# Create output folder if it doesn't exist
os.makedirs("C:\Users\nagar\OneDrive\Desktop\img\venkateshwara-swamy-3840x2160-14468.png", exist_ok=True)

# Loop through all files in input folder
for filename in os.listdir("C:\Users\nagar\OneDrive\Desktop\img\venkateshwara-swamy-3840x2160-14468.png"):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
        # Full path to current image
        img_path = os.path.join("C:\Users\nagar\OneDrive\Desktop\img\venkateshwara-swamy-3840x2160-14468.png", filename)
        img = Image.open(img_path)
        
        # Resize image
        img_resized = img.resize(resize_size)
        
        # Save to output folder
        base_filename = os.path.splitext(filename)[0]
        output_path = os.path.join(output_folder, f"{base_filename}.{output_format.lower()}")
        img_resized.save(output_path, output_format)
        print(f"Resized & saved: {output_path}")

print("Batch image resizing complete!")
