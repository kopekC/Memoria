from PIL import Image

def degrade_image_quality(input_image_path, output_image_path, quality):
    with Image.open(input_image_path) as img:
        img.save(output_image_path, "JPEG", quality=quality)

# function call with placeholder parameters
degrade_image_quality("path_to_input_image.jpg", "path_to_output_image.jpg", 30)