
import os
import chardet
import copy
import global_variable as gv



def read_file_data(path_dict, file_path):

    try:
        #创建目录文件·····  #直接当做文本来操作·····
        #f_cursor = cdf.creat_dest_file(path_dict)

        #直接当做excel来操作····

        file_cur = open(file_path, 'rb')
        file_data = file_cur.readlines()

        #检查文件类型····desc or registe······
        file_type=path_dict["filename"].split("_")[0]

        if file_type=="desc":
            data_repository=[]
            transform_repository=[[],[]]

            if len(file_data) != 0:                        # 因为有很多空文件··············
                encode_type = chardet.detect(file_data[0])
                if encode_type["encoding"] == "utf-8":
                    #global gv.encode_utf_8
                    gv.encode_utf_8.append(copy.deepcopy(path_dict["filename"]))
                    for registe in file_data:
                        registe=registe.decode().strip()
                        #print(registe)
                        registe=registe.split('\t')

                        registe_replace_buff=[]                                 #去除hive数据库中每个表字段中的空格，防止（write_differ_information）对比字段时出现错误····
                        for each_field in registe:
                            registe_replace_buff.append(each_field.replace(' ',''))
                        data_repository.append(copy.deepcopy(registe_replace_buff))
                        #print(registe)

                        #print(registe.decode().strip())
                elif encode_type["encoding"]=="Windows-1252":
                    #global gv.encode_Windows_1252
                    gv.encode_Windows_1252.append(copy.deepcopy(path_dict["filename"]))
                    for registe in file_data:
                        registe = registe.decode("Windows-1252")
                        registe=registe.encode("utf-8")
                        registe = registe.split('\t')

                        registe_replace_buff = []  # 去除hive数据库中每个表字段中的空格，防止（write_differ_information）对比字段时出现错误····
                        for each_field in registe:
                            registe_replace_buff.append(each_field.replace(' ', ''))
                        data_repository.append(copy.deepcopy(registe_replace_buff))

                else:
                    gv.encode_ascii.append(copy.deepcopy(path_dict["filename"]))
                    file_cur = open(file_path, 'r')
                    file_data = file_cur.readlines()
                    for registe in file_data:
                        registe = registe.split('\t')

                        registe_replace_buff = []  # 去除hive数据库中每个表字段中的空格，防止（write_differ_information）对比字段时出现错误····
                        for each_field in registe:
                            registe_replace_buff.append(each_field.replace(' ', ''))
                        data_repository.append(copy.deepcopy(registe_replace_buff))
                        #print(registe)

                for desc_field in  data_repository:
                    transform_repository[0].append(desc_field[0])
                    transform_repository[1].append(desc_field[1])
                data_repository=copy.deepcopy(transform_repository)


                return data_repository

            else:
                #global empty_file
                gv.empty_file.append(copy.deepcopy(path_dict["filename"]))

        elif file_type=="registe":
            data_repository = []

            if len(file_data) != 0:  # 因为有很多空文件··············
                encode_type = chardet.detect(file_data[0])
                if encode_type["encoding"] == "utf-8":
                    #global encode_utf_8
                    gv.encode_utf_8.append(copy.deepcopy(path_dict["filename"]))
                    for registe in file_data:
                        registe=registe.decode().strip()
                        registe = registe.split('\t')
                        data_repository.append(copy.deepcopy(registe))

                elif encode_type["encoding"] == "Windows-1252":
                    #global encode_Windows_1252
                    gv.encode_Windows_1252.append(copy.deepcopy(path_dict["filename"]))
                    for registe in file_data:
                        registe = registe.decode("Windows-1252")
                        registe=registe.encode("utf-8")
                        registe = registe.split('\t')
                        data_repository.append(copy.deepcopy(registe))

                else:
                    gv.encode_ascii.append(copy.deepcopy(path_dict["filename"]))
                    file_cur = open(file_path, 'r')
                    file_data = file_cur.readlines()
                    #for registe in file_data:
                    for registe in file_data:
                        registe = registe.split('\t')
                        data_repository.append(copy.deepcopy(registe))

                return data_repository

            else:
                #global empty_file
                gv.empty_file.append(copy.deepcopy(path_dict["filename"]))




    except Exception as result:

        print("eroor of read_file_data```")
        print("未知错误 %s" % result)
        #global error_list
        gv.error_list.append(copy.deepcopy(path_dict["filename"]))







'''
def read_file_data(path_dict, file_path):

    try:
        #创建目录文件·····  #直接当做文本来操作·····
        #f_cursor = cdf.creat_dest_file(path_dict)
        if path_dict["filename"]=="registe_youshu_userdeviceinfo":

            #直接当做excel来操作····

            filename="registe_youshu_userdeviceinfo"

            file_cur = open(file_path, 'rb')
            file_data = file_cur.readlines()

            #检查文件类型····desc or registe······
            file_type=path_dict["filename"].split("_")[0]

            if file_type=="desc":
                data_repository=[]
                transform_repository=[[],[]]

                if len(file_data) != 0:                        # 因为有很多空文件··············
                    encode_type = chardet.detect(file_data[0])
                    if encode_type["encoding"] == "utf-8":
                        #global gv.encode_utf_8
                        gv.encode_utf_8.append(copy.deepcopy(path_dict["filename"]))
                        for registe in file_data:
                            registe=registe.decode().strip()
                            #print(registe)
                            registe=registe.split('\t')
                            data_repository.append(copy.deepcopy(registe))
                            #print(registe)

                            #print(registe.decode().strip())
                    elif encode_type["encoding"]=="Windows-1252":
                        #global gv.encode_Windows_1252
                        gv.encode_Windows_1252.append(copy.deepcopy(path_dict["filename"]))
                        for registe in file_data:
                            registe = registe.decode("Windows-1252")
                            registe=registe.encode("utf-8")
                            registe = registe.split('\t')
                            data_repository.append(copy.deepcopy(registe))

                    else:
                        gv.encode_ascii.append(copy.deepcopy(path_dict["filename"]))
                        file_cur = open(file_path, 'r')
                        file_data = file_cur.readlines()
                        for registe in file_data:
                            registe = registe.split('\t')
                            data_repository.append(copy.deepcopy(registe))
                            #print(registe)

                    for desc_field in  data_repository:
                        transform_repository[0].append(desc_field[0])
                        transform_repository[1].append(desc_field[1])
                    data_repository=copy.deepcopy(transform_repository)


                    return data_repository

                else:
                    #global empty_file
                    gv.empty_file.append(copy.deepcopy(path_dict["filename"]))

            elif file_type=="registe":
                data_repository = []

                if len(file_data) != 0:  # 因为有很多空文件··············
                    encode_type = chardet.detect(file_data[0])
                    if encode_type["encoding"] == "utf-8":
                        #global encode_utf_8
                        gv.encode_utf_8.append(copy.deepcopy(path_dict["filename"]))
                        for registe in file_data:
                            registe=registe.decode().strip()
                            registe = registe.split('\t')
                            data_repository.append(copy.deepcopy(registe))

                    elif encode_type["encoding"] == "Windows-1252":
                        #global encode_Windows_1252
                        gv.encode_Windows_1252.append(copy.deepcopy(path_dict["filename"]))
                        for registe in file_data:
                            registe = registe.decode("Windows-1252")
                            registe=registe.encode("utf-8")
                            registe = registe.split('\t')
                            data_repository.append(copy.deepcopy(registe))                        
                    else:
                        gv.encode_ascii.append(copy.deepcopy(path_dict["filename"]))
                        file_cur = open(file_path, 'r')
                        file_data = file_cur.readlines()
                        #for registe in file_data:
                        for registe in file_data:
                            registe = registe.split('\t')
                            data_repository.append(copy.deepcopy(registe))

                    return data_repository

                else:
                    #global empty_file
                    gv.empty_file.append(copy.deepcopy(path_dict["filename"]))




    except Exception as result:

        print("eroor of read_file_data```")
        print("未知错误 %s" % result)
        #global error_list
        gv.error_list.append(copy.deepcopy(path_dict["filename"]))

'''


