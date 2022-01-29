import xml.etree.ElementTree as ET
import requests
tree = ET.ElementTree(file='C:\\Users\\Richa\\OneDrive\\Desktop\\Homework\\2021-22\\ITEC 4020\\4020a1-datasets.xml')
root = tree.getroot()

titles = []
responses = []
for chld in root:
    if(chld.tag=='PubmedArticle'):
        for chld2 in chld:
            if(chld2.tag == 'MedlineCitation'):
                for chld3 in chld2:
                    if(chld3.tag == 'Article'):
                        for chld4 in chld3:
                            if(chld4.tag == 'ArticleTitle'):
                                titles.append(chld4.text)
print(titles)

url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?"

for title in titles:
    query = {'db': 'pubmed', 'term': title, 'rettype': 'uilist'}

    response = requests.get(url, params = query)
    responses.append(response)
