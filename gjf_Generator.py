import os
import re
inp=re.compile('\s+[0]\s+[1]')
addtext='%nprocshared=20 \n%mem=5GB \n#p opt b3lyp/6-311+g(2d,p) \n\n'
def generate_gjf(gjfpath, groupid, id):
	with open(gjfpath,'r') as f:
		content=f.read()
		firstpost=re.search(inp,content).start()
		#firstpost=content.find('[No title]')
		lastpost=content.find('Lp')
		content=addtext+groupid+id+'\n'+content[firstpost:lastpost]+'\n \n'
	with open(gjfpath,'w') as f:
		f.write(content)

for l in ['G']:
	for i in range(1,30):
		try:
			generate_gjf(l+str(i)+'.gjf', l, str(i))
		except FileNotFoundError:
			pass

#generate_gjf('A16.gjf','A','16')