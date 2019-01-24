# Introduction
Elastic Beanstalk(이하 EB) application(이하 app, 앱)을 만들고, 첫 docker 서버를 배포하는 예제입니다.
운영체제 OSX 기준입니다.

### Create EB app
1. 콘솔에 로그인한 후, 우측 상단 `새 애플리케이션 생성`을 누릅니다.
2. `애플리케이션 이름`과 `설명`을 작성하고 다음페이지로 넘어갑니다
3. 생성한 앱을 클릭하여 들어가면, `이 애플리케이션을 지원하는 환경은 현재 없습니다. 지금 하나를 생성하십시오.` 라는 메시지가 보입니다. 클릭합니다.
4. `환경 티어 선택` 의 `웹 서버 환경`을 클릭합니다.
5. 이후 상세 설정이 나오는데, 사용자 환경에 맞춰 설정합니다. 이 예제에서는 `Docker` 환경으로 배포하도록 설정했습니다.

### Install EB CLI
```
brew update
```
```
brew install awsebcli
```
```
eb --version
```

### Setup EB CLI 
이 부분을 시작하기 전에,
```
cd ~
```
한 뒤, 
```
ls -al | grep aws
```
를 통해 aws 관련 디렉토리가 있는지 확인하고,
있다면,
```
cd .aws
cat config
```
를 통해 현재 설정된 계정의 `[profile eb-cli]` 항목의 `aws_access_key_id`, `aws_secret_access_key` 가 잘 있는지 먼저 확인해야 합니다.

### Run EB CLI
제일 먼저, EB CLI를 사용하기 위해서는, 유효한 source control(ex. git) 디렉토리로 이동해야 합니다.
```
cd some_availabe_source_control_directory
```
```
eb init
```
리전 선택 메시지가 나오면, 서울이므로 `10) ap-northeast-2 : Asia Pacific (Seoul)`를 선택합니다.
```
Select an application to use
1) 아까 만들었던 EB 앱 이름
```
위와같이 아까 만들었던 EB 앱 이름이 잘 나와야 합니다. 해당되는 앱을 선택합니다.
선택하자 마자 아래 메시지가 뜹니다. 아직 뭔지 모르니 사뿐하게 사용하지 않는다고 `n`을 입력하고 넘어갑니다.
```
Note: Elastic Beanstalk now supports AWS CodeCommit; a fully-managed source control service. To learn more, see Docs: https://aws.amazon.com/codecommit/
```