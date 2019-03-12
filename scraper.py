from bs4 import BeautifulSoup
import requests


get_req = requests.get('https://banweb.banner.vt.edu/ssb/prod/hzsktgid.P_DispTranGuide')
get_req.raise_for_status()

get_soup = BeautifulSoup(get_req.content, 'html5lib')
schools = get_soup.select('select[name="school_sbgi_code"] option')


def check_school(school_code):
    post_req = requests.post('https://banweb.banner.vt.edu/ssb/prod/hzsktgid.P_ProcChoices', 
        data={'inst_subj': 'CS', 'school_sbgi_code': school_code, school_code: 'SUBMIT'})
    post_req.raise_for_status()

    post_soup = BeautifulSoup(post_req.content, 'html5lib')

check_school(3)