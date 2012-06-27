# -*- coding: cp1251 -*-
# Shibalkin: Русские комментарии по тексту теперь тоже теперь должна понимать

from Github import Github #Linux
#from github import Github #Windows

class My_Github(Github):
# Authors:#   * E. Shibalkin <shibalkin@rambler.ru>
    def get_user(self, login=None):
        if login is None: # при None, стандартный метод выдает не ошибку, а другой объект
            login = raw_input("Введите логин: ")
        while 0 == 0:
            try:
                return Github.get_user(self, login)
            except (GithubException):
                if raw_input ("Такой пользователь не найден продолжить (y|n): ") == "n":
                    exit(0)
                else:
                    login = raw_input("Введите логин: ")
            
# Authors:
#   * A. Balyanova <bal0102@yandex.ru>
#   * E. Shibalkin <shibalkin@rambler.ru>
#   * D. Sandalov  <dmitry@sandalov.org>

def get_commits_number(user):
    commits_number = 0
    for repo in user.get_repos():
        for i in repo.get_commits():
            commits_number +=1
    return commits_number

# Authors:
#   * K. Sokolov   <kostikgold@gmail.com>
#   * D. Sandalov  <dmitry@sandalov.org>

def repos_sum_volume(user):
    sum_repository = 0
    for repo in user.get_repos():
        sum_repository += repo.size
    return sum_repository

# Authors:
#   * A. Korenev <korenev.alexander@gmail.com>

def f():
        list = []
        for x in user.get_repos():
                for y in x.get_commits():
                        for z in list:
                                if list[z] != y.committer or len(list) == 0:
                                        list.append( y.committer )
        return list


g = My_Github()
user = g.get_user("dmitrysandalov")
# Shibalkin: it's better to get once & use many times
# or even: repos = user.get_repos() => repos_sum_volume(repos)

#user = g.get_user("alsmirn")
print user._login, "wrote (sloc):", repos_sum_volume(user)
print user._login, "comitted times:", get_commits_number(user)
f()

