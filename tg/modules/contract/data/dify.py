import requests
from dify_client import CompletionClient

api_key = ""

completion_client = CompletionClient(api_key)
completion_client.base_url = 'http://dify.server33.pleasenever.click/v1'
completion_response = completion_client.create_completion_message(inputs={"query": "What's the weather like today?"},
                                                                  response_mode="blocking", user="user_id")
completion_response.raise_for_status()

result = completion_response.json()

print(result.get('answer'))
