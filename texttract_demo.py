# from texttract_wrapper import TextractWrapper
import boto3
from botocore.exceptions import ClientError

import time

def main():
    session = boto3.Session(profile_name='oguz')
    textract_client = session.client('textract', region_name='eu-west-2')
    with open("photo_2023-06-18_03-22-54.jpg", "rb") as image:
        image_bytes = image.read()
        try:
            start = time.time()
            response = textract_client.detect_document_text(Document={'Bytes': image_bytes})
            end = time.time()
            print(end - start)      
            print("Detected %s blocks.", len(response['Blocks']))
        except ClientError:
            print("Couldn't detect text.")
            raise
        else:
            blocks = response['Blocks']
            word_blocks = (filter(lambda x: x['BlockType'] == 'WORD', blocks))
            texts = (map(lambda x: x['Text'], word_blocks))
            print(list(texts))

if __name__ == "__main__":
    main()