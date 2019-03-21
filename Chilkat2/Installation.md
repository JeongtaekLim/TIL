# Introduction
유료 암호화 라이브러리인 Chilkat을 사용할 기회가 있어서 사용하는 도중, 설치에 애를 먹어 기록

# Installation

1. 설치파일 다운로드
https://www.chilkatsoft.com/chilkat2-python.asp#macDownloads
Chilkat2 Python 3.6 Mac OS X

2. `.so` 복사
다운로드 폴더 내부의 .so를, venv/lib/python3.6/site-packages로 copy

3. 사용중인 툴 재시작

그래도 안된다면 재부팅 권장

처음엔 툴 재시작 및 재부팅을 안해보고 안되는 줄 알고 "Common mistake"를 반복해서 하루를 허비함..

#  Common mistake - Installation 

DO NOT FOLLOW THIS WAY. I FAILED. PLEASE FOLLOW ABOVE GUIDE

1. 설치파일 다운로드

https://www.chilkatsoft.com/chilkat2-python.asp#macDownloads
> Chilkat2 Python 3.6 Mac OS X

2.  Virtual env 실행
$ source venv/bin/activate

3. Virtual env의 python을 통한 설치파일 실행 #1
(venv) $ python installChilkat.py

하지만 이때, “Module ’site’ has no attribute ‘getusersitepackages’” 라는 에러가 발생하며, 설치가 진행되지 않습니다.
Chilkat 라이브러리를 찾아 본 결과  https://www.chilkatsoft.com/installpythonlinux.asp 여기서와 같이, virtual env에 대해서는 별도 설치파일을 실행해야 한다고 합니다.

다운받아서 실행했습니다.

4. Virtual env의 python을 통한 설치파일 실행 #2
(Venv) $ python installChilkat_virtEnv.py

하지만 또다른 에러를 만나게 됩니다.
“AttributeError: module ’sys’ has no attribute ‘_framework’”

설치 코드를 까서 수정을 해야하.. 이게 가능할까.. 많은 고민끝에 여기까지 시도하고 그만둠