# coding: utf-8

"""
EAFP: easier to ask forgiveness then permission
LBYL: look before you leap
"""


def getPersonInfo(person=None):
    if person is None:
        print('person must be not null!')
    print('person %s' % person)


def getMemberInfo(member=None):
    try:
        member.info
    except Exception:
        print('member must be not null!')


getPersonInfo('kim')

# getMemberInfo('kawasaki')

getPersonInfo()

getMemberInfo()
