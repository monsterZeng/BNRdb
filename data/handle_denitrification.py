import pymysql as sql
import pandas as pd

# 打开数据库并且连接, host 用户名 密码 数据库名称
class DB():
    """
    self.conn:数据库连接
    self.cur:游标
    """

    def __init__(self, host="localhost", port=3306, db="", user="root", password="", charset="utf8"):
        # 创建连接
        self.conn = sql.connect(host=host,
                                port=port,
                                db=db    ,
                                user=user,
                                password=password,
                                charset=charset)
        # 创建游标，操作设置为字典类型
        self.cur = self.conn.cursor(cursor=sql.cursors.DictCursor)

    def __enter__(self):
        # 返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行
        self.conn.commit()
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        #
        self.cur.close()

    def get_one_data(self, query):
        # 执行SQL查询
        self.cur.execute(query)
        # 使用fectchone()获取单条数据
        return self.cur.fetchone()

    def create_table(self, table_name, query):
        # 如果当前表存在，则删除当前表
        self.cur.execute("DROP TABLE IF EXISTS " + table_name)
        # 开始创建数据表
        self.cur.execute(query)

    # 插入记录

    def insert(self, data, table_name,excel_keys):
        count = 0
        for i in range(0, len(data)):
            print(table_name, i, "total nums = ", len(data))
            query = ""
            Influent_Source_Type   = str(data[excel_keys[0]][i]).replace("'","\\'")
            Denitrification_System = str(data[excel_keys[1]][i]).replace("'","\\'")
            Denitrifying_Reactor   = str(data[excel_keys[2]][i]).replace("'","\\'")
            Medium                 = str(data[excel_keys[3]][i]).replace("'","\\'")
            Culture                = str(data[excel_keys[4]][i]).replace("'","\\'")
            Organism_cultured      = str(data[excel_keys[5]][i]).replace("'","\\'")
            Respiration            = str(data[excel_keys[6]][i]).replace("'","\\'")
            Electron_Donor         = str(data[excel_keys[7]][i]).replace("'","\\'")
            Electron_Acceptor      = str(data[excel_keys[8]][i]).replace("'","\\'")
            Input                  = str(data[excel_keys[9]][i]).replace("'","\\'")
            Nitrate_Removal_Rate   = str(data[excel_keys[10]][i]).replace("'","\\'")
            Denitrification_Rate   = str(data[excel_keys[11]][i]).replace("'","\\'")
            Microorganism_identified  = str(data[excel_keys[12]][i]).replace("'","\\'")
            Molecular_Tools        = str(data[excel_keys[13]][i]).replace("'","\\'")
            Major_Findings         = str(data[excel_keys[14]][i]).replace("'","\\'")
            Authors                = str(data[excel_keys[15]][i]).replace("'","\\'")
            Title                  = str(data[excel_keys[16]][i]).replace("'","\\'")
            Pubmed                 = str(data[excel_keys[17]][i]).replace("'","\\'")
            Link                   = str(data[excel_keys[18]][i]).replace("'","\\'")
            Abstract               = str(data[excel_keys[19]][i]).replace("'","\\'")
            
            query = """INSERT INTO %s (Influent_Source_Type,Denitrification_System,Denitrifying_Reactor,Medium,Culture,Organism_cultured,Respiration,Electron_Donor,Electron_Acceptor,Input,Nitrate_Removal_Rate,Denitrification_Rate,Microorganism_identified,Molecular_Tools,Major_Findings,Authors,Title,Pubmed,Link,Abstract)
                            VALUES( '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
                                    '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'  \
                                  )"""  \
                            % (    
                              table_name,         
                              Influent_Source_Type   ,   
                              Denitrification_System ,
                              Denitrifying_Reactor   ,
                              Medium                 ,
                              Culture                ,
                              Organism_cultured      ,
                              Respiration            ,
                              Electron_Donor         ,
                              Electron_Acceptor      ,
                              Input                  ,
                              Nitrate_Removal_Rate   ,
                              Denitrification_Rate   ,
                              Microorganism_identified ,
                              Molecular_Tools        ,
                              Major_Findings         ,
                              Authors                ,
                              Title                  ,
                              Pubmed                 ,
                              Link                   ,
                              Abstract               ,
                            )
            ## 执行sql语句
            self.cur.execute(query)
            # 执行sql语句
            
            self.conn.commit()
            #print(query)
            #self.check(query)
    def update(self, key, filed, value):
        sql = sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
        pass

    def check(self, query):
        try:
            self.cur.execute(query)
            self.conn.commit()

        except:
            # 回滚（Rollback）指的是程序或数据处理错误，将程序或数据恢复到上一次正确状态的行为。
            # 回滚包括程序回滚和数据回滚等类型。
            self.conn.rollback()

def Enzymes(file, sheet_name_list, DB):
    pass

if __name__ == "__main__":

    mydb = DB(db="dentrification")
    table_name = ["denitrifications_app_freshwatersystem",
                  "denitrifications_app_marinesystem",
                  "denitrifications_app_goundwatersystem",
                  "denitrifications_app_watertreatmentplant",
                  "denitrifications_app_wetlandriparianzones"]
    sheet_name_list = ["Freshwater systems", 
                       "Marine systems", 
                       "Groundwater Water systems", 
                       "Water Treatment Plant",
                       "Wetlands n Riparian zones"]
    #for i in range(1, len(sheet_name_list)):
    data = pd.read_excel("microbialdenitrification_systems_table.xlsx", sheet_name = sheet_name_list[0])      
    mydb.insert(data, table_name[0], data.keys())
    #print(data.keys())

