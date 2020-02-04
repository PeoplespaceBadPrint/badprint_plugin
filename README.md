# OctoPrint-Badprint

## Setup
먼저 옥토프린트 소스를 git에서 다운받고, 파이썬 버전 2.x으로 virtualenv를 생성한다.

### 일반 linux/mac 에서
```
$ source [옥토프린트 소스코드가 저장된 디렉토리]/venv/bin/activate
$ git clone https://github.com/PeoplespaceBadPrint/badprint_plugin.git
(venv) $ octoprint dev plugin:install
```
### Octopi 에서
```
$ source ~/oprint/bin/activate
(oprint) $ octoprint dev plugin:install
```