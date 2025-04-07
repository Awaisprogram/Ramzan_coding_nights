from fastapi import FastAPI
import random

app = FastAPI()

side_hustles = [
   "Freelance web development with Django or Flask",
    "Automate Excel reports and data entry tasks",
    "Create Python bots for social media or Discord",
    "Develop and sell Python-based desktop apps",
    "Build REST APIs and sell as services (SaaS)",
    "Scrape data and sell insights (with permission)",
    "Create & monetize coding tutorials on YouTube",
    "Write Python eBooks or blog posts for revenue",
    "Make CLI tools and publish on GitHub/marketplaces",
    "Offer data visualization services (e.g., Matplotlib, Plotly)",
    "Build Telegram bots for businesses",
    "Create Chrome extensions with Python (via PyScript)",
    "Develop automation scripts for small businesses",
    "Teach Python on platforms like Udemy or Skillshare",
    "Sell code snippets or automation tools on Gumroad",
    "Create resume generators or form builders in Python",
    "Work as a freelance Python tutor or mentor",
    "Offer API integration services to startups",
    "Build mini SaaS tools with Streamlit or Gradio",
    "Make and sell trading bots (legally, of course)",
    "Do tech writing for Python libraries or docs",
    "Offer PDF or invoice generation tools for small biz",
    "Analyze stock or crypto data and sell reports",
    "Participate in Kaggle competitions for cash",
    "Do AI/ML model fine-tuning and sell services"
]

money_quotes = [
    "Too many people spend money they haven't earned to buy things they don't want to impress people they don't like. – Will Rogers",
    "It's not your salary that makes you rich, it’s your spending habits. – Charles A. Jaffe",
    "Do not save what is left after spending, but spend what is left after saving. – Warren Buffett",
    "Time is more valuable than money. You can get more money, but you cannot get more time. – Jim Rohn",
    "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn",
    "Never depend on a single income. Make an investment to create a second source. – Warren Buffett",
    "Money is a terrible master but an excellent servant. – P.T. Barnum",
    "The goal isn’t more money. The goal is living life on your terms. – Chris Brogan",
    "Rich people have small TVs and big libraries, and poor people have small libraries and big TVs. – Zig Ziglar",
    "You must gain control over your money or the lack of it will forever control you. – Dave Ramsey",
    "A penny saved is a penny earned. – Benjamin Franklin",
    "Don’t tell me where your priorities are. Show me where you spend your money and I’ll tell you what they are. – James W. Frick",
    "An investment in knowledge always pays the best interest. – Benjamin Franklin",
    "If you live for having it all, what you have is never enough. – Vicki Robin",
    "Beware of small expenses; a small leak will sink a great ship. – Benjamin Franklin"
]

@app.get("/side_hustles")
def get_side_hustles():
  """Return a simple side hustle idea"""
  return {"side_hustle":random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes():
  """Return a simple money quotes idea"""
  return {"money_quotes":random.choice(money_quotes)}
