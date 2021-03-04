import requests, json, random, re, time
def get_email():
    a = random.randint(11, 99)
    b = random.randint(0, 20)
    email = 'varytmp+{}uu{}d@gmail.com'.format(a, b)
    return email
def send(email):
    data = {
        'email': email
    }
    s = requests.post(url='https://cv2.cheap/auth/send', data=data).text
    #print(s)
def get_num(email):
    head = {
        'Cookie': 'csrf_gmailnator_cookie=9283eccf4672e233327c1d07cbde2fbe; __gads=ID=808c92a03a3667c7-2268f1463cc6007d:T=1614844196:RT=1614845007:S=ALNI_MaEB-hZfUPTo6kHkEmOBLzPe4nqTQ; cto_bundle=AGHOXV9XSVpTNzY3TlRHbldjMDY5RFhQTlU4Y2J1cUpIWGNLVU0xa3ZiWGRKV1duNHo5cXpJYSUyQm5mZ0ROVDJBRFlIa211cG85JTJCOElMV0ZGQUIzVCUyRjg4NTdQZmZSSW9xMzZmMVY5dXdXeDViUUFYeG51SWNibEhqZGxqWGU5NjBQZHpxMg; _ga=GA1.2.1618068840.1614844229; _gid=GA1.2.103981802.1614844229; ci_session=15d382f04f7b998cecd0f9158bfe3db2c8f32629; __cfduid=d1f9a21dd34e5060cfd24ea55f37149961614844181'}
    data = {'csrf_gmailnator_token': '9283eccf4672e233327c1d07cbde2fbe', 'action': 'LoadMailList',
            'Email_address': email}
    s = requests.post(url='https://www.gmailnator.com/mailbox/mailboxquery', data=data, headers=head).text
    id = re.findall(r'(?<=messageid\\/#).+(?=\\">\\n\\t\\t\\t\\t\\t<table class=\\"message_container)', s)[0]
    data1 = {'csrf_gmailnator_token': '9283eccf4672e233327c1d07cbde2fbe', 'action': 'get_message', 'message_id': id,
             'email': 'varytmp'}
    mess = requests.post(url='https://www.gmailnator.com/mailbox/get_single_message/', headers=head, data=data1).text
    sixnum = re.findall(r'\d{6}', mess)[3]
    return sixnum

def register(email, sixnum):
    data = {'email': email, 'name': '我还在{}'.format(sixnum), 'passwd': 'refddr265rt', 'repasswd': 'refddr265rt',
            'code': '', 'emailcode': sixnum
            }
    s = requests.post(url='https://cv2.cheap/auth/register', data=data).json()
    #print(s)

def login(email):
    s = requests.session()
    data = {'email': email, 'passwd': 'refddr265rt', 'code': '', 'remember_me': '1'
            }
    result = s.post(url='https://cv2.cheap/auth/login', data=data).text
    #print(result)
    data1 = {'coupon': '', 'shop': '22', 'autorenew': '0', 'disableothers': '1'
             }
    buy_result = s.post(url='https://cv2.cheap/user/buy', data=data1).text
    #print(buy_result)
    hef_v2 = s.get(url='https://cv2.cheap/user').text
    #print(hef_v2)
    ssr_url = re.findall(r"(?<=neclickImport\('ssr',').+(?='\))", hef_v2)[0]
    return ssr_url
def main():
    email=get_email()
    send(email)
    time.sleep(10)
    sixnum = get_num(email)
    time.sleep(1)
    register(email, sixnum)
    time.sleep(1)
    ssr_url=login(email)
    return ssr_url
if __name__ == "__main__":
    main()
