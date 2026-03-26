import os
import random
import re
import sys
import numpy as np
import copy

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    #corpus = crawl("corpus0")
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    N=len(corpus)
    Ni=len((corpus[page]))
    dic_cop=copy.deepcopy(corpus)
    summation=(N*(1-damping_factor)+Ni*damping_factor)
    for i_page in corpus:
        flag=i_page in corpus[page]
        dic_cop[i_page]=(1-damping_factor+flag*(damping_factor))/summation

    if round(sum(dic_cop.values()))!=1:
        raise AssertionError
    return dic_cop
def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    N=len(corpus)
    dic_cop= {key:0 for key in corpus}
    page=random.choice(list(corpus.keys()))
    for i_n in range(n):
        dic_cop[page]+=1
        prob_dist=transition_model(corpus,page,damping_factor)
        page=random.choices(list(prob_dist.keys()),weights=list(prob_dist.values()),k=1)[0]

    result={page:clicks/n for page,clicks in dic_cop.items()}
    if round(sum(result.values()))!=1:
        raise AssertionError
    return result



def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    N=len(corpus)
    dic_cop= {key:1/N for key in corpus}
    dic_cop2=copy.deepcopy(dic_cop)

    while True:
        changes=False
        for page in dic_cop.keys():
            for page2 in dic_cop.keys():
                if page in corpus[page2] and page!=page2:
                    dic_cop2[page]+=damping_factor*dic_cop[page2]/len(corpus[page2])
        summation=sum(dic_cop2.values())
        dic_cop2={page:PD/summation for page, PD in dic_cop2.items()}
        change_val=abs(np.array(list(dic_cop.values()))-np.array(list(dic_cop2.values())))<=0.001

        dic_cop=copy.deepcopy(dic_cop2)
        if np.all(change_val):
            break

    result=dic_cop
    if round(sum(result.values()))!=1:
        raise AssertionError
    return result

if __name__ == "__main__":
    main()
