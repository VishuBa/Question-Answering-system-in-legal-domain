import torch
from summarizer import Summarizer

assert torch.cuda.is_available()

myfile_1 = open(r"C:\Users\prasad\Desktop\SKT_writ\SKT_writ.txt")

text = myfile_1.readlines()

def summarise(text):


	model = Summarizer('distilbert-base-uncased')

	#import time

	#start = time.time()

	resp = model(text)

	#end = time.time()

	#print(f'Response Time: {end-start}')
	print(f'Summary: {resp}')

	newfile = open(r"C:\Users\prasad\Desktop\SKT_writ\SKT_writ_summ.txt", 'w+')

	newfile.write(resp)

	#print(newfile.read())
summarise(text)

