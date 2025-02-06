import os
import requests
import logging

def save_image(image_url, idx):
    """Download an image from a URL and save it locally."""
    image_path = f"image_{idx}.png"
    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        with open(image_path, 'wb') as f:
            f.write(response.content)
        return image_path
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to download image from {image_url}: {e}")
        return None

def cleanup_images():
    """Remove temporary image files starting with 'image_' and ending with '.png'."""
    for filename in os.listdir('.'):
        if filename.startswith('image_') and filename.endswith('.png'):
            try:
                os.remove(filename)
            except Exception as e:
                logging.error(f"Error cleaning up image file {filename}: {e}")
