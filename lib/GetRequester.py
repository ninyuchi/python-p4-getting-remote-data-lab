import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Request failed with status code {response.status_code}")

    def load_json(self):
        response_body = self.get_response_body()
        try:
            return json.loads(response_body)
        except json.JSONDecodeError as e:
            raise Exception(f"Failed to decode JSON: {str(e)}")

if __name__ == "__main__":
    url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    requester = GetRequester(url)
    data = requester.load_json()
    print(data)
