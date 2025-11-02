# TASK- 1
# Simple Calculator

a=float(input('Enter Num1:'))
b=float(input('Enter Num2:'))
operator=input('Enter Operator(+,-,*,/):')
if operator=='+':
    result=a+b
    print('Result:',result)
elif operator=='-':
    result=a-b
    print('Result:',result)
elif operator=='*':
    result=a*b
    print('Result:',result)
elif operator=='/':
    if b!=0:
        result=a/b
        print('Result:',result)
    else:
        print('Error:Division by zero is not allowed')
else:
    print('Invalid Operation. Please enter valid operator')


#TASK- 2
#Create a Number Guessing Game
import random
def number_guessing_game():
    number_to_guess=random.randint(1,100)
    print("WELCOME, TO the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    while True:
        try:
            guess=int(input('enter your guessing number"'))
            if guess<number_to_guess:
                print('too low, try again')
            elif guess>number_to_guess:
                print('too high,try again')
            else:
                print('congratulations, Your guess is correct')
                break
        except:
            print("Please enter a valid number in the next game")
            break
number_guessing_game()


#TASK- 3
#BUILD A CONTACT BOOK
contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts.append({'name': name, 'phone': phone, 'email': email})

def view_contacts():
    for c in contacts:
        print(c)

def search_contact():
    name = input("Search name: ")
    results = [c for c in contacts if c['name'].lower() == name.lower()]
    print(results)

def delete_contact():
    name = input("Delete name: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            contacts.remove(c)
            print("Deleted")
            break

while True:
    print("1. Add | 2. View | 3. Search | 4. Delete | 5. Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        break

#TASK- 4
#AUTOMATE FILE RENAMING A FOLDER
import os

# Define folder path
folder_path = '.'

# Get list of .txt files to rename (e.g., starting with 'testfile')
files_to_rename = [f for f in os.listdir(folder_path) if f.startswith('testfile') and f.endswith('.txt')]

# Sort files for consistent ordering
files_to_rename.sort()

# Rename files with new pattern
for index, filename in enumerate(files_to_rename, start=1):
    new_name = f'file_{index}.txt'
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)
    print(f'Renamed: {filename} -> {new_name}')

#TASK-5
#PASSWORD STRENGTH CHECKER
password = input("Enter your password: ")
min_length = 8
has_number = any(char.isdigit() for char in password)
has_uppercase = any(char.isupper() for char in password)
special_chars = "!@#$%^&*()-_+=[]{};:'\",.<>?/\|"
has_special = any(char in special_chars for char in password)

if len(password) >= min_length and has_number and has_uppercase and has_special:
    print("Strong")
else:
    print("Weak")

#TASK: 6
#YOUTUBE VIDEO DOWNLOADER
from pytubefix import YouTube
from pytubefix.cli import on_progress

url=input("enter the url:")

yt= YouTube(url, on_progress_callback=on_progress)
print(yt.title)

ys= yt.streams.get_highest_resolution()
ys.download()

#TASK- 7
#BUILD A WEATHER APP
import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Temperature in Celsius
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def display_weather(data):
    if data:
        temp = data['main']['temp']
        condition = data['weather'][0]['description']
        humidity = data['main']['humidity']
        print(f"Temperature: {temp}°C")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")
    else:
        print("City not found or API error.")

 User input and usage example
api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
city_name = input("Enter city name: ")
weather_data = get_weather(city_name, api_key)
display_weather(weather_data)

#TASK- 8
#CREATE A SIMPLE CHATBOT (CLI)
print("Welcome to Simple Chatbot! Type 'exit' to quit.")
while True:
    user_input = input("You: ").strip().lower()

    if user_input == "exit":
        print("Chatbot: Goodbye! Have a great day.")
        break
    elif user_input in ["hello", "hi", "hey"]:
        print("Chatbot: Hello! How can I help you?")
    elif user_input == "what is your name?":
        print("Chatbot: I am a simple rule-based chatbot.")
    elif user_input == "what can you do?":
        print("Chatbot: I can answer basic questions like greetings and FAQs.")
    elif user_input == "how are you?":
        print("Chatbot: I'm just a bot, but I'm functioning well. How are you?")
    else:
        print("Chatbot: Sorry, I don't understand that. Please ask something else.")



    





    
    
    









