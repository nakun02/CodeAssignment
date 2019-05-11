from flask import Flask,request,send_file
import urllib, base64
from flask_cors import CORS
import io,requests,json
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import seaborn as sns
import numpy as np
import pandas as pd
app =Flask(__name__)
CORS(app)

@app.route('/PlotChangeInHoldings', strict_slashes=False)
@app.route('/PlotChangeInHoldings/<path:path>')
def PlotChangeInHoldings1(path=None):
    inputData= str(path).split('/')
    fromDate= inputData[0].replace('-','/')
    toDate=inputData[1].replace('-','/')
    ticker=inputData[2]
    Banks=CreateBanksData()
    df= FetchShareHoldings(Banks,fromDate,toDate,ticker)
    df['logHoldings'] = np.log(df['holdings'])
    sns.barplot(x=df.Bank,y=df.logHoldings)
    plt.ylabel("%change in Holdings (on Log Scale)")
    bytes_image= io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    encoded_string = base64.b64encode(bytes_image.getvalue()).decode()

    return encoded_string




def FetchShareHoldings(Banks,fromDate,toDate,ticker):
    driver = webdriver.Chrome('C:/Users/nakunl/Downloads/chromedriver.exe')
    driver.get("http://www.hkexnews.hk/sdw/search/searchsdw.aspx")
    stockholdings=[]
    for bank in Banks:
        bankslist=[]
        holdingsTotal=0
        bankslist.append(bank)
        for pID in Banks[bank]:
            holdingsTotal += GetShareHoldingsWithDate(toDate,pID,ticker,driver)
            holdingsTotal -= GetShareHoldingsWithDate(fromDate,pID,ticker,driver)
        bankslist.append(holdingsTotal)
        stockholdings.append(bankslist)
    df = pd.DataFrame(stockholdings, columns = ['Bank', 'holdings'])
    return df



def GetShareHoldingsWithDate(date,pID,ticker,driver):
    inputElement = driver.find_element_by_id("txtParticipantID")
    inputElement.send_keys(pID)
    inputElement = driver.find_element_by_id("txtShareholdingDate")
    inputElement.click()
    dateTime=date.split('/')
    elems = driver.find_elements_by_css_selector('b[class="year"]>ul>li')
    clickitem=2019-int(dateTime[0])
    elems[clickitem].click()
    elems = driver.find_elements_by_css_selector('b[class="month"]>ul>li')
    clickitem=int(dateTime[1])-1
    elems[clickitem].click()
    elems = driver.find_elements_by_css_selector('b[class="day"]>ul>li')
    clickitem=int(dateTime[2])-1
    elems[clickitem].click()
    inputElement = driver.find_element_by_id("txtStockCode")
    inputElement.click()
    inputElement.send_keys(ticker)
    button = driver.find_element_by_id('btnSearch')
    button.click()
    holding=''
    if not isElementExist(driver,'pnlResultSingle') :
        htmlText=driver.find_element_by_class_name('shareholding ')
        lines=htmlText.text.splitlines()
        holdings= lines[1]
    else :
        lines= htmlText=driver.find_element_by_id('pnlResultSingle').text.splitlines()
        holdings= lines[0].split(':')[1]

    return float(holdings.strip().replace(',',''))

def isElementExist(driver,id):
    try :
        driver.find_element_by_id(id)
        return True
    except NoSuchElementException :
        return False


def CreateBanksData() :
    Banks={}
    Banks['HSBC']=['C00019','B01490']
    Banks['SC']=['B01078','C00039']
    Banks['CITI']=['C00010']
    Banks['GS']=['B01451']
    Banks['DB']=['B01323','C00074']
    Banks['ML']=['B01224']
    Banks['MACQ']=['B01554','C00102']
    Banks['JPM']=['C00100','B01504']
    Banks['UBS']=['B01451','B01366']
    Banks['BNP']=['B01299','C00064','C00093']
    Banks['DBS']=['C00015','C00016']
    Banks['MS']=['B01274']
    Banks['CLSA']=['B01138']
    Banks['BARC']=['B01076','B01781','C00005','C00098']
    return Banks

@app.route('/GetStocksList', strict_slashes=False)
def GetStocksList():
    url="http://www.hkexnews.hk/sdw/search/stocklist.aspx?sortby=stockcode&shareholdingdate=20190414"
    s=requests.get(url).content
    html = requests.get(url).content
    df_list = pd.read_html(s)
    df = df_list[-1]
    df.columns = df.columns.droplevel()
    out = df.to_json(orient='records').replace("'", "")
    return out



if __name__=="__main__":
    app.run()
