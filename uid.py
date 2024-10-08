from config import TABLE_1, TABLE_2, TABLE_3

class Uid():

    def __init__(self, table=None, uid=None, uid_destination=None):

        """

        If no table is given, creates an empty one
        If given destination and uuid, inserts it

        """

        if table == '':
            self.dict = {TABLE_1: '', TABLE_2: '', TABLE_3: ''}
        else:
            self.dict = dict()
            self.dict[TABLE_1] = table[0]
            self.dict[TABLE_2] = table[1]
            self.dict[TABLE_3] = table[2]

        if (uid != None) and (uid_destination != None):
            self.dict[uid_destination] = uid


    def addid(self, uid, uid_destination):
        if self.dict[uid_destination] is not []:
            self.dict[uid_destination].append(uid)
        else:
            self.dict[uid_destination] = [uid]

    def print(self):
        print(self.dict[TABLE_1] + '\n' + self.dict[TABLE_2] + '\n' + self.dict[TABLE_3])

    def return_list(self):
        output = [[k] + [self.dict[k].get(x) for x in [TABLE_1,TABLE_2,TABLE_3]] for k in self.dict]
        return output
