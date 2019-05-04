import time
import sqlite3
from flask import Flask, render_template, request
from schema_create import create_store_schema, insert_initial_values

app = Flask(__name__)


def view_table():
	pass



@app.route('/useraction')
def user_action():
	return render_template('useraction.html')

@app.route('/tablepresent', methods=['POST'])
def table_present():
	
	user_input = request.form['sqlscript']

	sqlite_file = 'inventory_schema'	
	con = sqlite3.connect(sqlite_file)
	c = con.cursor()
	
	col_list = []
	val_list = []	
	
	try:
		if user_input[0:6].lower() == "select":
			c.execute(user_input)
			for i in c.fetchall():
				val_list.append(i)
			for j in c.description:
				col_list.append(j[0])
			return render_template('tablepresent.html', col_list=col_list, val_list=val_list)
		else:
			c.execute(user_input)
			con.commit()
			return "<p style='color:green;'>Command executed succesfuly!<br></p>" + render_template('useraction.html')
	except Exception as e:
		raise
		
@app.route('/viewtables')
def view_all_tables():
	import sqlite3	
	sqlite_file = 'inventory_schema'	
	con = sqlite3.connect(sqlite_file)
	c = con.cursor()
	
	col_list = []
	val_list = []

	c.execute('select productname, productprice,ispremium,numofproductsold from screens where productid in (2,3,4)')
	for i in c.fetchall():
		val_list.append(i)
	for j in c.description:
		col_list.append(j[0])
	return render_template('tables.html', col_list=col_list, val_list=val_list)
	
				
	
	
	

if __name__ == "__main__":
	app.run(debug = True)
