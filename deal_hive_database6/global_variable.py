
global error_list
global empty_file
global encode_utf_8
global encode_Windows_1252

#···············数据表所存在的数据状态信息数据机构················
error_list = []
empty_file = []
encode_utf_8 = []
encode_Windows_1252 = []
encode_ascii=[]

#···············每个表的所有数据临时暂存数据结构············
sigle_table_data = {"desc_data": [], "registe_data": [], "save_excel_data": ''}

#···············hive库中用于检索的表结构差异的数据信息存储结构··········
auto_check_database_dict={"database_name":{}}
auto_check_table_dict={"table_name":{}}
auto_check_table_information={"field_information":{},"field_partition_information":{}}

#···············DMP数据字典中用于检索表结构差异的数据信息存储结构·········
word_DMP_database_dict={"database_name":{}}
word_DMP_table_dict={"table_name":{}}
word_DMP_table_information={"field_information":{},"field_partition_information":{}}

#···············检索结束后的差异性信息表存储数据结构·················
check_fieldtype_differ_dict={"fieldtype_same":[],
                             "fieldtype_differ":{"hive_table_field_type":"","table_dict_field_type":""}}

check_field_differ_dict={"field_differ":{"hive_table_field_more":[],"table_dict_field_more":[],"both_exist_field":[]},
                         "both_exist_field_type_differ":{}
                         }

check_table_differ_dict={"table_differ":{"hive_table_more":[],"table_dict_table_more":[],"both_exist_table":[]},
                         "both_exist_table_field_differ":{}
                         }

check_all_differ_dict={"database_differ":{"hive_more":[],"table_dict_database_more":[],"both_exist_database":[]},
                         "both_exist_database_table_differ":{}
                       }