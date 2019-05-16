

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
		raisedef table_dict_edit(table_name):
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
		
	return render_template('tableedit.html',col_list=col_list, val_list=val_list, table_name=table_name)@app.route('/viewtables')
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