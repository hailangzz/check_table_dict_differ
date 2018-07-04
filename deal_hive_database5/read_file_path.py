import os
import os.path
import copy
import read_file_data as rfd
import check_file_type as cft
import global_variable as gv
import write_txt_to_xls as wttx
import creat_dest_file as cdf

def read_table_data_information(table_data,database_name,table_name_lower):

    '''
    for table_desc_information in table_data["desc_data"]:  #      每一行的信息····
        desc_slicer_index = []
        for desc_field_index in range(len(table_desc_information)):
            if table_desc_information[desc_field_index]=='':
                desc_slicer_index.append(desc_field_index)
        if len(desc_slicer_index)==2:  # 说明此表有分区·····
            for desc_field_index in range(0,desc_slicer_index[0]):

        print(table_desc_information)
        '''

    table_desc_field_information=copy.deepcopy(table_data["desc_data"][0])
    table_desc_field_type_information = copy.deepcopy(table_data["desc_data"][1])
    desc_slicer_index = []

    for desc_field_index in range(len(table_desc_field_information)):
        if table_desc_field_information[desc_field_index] == '':
            desc_slicer_index.append(desc_field_index)
    if len(desc_slicer_index) == 2:  # 说明此表有分区·····
        for desc_field_index in range(0, desc_slicer_index[0]):    # 填充database table 中的desc 数据信息····
            desc_field_name_lower=table_desc_field_information[desc_field_index].lower()
            desc_field_type_lower=table_desc_field_type_information[desc_field_index].lower()
            gv.auto_check_database_dict["database_name"][database_name]["table_name"][table_name_lower]["field_information"][desc_field_name_lower]=desc_field_type_lower

        for desc_field_index in range(desc_slicer_index[1]+1,len(table_desc_field_information)):    # 填充database table 中的partition  分组数据信息····
            desc_field_partition_lower=table_desc_field_information[desc_field_index].lower()
            desc_partition_type_lower=table_desc_field_type_information[desc_field_index].lower()
            gv.auto_check_database_dict["database_name"][database_name]["table_name"][table_name_lower]["field_partition_information"][desc_field_partition_lower]=desc_partition_type_lower



def read_file_path(source_path):
    try:
        path_dict={"database":"","table":"","filename":""}
        for parent, dirname , filename in os.walk(source_path):
            for database_name in dirname:
                # print(len(dirname))
                if database_name not in gv.auto_check_database_dict["database_name"] and database_name!="a2p":
                    gv.auto_check_database_dict["database_name"][database_name]=copy.deepcopy(gv.auto_check_table_dict)

                #print("the len keys is ",len(gv.auto_check_database_dict["database_name"]))
                database_path = os.path.join(parent,database_name)
                table_name_list = os.listdir(database_path)
                for table_name in table_name_list:
                    table_name_lower=table_name.lower()
                    if table_name_lower not in gv.auto_check_database_dict["database_name"][database_name]["table_name"]:
                        gv.auto_check_database_dict["database_name"][database_name]["table_name"][table_name_lower]=copy.deepcopy(gv.word_DMP_table_information)

                    table_path = os.path.join(database_path, table_name)
                    file_name_list = os.listdir(table_path)

                    table_data = copy.deepcopy(gv.sigle_table_data)   # 读取每一个table表时只初始化一次····


                    for file_name in file_name_list:
                        file_path = os.path.join(table_path, file_name)

                        if os.path.isfile(file_path):
                            #print(file_path)
                            path_dict["database"] = database_name
                            path_dict["table"] = table_name
                            path_dict["filename"] = file_name

                            table_data["save_excel_data"] = cdf.creat_dest_file(path_dict)

                            if path_dict["filename"].split("_")[0] == 'desc':
                                desc_data = rfd.read_file_data(path_dict, file_path)
                                table_data["desc_data"] = copy.deepcopy(desc_data)

                            else:
                                registe_data = rfd.read_file_data(path_dict, file_path)
                                table_data["registe_data"] = copy.deepcopy(registe_data)

                    read_table_data_information(table_data,database_name,table_name_lower)
                    wttx.write_txt_to_xls(table_data)

        return gv.auto_check_database_dict
    except Exception as result:
        return gv.auto_check_database_dict
        print("error of read_file_path ````")
        print("未知错误 %s" % result)



# read_file_path("E:\\hive_database")
#
# exist_question=cft.check_file_type()

#print(gv.auto_check_database_dict["database_name"]["dw_ods"]["table_name"]["a2p"]["field_information"])
#print(gv.auto_check_database_dict["database_name"]["dw_ods"]["table_name"]["a2p"]["field_partition_information"])
'''
print("the encode_utf_8 is :")
print(exist_question["encode_utf_8"])
print("the encode_Windows_1252 is :")
print(exist_question["encode_Windows_1252"])
print("the encode_ascii is :")
print(exist_question["encode_ascii"])
print("the error_list is :")
print(exist_question["error_list"])

print("the empty_file is :")
print(exist_question["empty_file"])
'''