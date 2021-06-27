import requests
from colorama import Fore, Back, Style


def track_url(url):
        try:
            resp = requests.get(url)
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
        except BaseException as be:
            print(Fore.RED + 'Tracking Failed! Check URL')
            print(be)
            exit()
link = input("Enter the link : ")
track_url(link)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
