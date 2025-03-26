import cv2
import os
import numpy as np

def resize_image(image_path, output_path, new_width, new_height, rounded=False):
    """
    Resizes an image, optionally rounds corners, and saves it to a specified output path.

    Args:
        image_path (str): Path to the input image.
        output_path (str): Path where the resized image should be saved (including filename).
        new_width (int): Desired width of the resized image.
        new_height (int): Desired height of the resized image.
        rounded (bool, optional): If True, rounds the corners of the image. Defaults to False.
    """
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    if img is None:
        print(f"Error: Could not read image at {image_path}")
        return

    img_resized = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)

    if rounded:
        mask = np.zeros((new_height, new_width, 4), dtype=np.uint8)
        cv2.ellipse(mask, (new_width // 2, new_height // 2), (new_width // 2, new_height // 2), 0, 0, 360, (255, 255, 255, 255), -1)

        if img_resized.shape[2] == 3:
            img_resized_rgba = cv2.cvtColor(img_resized, cv2.COLOR_BGR2BGRA)
            img_resized = cv2.bitwise_and(img_resized_rgba, mask)
        else:
            img_resized = cv2.bitwise_and(img_resized, mask)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    cv2.imwrite(output_path, img_resized)

    print(f"Image saved like: {output_path}")

# icons for android
resize_image("icon.png", "./mipmap-mdpi/ic_launcher_mdpi.png", 48, 48)
resize_image("icon.png", "./mipmap-hdpi/ic_launcher_hdpi.png", 72, 72)
resize_image("icon.png", "./mipmap-xhdpi/ic_launcher_xhdpi.png", 96, 96)
resize_image("icon.png", "./mipmap-xxhdpi/ic_launcher_xxhdpi.png", 144, 144)
resize_image("icon.png", "./mipmap-xxxhdpi/ic_launcher_xxxhdpi.png", 192, 192)

resize_image("icon.png", "./mipmap-mdpi/ic_launcher_round_mdpi.png", 48, 48, True)
resize_image("icon.png", "./mipmap-hdpi/ic_launcher_round_hdpi.png", 72, 72, True)
resize_image("icon.png", "./mipmap-xhdpi/ic_launcher_round_xhdpi.png", 96, 96, True)
resize_image("icon.png", "./mipmap-xxhdpi/ic_launcher_round_xxhdpi.png", 144, 144, True)
resize_image("icon.png", "./mipmap-xxxhdpi/ic_launcher_round_xxxhdpi.png", 192, 192, True)

resize_image("icon.png", "./mipmap-mdpi/ic_launcher_foreground_mdpi.png", 108, 108)
resize_image("icon.png", "./mipmap-hdpi/ic_launcher_foreground_hdpi.png", 162, 162)
resize_image("icon.png", "./mipmap-xhdpi/ic_launcher_foreground_xhdpi.png", 216, 216)
resize_image("icon.png", "./mipmap-xxhdpi/ic_launcher_foreground_xxhdpi.png", 324, 324)
resize_image("icon.png", "./mipmap-xxxhdpi/ic_launcher_foreground_xxxhdpi.png", 432, 432)

# splash for android
resize_image("icon.png", "./drawable-mdpi/splashscreen_logo_mdpi.png", 288, 288)
resize_image("icon.png", "./drawable-hdpi/splashscreen_logo_hdpi.png", 432, 432)
resize_image("icon.png", "./drawable-xhdpi/splashscreen_logo_xhdpi.png", 576, 576)
resize_image("icon.png", "./drawable-xxhdpi/splashscreen_logo_xxhdpi.png", 864, 864)
resize_image("icon.png", "./drawable-xxxhdpi/splashscreen_logo_xxxhdpi.png", 1152, 1152)