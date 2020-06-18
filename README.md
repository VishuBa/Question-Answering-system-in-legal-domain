# Question-Answering-system-in-legal-domain
This system had performed on various tasks like Question answering system, Auto-summarisation task, and keyword identification task.

Please check the case study file for understanding of the problem.

Documentation for the case study

For Part -I
Installations necessary: Torch, Torchvision, Transformers, mrakun,nltk.

1.	Since the length of given document is very large, I naturally had to select a model that performs well on large data, so I had chosen ‘bert-large-uncased’ model from huggingface pretrained model repository which was tested for QnA on Wikipedia Articles which is large data.
2.	Keyword detection for questions given to identify the topic that’s being discussed and fetch the relevant document, I did that by Rank-based Unsupervised Keyword Extraction via Metavertex Aggregation(https://github.com/SkBlaz/rakun), I have taken the code from the mentioned link. 
3.	Since Bert model takes only 512 token as input, I had to split the total tokens of the document identified into chunks(group of tokens) and implemented the model on those chunks.
4.	You can run QAbertlc.py for checking it out, make sure you have mrakun installed. (pip install mrakun)
5.	See “Sample answer.txt” for solution to the question.


For Part -II
Installations necessary: PIL, Pytesseract, pdf2image, Bert-extractive-summarizer-0.4.2, Torch.

1.	I had used pdf2image to convert PDF writ doc to images, and then passed the images through pytesseract to Tesseract engine to extract text from the images and then appended it to a new textfile.
2.	I had used Bert-extractive-summariser repo for doing the summarisation of the extracted writ document. I preferred extractive summarisation over abstractive summarisation as the domain of writ-doc is different and model might find it tough to perform abstractive summarisation.
3.	You can install the Bert-extractive-summariser by ‘pip install bert-extractive-summariser. (https://github.com/dmmiller612/bert-extractive-summarizer) here is the link for the repo. 
4.	You can go through “bert_extractive_summ.py“ for the code and the file “SKT_writ_summ.txt” contains the summary of the “SKT_writ.pdf”.





For part-III
Installations necessary: Rakun, NLTK, Cython
1.	Keyword detection for the summary that’s generated in part-II given to identify the topic that’s being discussed and fetch the relevant documents, I did that by Rank-based Unsupervised Keyword Extraction via Metavertex Aggregation(https://github.com/SkBlaz/rakun), I have taken the code from the mentioned link.
2.	I haven’t completed the code to Identify the relevant documents and summarise them contextually based on the keywords. But I have identified the keywords of every document and appended them at the end of their respective textfile, which can be used to search them.

Descriptions of each python file in the folder attached.
“bert-extractive-summ.py” – to summarise a text, function to use is “summarise(text)”
“keyword_detector.py”- to detect keywords in a text, functions include “word_detector(text)”
“Mergetxt.py” – a code snippet to merge all the Jugdments files into a single file named Combined, No functions included.
“Pdf2doc.py”- to convert all pdfs in a directory to text documents and store them in the same directory , functions included “pdf_to_text(file, file_name)”
“QAbertlc.py”- a code to identify the answers to a question from a text, functions included are “tokenize(question,text)”, “chunkify()”, “get_answer()”, “whichfile(query)” and one Class included “DocumentReader(‘path/to/model’)”






Yours sincerely,
Vikas Kesamreddy,
kesamreddyv@gmail.com






