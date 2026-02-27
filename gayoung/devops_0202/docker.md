## Docker Hub 에서 이미지 다운로드 CLI
```bash
docker pull ubuntu:24.04
```
- `docker` : 도커 명령어
- `pull` : 받다
- `ubuntu` : 이미지 이름
- `:` : 이미지 이름과 태그 구분자
- `24.04` : 태그 이름

## Docker 이미지 확인
```bash
docker images
```

파일만들고 실행
docker run -d -it --name nd node:24.13.0

docker exec -it nd /bin/bash

root@0ca00e98da53:/# cd ~
root@0ca00e98da53:~# pwd
/root
root@0ca00e98da53:~# mkdir app
root@0ca00e98da53:~# cd app
root@0ca00e98da53:~/app# pwd
/root/app
root@0ca00e98da53:~/app# npm create vite .
Need to install the following packages:
create-vite@8.2.0
Ok to proceed? (y) y

이러면 운영체제가 달라서 연결이 안됨.
root@0ca00e98da53:~/app# exit 후
docker stop nd (<<이미지 명)으로 일단 서버를 끔

만들 때 docker run -d -it -p 80:5173 --name nd node:24.13.0
-p가 포트를 설정해줌. 80(윈도우포트):5173(서버포트)

편하게 하려면 dev containers에 들어가서 화살표 누르고 드가서 하면 됨