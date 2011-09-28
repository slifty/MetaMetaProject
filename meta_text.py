import json
class meta_text:
	x= 3
	def GET(self, miid='', text='', url='', tasks='{}', results='{}'):
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
			results['identify_keywords'] = meta_text.identify_keywords()
		
		return results
		
	def POST(self, text_file='', url='', text='', ttl=180):
		return ''
	
	@staticmethod
	def identify_entities():
		return ''
	
	@staticmethod
	def identify_keywords():
		return ''