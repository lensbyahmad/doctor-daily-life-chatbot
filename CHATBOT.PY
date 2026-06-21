import tkinter as tk
from tkinter import scrolledtext

# Doctor Daily Life Questions and Answers
doctor_daily_life = {

    "what time do doctors start work":
    "Many doctors start work early in the morning, often between 7 AM and 9 AM.",

    "do doctors work long hours":
    "Yes, doctors often work long shifts that may last 10 to 24 hours depending on their specialty.",




    "what is the biggest challenge for doctors":
    "One of the biggest challenges is making accurate medical decisions under pressure.",

    "do doctors deal with stress":
    "Yes, doctors frequently experience stress due to emergencies, workload, and patient care responsibilities.",

    "how do doctors handle emergencies":
    "Doctors stay calm, assess the situation quickly, and provide immediate treatment to save lives.",

    "do doctors work on weekends":
    "Many doctors work on weekends, especially those employed in hospitals and emergency departments.",

    "do doctors have night shifts":
    "Yes, many doctors work night shifts to provide continuous patient care.",

    "how many patients does a doctor see daily":
    "The number varies, but many doctors see between 20 and 50 patients each day.",

    "what happens if a doctor makes a mistake":
    "Doctors must report, analyze, and learn from mistakes while ensuring patient safety remains the priority.",

    "how do doctors balance work and family":
    "Balancing work and family can be difficult, and many doctors carefully manage their schedules to spend time with loved ones.",

    "why do doctors keep studying":
    "Medicine constantly evolves, so doctors continue learning about new treatments, diseases, and technologies.",

    "what emotional challenges do doctors face":
    "Doctors may experience sadness, stress, and emotional exhaustion when dealing with serious illnesses or patient loss.",

    "how do doctors communicate with patients":
    "Doctors explain medical conditions, answer questions, and discuss treatment plans in a clear and respectful manner.",

    "what safety risks do doctors face":
    "Doctors may be exposed to infectious diseases, workplace stress, and physically demanding situations.",

    "why do doctors continue despite challenges":
    "Most doctors are motivated by helping people, improving health, and making a positive impact on society."
}

# Function to get chatbot response
def get_response():
    user_input = entry.get().lower().strip()
    

    response = doctor_daily_life.get(
        user_input,
        "Sorry, I only know the predefined questions about a doctor's daily life."
    )

    chat_area.insert(tk.END, f"You: {entry.get()}\n")
    chat_area.insert(tk.END, f"Doctor Bot: {response}\n\n")

    entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Doctor Daily Life Chatbot")
root.geometry("700x500")

# Title
title = tk.Label(
    root,
    text="Doctor Daily Life Chatbot",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

# Chat area
chat_area = scrolledtext.ScrolledText(
    root,
    width=80,
    height=20,
    wrap=tk.WORD
)
chat_area.pack(padx=10, pady=10)

# Input frame
frame = tk.Frame(root)
frame.pack(pady=10)


# Entry box
entry = tk.Entry(frame, width=60, font=("Arial", 12))
entry.pack(side=tk.LEFT, padx=5)

# Send button
send_button = tk.Button(
    frame,
    text="Send",
    command=get_response,
    font=("Arial", 12)
)
send_button.pack(side=tk.LEFT)

# Run application
root.mainloop()