"""Problem 01 (merged): setup + first GET request.

Install dependencies (once):
    pip install requests fastapi uvicorn

Task:
1. Send a GET request to https://jsonplaceholder.typicode.com/todos/1
2. Print:
   - status code
   - Content-Type header
   - raw body (response.text)
   - parsed JSON (response.json())
3. Read and print: id, title, completed
4. Add error handling with raise_for_status()

Expected result:
- You can explain the difference between raw text and parsed JSON.
"""

import requests

URL = "https://jsonplaceholder.typicode.com/todos/1"


def main() -> None:
    # TODO: implement request flow here.
    # Suggested variables: response, data
    response = requests.get(URL)

    response.raise_for_status()
    print("Status Code: ", response.status_code)
    print("Content-Type ", response.headers.get("Content-Type"))
    print("Raw body: ", response.text)
    data = response.json()
    print("Parsed Json: ", data)


    print("id:           ", data["id"])
    print("title:        ", data["title"])
    print("completed:    ", data["completed"])
    


if __name__ == "__main__":
    main()
