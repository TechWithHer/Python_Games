import requests
import random
import time

def fetch_pokemon_list():
    url = "https://pokeapi.co/api/v2/pokemon?limit=100"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print("❌ Failed to fetch Pokémon list.")
        return []

def get_pokemon_details(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        types = [t["type"]["name"] for t in data.get("types", [])]
        exp = data.get("base_experience", 0)
        return types, exp
    return [], 0

def play_pokemon_game():
    print("🐾 Welcome to 'Guess the Pokémon'!")
    time.sleep(1)

    pokemon_list = fetch_pokemon_list()
    if not pokemon_list:
        return

    p = random.choice(pokemon_list)
    name = p["name"]
    types, exp = get_pokemon_details(p["url"])

    print("\nHere are your hints:")
    print(f"- Type(s): {', '.join(types)}")
    print(f"- Base experience: {exp}")
    
    guess = input("\n❓ Who am I? ").strip().lower()

    if guess == name:
        print(f"🎉 Correct! You guessed **{name.title()}**!")
    else:
        print(f"❌ Wrong! I was **{name.title()}**.")

if __name__ == "__main__":
    play_pokemon_game()
