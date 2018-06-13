import csv

def get_html(dict):
	return """
<html>
	<body>
		<h1>""" + dict['name'] + """</h1>
		<p>""" + dict['description'] + """</p>
        <a href='""" + dict['url'] + """'>LINK</a>
        <img src='""" + dict['image'] + """'>
	</body>
</html>
"""

#product = {
    #'name' : 'Phone',
    #'description' : 'iPhone X',
    #'url': 'http://apple.com'
#}

with open('data.csv', 'r') as datafile:
    dread = csv.DictReader(datafile)
    
    for row in dread:
        print(row['name'])

        # Write HTML 
        with open(row['name'] + '.html', 'w') as file:
            file.write(get_html(row)) 
