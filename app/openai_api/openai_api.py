from dotenv import load_dotenv
from openai  import OpenAI
import os
import openai

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

class  Bll:
    def  __init__ (self, client):
        self.client = client

    @staticmethod
    def openAI_response(content):
        try:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=[{"role": "user", "content": content}],
                max_tokens=100,
                stop=None,
                n=1,
                temperature=0.8,
            )
            reply = completion.choices[0].message.content
            return reply
        except openai.OpenAIError as e:
            print(f"An OpenAI error occurred: {str(e)}")
            return str(e)
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            return str(e)
    
    @staticmethod
    def openAI_image(content):
        completion = client.images.generate(
            model="dall-e-2",
            prompt=content,
            n=1,
            size="512x512",
        )
        try:
            reply = completion.data[0].url
            return reply
        except openai.OpenAIError as e:
            print(f"An OpenAI error occurred: {str(e)}")
            return str(e)
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            return str(e)

    