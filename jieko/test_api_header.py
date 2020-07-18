import requests

# url_51job = "https://search.51job.com/list/030200,000000,0000,00,9,99,%25E8%25BD%25AF%25E4%25BB%25B6%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
#
# r_51 = requests.get(url=url_51job)
# r_51.encoding = 'gb2312'
# print(r_51.text)
# print(r_51.status_code)
# print(r_51.encoding)


url_12306 = "https://kyfw.12306.cn/otn/leftTicket/queryO?leftTicketDTO.train_date=2020-02-16&leftTicketDTO.from_station=CSQ&leftTicketDTO.to_station=SHH&purpose_codes=ADULT"
header = {"Cookie": "JSESSIONID=E701906E68088BA8CD380A4A6DAB6D6C; BIGipServerotn=837812746.38945.0000; RAIL_EXPIRATION=1582151667962; RAIL_DEVICEID=VPE0liWo4joErK2ElHhVHqnxyGrojV8P62w0PRGi2f43utn72M_NZtXvnUH-vF6COfOk056K4Qkfjl2Eca4ke2YBtUsveZKRLQwr-YF8qVEWUrKZeSqNE6T59yKhE5ZcXgR0Q76VjEmvBhq8t1m3fduneUv6FfE6; BIGipServerpool_passport=300745226.50215.0000; route=c5c62a339e7744272a54643b3be5bf64; _jc_save_fromStation=%u957F%u6C99%2CCSQ; _jc_save_toStation=%u4E0A%u6D77%2CSHH; _jc_save_fromDate=2020-02-16; _jc_save_toDate=2020-02-16; _jc_save_wfdc_flag=dc"}
r_12306 = requests.get(url=url_12306, headers=header)
print(r_12306.text)