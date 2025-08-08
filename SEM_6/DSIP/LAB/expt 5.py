import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to read an image
def read_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Image not found at the path: {image_path}")
    return image

# 1. Image Negative
def image_negative(image):
    return 255 - image

# 2. Thresholding
def thresholding(image, threshold_value=128):
    _, thresh_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    return thresh_image

# 3. Gray Level Slicing with Background
def gray_level_slicing_with_background(image, lower_bound, upper_bound):
    sliced_image = np.zeros_like(image)
    sliced_image[(image >= lower_bound) & (image <= upper_bound)] = 255
    return sliced_image

# 4. Gray Level Slicing without Background
def gray_level_slicing_without_background(image, lower_bound, upper_bound):
    sliced_image = np.zeros_like(image)
    sliced_image[(image >= lower_bound) & (image <= upper_bound)] = image[(image >= lower_bound) & (image <= upper_bound)]
    return sliced_image

# 5. Bit Plane Slicing
def bit_plane_slicing(image):
    bit_planes = []
    for i in range(8):
        bit_plane = (image >> i) & 1
        bit_plane = bit_plane * 255  # Convert to 0-255 range
        bit_planes.append(bit_plane)
    return bit_planes

# Function to display images
def show_images(images, titles):
    for i, img in enumerate(images):
        plt.subplot(1, len(images), i + 1)
        plt.imshow(img, cmap='gray')
        plt.title(titles[i])
        plt.axis('off')
    plt.show()

# Main function to process the image
def process_image(image):
    while True:
        print("\nChoose an operation:")
        print("1. Image Negative")
        print("2. Thresholding")
        print("3. Gray Level Slicing with Background")
        print("4. Gray Level Slicing without Background")
        print("5. Bit Plane Slicing")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            negative_image = image_negative(image)
            show_images([image, negative_image], ['Original Image', 'Negative Image'])

        elif choice == '2':
            threshold_value = int(input("Enter threshold value (0-255): "))
            thresholded_image = thresholding(image, threshold_value)
            show_images([image, thresholded_image], ['Original Image', 'Thresholded Image'])

        elif choice == '3':
            lower_bound = int(input("Enter lower bound for slicing (0-255): "))
            upper_bound = int(input("Enter upper bound for slicing (0-255): "))
            sliced_with_bg = gray_level_slicing_with_background(image, lower_bound, upper_bound)
            show_images([image, sliced_with_bg], ['Original Image', 'Gray Level Slicing with Background'])

        elif choice == '4':
            lower_bound = int(input("Enter lower bound for slicing (0-255): "))
            upper_bound = int(input("Enter upper bound for slicing (0-255): "))
            sliced_without_bg = gray_level_slicing_without_background(image, lower_bound, upper_bound)
            show_images([image, sliced_without_bg], ['Original Image', 'Gray Level Slicing without Background'])

        elif choice == '5':
            bit_planes = bit_plane_slicing(image)
            for i in range(0, 8, 2):  # Displaying only a few significant planes
                plt.subplot(1, 4, (i // 2) + 1)
                plt.imshow(bit_planes[i], cmap='gray')
                plt.title(f'Bit Plane {i}')
                plt.axis('off')
            plt.show()

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Upload an image
def upload_image():
    image_path = input("Enter the path to the image: ")
    return image_path

# Main code to run the program
image_path = upload_image()  # Upload the image
try:
    image = read_image(image_path)  # Read the image
    process_image(image)  # Process the image with the menu
except FileNotFoundError as e:
    print(e)