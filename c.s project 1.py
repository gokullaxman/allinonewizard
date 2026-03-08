import tkinter as tk
from PIL import Image, ImageTk
import speech_recognition as sr
import webbrowser
from time import strftime, sleep
import pyttsx3
from googlesearch import search
import requests
from tkinter import messagebox
import random
import pycountry

# Global variables
lbl, t_entry, root, img_speech = None, None, None, None
word, guesses, life_points = "", [], 6  # Initialize hangman game variables


word_label = None
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)  # Clear the entry field
    else:
        messagebox.showinfo("Empty Task", "Please enter a task.")

def remove_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        task_index = selected_index[0]
        del tasks[task_index]
        task_listbox.delete(task_index)
    else:
        messagebox.showinfo("No Task Selected", "Please select a task to remove.")

tasks = []


def get_places():
   places = list(country.name for country in pycountry.countries)
   return places


def get_display_word():
    display_word = ""
    for letter in word:
        if letter in guesses:
            display_word += letter
        else:
            display_word += "_"
    return display_word

def make_guess():
    global life_points

    guess = guess_entry.get().lower()

    if len(guess) == 1 and guess.isalpha():
        if guess in guesses:
            messagebox.showinfo("Invalid Guess", "You already guessed this letter.")
        else:
            guesses.append(guess)

            display_word = get_display_word()
            word_label.config(text=display_word)

            if guess not in word:
                life_points -= 1

            guessed_label.config(text=f"Guessed Letters: {' '.join(guesses)}")
            life_label.config(text=f"Life Points: {life_points}")

            if "_" not in display_word:
                messagebox.showinfo("Congratulations!", "You guessed the word!")
                reset_game()

            if life_points == 0:
                messagebox.showinfo("Game Over", f"Sorry, you ran out of life points. The word was '{word}'.")
                reset_game()

    else:
        messagebox.showinfo("Invalid Guess", "Please enter a single letter.")

def reset_game():
    global word, guesses, life_points
    word = random.choice(word_list)
    guesses = []
    life_points = 6
    word_label.config(text=get_display_word())
    guessed_label.config(text="Guessed Letters: ")
    life_label.config(text=f"Life Points: {life_points}")

def open_hangman_window():
    # Initialize the word list with places
    global word_list  # Make word_list global
    word_list = get_places()

    # Hangman window components
    hangman_window = tk.Toplevel(root)
    hangman_window.title("Hangman Game")

    # Make word_label global
    global word_label
    word_label = tk.Label(hangman_window, text=get_display_word(), font=('Helvetica', 24))
    word_label.pack(pady=20)

    hangman_guess_label = tk.Label(hangman_window, text="Guess a letter:", font=('Helvetica', 16))
    hangman_guess_label.pack()

    global guess_entry  # Make guess_entry global
    guess_entry = tk.Entry(hangman_window, font=('Helvetica', 16))
    guess_entry.pack()

    hangman_guess_button = tk.Button(hangman_window, text="Guess", command=make_guess, font=('Helvetica', 16))
    hangman_guess_button.pack(pady=10)

    global guessed_label, life_label  # Make labels global
    guessed_label = tk.Label(hangman_window, text="Guessed Letters: ", font=('Helvetica', 16))
    guessed_label.pack()

    life_label = tk.Label(hangman_window, text=f"Life Points: {life_points}", font=('Helvetica', 16))
    life_label.pack()

def get_weather(api_key, city):
    base_url = 'http://api.weatherstack.com/current'

    params = {
        'access_key': api_key,
        'query': city
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None


def get_weather(api_key, city):
    # Get weather data from Weatherstack API
    base_url = 'http://api.weatherstack.com/current'

    params = {
        'access_key': api_key,
        'query': city
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def update_weather(api_key, city, label_temperature, label_description):
    # Update weather information on the GUI
    data = get_weather(api_key, city)

    if data:
        temperature = data['current']['temperature']
        description = data['current']['weather_descriptions'][0]
        label_temperature.config(text=f"Temperature: {temperature}°C")
        label_description.config(text=f"Description: {description}")
    else:
        messagebox.showerror("Error", "Error fetching weather data.")

def create_button(root, text, row, column, command=None):
    # Function to create a button with the specified text and command
    b = tk.Button(root, text=text, font=("Arial", 12), command=command)
    b.grid(row=row, column=column, padx=10, pady=10, sticky="ew")

def f_voice(speech_engine):
    # Configure text-to-speech voice
    voices = speech_engine.getProperty('voices')
    speech_engine.setProperty('voice', voices[1].id)  # Adjust the index based on available voices

def speech_output(text):
    # Convert text to speech
    speech = pyttsx3.init()
    f_voice(speech)
    speech.say(f"sir: {text}")
    speech.runAndWait()

def on_click(event):
    voice_recognition()  # the voice button click event

def button_click(site):
    if site == "Speech":
        voice_recognition()
    elif site == "chess":
        open_chess()
    elif site == "neon pong":
        open_pong()
    else:
        webbrowser.open(w_urls.get(site, "https://www.google.com"))
def open_pong():
    url = "https://www.msn.com/en-in/play/games/neon-pong/cg-9pkb2m30zbv9?cgfrom=cg_shoreline_l1recommended&ocid=cghubl1&form=MT0072&hideNativeSidebar=1&cvid=f414c5217ae04e51b13d4761070b672c&ei=18"
    webbrowser.open(url)

def open_chess():
    url = "https://www.msn.com/en-in/play/games/master-chess/cg-9nrl2nj7l6s1?cgfrom=cg_shoreline_l1recommended&ocid=cghubl1&form=MT0072&hideNativeSidebar=1&cvid=98ef770bd4ee4ff0aa5d3232d2bbf169&ei=27"
    webbrowser.open(url)

def the_boss(_link):
    try:
        result = search(_link, num=1, stop=1)
        link = next(result, None)
        if link:
            webbrowser.open(link)
        else:
            txt = "No search results found."
            t_entry(tk.END, f'{txt}')
            print("No search results found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def voice_recognition():
    recorder = sr.Recognizer()

    try:
        with sr.Microphone() as AUDIO:
            print("Say Something...")
            t_entry.delete("1.0", tk.END)
            t_entry.insert(tk.END, f"say something.....")
            recorder.adjust_for_ambient_noise(AUDIO, duration=0.8)
            audio = recorder.listen(AUDIO)
            print("TIME OVER")
            
            t_entry.delete("1.0", tk.END)  
            t_entry.insert(tk.END, f"TIME OVER.")
            text = recorder.recognize_google(audio)
            
            t_entry.delete("1.0", tk.END)
            t_entry.insert(tk.END, f"You said: {text}\n")
            
            if "YouTube" in text :
                txt = "opening youtube"
                t_entry.insert(tk.END, f"{txt}")
                video_query = text.replace("YouTube", "")
                video_query = text.replace("open", "")
                speech_output(txt)
                webbrowser.open(f"https://www.youtube.com/results?search_query={video_query}")
            
            elif 'time' == text:
                 string = strftime('%I:%M %p')
                 speech_output(string)
            elif "search" in text:
                txt = "searching in google"
                t_entry.insert(tk.END, f"{txt}")
                search_query = text.replace("search", "")
                speech_output(txt)
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
            
            elif "tell" in text:
                txt = "searching in wikipedia"
                t_entry.insert(tk.END, f"{txt}")
                topic = text.replace("tell about", "")
                speech_output(txt)
                wikipedia_url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
                webbrowser.open(wikipedia_url)
            
            elif "close" in text:
                txt = "closing the application"
                t_entry.insert(tk.END, f"{txt}")
                close()
            
            elif "play" in text:
                query = text.replace("play", "")
                url = f"https://open.spotify.com/search/{query}"
                webbrowser.open(url)
            
            elif "open" in text:
                web_search = text.replace('open', '')
                speech_output(text)
                the_boss(web_search)

    except sr.UnknownValueError:
        a = "your majesty i could not understand audio."
        speech_output(a)
        t_entry.insert(tk.END, f"{a}")
    except sr.RequestError as e:
        a = f" I Could not request results or maybe its a network issue; {e}"
        speech_output(a)
        t_entry.insert(tk.END, f"{a}")
    except Exception as e:
        a = f"An error occurred: {e}"
        t_entry.insert(tk.END, f"{a}")
        speech_output(a)

def close():
    t_entry.insert(tk.END, "closing the application")
    sleep(1)
    root.destroy()

def time():
    string = strftime('%d-%m-%Y-|-%I:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

w_urls = {
    "Google": "https://www.google.com",
    "Youtube": "https://www.youtube.com",
    "Mail": "https://mail.google.com",
    "Wikipedia": "https://www.wikipedia.org",
    "whatsapp": "https://web.whatsapp.com/",
    "Music": "https://wynk.in/music",
    "Ssm website": "https://ssmetrust.in/ssm63/default.aspx"
}

def main():
    global lbl, t_entry, root, img_speech, task_entry, task_listbox
    api_key = '383ab22653eaf8f8a69284a15952ab00'
    city_name = 'Chennai'

    root = tk.Tk()
    root.title("All-in-One Wizard")
    root.iconbitmap(r"icon.ico")#give the path for ico
    # Example:
    root.config(bg='#DCDCDC')  # Light Amber


    # Example:
# Use an image for the speech recognition button
    img_speech = Image.open(r"voice-recognition.png")#path for voice-recognition.png
    img_speech = img_speech.resize((100, 100))
    img_speech = ImageTk.PhotoImage(img_speech)

# Create the speech recognition button with the assigned image
    speech_button = tk.Button(root, image=img_speech, command=voice_recognition, bd=0)
    speech_button.grid(row=0, column=0, padx=10, pady=10, rowspan=5, sticky="nsew")
    # List of buttons creates button in a loop
    
    button_list = ["Google", "Youtube", "Mail", "Wikipedia", "whatsapp", "Music", "Ssm website", "Hangman", "chess","neon pong"]
    for i, b in enumerate(button_list):
        if b == "Hangman":
            create_button(root, b, i + 1, 1, open_hangman_window)
        else:
            create_button(root, b, i + 1, 1, lambda site=b: button_click(site))

    t_entry = tk.Text(root, height=10, width=40)
    t_entry.grid(row=0, column=2, rowspan=5, padx=10, pady=10, sticky="ew")
    t_entry.insert(tk.END, "This code is a Tkinter-based application\n"
                           "for voice-controlled website navigation.\n"
                           "It features buttons for Google, YouTube, Gmail, Wikipedia, and voice \n"
                           "recognition. The output window displays voice recognition\n"
                           "results and actions taken  ")

    
    lbl = tk.Label(root, font=('calibri', 40, 'bold'), background='#FFFFFF', foreground='#4E342E') 
    lbl.grid(row=0, column=1, padx=10, pady=10, sticky="e")

    create_button(root, "Close", 6, 2, close)
    time()

    
    label_temperature = tk.Label(root, text="Temperature: Loading...", bg='#FFFFFF') 
    label_description = tk.Label(root, text="Description: Loading...", bg='#FFFFFF')  
    label_temperature.grid(row=8, column=2, pady=10)  
    label_description.grid(row=9, column=2, pady=10)  

    
 
    todo_frame = tk.Frame(root, bg='#CDCDC1')
    todo_frame.grid(row=0, column=3, rowspan=5, padx=10, pady=20, sticky="nsew")

    task_entry = tk.Entry(todo_frame, font=('Helvetica', 16))
    task_entry.pack(pady=10)

    add_button = tk.Button(todo_frame, text="Add Task", command=add_task, font=('Helvetica', 16))
    add_button.pack(pady=5)

    task_listbox = tk.Listbox(todo_frame, selectbackground="yellow", selectmode=tk.SINGLE, font=('Helvetica', 16))
    task_listbox.pack(pady=10)

    remove_button = tk.Button(todo_frame, text="Remove Task", command=remove_task, font=('Helvetica', 16))
    remove_button.pack(pady=5)

    

    create_button(root, "Refresh Weather", 7, 2,
                  lambda: update_weather(api_key, city_name, label_temperature, label_description))
    time()
    root.mainloop()

if __name__ == "__main__":
    main()

