
class Trendyol:

    trendyolDict:dict

    def RemoveVlinksOfTrendyolDict():
        del Trendyol.trendyolDict["vlinks"]

    def RemoveLinksOfTrendyolDict():
        del Trendyol.trendyolDict["links"]



    def GetValueOfDict(dict, key):
        if dict==None:
            return None
        if dict ==[]:
            return None
        if type(key) == int:
            return dict[key]
        if key in dict.keys():
            return dict[key]
        return None

    def GetAttributeOfProduct(product:dict,key:str):
        if key in product["product"].keys():
            return product["product"][key]
        return None

    def GetProductName(product:dict):
        return product["name"]

    def GetProduct(shopID:str,categoryID:str,brandID:str,productID):
        return Trendyol.trendyolDict["shops"][shopID][categoryID][brandID][productID]

    def GetProductIDList(shopID:str,categoryID:str,brandID:str):
        productList=[]
        for product in Trendyol.trendyolDict["shops"][shopID][categoryID][brandID].keys():
            if product!="name":
                productList.append(product)
        return productList

    def GetBrandName(shopID:str,categoryID:str,brandID:str):
        return Trendyol.trendyolDict["shops"][shopID][categoryID][brandID]["name"]

    def GetBrandIDList(shopID:str,categoryID:str):
        brandList=[]
        for brand in Trendyol.trendyolDict["shops"][shopID][categoryID].keys():
            if brand!="name":
                brandList.append(brand)
        return brandList

    def GetCategoryName(categoryID:str):
        return  Trendyol.trendyolDict["items"][categoryID]["name"]

    def GetCategoryIDList(shopID):
        categoryList=[]
        for category in Trendyol.trendyolDict["shops"][shopID].keys():
            if category !="name":
                categoryList.append(category)
        return categoryList

    def GetShopName(shopID:str):
        return Trendyol.trendyolDict["shops"][shopID]["name"]

    def GetShopIDList():
        shopsIDList = []
        for shopID in Trendyol.GetShops().keys():
            shopsIDList.append(shopID)
        return shopsIDList

    def GetShops():
        return Trendyol.trendyolDict["shops"]
    
    def GetRootOfTrendyolDict():
        return Trendyol.trendyolDict["https://www.trendyol.com/"]

    def GetTrendyolDict():
        return Trendyol.trendyolDict

    def SetTrendyolDict(dictionary):
        Trendyol.trendyolDict = dictionary