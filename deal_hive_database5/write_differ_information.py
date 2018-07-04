import os
import xlwt

def write_differ_information1(all_differ_dict,exist_question,auto_check_database_dict,write_differ_path="E:\\DMP_database\\differ_information.txt"):

    if os.path.exists(write_differ_path):
        os.remove(write_differ_path)
    file_cur = open(write_differ_path, 'w')
    file_cur.write("·············以下为统计的hive库中表信息与DMP数据字典中表信息的差异信息：············\n")
    file_cur.write("一、dw_ods 数据库中table（数据表）的差异信息：\n")
    file_cur.write("   1、hive的dw_ods 数据库中存在，而DMP数据字典中缺失的表名单：\n     ")
    for table_name in all_differ_dict["both_exist_database_table_differ"]['dw_ods']["table_differ"]["hive_table_more"]:
        file_cur.write(table_name+"\t")
    file_cur.write("\n")

    file_cur.close()


def write_differ_information(all_differ_dict,exist_question,auto_check_database_dict,word_DMP_database_dict,write_differ_path="E:\\DMP_database\\differ_information.xls"):
    workbook=xlwt.Workbook()

    table0 = workbook.add_sheet('0.hive_中dw_ods 表中的分区信息')
    table_number=0
    table0.write(0, 0, "hive数据库中dw_ods数据库中所有表的分区信息")
    for table_name in auto_check_database_dict["database_name"]['dw_ods']["table_name"]:
        table_number+=1
        table0.write(table_number, 0, table_number)
        table0.write(table_number, 1, table_name)
        table0.write(table_number, 3, "表分区:")

        partition_number=4
        for table_partiton in auto_check_database_dict["database_name"]['dw_ods']["table_name"][table_name]["field_partition_information"]:
            partition_number+=1
            table0.write(table_number, partition_number,table_partiton+":"+auto_check_database_dict["database_name"]['dw_ods']["table_name"][table_name]["field_partition_information"][table_partiton] )


    table1 = workbook.add_sheet('1.hive_中多出的表')
    for table_name_index in range(len(all_differ_dict["both_exist_database_table_differ"]['dw_ods']["table_differ"]["hive_table_more"])):
        table1.write(table_name_index, 0,table_name_index+1)
        table1.write(table_name_index,1,all_differ_dict["both_exist_database_table_differ"]['dw_ods']["table_differ"]["hive_table_more"][table_name_index])

    table2 = workbook.add_sheet('2.datadict_中多出的表')
    for table_name_index in range(len(all_differ_dict["both_exist_database_table_differ"]['dw_ods']["table_differ"]["table_dict_table_more"])):
        table2.write(table_name_index, 0,table_name_index+1)
        table2.write(table_name_index,1,all_differ_dict["both_exist_database_table_differ"]['dw_ods']["table_differ"]["table_dict_table_more"][table_name_index])

    table3 = workbook.add_sheet('3.hive_and _dict共同存在的表')
    table3.write(0, 0, "hive_and _datadict共同存在的表")
    for table_name_index in range(len(all_differ_dict["both_exist_database_table_differ"]['dw_ods']["table_differ"]["both_exist_table"])):
        table3.write(table_name_index+1, 0,table_name_index+1)
        table3.write(table_name_index+1,1,all_differ_dict["both_exist_database_table_differ"]['dw_ods']["table_differ"]["both_exist_table"][table_name_index])

        table3.write(table_name_index + 1, 3,"表分区：")

        partition_number = 4
        table_name=all_differ_dict["both_exist_database_table_differ"]['dw_ods']["table_differ"]["both_exist_table"][table_name_index]
        for table_partiton in auto_check_database_dict["database_name"]['dw_ods']["table_name"][table_name]["field_partition_information"]:
            partition_number+=1
            table3.write(table_name_index + 1, partition_number,table_partiton+":"+auto_check_database_dict["database_name"]['dw_ods']["table_name"][table_name]["field_partition_information"][table_partiton] )



    createVar = locals()
    for both_exist_table in range(len(all_differ_dict["both_exist_database_table_differ"]['dw_ods']["table_differ"]["both_exist_table"])):
        both_exist_table_name=all_differ_dict["both_exist_database_table_differ"]['dw_ods']["table_differ"]["both_exist_table"][both_exist_table]
        createVar['sheet' + str(both_exist_table)]=workbook.add_sheet(all_differ_dict["both_exist_database_table_differ"]['dw_ods']["table_differ"]["both_exist_table"][both_exist_table])


        createVar['sheet' + str(both_exist_table)].write(0,0,"1.hive中表"+all_differ_dict["both_exist_database_table_differ"]['dw_ods']["table_differ"]["both_exist_table"][both_exist_table]+"多出的字段")
        createVar['sheet' + str(both_exist_table)].write(0, 2,"字段类型（hive中）")
        for field_name_index in range(len(all_differ_dict["both_exist_database_table_differ"]['dw_ods']["both_exist_table_field_differ"][both_exist_table_name]["field_differ"]["hive_table_field_more"])):
            createVar['sheet' + str(both_exist_table)].write(field_name_index+1, 0, field_name_index+1)
            createVar['sheet' + str(both_exist_table)].write(field_name_index + 1, 1, all_differ_dict["both_exist_database_table_differ"]['dw_ods']["both_exist_table_field_differ"][both_exist_table_name]["field_differ"]["hive_table_field_more"][field_name_index])

            field_name=all_differ_dict["both_exist_database_table_differ"]['dw_ods']["both_exist_table_field_differ"][both_exist_table_name]["field_differ"]["hive_table_field_more"][field_name_index]
            createVar['sheet' + str(both_exist_table)].write(field_name_index + 1, 2,auto_check_database_dict["database_name"]['dw_ods']["table_name"][both_exist_table_name]["field_information"][field_name])

        createVar['sheet' + str(both_exist_table)].write(0, 3, "2.datadict中表" +all_differ_dict["both_exist_database_table_differ"]['dw_ods']["table_differ"]["both_exist_table"][both_exist_table] + "多出的字段")
        createVar['sheet' + str(both_exist_table)].write(0, 5, "字段类型（datadict中）")
        for field_name_index in range( len(all_differ_dict["both_exist_database_table_differ"]['dw_ods']["both_exist_table_field_differ"][both_exist_table_name]["field_differ"]["table_dict_field_more"])):
            createVar['sheet' + str(both_exist_table)].write(field_name_index + 1, 3, field_name_index + 1)
            createVar['sheet' + str(both_exist_table)].write(field_name_index + 1, 4,all_differ_dict["both_exist_database_table_differ"]['dw_ods']["both_exist_table_field_differ"][both_exist_table_name]["field_differ"]["table_dict_field_more"][field_name_index])

            field_name = all_differ_dict["both_exist_database_table_differ"]['dw_ods']["both_exist_table_field_differ"][both_exist_table_name]["field_differ"]["table_dict_field_more"][field_name_index]
            createVar['sheet' + str(both_exist_table)].write(field_name_index + 1, 5,word_DMP_database_dict["database_name"]['dw_ods']["table_name"][both_exist_table_name]["field_information"][field_name])

        createVar['sheet' + str(both_exist_table)].write(0, 6, "3." + all_differ_dict["both_exist_database_table_differ"]['dw_ods']["table_differ"]["both_exist_table"][both_exist_table] + "中共同存在的字段")
        createVar['sheet' + str(both_exist_table)].write(0, 8, "字段类型（hive中）")
        createVar['sheet' + str(both_exist_table)].write(0, 9, "字段类型（datadict中）")

        for field_name_index in range( len(all_differ_dict["both_exist_database_table_differ"]['dw_ods']["both_exist_table_field_differ"][both_exist_table_name]["field_differ"]["both_exist_field"])):
            createVar['sheet' + str(both_exist_table)].write(field_name_index + 1, 6, field_name_index + 1)
            createVar['sheet' + str(both_exist_table)].write(field_name_index + 1, 7, all_differ_dict["both_exist_database_table_differ"]['dw_ods']["both_exist_table_field_differ"][both_exist_table_name]["field_differ"]["both_exist_field"][field_name_index])

            field_name = all_differ_dict["both_exist_database_table_differ"]['dw_ods']["both_exist_table_field_differ"][both_exist_table_name]["field_differ"]["both_exist_field"][field_name_index]
            createVar['sheet' + str(both_exist_table)].write(field_name_index + 1, 8,auto_check_database_dict["database_name"]['dw_ods']["table_name"][both_exist_table_name]["field_information"][field_name])

            createVar['sheet' + str(both_exist_table)].write(field_name_index + 1, 9,word_DMP_database_dict["database_name"]['dw_ods']["table_name"][both_exist_table_name]["field_information"][field_name])

        #print (both_exist_table)
        #buff_table_number=5
        #heet_name=both_exist_table

        #both_exist_table[both_exist_table] = workbook.add_sheet("共同存在的表")



        # workbook.add_sheet(str(buff_table_number)+sheet_name)

    table4 = workbook.add_sheet('4._共同存在的表')

    table5 = workbook.add_sheet('5._共同存在的表')
    table6 = workbook.add_sheet('6._共同存在的表')
    table7 = workbook.add_sheet('7._共同存在的表')
    table8 = workbook.add_sheet('8._共同存在的表')

    workbook.save(write_differ_path)


