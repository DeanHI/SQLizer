import sqlite3
from flask import Flask, render_template, request
from app import app@app.route('/iteminsert/<table_name>', methods=['POST'])
def item_insert_filter_by(table_name):
	excols = request.form.getlist("colname")
	newvals = request.form.getlist("newvalue")
	excols = ", ".join(excols)	excols = " (" + excols +") "
	new_val = []
	for i in newvals:
		if i != '':
			new_val.append(i)	
	new_val_filter = []
	for word in new_val:
		if word.isnumeric() == True:
			new_val_filter.append(word)
		else:
			new_val_filter.append("'" + word + "'")		new_val_filter = " (" + ", ".join(new_val_filter) + ")"
	code_to_be_executed = "INSERT INTO " + table_name + excols + "VALUES" + new_val_filter
	#code_to_be_executed = "INSERT INTO " + table_name + excols +(" + new_val_filter + ") "
	return render_template("itemdeletefilterby.html", code_to_be_executed=code_to_be_executed)@app.route('/iteminsert', methods=['POST'])
def item_insert():
	sqlite_file = 'inventory_schema'	
	con = sqlite3.connect(sqlite_file)
	c = con.cursor()
	
	table_name = request.form["table"]

	col_list = []
	executor = 'select * from ' + table_name
	c.execute(executor)
	for j in c.description:		
		col_list.append(j[0])	return render_template('iteminsert.html', \
	table_name=table_name, col_list=col_list)