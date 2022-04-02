def hive_beeline_connection(clustername, username, password):
    try:
        import subprocess
        result_string = f"/home/ishika/apache-hive-1.2.1-bin/bin/beeline -u 'jdbc:hive2://{clustername}." \
                        f"azurehdinsight.net:443/;ssl=true;transportMode=http;httpPath=/hive2'" \
                        f" -n {username} -p '{password}' --outputformat=xmlattr -e 'show databases'>databases.xml "

        status, output = subprocess.getstatusoutput(result_string)
        if status == 1:
            return {'status': 400, 'message': 'Connection not made. Either of your credentials '
                                              'is incorrect, please recheck', 'output': output}
        return {'status': 200, 'message': 'connection made, databases fetched in databases.xml', 'output': output}
    except Exception as e:
        if hasattr(e,'message'):
            return {'status': 400, 'message': e.message}
        else:
            return {'status': 400, 'message': e}


def hive_beeline_show_tables(clustername, username, password, database_name):
    try:
        import subprocess
        result_string = f"/home/ishika/apache-hive-1.2.1-bin/bin/beeline -u 'jdbc:hive2://{clustername}." \
                        f"azurehdinsight.net:443/;ssl=true;transportMode=http;httpPath=/hive2'" \
                        f" -n {username} -p '{password}' --outputformat=xmlattr -e 'use {database_name};show tables'>tables.xml "
        status, output = subprocess.getstatusoutput(result_string)

        if status == 1:
            return {'status': 400, 'message': 'Could not show tables. check the credentials'}
        return {'status': 200, 'message': 'connection made', 'output': output}
    except Exception as e:
        if hasattr(e, 'message'):
            return {'status': 400, 'message': e.message}
        else:
            return {'status': 400, 'message': e}


def hive_beeline_select_query(clustername, username, password, database_name, table_name):
    try:
        import subprocess
        result_string = f"/home/ishika/apache-hive-1.2.1-bin/bin/beeline -u 'jdbc:hive2://{clustername}." \
                        f"azurehdinsight.net:443/;ssl=true;transportMode=http;httpPath=/hive2'" \
                        f" -n {username} -p '{password}' --outputformat=xmlattr -e 'use {database_name};" \
                        f"select * from {table_name}'>output.xml "

        status,output = subprocess.getstatusoutput(result_string)
        if status == 1:
            return {'status': 400,'message': 'select query unsuccessful. check the credentials'}
        return {'status': 200,'message': 'connection made'}
    except Exception as e:
        if hasattr(e,'message'):
            return {'status': 400,'message': e.message}
        else:
            return {'status': 400,'message': e}