import global_variable as gv
import copy

def active_check_dict_differ(auto_check_database_dict,word_DMP_database_dict):
    print(auto_check_database_dict["database_name"].keys())
    print(word_DMP_database_dict["database_name"].keys())

    print(auto_check_database_dict["database_name"]['dw_ods']["table_name"].keys())
    print(word_DMP_database_dict["database_name"]['dw_ods']["table_name"].keys())

    all_differ_dict=copy.deepcopy(gv.check_all_differ_dict)

    for hive_database in auto_check_database_dict["database_name"].keys():
        if hive_database not in word_DMP_database_dict["database_name"].keys():
            all_differ_dict["database_differ"]["hive_more"].append(hive_database)
        else:           # 当数据库存在于两个数据源文件中时···
            all_differ_dict["database_differ"]["both_exist_database"].append(hive_database)
            #````````````当数据库都同时存在时，计入相同数据库字典信息，并展开下一级比较数据库中table的差异性····
            if hive_database not in all_differ_dict["both_exist_database_table_differ"]:
                all_differ_dict["both_exist_database_table_differ"][hive_database]=copy.deepcopy(gv.check_table_differ_dict)

                for table_name in auto_check_database_dict["database_name"][hive_database]["table_name"]:
                    if table_name not in word_DMP_database_dict["database_name"][hive_database]["table_name"]:
                        all_differ_dict["both_exist_database_table_differ"][hive_database]["table_differ"]["hive_table_more"].append(table_name)
                    else:
                        all_differ_dict["both_exist_database_table_differ"][hive_database]["table_differ"]["both_exist_table"].append(table_name)

                        if table_name not in all_differ_dict["both_exist_database_table_differ"][hive_database]["both_exist_table_field_differ"]:
                            all_differ_dict["both_exist_database_table_differ"][hive_database]["both_exist_table_field_differ"][table_name]=copy.deepcopy(gv.check_field_differ_dict)

                            for field_of_table in auto_check_database_dict["database_name"][hive_database]["table_name"][table_name]["field_information"]:
                                if field_of_table not in word_DMP_database_dict["database_name"][hive_database]["table_name"][table_name]["field_information"]:
                                    all_differ_dict["both_exist_database_table_differ"][hive_database]["both_exist_table_field_differ"][table_name]["field_differ"]["hive_table_field_more"].append(field_of_table)
                                else:
                                    all_differ_dict["both_exist_database_table_differ"][hive_database]["both_exist_table_field_differ"][table_name]["field_differ"]["both_exist_field"].append(field_of_table)
                                    if  field_of_table not in all_differ_dict["both_exist_database_table_differ"][hive_database]["both_exist_table_field_differ"][table_name]["both_exist_field_type_differ"]:
                                        all_differ_dict["both_exist_database_table_differ"][hive_database]["both_exist_table_field_differ"][table_name]["both_exist_field_type_differ"][field_of_table]=copy.deepcopy(gv.check_fieldtype_differ_dict)

                                        if auto_check_database_dict["database_name"][hive_database]["table_name"][table_name]["field_information"][field_of_table]==word_DMP_database_dict["database_name"][hive_database]["table_name"][table_name]["field_information"][field_of_table]:
                                            all_differ_dict["both_exist_database_table_differ"][hive_database]["both_exist_table_field_differ"][table_name]["both_exist_field_type_differ"][field_of_table]["fieldtype_same"].append(field_of_table)
                                        else:
                                            all_differ_dict["both_exist_database_table_differ"][hive_database]["both_exist_table_field_differ"][table_name]["both_exist_field_type_differ"][field_of_table]["fieldtype_differ"]["hive_table_field_type"]=auto_check_database_dict["database_name"][hive_database]["table_name"][table_name]["field_information"][field_of_table]
                                            all_differ_dict["both_exist_database_table_differ"][hive_database]["both_exist_table_field_differ"][table_name]["both_exist_field_type_differ"][field_of_table]["fieldtype_differ"]["table_dict_field_type"]=word_DMP_database_dict["database_name"][hive_database]["table_name"][table_name]["field_information"][field_of_table]

                            for DMP_field_of_table in word_DMP_database_dict["database_name"][hive_database]["table_name"][table_name]["field_information"]:
                                if DMP_field_of_table not in auto_check_database_dict["database_name"][hive_database]["table_name"][table_name]["field_information"]:
                                    all_differ_dict["both_exist_database_table_differ"][hive_database]["both_exist_table_field_differ"][table_name]["field_differ"]["table_dict_field_more"].append(DMP_field_of_table)

                for DMP_table_name in word_DMP_database_dict["database_name"][hive_database]["table_name"]:
                    if DMP_table_name not in auto_check_database_dict["database_name"][hive_database]["table_name"]:
                        all_differ_dict["both_exist_database_table_differ"][hive_database]["table_differ"]["table_dict_table_more"].append(DMP_table_name)

    for DMP_database in word_DMP_database_dict["database_name"].keys():
        if DMP_database not in auto_check_database_dict["database_name"].keys():
            all_differ_dict["database_differ"]["table_dict_database_more"].append(DMP_database)


    return all_differ_dict






