import requests
url = "https://manit.evotingzone.com/api/index.php/users/index"
page_url = 'https://alansimpson.me/pyhton/scrape_sample.html'
headers = {'user_Agent':'Mozilla/5.0(Windows NT 10.0; Win64;x64)AppleWebkit/532.36 (KHTML,like Gecko)Chrome/92.0.4515.131 Safari/537.36'}
# open that page 
r = requests.get(url,headers=headers)
res = r.json()
print('toter voters',res ['data']['tptal_voters'])
print('voted',res['data']['voted'])
print('not voted',res['data']['non_voted'])