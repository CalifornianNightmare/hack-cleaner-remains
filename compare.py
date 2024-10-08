from config import ENGINE, TABLE_FIN, TABLE_DOUBLE
import pandas as pd
from compare_rules import getManager
from uid import Uid

def translate_data(table_name, from_columns=[], to_columns=[], engine=ENGINE):
    """
    Всегда имя передаём первым
    """

    # for sql_index in range(get_table_length(table_name, engine)):
    for sql_index in range(5):
        row = pd.read_sql(f"SELECT * FROM {table_name} WHERE `index` = {sql_index}", con=engine).to_dict()

        row['names'] = split_name(row, from_columns[0])
        row.pop(from_columns[0])

        manager = getManager()

        for export_index in range(get_table_length(TABLE_FIN, engine)):
            row_next = pd.read_sql(f"SELECT * FROM {TABLE_FIN} WHERE `index` = {export_index}", con=engine).to_dict()
            row_next['names'] = split_name(row, from_columns[0])
            row_next.pop(to_columns[0])


            dupes = manager.compare_rows(row, row_next)
            if (dupes):

                # 4,5

                uid = Uid(table=eval(row_next['uid']), uid=row['uid'], uid_destination=table_name)
                uid.addid(row['uid'])

                values = [row[i] for i in from_columns]
                values = '`' + values[0] + '`, `'.join(values[1:]) + '`'
                titles = '`' + to_columns[0] + '`, `'.join(to_columns[1:]) + '`'

                with engine.connect() as connection:
                    connection.execute(f"""INSERT INTO `anneurism`.`{TABLE_DOUBLE}`
                     ({titles}) VALUES 
                     ('{values}');""")

            else:

                # 4

                uid = Uid(uid=row['uid'], uid_destination=table_name)

                values = [row[i] for i in from_columns]
                values[from_columns.index('uid')] = str(uid.return_list())
                values = "'" + values[0] + "', '".join(values[1:]) + "'"
                titles = '`' + to_columns[0] + '`, `'.join(to_columns[1:]) + '`'


                with engine.connect() as connection:
                    connection.execute(f"""INSERT INTO `anneurism`.`{TABLE_DOUBLE}`
                     ({titles}) VALUES 
                     ('{values}');""")

def split_name(vals, key):
    if key == 'full_name':
        return vals['full_name'].split()
    elif key == 'first_name':
        return [vals['first_name'], vals['middle_name'], vals['last_name']]
    elif key == 'name':
        return vals['name'].split()

def get_table_length(table_name, engine):
    with engine.connect() as connection:
        result = connection.execute(f"SELECT COUNT(*) FROM {table_name}")
        table_length = result.scalar()

    return table_length
