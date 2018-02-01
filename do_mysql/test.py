import requests

def get_addr(ip):
    api_url = "http://ip.taobao.com/service/getIpInfo.php"
    params = {'ip': ip}
    r=requests.get(url=api_url,params=params)
    info=r.json()
    code=info.get('code')
    if code == 0:
        ret_data = info.get("data")
        isp = ret_data.get("isp")
        city = ret_data.get("city")
        country = ret_data.get("country")
        #返回国家,城市,和运营商
        return {'country':country,'city':city,'isp':isp}
    else:
        return '查询失败'


res=get_addr('180.153.232.170')
print(res)