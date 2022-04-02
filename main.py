from flask import Flask, render_template, request, jsonify, send_file
from hive import hive_beeline_connection, hive_beeline_show_tables, hive_beeline_select_query
from read_op import read_xml
app = Flask(__name__)

cluster = ''
username = ''
password = ''
db_name = ''


@app.route('/', methods=('GET', 'POST'))
def hello():
    try:
        if request.method == 'GET':
            return render_template('home.html')
        elif request.method == 'POST':
            if 'cluster' in request.form and 'form-select' not in request.form:
                print('first if')
                global cluster
                global username
                global password
                cluster = request.form['cluster']
                username = request.form['username']
                password = request.form['password']
                print(cluster, username, password)
                hive_connection = hive_beeline_connection(cluster, username, password)
                if hive_connection['status'] == 200:
                    read_dbs_file = read_xml('databases.xml')
                    if read_dbs_file['status'] == 200:
                        data = read_dbs_file['result']
                        print('database.xml', data)
                        return jsonify(data)
                    else:
                        print("error in read file")
                        return "error in read file"
                else:
                    return 'error in hive connection'
            elif "form-select" in request.form:
                print('inside it')
                global db_name
                db_name = request.form['form-select']
                print('db name', db_name, cluster, username, password)
                hive_tables = hive_beeline_show_tables(cluster, username, password, db_name)
                if hive_tables['status'] == 200:
                    read_table_file = read_xml('tables.xml')
                    if read_table_file['status'] == 200:
                        data = read_table_file['result']
                        print('table data', data)
                        return jsonify(data)
                    else:
                        return "error in read tables file"
                else:
                    return 'error in hive connection'
                # return "success"
            elif 'form3-select' in request.form:
                print('last if')
                table_name = request.form['form3-select']
                print('db name3', table_name, cluster, username, password)
                hive_output = hive_beeline_select_query(cluster, username, password, db_name, table_name)
                if hive_output['status'] == 200:
                    return send_file('output.xml', as_attachment=True)
        else:
            return "no specific http method"
    except Exception as e:
        return e


if __name__ == "__main__":
    app.run(debug=True)