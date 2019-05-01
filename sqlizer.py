import time
import sqlite3
from flask import Flask, render_template
from schema_create import create_store_schema, insert_initial_values

app = Flask(__name__)

@app.route('/') 
@app.route('/home')
def table_present():
	sqlite_file = 'inventory_schema'	
	con = sqlite3.connect(sqlite_file)
	c = con.cursor()
	col_list = []
	val_list = []
	c.execute('Select * from vacuumcleaners')
	for i in c.fetchall():
		val_list.append(i)
	for j in c.description:
		col_list.append(j[0])
	return render_template('home.html', val_list=val_list, col_list=col_list)
	
	
		



if __name__ == "__main__":
	app.run(debug = True)
	
