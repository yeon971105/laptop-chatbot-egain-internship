## Run the chatbot:

```bash
If not installed, download Python from: [https://www.python.org/downloads/](https://www.python.org/downloads/)

---

##  Setup & Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/laptop-whisperer.git
cd laptop-whisperer

python3 prototype.py
```

---

## Project Overview

The chatbot simulates a guided product recommendation process, similar to how an AI agent would operate in a retail environment.

---

## Conversation Flow

-  **Budget selection**
-  **Primary laptop use** (e.g., school, gaming, creative work)
-  **Portability preference**

It uses rule-based decision logic to output a personalized laptop suggestion.

---

##  Error Handling

This chatbot features two types of error handling:

###  Re-prompting  
For yes/no portability input, the chatbot loops until a valid answer is received.

###  Default Assumptions  
For budget and usage questions, invalid inputs trigger a friendly fallback with a default selection to keep the experience smooth.

---

##  Screenshots / Example Output

### Chatbot Screenshot

![Chatbot Screenshot](assets/chatbot-screenshot.png)

### Terminal Output

##  Project Files

```
laptop-whisperer/
├── prototype.py       # Main chatbot script
├── assets
└── README.md          # This file
```

---

##  Future Improvements

- Integrate NLP for natural conversation handling  
- Expand the laptop dataset using APIs or web scraping  
- Replace rule-based logic with ML-based recommendation  
- Build a web or GUI version using Flask or React  

---

##  Author

**Jewon Yeon**  
Data Science Student @ San Jose State University  
Aspiring AI Researcher | Clean Code Advocate | Conversational UX Enthusiast
