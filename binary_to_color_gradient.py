import numpy as np
from PIL import Image

def binary_to_gradient_image(binary_str, width_cm=70, height_cm=100, dpi=300, color_map='viridis'):
    # Calculate the desired image size in pixels
    width_px = int(width_cm * dpi / 2.54)  # Convert cm to inches and then to pixels
    height_px = int(height_cm * dpi / 2.54)  # Convert cm to inches and then to pixels
    
    # Calculate the total number of pixels
    total_pixels = width_px * height_px
    
    # Duplicate the binary string until it reaches the required size
    while len(binary_str) < total_pixels * 8:
        binary_str += binary_str  # Duplicate the string
    
    # Truncate the binary string to match the required size
    binary_str = binary_str[:total_pixels * 8]  # Ensure it's exactly the right length
    
    # Convert binary string to grayscale intensity values
    intensity_values = [int(binary_str[i:i + 8], 2) for i in range(0, len(binary_str), 8)]
    
    # Interpolate the intensity values to smooth the gradient (increase gradation)
    # Normalize values between 0 and 255 for smoothness
    intensity_values = np.interp(intensity_values, (min(intensity_values), max(intensity_values)), (0, 255))
    
    # Generate the RGB gradient using a colormap (viridis, inferno, etc.)
    # You can choose any color map that makes sense for your design
    from matplotlib import cm
    
    # Normalize to the [0, 1] range
    normed_values = np.array(intensity_values) / 255.0
    
    # Map the normalized grayscale values to RGB using a color map
    rgb_values = cm.viridis(normed_values)  # You can change 'viridis' to any other color map
    
    # Convert the RGB values to 8-bit format (0-255)
    rgb_values = (rgb_values * 255).astype(np.uint8)
    
    # Create an image using RGB mode
    img = Image.new("RGB", (width_px, height_px))
    
    # Flatten the RGB values to a list and put the data into the image
    img.putdata([tuple(rgb) for rgb in rgb_values])
    
    return img

# Provided binary string
binary_string = "001000110010011001000001001001000110011001100100010001010000010001000100011001000110011001001101101010001100010001100100101001011100011000110011001000001000100"

# Generate the smooth color gradient image
image = binary_to_gradient_image(binary_string, width_cm=70, height_cm=100)  # Specify the desired physical size
image.show()  # Display the image