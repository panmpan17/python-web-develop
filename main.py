import webapp2
from deploy import printoutput

html = """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Test</title>
</head>
<body>
	<form method="post">
		<textarea name="code" id="" cols="30" rows="10">%s</textarea>
		<input type="submit">
	</form>
	<pre><code>
	%s
	</code></pre>
</body>
</html>
"""



class MainHandler(webapp2.RequestHandler):
	def get(self):
		code = self.request.get("code")
		# if other people use http://localhost?code=%code%
		if code:
			# <br> == change line
			self.response.write(printoutput(code.replace("<br>","\n")))
		else:
			self.response.write(html%("",""))
	def post(self):
		code = self.request.get("code")
		self.response.write(html%(code,"<br />"+printoutput(code)))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
