from bs4 import BeautifulSoup
import requests


url = 'https://banweb.banner.vt.edu/ssb/prod/hzsktgid.P_DispTranGuide'
# use this one?
url2 = 'https://banweb.banner.vt.edu/ssb/prod/hzsktgid.P_ProcChoices'

req = requests.get(url)
req.raise_for_status()


def check_school(school_code):
    req = requests.post(url, data={'school_sbgi_code': str(school_code), 'submit': 'Find Courses'})

    soup = BeautifulSoup(req.content, 'html5lib')
    soup = BeautifulSoup
