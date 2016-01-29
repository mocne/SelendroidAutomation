__author__ = 'andrii.tiutiunnyk'


class User(object):

    def __init__(self, name, user_name, password):
        self.name = name
        self.user_name = user_name
        self.password = password
        self.programming_language = ['Ruby',
                                     'PHP',
                                     'Scala',
                                     'Python',
                                     'JavaScript',
                                     'Java',
                                     'C++',
                                     'C#']

    @property
    def e_mail(self):
        return self.user_name + '@email.com'
