import cv2
import os

def resize_image(image_path, new_width, new_height):
    img = cv2.imread(image_path)

    img_resized = cv2.resize(img, (new_width, new_height))

    root_path = os.path.dirname(os.path.abspath(__file__))

    file_name, extension = os.path.splitext(image_path)

    image_resized_path = os.path.join(root_path, f"{file_name}_{new_width}x{new_height}{extension}")

    cv2.imwrite(image_resized_path, img_resized)

    print(f"Image saved like: {image_resized_path}")


# icons for android
resize_image("icon.png", 162, 162)
resize_image("icon.png", 108, 108)
resize_image("icon.png", 216, 216)
resize_image("icon.png", 324, 324)
resize_image("icon.png", 432, 432)

# splash for android
resize_image("splash.png", 1414, 2000)