import nltk
from textblob import TextBlob
from newspaper import Article
import tkinter as tk

def summarize():
    url = utext.get('1.0',"end").strip()
    #print("URL entered:", url)  # Add this line for debugging
    nltk.download('punkt') # for sentiment analysis
    

    #url = 'https://www.theatlantic.com/magazine/archive/2011/07/the-madness-of-cesar-chavez/308557/'

    article = Article(url, browser_user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")


    article.download() # download the article
    article.parse() # disect the article to required parts.

    article.nlp() # process nlp
    #print("Article title:", article.title)  # Add this line for debugging
    #print("Article authors:", article.authors)  # Add this line for debugging

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')
     
    title.delete('1.0','end')
    title.insert('1.0',article.title)
    
    author.delete('1.0','end')
    author.insert('1.0',article.authors)

    publication.delete('1.0','end')
    publication.insert('1.0',article.publish_date)

    summary.delete('1.0','end')
    summary.insert('1.0',article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0','end')
    sentiment.insert('1.0', f'Polarity: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

    
 



root = tk.Tk()
root.title("Article Summarizer")
root.geometry("1200x600")

tlabel=tk.Label(root,text="Title")
tlabel.pack()

title = tk.Text(root,height=1,width=140)
title.config(state='disabled',bg='#dddddd')
title.pack()


alabel=tk.Label(root,text="Author")
alabel.pack()

author = tk.Text(root,height=1,width=140)
author.config(state='disabled',bg='#dddddd')
author.pack()

plabel=tk.Label(root,text="Publication")
plabel.pack()


publication = tk.Text(root,height=1,width=140)
publication.config(state='disabled',bg='#dddddd')
publication.pack()

slabel=tk.Label(root,text="Summary")
slabel.pack()


summary = tk.Text(root,height=20,width=140)
summary.config(state='disabled',bg='#dddddd')
summary.pack()

selabel=tk.Label(root,text="Sentiment")
selabel.pack()

sentiment = tk.Text(root,height=1,width=140)
sentiment.config(state='disabled',bg='#dddddd')
sentiment.pack()

url=tk.Label(root,text="Url")
url.pack()

utext = tk.Text(root,height=1,width=140)
utext.pack()

btn = tk.Button(root,text="Summerize", command=summarize)
btn.pack()


root.mainloop()