import os
import sys
from main import encode_image, load_env_vars, get_chat_response, Mistral

def test_image_encoding(image_path):
    """Test the image encoding function."""
    base64_image = encode_image(image_path)
    if base64_image is None:
        print("Image encoding failed. Exiting.")
        sys.exit(1)
    else:
        print("Image encoding successful.")
        return base64_image

def test_api_response(base64_image):
    """Test the API response function."""
    api_key = load_env_vars()
    client = Mistral(api_key=api_key)
    model = "pixtral-12b-2409"

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What's in this image?"
                },
                {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{base64_image}"
                }
            ]
        }
    ]

    response = get_chat_response(client, model, messages)
    print("API response successful.")
    print(response)

if __name__ == '__main__':
    # Path to your test image
    test_image_path = "S:\\CODE\\TinyTroupeBB\\examples\\test_image.jpg"

    # Test image encoding
    base64_image = test_image_encoding(test_image_path)

    # Test API response
    test_api_response(base64_image)
