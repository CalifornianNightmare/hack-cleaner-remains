import sqlite3
import

def translate_data(engine, table_name, from_columns=[], to_columns=[]):
    """
    Всегда имя передаём первым
    """

    # for sql_index in range(get_table_length(table_name, engine)):
    for sql_index in range(5):
        row = pd.read_sql(f"SELECT * FROM {table_name} WHERE `index` = {sql_index}", con=engine)
        uid = row['uid']
        names = split_name(row, from_columns[0])

        dupes = look_for_dupes(val, uuid)
        if (dupes[0]):
            # add to table 5
        elif:
            # add to table 4
        
        print(row.to_dict())
        
translate_data(engine, 'db1', ['full_name', 'email', 'address', 'sex', 'birthdate', 'phone'], ['names', 'email', 'address', 'sex', 'birthdate', 'phone'])
