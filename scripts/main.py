
from Json.jsonManager import JsonManager
from Trendyol.trendyol import Trendyol
from Excel.excel import Excel

class Main:
    trendyolJson= "sources/trendyolcopy.json"

    def Start():
        Trendyol.SetTrendyolDict(
            JsonManager.ReadJson("sources/trendyolcopy.json")
        )

        Trendyol.SetTrendyolDict(
            Trendyol.GetRootOfTrendyolDict()
        )

        Trendyol.RemoveLinksOfTrendyolDict()
        Trendyol.RemoveVlinksOfTrendyolDict()


        dataFrame = {
        }

        for shopID in Trendyol.GetShopIDList():
            shopName= Trendyol.GetShopName(shopID)
            for categoryID in Trendyol.GetCategoryIDList(shopID):
                categoryName = Trendyol.GetCategoryName(categoryID)
                for brandID in Trendyol.GetBrandIDList(shopID,categoryID):
                    brandName = Trendyol.GetBrandName(shopID,categoryID,brandID)
                    for productID in Trendyol.GetProductIDList(shopID,categoryID,brandID):
                        product = Trendyol.GetProduct(shopID,categoryID,brandID,productID)
                        
                        metaData = {
                            "Shop ID":[shopID],
                            "Shop Name":[shopName],
                            "Category ID":[categoryID],
                            "Category Name":[categoryName],
                            "Brand ID":[brandID],
                            "Brand Name":[brandName]
                        }
                        
                        metaData["Shop ID"] = [shopID]
                        metaData["Shop Name"] = [shopName]
                        metaData["Product ID"] = [productID]
                        metaData["Product Name"] = [Trendyol.GetProductName(product)]
                        metaData["Attributes"] = [Trendyol.GetAttributeOfProduct(product,"attributes")]
                        metaData["Color"] = [Trendyol.GetAttributeOfProduct(product,"color")]
                        metaData["Campaign"] = [Trendyol.GetValueOfDict(Trendyol.GetAttributeOfProduct(product,"campaign"),"name")]
                        metaData["Category"] = [Trendyol.GetAttributeOfProduct(product,"category")["name"]]
                        metaData["Category Full"] = [Trendyol.GetAttributeOfProduct(product,"category")["hierarchy"]]
                        metaData["Brand ID"] = [brandID]
                        metaData["Brand Name"] = [brandName]
                        metaData["Content Descriptions"] = [Trendyol.GetAttributeOfProduct(product,"contentDescriptions")]
                        metaData["Descriptions"] = [Trendyol.GetAttributeOfProduct(product,"description")]
                        metaData["Business Unit"] = [Trendyol.GetAttributeOfProduct(product,"businessUnit")]
                        metaData["Gender"] = [Trendyol.GetValueOfDict(Trendyol.GetAttributeOfProduct(product,"gender"),"name")]
                        metaData["Url"] = [Trendyol.GetAttributeOfProduct(product,"url")]
                        metaData["Is Sellable"] = [Trendyol.GetAttributeOfProduct(product,"isSellable")]
                        metaData["Is Basket Discount"] = [Trendyol.GetAttributeOfProduct(product,"isBasketDiscount")]
                        metaData["Has Stock"] = [Trendyol.GetAttributeOfProduct(product,"hasStock")]
                        metaData["Original Price"] = [Trendyol.GetAttributeOfProduct(product,"price")["originalPrice"]]
                        metaData["Selling Price"] = [Trendyol.GetAttributeOfProduct(product,"price")["sellingPrice"]]
                        metaData["Is Free Cargo"] = [Trendyol.GetAttributeOfProduct(product,"isFreeCargo")]
                        metaData["Is Long Term Delivery"] = [Trendyol.GetAttributeOfProduct(product,"isLongTermDelivery")]
                        metaData["Promotions"] = [Trendyol.GetAttributeOfProduct(product,"promotions")]
                        metaData["Is Searchable Merchant "] = [Trendyol.GetAttributeOfProduct(product,"merchant")["isSearchableMerchant"]]
                        metaData["Merchant Name"] = [Trendyol.GetAttributeOfProduct(product,"merchant")["name"]]
                        metaData["Merchant Official Name"] = [Trendyol.GetAttributeOfProduct(product,"merchant")["officialName"]]
                        metaData["Merchant City Name"] = [Trendyol.GetAttributeOfProduct(product,"merchant")["cityName"]]
                        metaData["Merchant Address"] = [Trendyol.GetValueOfDict(Trendyol.GetValueOfDict(Trendyol.GetValueOfDict(Trendyol.GetAttributeOfProduct(product,"merchantListings"),0),"merchant"),"address")]
                        metaData["Merchant Email"] = [Trendyol.GetValueOfDict(Trendyol.GetAttributeOfProduct(product,"merchant"),"registeredEmailAddress")]
                        metaData["Merchant Tax Number"] = [Trendyol.GetAttributeOfProduct(product,"merchant")["taxNumber"]]
                        metaData["Merchant Seller Score"] = [Trendyol.GetValueOfDict(Trendyol.GetAttributeOfProduct(product,"merchant"),"sellerScore")]
                        metaData["Merchant Seller Score Color"] = [Trendyol.GetValueOfDict(Trendyol.GetAttributeOfProduct(product,"merchant"),"sellerScoreColor")]
                        metaData["Merchant Corporate Invoice Applicable"] = [Trendyol.GetAttributeOfProduct(product,"merchant")["corporateInvoiceApplicable"]]
                        metaData["Merchant Location Based Sales"] = [Trendyol.GetValueOfDict(Trendyol.GetAttributeOfProduct(product,"merchant"),"locationBasedSales")]
                        metaData["Merchant Bulk Sales Limit"] = [Trendyol.GetValueOfDict(Trendyol.GetAttributeOfProduct(product,"merchant"),"bulkSalesLimit")]
                        metaData["Merchant Seller Link"] = [Trendyol.GetValueOfDict(Trendyol.GetAttributeOfProduct(product,"merchant"),"sellerLink")]
                        metaData["Is Market Place"] = [Trendyol.GetAttributeOfProduct(product,"isMarketplace")]
                        metaData["Favori Count"] = [Trendyol.GetAttributeOfProduct(product,"favoriteCount")]
                        metaData["Ux Layout"] = [Trendyol.GetAttributeOfProduct(product,"uxLayout")]
                        metaData["Is Digital Good"] = [Trendyol.GetAttributeOfProduct(product,"isDigitalGood")]
                        metaData["Is Running Out"] = [Trendyol.GetAttributeOfProduct(product,"isRunningOut")]
                        metaData["Scheduled Delivery"] = [Trendyol.GetAttributeOfProduct(product,"scheduledDelivery")]
                        metaData["Avg Rating"] = [Trendyol.GetAttributeOfProduct(product,"ratingScore")["averageRating"]]
                        metaData["Total Rating Count"] = [Trendyol.GetAttributeOfProduct(product,"ratingScore")["totalRatingCount"]]
                        metaData["Total Comment Count"] = [Trendyol.GetAttributeOfProduct(product,"ratingScore")["totalCommentCount"]]
                        metaData["Questions"] = [product["questions"]]



                        dataFrame = Excel.AddDataFrame(dataFrame, metaData)
        

        Excel.ConvertToExcel(dataFrame,"trendyol")



        ##
        ## Ürün Adı LDA
        ##
        import pandas as pd
        from nltk.tokenize import word_tokenize
        from gensim import corpora, models
        import matplotlib.pyplot as plt
        import string
        from nltk.corpus import stopwords
        import os

        df3 = pd.read_excel("out/trendyol.xlsx")


        def remove_punct(text):
            text = str(text)
            text  = "".join([char for char in text if char not in string.punctuation])
            return text

        df3['lemma_utt'] = df3['Product Name'].apply(lambda x: remove_punct(x.lower()))

        stop = set(stopwords.words('turkish'))
        def remove_stopwords(text):
            text =  ' '.join([word for word in text.split() if word not in stop]) # delete stopwords from text
            return text

        df3['lemma_utt'] = df3['lemma_utt'].apply(lambda x: remove_stopwords(x.lower()))

        # Tokenization için lemma_utt sütununu oluştur
        df3["lemma_utt"] = df3["lemma_utt"].apply(lambda x: word_tokenize(x.lower()))

        # Gensim için sözlük oluştur
        dictionary = corpora.Dictionary(df3["lemma_utt"])
        doc_term_matrix = df3['lemma_utt'].apply(lambda x: dictionary.doc2bow(x))

        # LDA modelini oluştur ve eğit
        lda_model = models.LdaModel(corpus=doc_term_matrix, num_topics=9, id2word=dictionary, passes=15, random_state=100, chunksize=2000)

        # # LDA modelinden konu başlıklarını al
        topic_terms = lda_model.print_topics()

        # Görselleştirmeyi oluştur
        import pyLDAvis.gensim_models
        vis = pyLDAvis.gensim_models.prepare(lda_model, doc_term_matrix, dictionary)

        # # Konu başlıklarını güncelleme işlemi
        # prepared_data = vis.to_dict()
        # prepared_data['topic_info'] = pd.DataFrame(topic_terms, columns=['Topic', 'Terms'])

        # # Güncellenmiş veriyi görselleştirmeye atama
        # vis = pyLDAvis.PreparedData(**prepared_data)

        # HTML dosyasına kaydetme
        pyLDAvis.save_html(vis, 'out/LDA_Topic_Modeli.html')



        # Excel.OpenExcel("trendyol")
        
        import matplotlib.pyplot as plt

        # Excel dosyasından veriyi oku
        df3 = pd.read_excel("out/trendyol.xlsx")


        ##
        # En çok favorilenenen ilk 20 ürün
        ##
        top_20_favorites = df3.sort_values(by='Favori Count', ascending=False).head(20)

        plt.figure(figsize=(10, 8))
        plt.bar(top_20_favorites['Product Name'], top_20_favorites['Favori Count'], color='skyblue')
        plt.title('En Çok Beğenilen 20 Ürün')
        plt.xlabel('Ürün Adı')
        plt.ylabel('Favori Sayısı')
        plt.xticks(rotation=90, ha='right')
        plt.tight_layout()

        # Grafiği göster
        plt.savefig("out/En çok Favorilenen 20 Ürün.png")
        plt.show()


        plt.close()

        # En çok satılan kategoriler
        category_sales = df3.groupby('Category Name')['Total Rating Count'].sum().reset_index()

        sorted_categories = category_sales.sort_values(by='Total Rating Count', ascending=False).head(20)

        # Matplotlib kullanarak çubuk grafiği oluştur
        plt.figure(figsize=(10, 6))
        plt.bar(sorted_categories['Category Name'], sorted_categories['Total Rating Count'], color='lightcoral')
        plt.title('En Çok Satılan Kategoriler')
        plt.xlabel('Kategori Adı')
        plt.ylabel('Toplam Rating Sayısı')
        plt.xticks(rotation=90, ha='right')
        plt.tight_layout()

        # Grafiği göster veya kaydet
        plt.savefig("out/En Çok Satılan 20 Kategori.png")  
        plt.show()


        # Mağaza bazında toplam skoru hesapla
        store_scores = df3.groupby('Merchant Name')['Merchant Seller Score'].mean().reset_index()

        # Skorlarına göre mağazaları sırala
        sorted_stores = store_scores.sort_values(by='Merchant Seller Score', ascending=False).head(20)

        # Matplotlib kullanarak çubuk grafiği oluştur
        plt.figure(figsize=(10, 6))
        plt.bar(sorted_stores['Merchant Name'], sorted_stores['Merchant Seller Score'], color='lightgreen')
        plt.title('En Yüksek Skorlu Mağazalar')
        plt.xlabel('Mağaza Adı')
        plt.ylabel('Ortalama Skor')
        plt.xticks(rotation=90, ha='right')
        plt.tight_layout()

        # Grafiği göster veya kaydet
        plt.savefig("out/En yüksek Skorlu 20 Mağaza.png")
        plt.show()

        # Ürün bazında toplam yorum sayısını hesapla
        product_comments = df3.groupby('Product Name')['Total Comment Count'].sum().reset_index()

        # Yorum sayılarına göre ürünleri sırala
        sorted_products = product_comments.sort_values(by='Total Comment Count', ascending=False).head(20)

        # Matplotlib kullanarak çubuk grafiği oluştur
        plt.figure(figsize=(10, 8))
        plt.bar(sorted_products['Product Name'], sorted_products['Total Comment Count'], color='coral')
        plt.title('En Fazla Yorum Yapılan Ürünler')
        plt.xlabel('Ürün Adı')
        plt.ylabel('Toplam Yorum Sayısı')
        plt.xticks(rotation=90, ha='right')
        plt.tight_layout()

        # Grafiği göster veya kaydet
        plt.savefig("out/En Fazla Yorum Yapılan 20 Ürün.png")
        plt.show()


        # En çok puanlanan 20 mağaza
        top_20_sellers = df3.groupby('Merchant Name')['Total Rating Count'].sum().reset_index().sort_values(by='Total Rating Count', ascending=False).head(20)

        # Matplotlib kullanarak çubuk grafiği oluştur
        plt.figure(figsize=(10, 6))
        plt.bar(top_20_sellers['Merchant Name'], top_20_sellers['Total Rating Count'], color='green')
        plt.title('En Çok Puanlanan Mağazalar')
        plt.xlabel('Mağaza Adı')
        plt.ylabel('Toplam Satış Sayısı')
        plt.xticks(rotation=90, ha='right')
        plt.tight_layout()

        # Grafiği göster veya kaydet
        plt.savefig("out/En Çok Puanlanan Mağazalar İlk 20 .png")
        plt.show()


        # Total Rating Count'a göre markaları sırala
        top_brands = df3.groupby('Brand Name')['Total Rating Count'].sum().reset_index().sort_values(by='Total Rating Count', ascending=False).head(20)

        # Matplotlib kullanarak çubuk grafiği oluştur
        plt.figure(figsize=(10, 6))
        plt.bar(top_brands['Brand Name'], top_brands['Total Rating Count'], color='orange')
        plt.title('En Yüksek Puan Alan Markalar')
        plt.xlabel('Marka Adı')
        plt.ylabel('Toplam Puan Sayısı')
        plt.xticks(rotation=90, ha='right')
        plt.tight_layout()

        # Grafiği göster veya kaydet
        plt.savefig("out/En Yüksek Puan Alan 20 Marka.png")
        plt.show()



Main.Start()

