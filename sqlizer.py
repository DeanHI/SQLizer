import time
import sqlite3
from flask import Flask, render_template
from schema_create import create_store_schema, insert_initial_values


def main():
	sqlite_file = 'inventory_schema'	
	con = sqlite3.connect(sqlite_file)
	c = con.cursor()
	
	while True:
		user_input = input("execute SQL script:")
		
		if user_input[0:6].lower() == 'select':
			c.execute(user_input)
			print(c.fetchall())
		elif user_input[0].lower() == 'q':
			return
		else:
			c.execute(user_input)
			con.commit()

	con.close()



if __name__ == "__main__":
	main()
	






# @app.route('/') #remember this because this what comes after local host, which 127.0.0.1:whatever port(5000 default), then anything after / is another page
# @app.route('/home')
# def printme(): 
	# return render_template ('home.html')


#if __name__ == "__main__":
	#with sqlite3.connect('inventory_schema') as  
	#app.run(port = 443, debug = True)
	#intro_print()
