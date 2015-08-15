#LAB6 Python starter code
#imports go here
#import MySQLdb
import _mysql
import sys

#code goes here

buffer = "true"



def oneQuery():
	db = _mysql.connect(host="localhost",user="kopet",passwd="RE2",db="honeydo2")
	db.query("""SELECT * FROM brand;""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()

def twoQuery():
	db = _mysql.connect(host="localhost",user="kopet",passwd="RE2",db="honeydo2")
	db.query("""SELECT ItemName FROM home_item;""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()

def threeQuery():
	db = _mysql.connect(host="localhost",user="kopet",passwd="RE2",db="honeydo2")
	#db.query("""SELECT * FROM vineyard WHERE vineyardID NOT IN (SELECT * FROM vineyard as a, funding AS b WHERE  
	#	a.vineyardID = b.vineyardID;)""")
	# db.query("""SELECT vineyardID FROM vineyard WHERE vineyardID not in (select vineyardID from funding)""")
	db.query("""SELECT storeName FROM store""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	if nR == 0:
		print("""nothing to see here""")
	db.close()
	
while buffer:

	print("""
	0.Exit
	1.See brands
	2.See items in your home pantry
	3.See your favorite stores
	""")
	buffer=input("what would you like to do? ")
	
	if (buffer == "0"): 
		print ("\n\n\n\n\nNooooo don\'t quit me now!!!") 
		sys.exit("Bye!");
		
	if (buffer == "1"):
		oneQuery();
	if (buffer == "2"):
		twoQuery();
	if (buffer == "3"):
		threeQuery();
