from django.http import HttpResponse

class JSONResponse(HttpResponse):

	# An HttpResponse that renders its content into JSON

	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)
		