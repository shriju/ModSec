#------------------------------importing complete-----------------------------------

frames = []

def get_data(cursor, sql):
    cursor.execute(sql)
    result = cursor.fetchall()
    
    return (cursor.column_names, result)