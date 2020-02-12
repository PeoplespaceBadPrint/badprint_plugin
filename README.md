# OctoPrint-Badprint

## Setup
먼저 옥토프린트 소스를 git에서 다운받고, 파이썬 버전 2.x으로 virtualenv를 생성한다.

참고) https://lhy0718.github.io/python/2020/01/26/Setup-virtualenv-with-a-specific-version-of-Python.html
https://lhy0718.github.io/python/2020/01/26/Installing-the-Python-virtual-enviroment.html

### 일반 linux/mac 에서
```
$ git clone https://github.com/PeoplespaceBadPrint/badprint_plugin.git
$ cd badprint_plugin
$ source [옥토프린트 소스코드가 저장된 디렉토리]/venv/bin/activate
(venv) $ octoprint dev plugin:install
```
### Octopi 에서
```
$ git clone https://github.com/PeoplespaceBadPrint/badprint_plugin.git
$ cd badprint_plugin
$ source ~/oprint/bin/activate
(oprint) $ octoprint dev plugin:install
```

### 메일수신기능 이용하기
keyring에 메일을 보낼 계정의 주소와 암호를 입력해야 합니다!
아래는 Python3로 keyring에 암호를 저장하는 코드입니다.
```
>>> import keyring
>>> keyring.set_password("yagmail", username, password)
```