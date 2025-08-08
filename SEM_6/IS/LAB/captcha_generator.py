# Import required libraries
import random
import string
from captcha.image import ImageCaptcha

# Function to generate randomized CAPTCHA
def generateCaptcha():
    R1 = random.randint(1, 9)  # CAPTCHA length between 1 and 9
    captcha = []
    for i in range(R1):
        R2 = random.randint(0, 9)
        if R2 < 6:
            R3 = random.randint(0, 9)
            captcha.append(str(R3))
        else:
            R3 = random.choice(string.ascii_letters)
            captcha.append(R3)
    return ''.join(captcha)

# Function to create image-based CAPTCHA
def createImageCaptcha(captcha_text, image_path='CAPTCHA.png'):
    image = ImageCaptcha(width=280, height=90)
    data = image.generate(captcha_text)
    image.write(captcha_text, image_path)
    return image_path

# Main authentication logic
def captcha_authentication():
    print("\n--- CAPTCHA Authentication System ---\n")
    
    while True:
        # Choose CAPTCHA type
        captcha_type = input("Choose CAPTCHA type:\n[T]ext-based\n[I]mage-based\n[Q]uit\nEnter choice: ").strip().lower()
        
        if captcha_type == 'q':
            print("\n🔒 Session terminated.")
            break
        
        captcha_text = generateCaptcha()

        if captcha_type == 't':
            # Text-based CAPTCHA
            print(f"\nGenerated Text CAPTCHA: {captcha_text}")
            
        elif captcha_type == 'i':
            # Image-based CAPTCHA
            image_path = createImageCaptcha(captcha_text)
            print("\nImage-based CAPTCHA generated.")
            print(f"Please open the image at '{image_path}' to view the CAPTCHA.")
            
        else:
            print("⚠️ Invalid choice. Please select again.\n")
            continue
        
        # User verification loop
        while True:
            user_input = input("\nEnter the CAPTCHA: ").strip()
            
            if user_input == captcha_text:
                print("✅ Captcha matches. Authentication successful!\n")
                return
            
            else:
                print("❌ Captcha didn't match.")
                retry_choice = input("[R]etry | [N]ew CAPTCHA | [Q]uit: ").strip().lower()
                
                if retry_choice == 'q':
                    print("\n🔒 Session terminated.")
                    return
                
                elif retry_choice == 'n':
                    break  # Generate new CAPTCHA
                
                elif retry_choice != 'r':
                    print("⚠️ Invalid option. Defaulting to retry.")

# Run the authentication system
if __name__ == "__main__":
    captcha_authentication()
