import base64
import sys

# Function to encode a string to Base64
def encode_to_base64(input_string):
    encoded = base64.b64encode(input_string.encode())
    return encoded.decode()

# Function to decode a Base64 string
def decode_from_base64(encoded_string):
    decoded = base64.b64decode(encoded_string)
    return decoded.decode()

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <encode/decode> <string>")
        sys.exit(1)

    action = sys.argv[1].lower()
    input_string = sys.argv[2]

    if action == 'encode':
        encoded_string = encode_to_base64(input_string)
        print(f"Base64 Encoded: {encoded_string}")
    elif action == 'decode':
        try:
            decoded_string = decode_from_base64(input_string)
            print(f"Decoded String: {decoded_string}")
        except Exception as e:
            print(f"Error decoding Base64 string: {e}")
    else:
        print("Invalid action. Use 'encode' or 'decode'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
