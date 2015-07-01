import StringIO, sys

def printoutput(code):
	output = ""
	if code:
		codeOut = StringIO.StringIO()
		# set system out put codeOut
		sys.stdout = codeOut

		err = ""
		# catch error and store it
		try:
			exec code
		except Exception, e:
			err = e

		# set system out put back
		sys.stdout = sys.__stdout__
		# get value
		out = codeOut.getvalue()
		# close it
		codeOut.close()
		# set out put text
		output = out.replace("\n","<br>") + "<br /><br />" + str(err).replace("\n","<br>")
	return output