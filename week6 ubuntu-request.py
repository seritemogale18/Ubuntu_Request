import os
import requests
from urllib.parse import urlparse
import time

def fetch_image():
    print("Ubuntu-Inspired Image Fetcher")
    print("The Wisdom of Ubuntu: 'I am because we are'")
    print("Connecting to the global community to respectfully fetch shared resources...\n")
    
    # Prompt user for URL
    url = input("Please enter the image URL: ").strip()
    
    if not url:
        print("❌ No URL provided. Exiting.")
        return
    
    # Create directory if it doesn't exist
    directory = "Fetched_Images"
    os.makedirs(directory, exist_ok=True)
    print(f"📁 Directory '{directory}' is ready for your images.")
    
    try:
        # Fetch the image
        print(f"🌐 Fetching image from: {url}")
        response = requests.get(url, timeout=10)
        
        # Check for HTTP errors
        response.raise_for_status()
        
        # Determine filename
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        # If no filename or extension, generate one
        if not filename or '.' not in filename:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"image_{timestamp}.jpg"
            print(f"ℹ️  No filename detected. Using generated name: {filename}")
        else:
            # Ensure it's a valid image extension
            if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp')):
                filename = filename.split('.')[0] + '.jpg'
                print(f"ℹ️  Adding .jpg extension for compatibility: {filename}")
        
        # Save the image
        filepath = os.path.join(directory, filename)
        
        with open(filepath, 'wb') as file:
            file.write(response.content)
        
        print(f"✅ Image successfully saved to: {filepath}")
        print("🌍 Thank you for sharing in the spirit of Ubuntu!")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        print("💡 This might be due to connection issues, invalid URL, or server problems.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print("💡 Something went wrong during processing.")

if __name__ == "__main__":
    fetch_image()