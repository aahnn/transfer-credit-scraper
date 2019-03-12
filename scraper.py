from bs4 import BeautifulSoup
import requests
import re

"""Check if a certain school has the requested course"""
def check_school(school_code, requested_subject, requested_course):
    post_req = requests.post('https://banweb.banner.vt.edu/ssb/prod/hzsktgid.P_ProcChoices', 
        data={'inst_subj': requested_subject, 'school_sbgi_code': school_code, 'vt_btn': 'SUBMIT'})
    post_req.raise_for_status()

    post_soup = BeautifulSoup(post_req.content, 'html5lib')

"""Start Script"""
# Get a list of school codes, needed to check if a school has a certain course
get_req = requests.get('https://banweb.banner.vt.edu/ssb/prod/hzsktgid.P_DispTranGuide')
get_req.raise_for_status()

get_soup = BeautifulSoup(get_req.content, 'html5lib')
schools = get_soup.select('select[name="school_sbgi_code"] option')
codes = []
for tag in schools:
    codes.append(tag.get('value'))

# TODO: Add sys args functionality, e.g. scraper.py CS 1114
# TODO: Finish check_school function