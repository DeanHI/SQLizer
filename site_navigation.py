import sqlite3
from flask import Flask, render_template, requestfrom app import app

@app.route('/useraction')
def user_action():
	return render_template('useraction.html')	

		
@app.route('/category/<cat>/<product>')
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

	return render_template('productview.html', cat=cat, product=product, product_dict=product_dict)

@app.route('/category/<cat>')
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

def table_dict(table_name):
	"""function for returning complete html tables by paramaters passed to table (table name)"""
	
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

	return table_dict
@app.route('/tableview', methods=['POST'])
def table_view():

	table_name = request.form["table"]	
	chosen_table = table_dict(table_name)
	return render_template("tableview.html", chosen_table=chosen_table, table_name=table_name)


@app.route('/dashboard')
def choose_table_to_view():
	import sqlite3	
	sqlite_file = 'inventory_schema'	
	con = sqlite3.connect(sqlite_file)
	c = con.cursor()
	
	table_names = []
	c.execute('select name from sqlite_master where name not like "sqlite_sequence"')
	for name in c.fetchall():
		table_names.append((str(name))[2:-3])	
	
	return render_template("inventory_management_and_statistics.html", table_names=table_names)

@app.route('/')
def homepage():
	return render_template('homepage.html')