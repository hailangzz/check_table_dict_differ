import xlrd
import os
import global_variable as gv
import copy
import re  #判断字段是否包含汉字····



def read_word_DMP_dict(word_DMP_database_path,word_DMP_database):
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')                  #   判断字段是否包含汉字····

    workbook = xlrd.open_workbook(word_DMP_database_path)
    worksheet_list=workbook.sheets()
    #print(len(worksheet_list))   #打印sheet表的个数····
    for sheet in worksheet_list:
        sheet_row_number=0
        if sheet.name not in gv.word_DMP_database_dict["database_name"][word_DMP_database]["table_name"]:
            sheet_name_lower=sheet.name.lower()
            gv.word_DMP_database_dict["database_name"][word_DMP_database]["table_name"][sheet_name_lower]=copy.deepcopy(gv.word_DMP_table_information)
        #print(sheet_name_lower)    # 打印sheet表名称····
        sheet_row_number=sheet.nrows
        if sheet_row_number!=0:
            for table_sheet_row in range(sheet_row_number):
                table_row_data=sheet.row_values(table_sheet_row)     #desc中每行数据的值
                if len(table_row_data)==2:
                    table_row_data_0_lower=table_row_data[0].lower().replace(" ",'')   # 为数据去除空格符号···

                    chinese_match = zhPattern.search(table_row_data[1])             #   判断字段是否包含汉字····
                    if chinese_match:                                               #   判断字段是否包含汉字····
                        gv.word_DMP_database_dict["database_name"][word_DMP_database]["table_name"][sheet_name_lower]["field_information"][table_row_data_0_lower] = table_row_data[1]
                    else:
                        gv.word_DMP_database_dict["database_name"][word_DMP_database]["table_name"][sheet_name_lower]["field_information"][table_row_data_0_lower] = table_row_data[1].lower().replace(" ",'')  #字段类型也得去重空格···

                else:
                    table_row_data_0_lower = table_row_data[0].lower().replace(" ",'')  ## 为数据去除空格符号···
                    gv.word_DMP_database_dict["database_name"][word_DMP_database]["table_name"][sheet.name]["field_information"][table_row_data_0_lower] = "null"

        #print(gv.word_DMP_database_dict["database_name"][word_DMP_database]["table_name"][sheet.name.lower()]["field_information"])
        '''
        field_1_column=sheet.col_values(0)
        print(sheet.cell(0,1))
        #if len(sheet.col_values(1)):
        #    field_2_column=sheet.col_values(1)
        '''

        #print(field_1_column)








def read_dmp_table_dict(source_path="E:\word_DMP_dict"):

    word_DMP_database=""
    word_DMP_table=""
    for parent, dirname, database_filename in os.walk(source_path):
        for database in database_filename:
            database_path = os.path.join(parent, database)
            #print(database_path)
            #print(database.split(".")[0])
            word_DMP_database=database.split(".")[0]
            if word_DMP_database not in gv.word_DMP_database_dict["database_name"]:
                gv.word_DMP_database_dict["database_name"][word_DMP_database]=copy.deepcopy(gv.word_DMP_table_dict)
            read_word_DMP_dict(database_path,word_DMP_database)

    return gv.word_DMP_database_dict


    # workbook = xlrd.open_workbook(source_path)
    # worksheet_list=workbook.sheets()
    #
    # print(len(worksheet_list))
    # for sheet in worksheet_list:
    #     print (sheet.name)


#DMP_table_dict=copy.deepcopy(read_dmp_table_dict())
#print (DMP_table_dict)




