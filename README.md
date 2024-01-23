# Facebook Post Using AWS Lambda and Graph API

## Introduction

This repository demonstrates a simple yet powerful process to automate image uploads to a Facebook page using AWS Lambda, Python, and the Facebook Graph API.
## Prerequisites

Before you begin, make sure you have the following:

- AWS account
- Facebook Developer account
- Facebook App created with App ID and App Secret
- Page ID and Page Access Token

## Configuration

Update the `lambda_function.py` file with your actual values:

- `page_id`: Your Facebook page ID
- `page_access_token`: Your Facebook page access token
- `message`: Your desired message for the Facebook post
- `photo_urls`: List of URLs for the images you want to upload

## Setup

### Install Required Libraries
Before deploying the AWS Lambda function, ensure you have the required Python libraries installed. You may also need to add a custom Lambda layer for the `requests` library (If needed).

## Custom Lambda Layer for `requests` Library

1. **Install `requests` Locally:**
    - Create a folder on your directory, e.g., "customLayer."
    - Open a terminal: `cd customLayer`
    - Install `requests`: `pip install requests -t .`

2. **Create Zip Archive:**
    - Zip the "customLayer" folder to 'customLayer.zip.'

3. **Upload as Lambda Layer:**
    - AWS Console > Lambda > Layers > Create Layer.
    - Upload 'customLayer.zip' with a layer name.

4. **Associate Layer with Lambda Function:**
    - AWS Lambda Console > Functions > Create Function.
    - In "Designer," add a layer, select "Custom Layers," and choose your custom layer.

Now, your Lambda function includes the `requests` library as a custom layer.

## Usage

1. Deploy the AWS Lambda function.
2. Trigger the Lambda function to upload images to your Facebook page.

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
