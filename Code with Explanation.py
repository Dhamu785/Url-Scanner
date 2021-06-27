#Module import
import requests

#To get a colorful output
from colorama import Fore, Back, Style

#Creating a function
def track_url(url):
  
        #Try and Except rule
        try:
            
            #Passing input url in the requests module
            resp = requests.get(url)
            
            #CHWCKING FOR REDIRECTED SITES 
            
            #If exists the history of the redirected sites are printed
            if resp.history:
                print(Fore.RED + '\nYes URL is Redirected or Shorten!')
                print(Fore.RED + 'Here the following redirected chain...\n')
                for r in resp.history:
                    print(Fore.RED + '|', r.status_code, '|', r.url, '|', r.reason)
                print(Fore.GREEN + '\nEND URL :', resp.url)
                print(Fore.GREEN + 'Status Code :', resp.status_code, resp.reason)
            else:
                print(Fore.WHITE + '\nURL is Not Redirected or Shorten!')
                print(Fore.WHITE + 'END URL :', resp.url)
                print(Fore.WHITE + 'Status Code :',resp.status_code, resp.reason)
                
        # To check the url is valid or not
        except BaseException as be:
            print(Fore.RED + 'Tracking Failed! Check URL')
            print(be)
            exit()
            
#To get the url from user
link = input("Enter the link : ")

#To call the function
track_url(link)
