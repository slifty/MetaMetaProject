import json
import web
class meta_video:
	def GET(self, miid='', url='', tasks='{}', results='{}'):
		try:
			tasks = json.loads(tasks)
			results = json.loads(results)
		except:
			return {"error": "Invalid input parameters."}
		
		# Run through the task list
		if('identify_audio_transitions' in tasks):
			results['identify_audio_transitions'] = meta_text.identify_audio_transitions()
		if('identify_entities' in tasks):
			results['identify_entities'] = meta_text.identify_entities()
		if('identify_faces' in tasks):
			results['identify_faces'] = meta_text.identify_faces()
		if('identify_keywords' in tasks):
			results['identify_keywords'] = meta_text.identify_keywords()
		if('identify_video_transitions' in tasks):
			results['identify_video_transitions'] = meta_text.identify_video_transitions()
		if('ocr' in tasks):
			results['ocr'] = meta_text.ocr()
		if('transcribe' in tasks):
			results['transcribe'] = meta_text.transcribe()
		return results
		
	def POST(self, video_file='', url='', ttl=180):
		return ''
		
	@staticmethod
	def identify_audio_transitions():
		return ''
		
	@staticmethod
	def identify_entities():
		return ''
		
	@staticmethod
	def identify_faces():
		return ''
		
	@staticmethod
	def identify_keywords():
		return ''
		
	@staticmethod
	def identify_video_transitions():
		return ''
		
	@staticmethod
	def ocr():
		return ''
		
	@staticmethod
	def transcribe():
		return ''