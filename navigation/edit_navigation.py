import sqlite3
from flask import Flask, render_template, requestfrom app import app######---------------<<<<<<<<<<<<DASHBOARD STUFF>>>>>>>>>>>--------------#############

	
	
@app.route('/tableedit/<table_name>/filters<update_list>', methods=['POST', 'GET'])
def updatefilterby(table_name, update_list):
	excols = request.form.getlist("existing_columns")
	exvals = request.form.getlist("existing_values")
	clause = request.form["clause"]
	
	exis_val = []
	for i in exvals:
		if i != '':
			exis_val.append(i)	
	
	update_zip = zip(excols, exis_val)
	filters = []
	for word1, word2 in update_zip:
		if word2.isnumeric() == True :
			filters.append(word1 + " = " + word2 + " " + clause + " ")
		else:
			filters.append(word1 + " = '"+ word2 + "' " + clause + " ")
	
	if len(filters) > 0:
		filters = "".join(filters)
		filtersplit = filters.split(" ") 
		if filtersplit[-2] == "OR":
			filters = filters[:-3]
		elif filtersplit[-2] == "AND":
			filters = filters[:-4]
		code_to_be_executed = "UPDATE " + table_name + " SET " + update_list + " WHERE " + filters
	else:
		code_to_be_executed = "UPDATE " + table_name + " SET " + update_list

	
	return render_template("/update/updatefilterby.html", update_list=update_list, table_name=table_name,\
	filters=filters, code_to_be_executed=code_to_be_executed)

@app.route('/tableedit/<table_name>', methods=['POST', 'GET'])
def updatetable(table_name):
	sqlite_file = 'inventory_schema'	
	con = sqlite3.connect(sqlite_file)
	c = con.cursor()
	
	col_list = []
	executor = 'select * from ' + table_name
	c.execute(executor)
	for j in c.description:		
		col_list.append(j[0])
	
	colname = request.form.getlist("colname")
	newvalue = request.form.getlist("newvalue")
	#get all checked boxes from colname, get all text inputs from newvalue
	new_val = []
	for i in newvalue:
		if i != '':
			new_val.append(i)
	
	#this is for receiving only non-empty input from user to match with number of ticked boxes
	update_zip = zip(colname, new_val)
	update_list = []
	for word1, word2 in update_zip:
		if word2.isnumeric() == True :
			update_list.append(word1 + " = " + word2 + ", ")
		else:
			update_list.append(word1 + " = '" + word2 + "', ")
	
	update_list = "".join(update_list)
	update_list = update_list[:-2]
	#this is for creating the new SQL hint - UPDATE{{table_name}} SET {{columname}}={{value}}
	#also for eliminating any ''s from numbers if possible
	
	c.execute("select * from " + table_name)
	all_vals = [i for i in c.fetchall()]
	single_column = len(all_vals[0])
	existing_columns = []
	for i in range(single_column):
		for j in all_vals:
			
			existing_columns.append(j[i])
	#this brings all the existing values in table for the filter-by section
	newl = []
	for i in range(0, len(existing_columns), len(all_vals)):
		newl.append(existing_columns[i:i + len(all_vals)])
	#this arranges the list before in byte-sized chunks for iteration in the html
	
	
	return render_template('/update/tableupdate.html', colname=colname, \
	table_name=table_name, col_list=col_list, new_val=new_val, update_list=update_list,\
	newl=newl)
	
	
	
@app.route('/tableedit', methods=['POST'])
def table_edit():
	table_name = request.form["table"]
	sqlite_file = 'inventory_schema'	
	con = sqlite3.connect(sqlite_file)
	c = con.cursor()
	
	val_list = []
	col_list = []
	
	executor = 'select * from ' + table_name
	c.execute(executor)
	for i in c.fetchall():
		val_list.append(i)
	for j in c.description:		
		col_list.append(j[0])
	return render_template("/update/tableedit.html", table_name=table_name, col_list=col_list, val_list=val_list)

	

	