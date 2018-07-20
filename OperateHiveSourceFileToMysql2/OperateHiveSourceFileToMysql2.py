import pymysql
import os
import chardet

class source_file_to_mysql:
    _MysqlHost={"host":'',"port":'',"user":'',"password":''}
    _SourceExcelDataDict={"databases":{}}
    _SourceFileRootPath=""
    _FileEncoding={}
    _FileFieldEncoding={}
    _MysqlDatabase=''
    _MysqlCursor=''

    def __init__(self, host, port, user, password):
        self._MysqlHost["host"]=host
        self._MysqlHost["port"]=port
        self._MysqlHost["user"]=user
        self._MysqlHost["password"]=password
        self.ConnectMysql()

    def displayMysqlHost(self):

        #print(self._MysqlHost)
        #print(self._SourceFileRootPath)
        #print(self._SourceExcelDataDict)
        #print(self._FileEncoding.keys())
        #print(self._FileFieldEncoding.keys())
        #print(self._SourceExcelDataDict["databases"]['tags']["tables"]['tag_1101_age']['registe'])
        #print(self._SourceExcelDataDict["databases"]['tags']["tables"].keys())
        #print(len(self._SourceExcelDataDict["databases"]['tags']["tables"].keys()))
        #print(self._SourceExcelDataDict["databases"]['dw_ods']["tables"]['a2p']['registe'])
        #print(self._SourceExcelDataDict["databases"]['tags']['tables'].keys())
        #print(self._SourceExcelDataDict["databases"]['tags']['tables']['tag_1101_age'].keys())
        #print(self._SourceExcelDataDict["databases"]['tags']['tables']['tag_1101_age']['desc'].keys())
        return


    def ConnectMysql(self):
        self._MysqlDatabase = pymysql.connect(self._MysqlHost["host"], self._MysqlHost["user"], self._MysqlHost["password"])
        self._MysqlCursor=self._MysqlDatabase.cursor()

    def CreateDatabases(self,DatabaseName):
        CommandSql="create database if not exists %s;" % DatabaseName
        self._MysqlCursor.execute(CommandSql)

    def CreateTables(self,DatabaseName,TableName,Desc):
        try:
            FieldAndTypeStr =""
            for Field in Desc:
                if Desc[Field]=='string' or Desc[Field]=='map<string,string>':
                    Desc[Field]='varchar(100)'
                FieldAndTypeStr+=Field+' '+Desc[Field]+','
            FieldAndTypeStr=FieldAndTypeStr.strip(',')
            FieldAndTypeStr='('+FieldAndTypeStr+')'

            CommandSql = "create table if not exists %s.%s %s;" % (DatabaseName,TableName,FieldAndTypeStr)
            #print(CommandSql)
            self._MysqlCursor.execute(CommandSql)

        except Exception as result:
            print("Error of Create Tables``````")
            print("创建数据表时出现错误！ %s" % result)

    def InsertTableALLRegiste(self,DatabaseName,TableName,RegisteList):
        #print(RegisteList)
        try:
            AllTableRegiste=""
            for Registe in RegisteList:
                EachTableRegiste = ""
                for Field in Registe:
                    EachTableRegiste+="'"+Field+"',"
                EachTableRegiste=EachTableRegiste.strip(',')
                EachTableRegiste='('+EachTableRegiste+')'

                AllTableRegiste+=EachTableRegiste+","
            AllTableRegiste=AllTableRegiste.strip(',')
            #AllTableRegiste = '(' + AllTableRegiste + ')'

            CommandSql = "insert into %s.%s values %s;" % (DatabaseName,TableName,AllTableRegiste)
            print(CommandSql)
            #print(CommandSql)
            self._MysqlCursor.execute(CommandSql)
            self._MysqlDatabase.commit()

        except Exception as result:
            self._MysqlDatabase.rollback()
            print("Error of Create Tables``````")
            print("向数据表插入数据时出现错误！ %s" % result)

    def InsertTableEachRegiste(self,DatabaseName,TableName,RegisteList):

        for Registe in RegisteList:
            EachTableRegiste = ""
            for Field in Registe:
                EachTableRegiste += "'" + Field + "',"
            EachTableRegiste = EachTableRegiste.strip(',')
            EachTableRegiste = '(' + EachTableRegiste + ')'
            CommandSql = "insert into %s.%s values %s;" % (DatabaseName, TableName, EachTableRegiste)
            #print(CommandSql)
            # print(CommandSql)
            try:

                self._MysqlCursor.execute(CommandSql)
                self._MysqlDatabase.commit()
            except Exception as result:
                #self._MysqlDatabase.rollback()
                print("Error of Create Tables``````")
                print("向数据表插入数据时出现错误！ %s-->> %s" % (result,TableName))
                continue


    def FileDataTransformSql(self):
        for DatabaseName in self._SourceExcelDataDict["databases"]:
            self.CreateDatabases(DatabaseName)
            for TableName in self._SourceExcelDataDict["databases"][DatabaseName]["tables"]:
                self.CreateTables(DatabaseName,TableName,self._SourceExcelDataDict["databases"][DatabaseName]["tables"][TableName]['desc'])
                self.InsertTableEachRegiste(DatabaseName, TableName,self._SourceExcelDataDict["databases"][DatabaseName]["tables"][TableName]['registe'])


    def ReadFileRootPath(self,source_root_path):
        self._SourceFileRootPath=source_root_path

        database_list = os.listdir(self._SourceFileRootPath)
        for database_name in database_list:
            if database_name not in self._SourceExcelDataDict["databases"]:
                self._SourceExcelDataDict["databases"][database_name]={"tables":{}}
            database_path = os.path.join(self._SourceFileRootPath, database_name)
            #print(database_path)
            table_name_list = os.listdir(database_path)
            for table_name in table_name_list:
                if table_name not in self._SourceExcelDataDict["databases"][database_name]["tables"]:
                    self._SourceExcelDataDict["databases"][database_name]["tables"][table_name]= {"desc":{},"registe":[]}

                table_path = os.path.join(database_path, table_name)
                file_name_list = os.listdir(table_path)
                for file_name in file_name_list:
                    file_path = os.path.join(table_path, file_name)
                    file_path = os.path.join(table_path, file_name)
                    print(file_path)
                    #print(file_path)
                    # if database_name == 'tags':
                    #     print(file_path)
                    #     self.ReadFileData(file_path,database_name,table_name,file_name)
                    self.ReadFileData(file_path, database_name, table_name, file_name)


    def ReadFileData(self,file_path,database_name,table_name,file_name):
        try:
            # if database_name =='tags':
            #     print(file_path)
            #print(file_path)
            file_cur=open(file_path,'rb')
            all_file_data=file_cur.readlines()
            encode_type = chardet.detect(all_file_data[0])
            if encode_type['encoding'] not in self._FileEncoding:
                self._FileEncoding[encode_type['encoding']]={}
                self._FileEncoding[encode_type['encoding']][database_name]=[]
                self._FileEncoding[encode_type['encoding']][database_name].append(file_name)
            else:
                if database_name not in self._FileEncoding[encode_type['encoding']]:
                    self._FileEncoding[encode_type['encoding']][database_name].append(file_name)
                else:
                    self._FileEncoding[encode_type['encoding']][database_name].append(file_name)


            # 检查文件类型····desc or registe······
            file_type = file_name.split("_")[0]
            if file_type == "desc":
                if len(all_file_data) != 0:  # 因为有很多空文件··············
                    encode_type = chardet.detect(all_file_data[0])
                    if encode_type["encoding"] == "utf-8":
                        for registe in file_data:
                            registe = registe.decode().strip()
                            registe = registe.split('\t')
                            registe[0] = registe[0].strip(' ')  # 去除多余的空格···
                            registe[1] = registe[1].strip(' ')
                            #print(registe)
                            if registe[1] not in self._FileFieldEncoding:
                                self._FileFieldEncoding[registe[1]]=''
                            if '' in registe:  # 当遇到分区前，退出读取字段信息····
                                break
                            else:
                                self._SourceExcelDataDict["databases"][database_name]["tables"][table_name]['desc'][registe[0]] = registe[1]

                    elif encode_type["encoding"]=="Windows-1252":

                        for registe in all_file_data:
                            registe = registe.decode("Windows-1252")
                            registe=registe.encode("utf-8")
                            registe = registe.split('\t')
                            registe[0] = registe[0].strip(' ')  # 去除多余的空格···
                            registe[1] = registe[1].strip(' ')
                            #print(registe)

                            if registe[1] not in self._FileFieldEncoding:
                                self._FileFieldEncoding[registe[1]]=''

                            if '' in registe:  # 当遇到分区前，退出读取字段信息····
                                break
                            else:
                                self._SourceExcelDataDict["databases"][database_name]["tables"][table_name]['desc'][registe[0]] = registe[1]

                    else:
                        file_cur = open(file_path, 'r')
                        file_data = file_cur.readlines()
                        for registe in file_data:
                            registe = registe.split('\t')
                            registe[0]=registe[0].strip(' ')   #去除多余的空格···
                            registe[1] = registe[1].strip(' ')
                            #print(file_name,registe)
                            if registe[1] not in self._FileFieldEncoding:
                                self._FileFieldEncoding[registe[1]]=''
                            if '' in registe:            #当遇到分区前，退出读取字段信息····
                                break
                            else:
                                self._SourceExcelDataDict["databases"][database_name]["tables"][table_name]['desc'][registe[0]]=registe[1]
                                #print(self._SourceExcelDataDict["databases"][database_name]["tables"][table_name]['desc'])

            elif file_type == "registe":
                if len(all_file_data) != 0:
                    encode_type = chardet.detect(all_file_data[0])
                    #print(encode_type)
                    if encode_type["encoding"] == "utf-8":
                        for registe in all_file_data:
                            registe = registe.decode().strip()
                            registe = registe.split('\t')
                            self._SourceExcelDataDict["databases"][database_name]["tables"][table_name]['registe'].append(registe)

                    elif encode_type["encoding"] == "Windows-1252":
                        for registe in all_file_data:
                            registe = registe.decode("Windows-1252")
                            registe.encode("utf-8")
                            #print(registe.split('\t'))
                            self._SourceExcelDataDict["databases"][database_name]["tables"][table_name]['registe'].append(registe.split('\t'))
                            #print(self._SourceExcelDataDict["databases"][database_name]["tables"][table_name]['registe'])
                    else:
                        file_cur = open(file_path, 'r')
                        file_data = file_cur.readlines()
                        for registe in file_data:
                            registe = registe.split('\t')
                            self._SourceExcelDataDict["databases"][database_name]["tables"][table_name]['registe'].append(registe)

                            # if database_name =='dw_ods':
                            #     print(registe)

            file_cur.close()
        except Exception as result:
            file_cur.close()
            print("eroor of read_file_data```")
            print("未知错误 %s" % result)

a=source_file_to_mysql('127.0.0.1','3306','root','mysql')
a.ReadFileRootPath(r'E:\FileToMysql')
a.displayMysqlHost()
a.FileDataTransformSql()


