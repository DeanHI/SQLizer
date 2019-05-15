import timeimport sqlite3from flask import Flask, render_template, requestfrom schema_create import create_store_schema, insert_initial_valuesfrom sitenavigation import get_category, products_from_cat, product_presentapp = Flask(__name__)####################these are the imports and flask connectivity##############	##https://upload.wikimedia.org/wikipedia/commons/b/bc/Nikola_Tesla_holding_in_his_hands_balls_of_flame.gif############everything below here down to next hashtag sign deals with site navigation#################@app.route('/<cat>/<product>')def product_present(cat, product):	import sqlite3		sqlite_file = 'inventory_schema'		con = sqlite3.connect(sqlite_file)	c = con.cursor()	val_list = []	col_list = []		 	col_list_multiplier = 0			executor = 'select * from {} where productname = "{}"'.format(cat, product)	c.execute(executor)	for i in c.fetchall():		col_list_multiplier += 1		val_list.append(i)	for j in c.description:				col_list.append(j[0])			col_list = [col_list]*col_list_multiplier	product_dict = list(map(dict, map(zip, col_list, val_list)))	product_dict = product_dict[0]	return render_template('productview.html', cat=cat, product=product, product_dict=product_dict)@app.route('/<cat>')def products_from_cat(cat):	import sqlite3		sqlite_file = 'inventory_schema'		con = sqlite3.connect(sqlite_file)	c = con.cursor()		products_line = []		get_products = ('select productname from ' + cat)	c.execute(get_products)	for productname in c.fetchall():		products_line.append((str(productname)[2:-3]))				return render_template('products.html', products_line=products_line, cat=cat)@app.route('/')@app.route('/productcat')def get_category():	import sqlite3		sqlite_file = 'inventory_schema'		con = sqlite3.connect(sqlite_file)	c = con.cursor()		category_line = []	c.execute('select name from sqlite_master where name not like "sqlite_sequence"')	for name in c.fetchall():		category_line.append((str(name))[2:-3])			return render_template('categories.html', category_line=category_line)######---------------<<<<<<<<<<<<DASHBOARD STUFF>>>>>>>>>>>--------------#############@app.route('/tableview', methods=['POST'])def table_view():	table_name = request.form["table"]		chosen_table = table_dict(table_name)	return render_template("tableview.html", chosen_table=chosen_table, table_name=table_name)	@app.route('/tableedit/<table_name>/filters<update_list>', methods=['POST', 'GET'])def updatefilterby(table_name, update_list):	excols = request.form.getlist("existing_columns")	exvals = request.form.getlist("existing_values")	clause = request.form["clause"]		exis_val = []	for i in exvals:		if i != '':			exis_val.append(i)			update_zip = zip(excols, exis_val)	filters = []	for word1, word2 in update_zip:		if word2.isnumeric() == True :			filters.append(word1 + " = " + word2 + " " + clause + " ")		else:			filters.append(word1 + " = '"+ word2 + "' " + clause + " ")			filters = "".join(filters)	filtersplit = filters.split(" ") 	if filtersplit[-2] == "OR":		filters = filters[:-3]	if filtersplit[-2] == "AND":		filters = filters[:-4]	#filters = "(" + filters + ")"			return render_template("updatefilterby.html", update_list=update_list, table_name=table_name,\	filters=filters)@app.route('/tableedit/<table_name>', methods=['POST', 'GET'])def updatetable(table_name):	sqlite_file = 'inventory_schema'		con = sqlite3.connect(sqlite_file)	c = con.cursor()		col_list = []	executor = 'select * from ' + table_name	c.execute(executor)	for j in c.description:				col_list.append(j[0])		colname = request.form.getlist("colname")	newvalue = request.form.getlist("newvalue")	#get all checked boxes from colname, get all text inputs from newvalue	new_val = []	for i in newvalue:		if i != '':			new_val.append(i)		#this is for receiving only non-empty input from user to match with number of ticked boxes	update_zip = zip(colname, new_val)	update_list = []	for word1, word2 in update_zip:		if word2.isnumeric() == True :			update_list.append(word1 + " = " + word2 + ", ")		else:			update_list.append(word1 + " = '" + word2 + "', ")		update_list = "".join(update_list)	update_list = update_list[:-2]	#this is for creating the new SQL hint - UPDATE{{table_name}} SET {{columname}}={{value}}	#also for eliminating any ''s from numbers if possible		c.execute("select * from " + table_name)	all_vals = [i for i in c.fetchall()]	single_column = len(all_vals[0])	existing_columns = []	for i in range(single_column):		for j in all_vals:						existing_columns.append(j[i])	#this brings all the existing values in table for the filter-by section	newl = []	for i in range(0, len(existing_columns), len(all_vals)):		newl.append(existing_columns[i:i + len(all_vals)])	#this arranges the list before in byte-sized chunks for iteration in the html			return render_template('tableupdate.html', colname=colname, \	table_name=table_name, col_list=col_list, new_val=new_val, update_list=update_list,\	newl=newl)			@app.route('/tableedit', methods=['POST'])def table_edit():	table_name = request.form["table"]	sqlite_file = 'inventory_schema'		con = sqlite3.connect(sqlite_file)	c = con.cursor()		val_list = []	col_list = []		executor = 'select * from ' + table_name	c.execute(executor)	for i in c.fetchall():		val_list.append(i)	for j in c.description:				col_list.append(j[0])	return render_template("tableedit.html", table_name=table_name, col_list=col_list, val_list=val_list)	@app.route('/dashboard')def choose_table_to_view():	import sqlite3		sqlite_file = 'inventory_schema'		con = sqlite3.connect(sqlite_file)	c = con.cursor()		table_names = []	c.execute('select name from sqlite_master where name not like "sqlite_sequence"')	for name in c.fetchall():		table_names.append((str(name))[2:-3])			return render_template("inventory_management_and_statistics.html", table_names=table_names)	@app.route('/useraction')def user_action():	return render_template('useraction.html')			######---------------<<<<<<<<<<<<DASHBOARD STUFF>>>>>>>>>>>--------------#############		############everything above here up to next hashtag sign deals with site navigation#################		@app.route('/viewtables')def view_all_tables():	sqlite_file = 'inventory_schema'		con = sqlite3.connect(sqlite_file)	c = con.cursor()		newl = []	c.execute('select name from sqlite_master where name not like "sqlite_sequence"')	for name in c.fetchall():		newl.append(table_dict((str(name))[2:-3]))			con.close()		return render_template("viewtables.html", newl=newl)		def get_product_dict(cat, product):	import sqlite3		sqlite_file = 'inventory_schema'		con = sqlite3.connect(sqlite_file)	c = con.cursor()		val_list = []	col_list = []	 	col_list_multiplier = 0			executor = 'select * from {} where productname = "{}"'.format(cat, product)	c.execute(executor)	for i in c.fetchall():		col_list_multiplier += 1		val_list.append(i)	for j in c.description:				col_list.append(j[0])		col_list = [col_list]*col_list_multiplier		table_dict = list(map(dict, map(zip, col_list, val_list)))		return render_template('tables.html')	def table_dict(table_name):	"""function for returning complete html tables by paramaters passed to table (table name)"""		sqlite_file = 'inventory_schema'		con = sqlite3.connect(sqlite_file)	c = con.cursor()		val_list = []	col_list = []	 	col_list_multiplier = 0			executor = 'select * from ' + table_name	c.execute(executor)	for i in c.fetchall():		col_list_multiplier += 1		val_list.append(i)	for j in c.description:				col_list.append(j[0])		col_list = [col_list]*col_list_multiplier		table_dict = list(map(dict, map(zip, col_list, val_list)))	return table_dict			##################this runs the app so ignore this##############if __name__ == "__main__":	app.run(debug = True)	#product()
