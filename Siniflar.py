from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys
from bs4 import BeautifulSoup
import lxml
import requests

class CheckGoogle():

  def __init__(self,url,path,str):
     self.country =url
     self.CrmDrvpth =path
     self.SrcTrm =str
  def RunR(self):
      driver = webdriver.Chrome(executable_path=self.CrmDrvpth)
     # driver.maximize_window()
      driver.minimize_window()
      driver.implicitly_wait(5)
      driver.get(self.country)
      assert "Amazon" in driver.title
      searchTextBox = driver.find_element_by_id("twotabsearchtextbox")
      searchTextBox.clear()
      searchTextBox.send_keys(self.SrcTrm)
      searchTextBox.send_keys(Keys.RETURN)
      time.sleep(3)
      return driver
  def urunBilgi(self,pageobj):
            src = BeautifulSoup(pageobj.page_source, "lxml")
            Rtr = src.find("div", attrs={"class": "s-card-container"}).text
            return Rtr
  def CookieOk(self,pageobj):
            cookieok = pageobj.find_element_by_id("sp-cc-accept")
            cookieok.send_keys(Keys.RETURN)
  def check_title(self,pageobj):
            url = pageobj.title
            return url
  def check_url(self,pageobj):
            title = pageobj.current_url
            return title
  def ScreenShot(self,pageobj):
            pageobj.save_screenshot( ".png")
  def PageQuit(self,pageobj):
      pageobj.quit()
