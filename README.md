Challenge AI - Generating Relevant Tag Objects for Challenges

Overview:
• Project Context: This challenge is a part of a brand new project to introduce new AI based capabilities to the Topcoder platform. As of now, the project's immediate goal is to extract useful information from the challenge specification and explore its use cases. 	

Challenge Context : Within the project context mentioned above, the current challenge aims to deliver an implementation that can generate relevant tags for a challenge, using its challenge specification as input.

Implementation:
Web Framework: Django Rest Framework
IDE:PyCharm

Libraries use:
    1) Bert-extractive-summerizer: Used XLNet for text summarization
    2) Transformers
    3) TextRank Algorithm to find out the Keywords
    4) NLTK
    5) Spacy: for POS tagging
    6) Pytorch

Additional files:
    1) Stopword.txt: Addition stopword list as per the requirement and challenge.
    2) Config.json: contails the URL to EMSI and OAuth.

Input: challenge spec which a string and can either be with or without the HTML

The project consists of three part:
    1) EMSI skill Extraction: As per the guidelines, I have use the EMSI Skill API for extracting skills from the challenge spec.
    2) The Problem domain tagger
    3) Summary phrase tagger
    
