# '%s' & '문자열'
from ensurepip import version


name = 'maria'
print('I am %s.' % name)

#format 메서드
print('Hello, {0}'.format('World!'))
print('Hello, {0}'.format(100))

#f-string *파이썬 ver 3.6부터 사용 가능
language = 'Python'
version = 3.6
print(f'Hello, {language} {version}')