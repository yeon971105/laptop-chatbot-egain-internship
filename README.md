Python 3.12.6
```

If not installed, download Python from: [https://www.python.org/downloads/](https://www.python.org/downloads/)

---

## ⚙️ Setup & Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/laptop-whisperer.git
cd laptop-whisperer
```

2. Run the chatbot:

```bash
python3 prototype.py
```

---

## 💡 Project Overview

The chatbot simulates a guided product recommendation process, similar to how an AI agent would operate in a retail environment.

---

## 💬 Conversation Flow

- 💰 **Budget selection**
- 🎯 **Primary laptop use** (e.g., school, gaming, creative work)
- 🧳 **Portability preference**

It uses rule-based decision logic to output a personalized laptop suggestion.

---

## 🔁 Error Handling

This chatbot features two types of error handling:

### 🔄 Re-prompting  
For yes/no portability input, the chatbot loops until a valid answer is received.

### 🛠️ Default Assumptions  
For budget and usage questions, invalid inputs trigger a friendly fallback with a default selection to keep the experience smooth.

---

## 📸 Screenshots / Example Output

### 💻 Terminal Output

```
Hi! I’m your Laptop Whisperer, here to match you with your perfect tech soulmate!

Let’s have a quick chat, and I’ll find just the right laptop for you. Sound good?
Hey there! Let’s talk budgets—what’s your price range for a shiny new laptop?
1. Keeping it chill under $600
2. Mid-range magic between $600 and $1000
3. Splurging over $1000 for the good stuff
Just pick 1, 2, or 3, and we’ll get rolling: 2

What’s the main thing you’ll be doing with your laptop?
1. Crushing it at office work or school stuff
2. Diving into epic gaming adventures
3. Unleashing your inner artist with video or photo editing
Pick 1, 2, or 3, and let’s see what fits: 2

Do you dream of a laptop that’s light as a feather and easy to carry around?
Just say ‘yes’ or ‘no’, and we’re golden: no

Based on what you told me, here’s my top pick:
-------------------------------------------------
  Acer Nitro 5 – your new gaming beast, no suitcase needed!
-------------------------------------------------
```

> 💡 You can also include a screenshot of your code or chatbot running in VS Code by adding an image named `screenshot.png` to the project folder and referencing it like this:  
> `![Chatbot Screenshot](./screenshot.png)`

---

## 📁 Project Files

```
laptop-whisperer/
├── prototype.py       # Main chatbot script
├── screenshot.png     # (Optional) Terminal or code screenshot
└── README.md          # This file
```

---

## 📈 Future Improvements

- Integrate NLP for natural conversation handling  
- Expand the laptop dataset using APIs or web scraping  
- Replace rule-based logic with ML-based recommendation  
- Build a web or GUI version using Flask or React  

---

## 👨‍💻 Author

**Jewon Yeon**  
Data Science Student @ San Jose State University  
Aspiring AI Researcher | Clean Code Advocate | Conversational UX Enthusiast
