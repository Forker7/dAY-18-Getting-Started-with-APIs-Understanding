import requests

def get_random_data():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()
        return f"{joke['setup']} - {joke['punchline']}"
    else:
        return "Failed to retrieve joke from the API."\

def main():
    print("Welcome to the Random Joke Generator!")
    while True:
        user_input = input("Press Enter to get a random joke or type 'exit' to quit: ").strip().lower()
        if user_input in ("q", "exit"):
            print("Goodbye!")
            break
        else:
            joke = get_random_data()
            print(joke)

if __name__ == "__main__":
    main() #dd
