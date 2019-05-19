import sqlite3
from flask import Flask, render_template, request
from app import app@app.route('/itemdelete/<table_name>', methods=['POST'])def item_delete_filter_by(table_name):	excols = request.form.getlist("existing_columns")
	exvals = request.form.getlist("existing_values")
	clause = request.form["clause"]	exis_val = []
	for i in exvals:
		if i != '':
			exis_val.append(i)	
	
	update_zip = zip(excols, exis_val)
	filters = []
	for word1, word2 in update_zip:
		if word2.isnumeric() == True:
			filters.append(word1 + " = " + word2 + " " + clause + " ")
		else:
			filters.append(word1 + " = '"+ word2 + "' " + clause + " ")
	
	if len(filters) > 0:
		filters = "".join(filters)
		filtersplit = filters.split(" ") 
		if filtersplit[-2] == "OR":
			filters = filters[:-3]
		elif filtersplit[-2] == "AND":
			filters = filters[:-4]		code_to_be_executed = "DELETE FROM " + table_name + " WHERE " + filters
	else:
		code_to_be_executed = "DELETE FROM " + table_name	return render_template("itemdeletefilterby.html", table_name=table_name,\
	filters=filters, code_to_be_executed=code_to_be_executed)	

@app.route('/itemdelete', methods=['POST'])
def item_delete():
	sqlite_file = 'inventory_schema'	
	con = sqlite3.connect(sqlite_file)
	c = con.cursor()
		table_name = request.form["table"]
	col_list = []
	executor = 'select * from ' + table_name
	c.execute(executor)
	for j in c.description:		
		col_list.append(j[0])
		
	
	c.execute("select * from " + table_name)
	all_vals = [i for i in c.fetchall()]
	single_column = len(all_vals[0])
	existing_columns = []
	for i in range(single_column):
		for j in all_vals:
			
			existing_columns.append(j[i])
	newl = []
	for i in range(0, len(existing_columns), len(all_vals)):
		newl.append(existing_columns[i:i + len(all_vals)])
	#this arranges the list before in byte-sized chunks for iteration in the html
	
	
	return render_template('itemdelete.html', \
	table_name=table_name, col_list=col_list, newl=newl)
