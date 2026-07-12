from google import genai
from dotenv import load_dotenv

load_dotenv(override=True)
client = genai.Client()


response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain how AI works in a few words",
)

print(response.text)
print(response.candidates[0].content.parts[0].text)


print(response)

"""
response
  └── candidates[0]        # first response
        └── content        # the content
              └── parts[0] # first part
                    └── text  # actual text ✅

The complete Response 
sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text='Finding patterns in data to predict outcomes.',
        thought_signature=b'\x12\xfe\x08\n\xfb\x08\x01\xbe>\xf6\xfbEw:+}Z\xa9\x19\tCzl\x13\xa2\xcb0\x89u\xa5J\x96\xd6\x8c/\xbfli\xdd\xca,c\x81\xab\xa1\xb2\xe1\x11\x1bq\xde.\xbc\xfeO\xffT\x87}\xd3@\xc0\xd0Td\xb97\x8c\x97\xce\xc28A\xd6\x06dk\x96\xefk\xad\xaa4\xda\x06\xebX=\xd5\xbaf*\xac\x02\xe5\xde\xba...'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-3-flash-preview' prompt_feedback=None response_id='zj2jaYSAFKu7qfkPo4fW0Q4' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=8,
  prompt_token_count=9,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=9
    ),
  ],
  thoughts_token_count=295,
  total_token_count=312
) automatic_function_calling_history=[] parsed=None
"""