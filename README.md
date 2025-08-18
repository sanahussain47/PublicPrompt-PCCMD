# PublicPrompt-PCCMD
# 💬 PublicPrompt Chatbot

**PublicPrompt** is a lightweight AI-powered chatbot designed to handle public queries related to the **Price Control & Commodity Management Department (PC&CMD), Punjab**.  

This project demonstrates a practical use case for automating repetitive public queries and providing quick responses via a friendly chat interface.

---

## **Features**

- Text-based conversational interface  
- Predefined intent recognition for PC&CMD queries  
- Rule-based responses stored in `intents.json`  
- Sample questions with clickable buttons  
- Latest messages displayed at the top (chat-like view)  
- Lightweight and easy to deploy using **Streamlit**  
- Optional OpenAI API integration for fallback responses  

---

## **How It Works**

1. User types a question or clicks a sample query.  
2. Chatbot checks the **intent database (`intents.json`)**.  
3. If the intent matches → returns a predefined response.  
4. If the intent is unknown → optional fallback to OpenAI API.  
5. Chat history is maintained, with the latest messages shown first.  

---

## **Sample Queries**

- Current wheat price  
- File a complaint  
- PC&CMD contact number  
- Office hours  
- Flour license procedure  
- Upcoming auctions or notifications  
- Warehouse stock availability  
- Payment procedure  
- Submit feedback  

---

## **Getting Started**

### **Prerequisites**

- Python 3.x  
- Streamlit library  
- Optional: OpenAI API key for enhanced responses  

---

### **Installation**

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/PublicPrompt-PCCMD.git
cd PublicPrompt-PCCMD
