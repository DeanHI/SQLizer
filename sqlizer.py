<<<<<<< HEAD
import timeimport sqlite3from flask import Flask, render_template, requestfrom schema_create import create_store_schema, insert_initial_valuesapp = Flask(__name__)####################these are the imports and flask connectivity##############	############everything below here down to next hashtag sign deals with site navigation#################@app.route('/<cat>/<product>')def product_present(cat, product):	import sqlite3		sqlite_file = 'inventory_schema'		con = sqlite3.connect(sqlite_file)	c = con.cursor()	val_list = []	col_list = []		 	col_list_multiplier = 0				executor = 'select * from {} where productname = "{}"'.format(cat, product)	c.execute(executor)	for i in c.fetchall():		col_list_multiplier += 1		val_list.append(i)	for j in c.description:				col_list.append(j[0])			col_list = [col_list]*col_list_multiplier	product_dict = list(map(dict, map(zip, col_list, val_list)))	product_dict = product_dict[0]	#return (product_dict)	return render_template('productview.html', cat=cat, product=product, product_dict=product_dict)@app.route('/<cat>')def products_from_cat(cat):	import sqlite3		sqlite_file = 'inventory_schema'		con = sqlite3.connect(sqlite_file)	c = con.cursor()		products_line = []		get_products = ('select productname from ' + cat)	c.execute(get_products)	for productname in c.fetchall():		products_line.append((str(productname)[2:-3]))				return render_template('products.html', products_line=products_line, cat=cat)	@app.route('/productcat')def get_category():	import sqlite3		sqlite_file = 'inventory_schema'		con = sqlite3.connect(sqlite_file)	c = con.cursor()		category_line = []	c.execute('select name from sqlite_master where name not like "sqlite_sequence"')	for name in c.fetchall():		category_line.append((str(name))[2:-3])			return render_template('categories.html', category_line=category_line)	############everything above here up to next hashtag sign deals with site navigation#################@app.route('/useraction')def user_action():	return render_template('useraction.html')@app.route('/tablepresent', methods=['POST'])def table_present():		user_input = request.form['sqlscript']	sqlite_file = 'inventory_schema'		con = sqlite3.connect(sqlite_file)	c = con.cursor()		col_list = []	val_list = []			try:		if user_input[0:6].lower() == "select":			c.execute(user_input)			for i in c.fetchall():				val_list.append(i)			for j in c.description:				col_list.append(j[0])			return render_template('tablepresent.html', col_list=col_list, val_list=val_list)		else:			c.execute(user_input)			con.commit()			return "<p style='color:green;'>Command executed succesfuly!<br></p>" + render_template('useraction.html')	except Exception as e:		raise		@app.route('/viewtables')def view_all_tables():	sqlite_file = 'inventory_schema'		con = sqlite3.connect(sqlite_file)	c = con.cursor()		newl = []	c.execute('select name from sqlite_master where name not like "sqlite_sequence"')	for name in c.fetchall():		newl.append(table_dict((str(name))[2:-3]))						con.close()		return render_template("viewtables.html", newl=newl)	@app.route('/tables')def tables():	#sqlite_file = 'inventory_schema'		#con = sqlite3.connect(sqlite_file)	#c = con.cursor()		toffee = table_dict('Screens')						#print(toffee)		return render_template("tables.html", toffee=toffee)	def get_product_dict(cat, product):	import sqlite3		sqlite_file = 'inventory_schema'		con = sqlite3.connect(sqlite_file)	c = con.cursor()		val_list = []	col_list = []	 	col_list_multiplier = 0			executor = 'select * from {} where productname = "{}"'.format(cat, product)	c.execute(executor)	for i in c.fetchall():		col_list_multiplier += 1		val_list.append(i)	for j in c.description:				col_list.append(j[0])		col_list = [col_list]*col_list_multiplier		table_dict = list(map(dict, map(zip, col_list, val_list)))		#table_dict_in_rows = [i for i in table_dict]		return render_template('tables.html')	def table_dict(table_name):	import sqlite3		sqlite_file = 'inventory_schema'		con = sqlite3.connect(sqlite_file)	c = con.cursor()		val_list = []	col_list = []	 	col_list_multiplier = 0			executor = 'select * from ' + table_name	c.execute(executor)	for i in c.fetchall():		col_list_multiplier += 1		val_list.append(i)	for j in c.description:				col_list.append(j[0])		col_list = [col_list]*col_list_multiplier		table_dict = list(map(dict, map(zip, col_list, val_list)))		table_dict_in_rows = [i for i in table_dict]	return table_dict			##################this runs the app so ignore this##############if __name__ == "__main__":	app.run(debug = True)	#product()
=======
import time
import sqlite3
from flask import Flask, render_template, request
from schema_create import create_store_schema, insert_initial_values

app = Flask(__name__)
####################these are the imports and flask connectivity##############

	
############everything below here down to next hashtag sign deals with site navigation#################
@app.route('/<cat>/<product>')
def product_present(cat, product):
	import sqlite3	
	sqlite_file = 'inventory_schema'	
	con = sqlite3.connect(sqlite_file)
	c = con.cursor()

	val_list = []
	col_list = []
		 
	col_list_multiplier = 0	
		

	executor = 'select * from {} where productname = "{}"'.format(cat, product)
	c.execute(executor)
	for i in c.fetchall():
		col_list_multiplier += 1
		val_list.append(i)
	for j in c.description:		
		col_list.append(j[0])
		
	col_list = [col_list]*col_list_multiplier
	product_dict = list(map(dict, map(zip, col_list, val_list)))
	product_dict = product_dict[0]

	#return (product_dict)
	return render_template('productview.html', cat=cat, product=product, product_dict=product_dict)

@app.route('/<cat>')
def products_from_cat(cat):
	import sqlite3	
	sqlite_file = 'inventory_schema'	
	con = sqlite3.connect(sqlite_file)
	c = con.cursor()
	
	products_line = []	
	get_products = ('select productname from ' + cat)
	c.execute(get_products)
	for productname in c.fetchall():
		products_line.append((str(productname)[2:-3]))
			
	return render_template('products.html', products_line=products_line, cat=cat)
	
@app.route('/productcat')
def get_category():
	import sqlite3	
	sqlite_file = 'inventory_schema'	
	con = sqlite3.connect(sqlite_file)
	c = con.cursor()
	
	category_line = []
	c.execute('select name from sqlite_master where name not like "sqlite_sequence"')
	for name in c.fetchall():
		category_line.append((str(name))[2:-3])
		
	return render_template('categories.html', category_line=category_line)
	
############everything above here up to next hashtag sign deals with site navigation#################


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
	sqlite_file = 'inventory_schema'	
	con = sqlite3.connect(sqlite_file)
	c = con.cursor()
	
	newl = []
	c.execute('select name from sqlite_master where name not like "sqlite_sequence"')
	for name in c.fetchall():
		newl.append(table_dict((str(name))[2:-3]))
		
		

	
	con.close()	
	return render_template("viewtables.html", newl=newl)
	
@app.route('/tables')
def tables():
	#sqlite_file = 'inventory_schema'	
	#con = sqlite3.connect(sqlite_file)
	#c = con.cursor()
	
	toffee = table_dict('Screens')
		
		

	
	#print(toffee)	
	return render_template("tables.html", toffee=toffee)
	
def get_product_dict(cat, product):
	import sqlite3	
	sqlite_file = 'inventory_schema'	
	con = sqlite3.connect(sqlite_file)
	c = con.cursor()
	
	val_list = []
	col_list = []
	 
	col_list_multiplier = 0
	
	
	executor = 'select * from {} where productname = "{}"'.format(cat, product)
	c.execute(executor)
	for i in c.fetchall():
		col_list_multiplier += 1
		val_list.append(i)
	for j in c.description:		
		col_list.append(j[0])
	
	col_list = [col_list]*col_list_multiplier
	
	table_dict = list(map(dict, map(zip, col_list, val_list)))
	
	#table_dict_in_rows = [i for i in table_dict]
	
	return render_template('tables.html')
	

def table_dict(table_name):

	import sqlite3	
	sqlite_file = 'inventory_schema'	
	con = sqlite3.connect(sqlite_file)
	c = con.cursor()
	
	val_list = []
	col_list = []
	 
	col_list_multiplier = 0
	
	
	executor = 'select * from ' + table_name
	c.execute(executor)
	for i in c.fetchall():
		col_list_multiplier += 1
		val_list.append(i)
	for j in c.description:		
		col_list.append(j[0])
	
	col_list = [col_list]*col_list_multiplier
	
	table_dict = list(map(dict, map(zip, col_list, val_list)))
	
	table_dict_in_rows = [i for i in table_dict]
	return table_dict
	
	
	
##################this runs the app so ignore this##############
if __name__ == "__main__":
	app.run(debug = True)
	#product()
>>>>>>> fc6a870dc67a0ec233421b058f47cf9e1881dae5
