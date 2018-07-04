import read_file_path as rfp
import check_file_type as cft
import read_dmp_table_dict as rdtd
import copy
import active_check_dict_differ as acdd
import global_variable as gv
import write_differ_information as wdi


def main():
    auto_check_database_dict=copy.deepcopy(rfp.read_file_path("E:\\hive_database"))
    word_DMP_database_dict=copy.deepcopy(rdtd.read_dmp_table_dict())
    exist_question = cft.check_file_type()
    #print (auto_check_database_dict)
    #print(len(auto_check_database_dict["database_name"]['dw_ods']['table_name']))
    all_differ_dict=copy.deepcopy(acdd.active_check_dict_differ(auto_check_database_dict,word_DMP_database_dict))

    #print (all_differ_dict)

    wdi.write_differ_information(all_differ_dict, exist_question,auto_check_database_dict,word_DMP_database_dict)
    print(auto_check_database_dict["database_name"]['dw_ods']["table_name"]['application_detail']["field_information"])
    print(auto_check_database_dict["database_name"]['dw_ods']["table_name"]['application_detail'])
    #print(all_differ_dict["both_exist_database_table_differ"]["dw_ods"]["both_exist_table_field_differ"]['a2p']["field_differ"]["hive_table_field_more"])
    #print(all_differ_dict["both_exist_database_table_differ"]["dw_ods"]["both_exist_table_field_differ"]['a2p']["field_differ"]["table_dict_field_more"])
    #print(all_differ_dict["both_exist_database_table_differ"]["dw_ods"]["both_exist_table_field_differ"]['a2p']["field_differ"]["both_exist_field"])
    print (all_differ_dict["both_exist_database_table_differ"]["dw_ods"]["both_exist_table_field_differ"]['application_detail']["field_differ"]["hive_table_field_more"])
    print(all_differ_dict["both_exist_database_table_differ"]["dw_ods"]["both_exist_table_field_differ"]['application_detail']["field_differ"]["table_dict_field_more"])



if __name__ == '__main__':
    main()
