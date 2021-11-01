# aifactory-beta-tutorial
Tutorial for `AI Factory` python API

## 키 요청 가이드 
How-to-request-your-key

1. aifactory-beta 설치

아래 명령어로 `aifactory-beta` 패키지를 설치합니다.
잦은 업데이트가 예상되오니 오류가 발생할 경우에는 업데이트를 시도해봐주세요.
```angular2html
pip install aifactory-beta
# or
pip install aifactory-beta -u
```

2. `aifactory-request-key` 명령어 실행

아래 명령어를 실행해주세요.

```
aifactory-request-key                
```

3. 이메일 주소 입력

명령어를 입력하면 이메일 주소를 요구합니다.
인공지능 팩토리 플랫폼을 이용할 때 사용하시는 아이디를 입력해주세요.
해당 이메일 주소로 제출에 사용할 수 있는 키를 보내드립니다.

```angular2html
% aifactory-request-key
Please enter your user email: your-id@your-email-host.com
```

4. 오류 확인

이메일을 못 받으신 경우 'log/' 폴더에 생기는 로그를 확인해주시고 스팸함도 확인해주세요.

또, 참여하신 *진행중* 태스크가 없으신 경우에도 키가 발송되지 않습니다.

키를 받으시려는 태스크 페이지에서 `대회 참여하기`를 꼭 눌러주세요!

## 제출 가이드

1. 키 저장

위의 키 요청 가이드를 참고해 먼저 키를 받아주세요.

키를 받으셨으면 `--key` 옵션을 이용해 키를 직접 입력하시거나 `sample_data/mykey.afk` 등의 텍스트 파일을 만들어 가장 윗줄에 키를 넣어놓고 사용하실 수 있습니다.

