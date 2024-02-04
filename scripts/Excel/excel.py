import pandas as pd

class Excel:

    def AddDataFrame(dataFrame:dict,metaDataFrame:dict)->dict:
        for dataFrameKey in dataFrame.keys():
            if dataFrameKey in metaDataFrame.keys():
                dataFrame[dataFrameKey]+=metaDataFrame[dataFrameKey]
        
        for metaDataFrameKey in metaDataFrame.keys():
            if metaDataFrameKey not in dataFrame.keys():
                dataFrame[metaDataFrameKey] = metaDataFrame[metaDataFrameKey]
        
        return dataFrame
            
    
    def ConvertToExcel(dataFrame:dict,outFileName:str):
        df = pd.DataFrame(dataFrame)

        excelFilePath= f"out/{outFileName}.xlsx"
        writer = pd.ExcelWriter(excelFilePath, engine="xlsxwriter", )
        df.to_excel(writer,sheet_name="Sheet1",index=True)

        workbook = writer.book

        cellFormat =workbook.add_format({ "text_wrap" : True , "align" : "left" , "valign" : "top"}) 

        
        if "Sheet1" in writer.sheets:
            worksheet = writer.sheets["Sheet1"]
        else:
            # Sayfa yoksa oluştur
            worksheet = writer.sheets["Sheet1"] = workbook.add_worksheet()

        for col_num, value in enumerate(df.columns.values):
            max_len = max(df[value].astype(str).apply(len).max(), len(value))
            worksheet.set_column(col_num+1, col_num+1, max_len + 2, cellFormat)

        writer._save()
    
    def OpenExcel(outFileName):
        excelFilePath= f"out/{outFileName}.xlsx"
        import os 

        os.system(f"start excel {excelFilePath}")
        input("")
