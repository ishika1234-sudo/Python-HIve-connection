def read_xml(filename):
    try:
        dbs = {'result': []}
        # importing element tree
        import os
        import xml.etree.ElementTree as ET
        # Pass the path of the xml document
        if os.path.exists(filename):
            if 'databases' in filename:
                if os.stat(filename).st_size == 0:
                    return {'status': 400, 'message': 'the file to read is empty'}
                tree = ET.parse(filename)
                # get the parent tag
                root = tree.getroot()
                for idx, item in enumerate(root):
                    dbs['result'].append(item.attrib['database_name'])
                # print(dbs)
                return {'status': 200, 'result': dbs}
            elif 'tables' in filename:
                if os.stat(filename).st_size == 0:
                    return {'status': 400, 'message': 'the file to read is empty'}
                tree = ET.parse(filename)
                # get the parent tag
                root = tree.getroot()
                for idx, item in enumerate(root):
                    dbs['result'].append(item.attrib['tab_name'])
                # print(dbs)
                return {'status': 200, 'result': dbs}

        else:
            return {'status': 400, 'message': "file to read does not exists"}
    except Exception as e:
        if hasattr(e, 'message'):
            return {'status': 400, 'message': e.message}
        else:
            return {'status': 400, 'message': e}

# print(read_xml('tables.xml'))