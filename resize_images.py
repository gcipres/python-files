import cv2
import os

def resize_image(image_path, mipmap, new_width, new_height, rounded = False):
    img = cv2.imread(image_path)

    img_resized = cv2.resize(img, (new_width, new_height))
    
    if rounded:
        mask = np.zeros((new_height, new_width, 4), dtype=np.uint8) #create alpha channel if it doesnt exist
        cv2.ellipse(mask, (new_width // 2, new_height // 2), (new_width // 2, new_height // 2), 0, 0, 360, (255, 255, 255, 255), -1)

        if img_resized.shape[2] == 3: #if the image has no alpha channel
            img_resized_rgba = cv2.cvtColor(img_resized, cv2.COLOR_BGR2BGRA)
            img_resized = cv2.bitwise_and(img_resized_rgba, mask)
        else:
            img_resized = cv2.bitwise_and(img_resized, mask)

    root_path = os.path.dirname(os.path.abspath(__file__))

    file_name, extension = os.path.splitext(image_path)

    image_resized_path = os.path.join(root_path, f"{file_name}_{mipmap}{extension}")

    cv2.imwrite(image_resized_path, img_resized)

    print(f"Image saved like: {image_resized_path}")


# icons for android

resize_image("icon.png", "ic_launcher_mdpi", 48, 48)
resize_image("icon.png", "ic_launcher_hdpi", 72, 72)
resize_image("icon.png", "ic_launcher_xhdpi", 96, 96)
resize_image("icon.png", "ic_launcher_xxhdpi", 144, 144)
resize_image("icon.png", "ic_launcher_xxxhdpi", 192, 192)

resize_image("icon.png", "ic_launcher_round_mdpi", 48, 48, True)
resize_image("icon.png", "ic_launcher_round_hdpi", 72, 72, True)
resize_image("icon.png", "ic_launcher_round_xhdpi", 96, 96, True)
resize_image("icon.png", "ic_launcher_round_xxhdpi", 144, 144, True)
resize_image("icon.png", "ic_launcher_round_xxxhdpi", 192, 192, True)

resize_image("icon.png", "ic_launcher_foreground_mdpi", 108, 108)
resize_image("icon.png", "ic_launcher_foreground_hdpi", 162, 162)
resize_image("icon.png", "ic_launcher_foreground_xhdpi", 216, 216)
resize_image("icon.png", "ic_launcher_foreground_xxhdpi", 324, 324)
resize_image("icon.png", "ic_launcher_foreground_xxxhdpi", 432, 432)

# splash for android
resize_image("icon.png", "splashscreen_logo_mdpi", 288, 288)
resize_image("icon.png", "splashscreen_logo_hdpi", 432, 432)
resize_image("icon.png", "splashscreen_logo_xhdpi", 576, 576)
resize_image("icon.png", "splashscreen_logo_xxhdpi", 864, 864)
resize_image("icon.png", "splashscreen_logo_xxxhdpi", 1152, 1152)