import os

def write_txt_to_xls(table_data):

    try:

        file_cur = open(table_data["save_excel_data"], 'w')
        #print(len(table_data["desc_data"]))
        for desc_registe_row in table_data["desc_data"]:
            for column_field in desc_registe_row:
                try:
                    file_cur.write(column_field)
                    file_cur.write("\t")
                except:
                    continue
            file_cur.write("\n")
        for registe_registe_row in table_data["registe_data"]:
            for column_field in registe_registe_row:
                try:

                    file_cur.write(column_field)
                    if column_field != registe_registe_row[-1]:
                        file_cur.write("\t")
                except:
                    continue
            if '\n' in registe_registe_row[-1]:

                continue
            else:
                file_cur.write("\n")


        file_cur.close()

    except Exception as result:
        print("error of write_txt_to_xls```")
        print("未知错误 %s" % result)





