def caesar_cipher(text, shift):
    result = ""

    for char in text:
        # Check if character is an uppercase letter
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If it's not a letter, leave it as is
            result += char

    return result

# User input for the text and the shift value
text = input("Enter the text to be ciphered: ")
shift = int(input("Enter the shift value: "))

# Apply the Caesar cipher
ciphered_text = caesar_cipher(text, shift)

# Display the ciphered text
print(f"Ciphered text: {ciphered_text}")
