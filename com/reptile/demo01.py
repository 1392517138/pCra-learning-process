import requests

url = 'https://www.amazon.cn/dp/B01EIS3790?ref_=Oct_DLandingS_D_c787cc85_61&smid=A3TEGLC21NOO5Y'
kv = {'user-agent':'Mozilla/5.0'}
r = requests.get(url,headers = kv)
print(r.status_code)
print(r.text)
