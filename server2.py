from flask import Flask, request, jsonify, make_response
import pymysql

app = Flask(__name__)

mydb = pymysql.connect(
	host="localhost",
	user="root",
	passwd="",
	database="db_univ"
)

@app.route('/get_data', methods=['GET'])
def get_data_siswa():
	# Awal Query
	query = "SELECT * FROM tb_university WHERE 1=1"
	values = ()

	# Mengatur Parameter
	id = request.args.get("id")
	name = request.args.get("name")
	country = request.args.get("country")

	if id:
		query += " AND id=%s "
		values += (id,)
	if name:
		query += " AND nama LIKE %s " 
		values += ("%"+name+"%", )
	if country:
		query += " AND country=%s "
		values += (country,)

	mycursor = mydb.cursor()
	mycursor.execute(query, values)	
	row_headers = [x[0] for x in mycursor.description]
	data = mycursor.fetchall()
	json_data = []
	for result in data:
		json_data.append(dict(zip(row_headers, result)))
	return make_response(jsonify(json_data),200)


@app.route('/')
def index():
    return "Hello, Ini server2!"

if __name__ == '__main__':
    app.run(debug=True,port=5002)

