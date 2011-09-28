import json
import nltk
import re

class meta_text:
	def GET(self, miid='', text='', url='', tasks='{}', results='{}', **kwargs):
		try:
			tasks = json.loads(tasks)
		except:
			return {"error": "Invalid input parameters."}
		
		try:
			results = json.loads(results)
		except:
			results = {}
		
		# Run through the task list
		if('identify_entities' in tasks):
			results['identify_entities'] = meta_text.identify_entities()
		if('identify_keywords' in tasks):
			results['identify_keywords'] = meta_text.identify_keywords(text, **tasks['identify_keywords'])
		
		return results
		
	def POST(self, text_file='', url='', text='', ttl=180, **kwargs):
		return ''
	
	
	@staticmethod
	def identify_entities(**kwargs):
		return ''
	
	@staticmethod
	def identify_keywords(text, type='document', **kwargs):
		text=text.lower()
		
		bigram_measures = nltk.collocations.BigramAssocMeasures()
		
		# split across any non-word character
		tokenizer = nltk.tokenize.RegexpTokenizer('[^\w\']+', gaps=True)
		
		# tokenize
		tokens = tokenizer.tokenize(text)
		
		# remove stopwords
		tokens = [w for w in tokens if not w in nltk.corpus.stopwords.words('english')]
		
		# generate bigram
		finder = nltk.collocations.BigramCollocationFinder.from_words(tokens)

		# only bigrams that appear 3+ times
		finder.apply_freq_filter(3)

		# return the 5 n-grams with the highest PMI
		return finder.nbest(bigram_measures.pmi, 3)