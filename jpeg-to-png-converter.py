import os
from PIL import Image

def upload_jpeg_file():
    while True:
        file_path = input("Enter the path to the JPEG file: ")
        if os.path.exists(file_path):
            return file_path
        print("File not found. Please enter a valid path to a JPEG file.")

def check_if_valid_jpeg(file_path):
    try:
        with Image.open(file_path) as img:
            return img.format == "JPEG"
    except:
        return False

def convert_jpeg_to_png(jpeg_path):
    try:
        with Image.open(jpeg_path) as img:
            png_path = os.path.splitext(jpeg_path)[0] + ".png"
            img.save(png_path, "PNG")
        return png_path
    except Exception as e:
        print(f"Error converting image: {e}")
        return None

def main():
    print("Welcome to the JPEG to PNG Converter!")

    # Upload JPEG file
    jpeg_path = upload_jpeg_file()

    # Check if file is valid JPEG
    if check_if_valid_jpeg(jpeg_path):
        # Convert JPEG to PNG
        png_path = convert_jpeg_to_png(jpeg_path)
        if png_path:
            print(f"Conversion successful! PNG file saved as: {png_path}")
        else:
            print("Conversion failed.")
    else:
        print("Error: The uploaded file is not a valid JPEG image.")

    print("Thank you for using the JPEG to PNG Converter!")

if __name__ == "__main__":
    main()
