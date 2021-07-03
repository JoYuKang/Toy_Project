# Toy_Project      

## 정리     


### JSONView         
https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc?hl=ko


### CSS
https://developer.mozilla.org/ko/docs/Web/CSS/border     
https://getbootstrap.com/docs/4.0/components/alerts/     
https://www.w3schools.com/css/css_border.asp     

### mongoDB 다운
https://www.mongodb.com/try/download/community

### Git bash 다운
https://git-scm.com/
### Robo3T 다운 
https://robomongo.org/download
### Pymongo w3school
https://www.w3schools.com/python/python_mongodb_sort.asp
### 프레임워크 다운     
flask     
pymongo    
bs4     
requests     
### 북리뷰 사이트 
### 무비스타
      
### 서버 만들기
https://ap-northeast-2.console.aws.amazon.com/console/home?region=ap-northeast-2#
### 세팅
sudo chmod 755 initial_ec2.sh     
#### pip3 설치
sudo apt-get update
sudo apt-get install -y python3-pip

#### pip3 대신 pip 라고 입력하기 위한 명령어
sudo update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

#### 포트포워딩
80포트로 들어오는 요청을 5000포트로 넘겨주는 명령어     
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 5000
