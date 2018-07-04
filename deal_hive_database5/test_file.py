# createVar = locals()
# # listTemp = range(1,10)
# # list=[]
# # for i,s in enumerate(listTemp):
# #     print(i,s)
# #     createVar['a'+str(i)]=s
# #     list.append(createVar['a'+str(i)])
# #
# #
# # print(list)

names = locals()
for i in range(1,10):
    names['a%i'%i] = input('Abss %d'%i)
for i in range(1,10):
    print(names['a%i'%i])




        # for field_name_index in range(len(all_differ_dict["both_exist_database_table_differ"]['dw_ods']["both_exist_table_field_differ"][both_exist_table]["field_differ"]["hive_table_field_more"])):
        #     createVar['sheet' + str(both_exist_table)].write(field_name_index+1, 0, field_name_index+1)
        #     createVar['sheet' + str(both_exist_table)].write(field_name_index + 1, 1, all_differ_dict["both_exist_database_table_differ"]['dw_ods']["both_exist_table_field_differ"][both_exist_table]["field_differ"]["hive_table_field_more"][field_name_index])
        '''
        createVar['sheet' + str(both_exist_table)].write(0, 3, "2.datadict中表" +all_differ_dict["both_exist_database_table_differ"]['dw_ods']["table_differ"]["both_exist_table"][both_exist_table] + "多出的字段")
        for field_name_index in range( len(all_differ_dict["both_exist_database_table_differ"]['dw_ods']["both_exist_table_field_differ"][both_exist_table]["field_differ"]["table_dict_field_more"])):
            createVar['sheet' + str(both_exist_table)].write(field_name_index + 1, 3, field_name_index + 1)
            createVar['sheet' + str(both_exist_table)].write(field_name_index + 1, 4,all_differ_dict["both_exist_database_table_differ"]['dw_ods']["both_exist_table_field_differ"][both_exist_table]["field_differ"]["table_dict_field_more"][field_name_index])

        createVar['sheet' + str(both_exist_table)].write(0, 6, "3." + all_differ_dict["both_exist_database_table_differ"]['dw_ods']["table_differ"]["both_exist_table"][both_exist_table] + "中共同存在的字段")
        for field_name_index in range( len(all_differ_dict["both_exist_database_table_differ"]['dw_ods']["both_exist_table_field_differ"][both_exist_table]["field_differ"]["both_exist_field"])):
            createVar['sheet' + str(both_exist_table)].write(field_name_index + 1, 6, field_name_index + 1)
            createVar['sheet' + str(both_exist_table)].write(field_name_index + 1, 7, all_differ_dict["both_exist_database_table_differ"]['dw_ods']["both_exist_table_field_differ"][both_exist_table]["field_differ"]["both_exist_field"][field_name_index])
        #print (both_exist_table)
        #buff_table_number=5
        #heet_name=both_exist_table

        #both_exist_table[both_exist_table] = workbook.add_sheet("共同存在的表")
     '''


        # workbook.add_sheet(str(buff_table_number)+sheet_name)

    table4 = workbook.add_sheet('4._共同存在的表')

    table5 = workbook.add_sheet('5._共同存在的表')
    table6 = workbook.add_sheet('6._共同存在的表')
    table7 = workbook.add_sheet('7._共同存在的表')
    table8 = workbook.add_sheet('8._共同存在的表')