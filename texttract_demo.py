# from texttract_wrapper import TextractWrapper
import boto3
from botocore.exceptions import ClientError

def main():
    session = boto3.Session(profile_name='oguz')
    textract_client = session.client('textract', region_name='us-east-1')
    with open("photo_2023-06-02_12-52-19.jpg", "rb") as image:
        image_bytes = image.read()
        try:
            response = textract_client.detect_document_text(Document={'Bytes': image_bytes})
            print("Detected %s blocks.", len(response['Blocks']))
        except ClientError:
            print("Couldn't detect text.")
            raise
        else:
            blocks = response['Blocks']
            word_blocks = filter(lambda x: x['BlockType'] == 'WORD', blocks)
            print(word_blocks)

if __name__ == "__main__":
    main()