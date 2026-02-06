#!/usr/bin/env python3
"""
Image Index Generator for TAG KC Fundraiser
Automatically creates images.json with all image files from the images folder
"""

import os
import json
from pathlib import Path

# Configuration
IMAGE_FOLDER = "images"
OUTPUT_FILE = os.path.join(IMAGE_FOLDER, "images.json")
SUPPORTED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.svg'}

def get_all_images(folder_path):
    """
    Scan the images folder and return all image files
    """
    images = []

    if not os.path.exists(folder_path):
        print(f"⚠️  Warning: '{folder_path}' folder not found!")
        print(f"Creating '{folder_path}' folder...")
        os.makedirs(folder_path)
        return images

    # Get all files in the folder
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Skip the images.json file itself
        if file == "images.json":
            continue

        # Check if it's an image file
        _, ext = os.path.splitext(file)
        if ext.lower() in SUPPORTED_EXTENSIONS:
            images.append(file)

    # Sort alphabetically (case-insensitive)
    images.sort(key=lambda x: x.lower())

    return images

def main():
    print("🖼️  TAG KC Image Index Generator")
    print("=" * 50)

    # Get all images
    images = get_all_images(IMAGE_FOLDER)

    if not images:
        print(f"❌ No images found in '{IMAGE_FOLDER}' folder!")
        print(f"\nℹ️  Supported formats: {', '.join(sorted(SUPPORTED_EXTENSIONS))}")
        print(f"\nPlease add your images to the '{IMAGE_FOLDER}' folder and run this script again.")

        # Create an empty images.json
        data = {"images": [], "count": 0, "folder": IMAGE_FOLDER}
        with open(OUTPUT_FILE, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"\n✅ Created empty {OUTPUT_FILE}")
        return

    # Create the JSON data
    data = {
        "images": images,
        "count": len(images),
        "folder": IMAGE_FOLDER,
        "generated": "auto"
    }

    # Write to images.json
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"✅ Successfully generated {OUTPUT_FILE}")
    print(f"\n📸 Found {len(images)} image(s):")
    for i, img in enumerate(images, 1):
        print(f"   {i}. {img}")

    print(f"\n🚀 Your slideshow is ready!")
    print(f"   Open fundraiser-with-slideshow.html in your browser to see the images.")

if __name__ == "__main__":
    main()
