\# 🌐 PageRank (CS50 AI)



\## 📌 Overview

This project implements the \*\*PageRank algorithm\*\*, originally developed by Google to rank web pages based on their importance.



The program estimates the probability that a random surfer lands on each page by analyzing the structure of links between pages.



Two approaches are implemented:

\- \*\*Sampling (Monte Carlo simulation)\*\*

\- \*\*Iterative calculation (power iteration method)\*\*



\---



\## 🧠 How It Works



The web is modeled as a \*\*directed graph\*\*:



\- \*\*Nodes\*\* → Web pages  

\- \*\*Edges\*\* → Links from one page to another  



PageRank is based on the idea that:

> A page is important if it is linked to by other important pages.



\---



\## 🔁 PageRank Model



At each step, a random surfer:



\- Follows a link from the current page with probability \*\*d (damping factor)\*\*  

\- Jumps to a random page with probability \*\*1 - d\*\*



This results in a probability distribution over all pages.



\---



\## ⚙️ Features



\- Computes PageRank using \*\*sampling\*\*  

\- Computes PageRank using \*\*iterative convergence\*\*  

\- Handles pages with no outgoing links (dangling pages)  

\- Ensures final probabilities sum to 1  



\---



\## 📂 Project Structure



```

pagerank/

│── pagerank.py     # Main program

│── corpus0/        # Sample dataset

│── corpus1/        # Larger dataset

│── corpus2/        # Additional dataset

```



\---



\## ▶️ Usage



Run the program:



```bash

python3 pagerank.py corpus0

```



\---



\## 🧪 Example Output



```

PageRank Results from Sampling (n = 10000)

&#x20; 1.html: 0.2212

&#x20; 2.html: 0.4321

&#x20; 3.html: 0.3467



PageRank Results from Iteration

&#x20; 1.html: 0.2198

&#x20; 2.html: 0.4305

&#x20; 3.html: 0.3497

```



\---



\## 🧩 Key Concepts



\- Markov chains  

\- Probability distributions  

\- Graph theory  

\- Monte Carlo methods  

\- Iterative convergence  



\---



\## 🚀 Possible Improvements



\- Optimize performance for larger datasets  

\- Visualize the link graph  

\- Compare convergence speed of methods  

\- Extend to weighted links  



\---



\## 📚 Acknowledgements



This project is part of Harvard's \*\*CS50: Introduction to Artificial Intelligence with Python\*\*.



\---



\## 👨‍💻 Author



Karl Henrik May

https://github.com/khmmay

