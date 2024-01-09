import json
import requests
from concurrent.futures import ThreadPoolExecutor

def upload_photo(photo_url, page_id, page_access_token):
    url = f"https://graph.facebook.com/v13.0/{page_id}/photos"
    params = {
        'access_token': page_access_token,
        'published': 'false',
        'url': photo_url,
    }

    try:
        response = requests.post(url, params=params)
        result = response.json()

        return result.get('id') or f"Error uploading photo: {result}"
    except requests.exceptions.RequestException as e:
        return f"Request error: {e}"

def lambda_handler(event, context):
    # Replace with your actual values
    page_id = 'YOUR_PAGE_ID'
    page_access_token = 'YOUR_PAGE_ACCESS_TOKEN'
    message = 'Post from Lambda'

    photo_urls = [
        'https://example.com/photo1.jpg',
        'https://example.com/photo2.jpg',
        # Add more photo URLs as needed
    ]

    # Upload photos with published state set to false using ThreadPoolExecutor
    with ThreadPoolExecutor() as executor:
        photo_ids = list(executor.map(lambda x: upload_photo(x, page_id, page_access_token), photo_urls))

    # Use the IDs of unpublished photos to schedule a post
    url = f'https://graph.facebook.com/v13.0/me/feed'
    params = {
        'access_token': page_access_token,
        'message': message,
    }

    for i, photo_id in enumerate(photo_ids, start=1):
        params[f'attached_media[{i}]'] = f'{{"media_fbid":"{photo_id}"}}'

    try:
        response = requests.post(url, params=params)
        result = response.json()

        if 'id' in result:
            msg = f"Post scheduled successfully. Post ID: {result['id']}"
        else:
            msg = f"Error scheduling post: {result}"
    except requests.exceptions.RequestException as e:
        msg = f"Request error: {e}"

    return {
        'statusCode': 200,
        'body': json.dumps(msg)
    }
