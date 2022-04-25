# WebCrawler
This is a web crawler application that navigates trough the web https://news.ycombinator.com/ and extracts the **title, rank, amount of commentaries and score** of the first 30 entries that it finds. It also let you filter the entries which title have more than 5 words, or less or equal than 5 words.

# Instructions
This console application uses the following libraries, so make sure you have them:
1. Requests

    ```pip install requests```
2. BeautifulSoup

    ```pip install beautifulsoup4```
3. Pandas

    ```pip install pandas```
4. Regex

    ```pip install regex```
    
Once you have these libraries installed and run the console application you will have some options like this:
```
Type 1 if you want the entries with more than 5 words in the title.
Type 2 if you want the entries 5 words or less
Type 3 if you don't want to use filters
```

You will have to type 1, 2 or 3 depending if you want to filter the data or if you don't want to filter the data. After you type the option you prefer it will show you the results like this.

```
                                               Titles Ranks      Points      Comments
0   French fighter jet joy ride goes très, très wr...    1.  339 points  143 comments
1   Maximum Flow and Minimum-Cost Flow in Almost-L...    2.   11 points          None
2    Drones have transformed blood delivery in Rwanda    3.  166 points   27 comments
3         Fedora 36: A brave new (DRM/KMS only) world    4.  185 points   95 comments
4   Patching an embedded synthesiser OS from 1996 ...    5.  211 points   28 comments
5   Pushing back against contract demands is scary...    6.  189 points   99 comments
6   Calling NSA to find your encryption key after ...    7.  150 points   65 comments
7    How easy is it in 2022 to find a SHA1 collision?    8.    6 points          None
8    Some of the forces blocking new ideas in science    9.   98 points   26 comments
9   A Swedish skier was basically frozen, but live...   10.  171 points   97 comments
10  The Psychedelic Experience: A new concept in p...   11.   75 points   49 comments
11  Zeit Medical (YC S21) Is Hiring an ML scientis...   12.        None          None
12                         The TTY Demystified (2008)   13.   58 points   10 comments
13  Textualize – A framework for building Text Use...   14.  282 points   63 comments
14  Norway convinced Japan to love salmon sushi (2...   15.   51 points   37 comments
15                   The afterlife of used hotel soap   16.  242 points  187 comments
16   Large-Scale Artificial Intelligence Open Network   17.    5 points          None
17  A simple explanation of how money moves around...   18.  110 points   34 comments
18  Generating the pseudo-random codes that measur...   19.    4 points          None
19  Evolution is not a tree of life but a fuzzy ne...   20.   46 points   12 comments
20                                     Perpetual Bond   21.    4 points          None
21  In a surprise move, honeybee tongue hairs repe...   22.   12 points          None
22  Do the same mechanisms that create complex lif...   23.    3 points          None
23  Twitter re-examines Elon Musk’s bid, may be mo...   24.   36 points   24 comments
24                        Making 3D printing truly 3D   25.    6 points          None
25  10 years since Google said to “hang tight” abo...   26.  307 points  116 comments
26     My lazy Wordle strategy: same words every time   27.   69 points  103 comments
27  Trove of tumour genomes offers clues to cancer...   28.   46 points    5 comments
28  How to Build a BVH (Bounding Volume Hierarchy)...   29.   50 points   10 comments
29                            Forced Colors Explained   30.    9 points          None
```
