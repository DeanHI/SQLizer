import sqlite3

def main():
	sqlite_file = 'inventory_schema'	# name of the sqlite database file
	

	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()

	while True:
		user_input = input("execute SQL script:  ")
		if user_input[0:6].lower() == 'select':
			c.execute(user_input)
			print(c.fetchall())
		elif user_input[0].lower() == 'q':
			return
		else:
			c.execute(user_input)
			
		conn.commit()
		


def insert_values():

	sqlite_file = 'inventory_schema'	# name of the sqlite database file
	

	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	laptop_value_template = 'INSERT INTO Laptops (ProductName, ManufacturerName, ManufacturerCountry, ModelYear,\
	ProductColour, ProductPrice, IsPremium, NumofProductSold, ProductSpecs, ProductComments) VALUES \
	({pname} ,{manname} ,{mancount}, {year}, {prodcolour}, {prodprice}, {ispremium}, \
	{numofproductsold}, {productspecs}, {productcomments})'
	vacuumcleaners_value_template = 'INSERT INTO VacuumCleaners (ProductName, ManufacturerName, ManufacturerCountry, ModelYear,\
	ProductColour, ProductPrice, IsPremium, NumofProductSold, ProductSpecs, ProductComments) VALUES \
	({pname} ,{manname} ,{mancount}, {year}, {prodcolour}, {prodprice}, {ispremium}, \
	{numofproductsold}, {productspecs}, {productcomments})'
	screens_value_template = 'INSERT INTO Screens (ProductName, ManufacturerName, ManufacturerCountry, ModelYear,\
	ProductColour, ProductPrice, IsPremium, NumofProductSold, ProductSpecs, ProductComments) VALUES \
	({pname} ,{manname} ,{mancount}, {year}, {prodcolour}, {prodprice}, {ispremium}, \
	{numofproductsold}, {productspecs}, {productcomments})'
	
	
	
	laptops_population = {
	'insert_value_laptops_1': laptop_value_template.format(pname = "'LayZBoy'",\
	manname = "'JLC'", mancount = "'China'", year = "'2013'", prodcolour = "'Blackish'", \
	prodprice = 3000, ispremium = 1, numofproductsold = 4, \
	productspecs = "'length: 0.3 m, width: 0.5 meters'", productcomments = "'Our number 1 product, must push more!'"),
	
	'insert_value_laptops_2': laptop_value_template.format(pname = "'Time$ucker'",\
	manname = "'JLC'", mancount = "'China'", year = "'2014'", prodcolour = "'Green'", \
	prodprice = 2300, ispremium = 0, numofproductsold = 30, \
	productspecs = "'length: 0.3 meters, width: 0.7 meters'", productcomments = "'Customer favorite, no discounts.'"),
	
	'insert_value_laptops_3': laptop_value_template.format(pname = "'Template King'",\
	manname = "'Achpunkt'", mancount = "'Germany'", year = "'2016'", prodcolour = "'Green'", \
	prodprice = 2000, ispremium = 0, numofproductsold = 7, \
	productspecs = "'length: 0.3 meters, width: 0.7 meters'", productcomments = "'Try pushing Timesucker instead.'"),
	
	'insert_value_laptops_4': laptop_value_template.format(pname = "'Hoochi-Mama'",\
	manname = "'Stars and Strips'", mancount = "'USA'", year = "'2018'", prodcolour = "'Teal'", \
	prodprice = 1500, ispremium = 0, numofproductsold = 8 , \
	productspecs = "'length: 0.5 meters, width: 0.5 meters'", productcomments = "'New and promising, maybe will sell more on holidays.'"),
	
	'insert_value_laptops_5': laptop_value_template.format(pname = "'Poor Man''s Notebook'",\
	manname = "'HLC'", mancount = "'Hungary'", year = "'2010'", prodcolour = "'Yellow'", \
	prodprice = 800, ispremium = 0, numofproductsold = 15, \
	productspecs = "'length: 0.3 meters, width: 0.7 meters'", productcomments = "'Poor man''s choice, if someone asks for it don''t waste time pushing other stuff.'")
	}
	
	vacuums_population = {
	'insert_value_vacuums_1': vacuumcleaners_value_template.format(pname = "'Vakuumator'",\
	manname = "'Achpunkt'", mancount = "'Germany'", year = "'2018'", prodcolour = "'Black'", \
	prodprice = 2500, ispremium = 1, numofproductsold = 2, \
	productspecs = "'length: 2 meters, width: 0.5 meters'", productcomments = "'Good vacuum all around!'"),
	
	'insert_value_vacuums_2': vacuumcleaners_value_template.format(pname = "'Weed$ucker'",\
	manname = "'Achpunkt'", mancount = "'Germany'", year = "'2017'", prodcolour = "'Pink'", \
	prodprice = 2300, ispremium = 0, numofproductsold = 14, \
	productspecs = "'length: 2.3 meters, width: 0.7 meters'", productcomments = "''"),
	
	'insert_value_vacuums_3': vacuumcleaners_value_template.format(pname = "'CheepSheep'",\
	manname = "'Stars and Stripes'", mancount = "'USA'", year = "'2005'", prodcolour = "'Green'", \
	prodprice = 2000, ispremium = 0, numofproductsold = 7, \
	productspecs = "'length: 1.4 meters, width: 0.9 meters'", productcomments = "'Good but old, keep clean on display'"),
	
	'insert_value_vacuums_4': vacuumcleaners_value_template.format(pname = "'ErgeSegedem'",\
	manname = "'HLC'", mancount = "'Hungary'", year = "'2019'", prodcolour = "'Maroon'", \
	prodprice = 1900, ispremium = 0, numofproductsold = 32 , \
	productspecs = "'length: 3 meters, width: 0.5 meters'", productcomments = "'Long but the customers love it.'"),
	
	'insert_value_vacuums_5': vacuumcleaners_value_template.format(pname = "'Chimera'",\
	manname = "'CVC'", mancount = "'China'", year = "'2010'", prodcolour = "'Brown'", \
	prodprice = 300, ispremium = 0, numofproductsold = 40, \
	productspecs = "'length: 0.3 meters, width: 0.7 meters'", productcomments = "'Please keep in back.'")
	}
	
	screens_population = {
	'insert_value_screens_1': screens_value_template.format(pname = "'Hunyeah'",\
	manname = "'HLC'", mancount = "'Hungary'", year = "'2018'", prodcolour = "'Gray'", \
	prodprice = 1800, ispremium = 1, numofproductsold = 12, \
	productspecs = "'length: 0.3 meters, width: 0.8 meters'", productcomments = "'New standard in screens, must put up poster'"),
	
	'insert_value_screens_2': screens_value_template.format(pname = "'UView'",\
	manname = "'Stars and Stripes'", mancount = "'USA'", year = "'2016'", prodcolour = "'Black'", \
	prodprice = 1500, ispremium = 0, numofproductsold = 30, \
	productspecs = "'length: 0.3 meters, width: 0.7 meter'", productcomments = "''"),
	
	'insert_value_screens_3': screens_value_template.format(pname = "'Vuester'",\
	manname = "'Achpunkt'", mancount = "'Germany'", year = "'2016'", prodcolour = "'Black'", \
	prodprice = 1100, ispremium = 0, numofproductsold = 13, \
	productspecs = "'length: 0.3 meters, width: 0.5 meter'", productcomments = "''"),
	
	'insert_value_screens_4': screens_value_template.format(pname = "'NoShow'",\
	manname = "'CVC'", mancount = "'China'", year = "'2018'", prodcolour = "'Try and dump in another supplier'", \
	prodprice = 1500, ispremium = 0, numofproductsold = 2 , \
	productspecs = "'length: 0.5 meters, width: 0.5 meter'", productcomments = "'New and promising, maybe will sell more on holidays.'"),
	
	'insert_value_screens_5': screens_value_template.format(pname = "'Funkey'",\
	manname = "'Slovkids'", mancount = "'Slovakia'", year = "'2010'", prodcolour = "'Grayish'", \
	prodprice = 150, ispremium = 0, numofproductsold = 45, \
	productspecs = "'length: 0.1 meters, width: 0.25 meter'", productcomments = "'Downplay this one'")
	}



	
	for i in range (1, 6):
		c.execute(laptops_population['insert_value_laptops_'+str(i)])
		grosssetlaptops = 'update laptops set grossproductrevenue = (select\
		numofproductsold*productprice from laptops where productid = {})\
		where productid={}'.format(str(i), str(i))
		c.execute(grosssetlaptops)
	for i in range (1, 6):
		c.execute(vacuums_population['insert_value_vacuums_'+str(i)])
		grosssetvacuums = 'update vacuumcleaners set grossproductrevenue = (select\
		numofproductsold*productprice from vacuumcleaners where productid = {})\
		where productid={}'.format(str(i), str(i))
		c.execute(grosssetvacuums)
	for i in range (1, 6):
		c.execute(screens_population['insert_value_screens_'+str(i)])
		grosssetscreens = 'update screens set grossproductrevenue = (select\
		numofproductsold*productprice from screens where productid = {})\
		where productid={}'.format(str(i), str(i))
		c.execute(grosssetscreens)

	conn.commit()
	
insert_values()
main()
