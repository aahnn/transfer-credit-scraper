import time
import sys

import requests
from bs4 import BeautifulSoup


"""Check if a certain school has the requested course."""
def check_school(school_code, requested_subject, requested_courseid):
    post_req = requests.post('https://banweb.banner.vt.edu/ssb/prod/hzsktgid.P_ProcChoices', 
        data={'inst_subj': requested_subject, 'school_sbgi_code': school_code, 'vt_btn': 'SUBMIT'})
    if post_req.status_code == requests.codes.ok:
        post_soup = BeautifulSoup(post_req.content, 'html5lib')
        courses = post_soup.select('table.dataentrytable tbody tr td b')

        subject_courses = []
        for course in courses:
            course_string = course.getText()
            if requested_subject in course_string:
                subject_courses.append(course_string)
        if requested_courseid:
            id_matches = []
            for subject_course in subject_courses:
                if requested_courseid in subject_course:
                    return id_matches.append(subject_course)
            return id_matches

        return subject_courses

"""Start Script"""
# Get a list of school codes, needed to check if a school has a certain course
if len(sys.argv) < 2 or len(sys.argv) > 3:
    sys.exit('Usage: python scraper.py <SUBJECT> <COURSE ID>\n   or: python scraper.py <SUBJECT>')
subject = sys.argv[1]
if len(sys.argv) == 3:
    courseid = sys.argv[2]
else:
    courseid = None

get_req = requests.get('https://banweb.banner.vt.edu/ssb/prod/hzsktgid.P_DispTranGuide')
get_req.raise_for_status()

get_soup = BeautifulSoup(get_req.content, 'html5lib')
schools = get_soup.select('select[name="school_sbgi_code"] option')
school_codes = {}
for tag in schools:
    school_codes[tag.get('value')] = tag.getText()

for school_code, school_name in school_codes.items():
    time.sleep(5)
    print('{}: {}'.format(school_name, check_school(school_code, subject, courseid)))


# TODO: Add sys args functionality, e.g. scraper.py CS 1114.. make this case insensitive, make it work with only subject arg