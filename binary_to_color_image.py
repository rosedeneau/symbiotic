from PIL import Image

def binary_to_gradient_image(binary_str, width=None):
    # Ensure binary string length is divisible by 8 (1 byte per pixel for grayscale)
    if len(binary_str) % 8 != 0:
        raise ValueError("The binary string length must be divisible by 8.")
    
    # Convert binary string to grayscale intensity values
    intensity_values = [int(binary_str[i:i + 8], 2) for i in range(0, len(binary_str), 8)]
    
    # Generate a gradient by sorting the intensity values
    gradient_values = sorted(intensity_values)
    
    # Determine image dimensions
    if width is None:
        # Calculate a square dimension if no width is provided
        side_length = int(len(gradient_values) ** 0.5)
        width = side_length
    height = (len(gradient_values) + width - 1) // width  # Round up to fit all pixels
    
    # Pad the gradient values to fit the image dimensions
    padded_gradient = gradient_values + [gradient_values[-1]] * (width * height - len(gradient_values))
    
    # Create a grayscale image
    img = Image.new("L", (width, height))
    img.putdata(padded_gradient)
    return img

# Provided binary string
binary_string = "001000110010011001000001001001000110011001100100010001010000010001000100011001000110011001001101101010001100010001100100101001011100011000110011001000001000100"

# Generate the gradient image
image = binary_to_gradient_image(binary_string, width=10)  # Specify desired width (adjustable)
image.show()  # Display the image