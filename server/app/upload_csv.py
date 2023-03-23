import os
fi = form['filename']
if fi.filename:
	# This code will strip the leading absolute path from your file-name
	fil = os.path.basename(fi.filename)
	# open for reading & writing the file into the server
	open(fn, 'wb').write(fi.file.read())