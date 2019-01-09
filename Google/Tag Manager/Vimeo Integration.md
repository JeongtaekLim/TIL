# Before Start - 도입실패이유
영상을 한번 띄워주는 랜딩페이지와는 다르게, 유동적으로 영상을 보이게, 안보이게 조작하는 Learning Management System(이하 LMS)의 경우, 

# Introduction

## 1 단계: 사이트에 트래킹 스크립트 추가

Vimeo 플레이어 이벤트에서 Google Tag Manager 이벤트로 번역하는 커스텀 스크립트를 추가해야 합니다. 로그인한 후 https://vimeo.com/settings/로 이동하세요. 마케팅 탭 맨 아래에 트래킹 코드 및 트래킹하고자 하는 페이지에 스크립트를 추가하는 방법이 있습니다.

출처 - https://vimeo.zendesk.com/hc/ko/articles/115002859607-Google-Tag-Manager%EC%99%80-%EC%97%B0%EB%8F%99%ED%95%98%EA%B8%B0

## 2 단계: Vimeo 이벤트에 대한 변수 생성
Google Tag Manager 계정에서 다음 데이터 레이어 값의 각 GTM의 '변수' 섹션에서 새 사용자 지정 변수를 생성합니다.

- event_category (항상 ‘Video’)
- event_action (3 단계에 나열된 이벤트 중 하나)
- event_label (동영상 제목 + 동영상 ID. 예: 'My Vimeo Video | 78934')
이 데이터 레이어에 대한 변수를 이미 생성한 경우 해당 변수를 재사용해도 됩니다.

## 3 단계: 트래킹하려는 Vimeo 이벤트에 대한 트리거 생성
Vimeo에서 제공하는 모든 플레이어 트래킹 이벤트에 대한 새 트리거를 생성할 수 있습니다.
![https://help.vimeo.com/hc/en-us/article_attachments/115006061968/GA.png](https://help.vimeo.com/hc/en-us/article_attachments/115006061968/GA.png)

아래 그림은 재생 이벤트를 트래킹하는 트리거의 예입니다. 또한 다음 이벤트들도 모두 트래킹할 수 있습니다:
- loadprogress - 25%
- progress - 50%
- progress - 75%
- progress - 100%
- 이메일 수집

![https://help.vimeo.com/hc/en-us/article_attachments/115006063468/GA6.png](https://help.vimeo.com/hc/en-us/article_attachments/115006063468/GA6.png)

## 4 단계: 트리거를 GTM 태그와 연결