# Introduction

> what Google Tag Manager was anyway? What’s the difference between Google Analytics events and GTM events?
도대체 Googla Analytics event와 GTM event의 차이가 무엇인가?


## Google Analytics In a Nutshell - GA 한줄요약
Google Analytics’ main purpose is generating reports and statistics about your website, for example:
GA의 주된 목적은 레포트 만들고 웹사이트에 대한 통계자료를 생성하는 것이다. 가령,
- how many people visited your website yesterday.
얼마나 많은 사람들이 어제 웹사이트에 들어왔는지

- what country are they from.
어떤나라의 사람들이왔는지

- how many pages they visited per session.
한 세션에 얼마나 많은 페이지를 방문했는지

- how many visitors bounced off your website (without performing any action).
얼마나 많은 사람들이 아무것도 안하고 웹사이트에서 튕겨나갔는지

- which pages were the most popular, etc.
어떤 페이지가 가장 인기있는지 등

## Google Tag Manager

> However, you may want to track how many people use a specific feature on your website/app. Or maybe you are interested in tracking sales, huh? In this case, you’ll need to add custom tags – Google Analytics events which send the data only when a visitor completes a particular action on your website. A good example here could be a form submission.
하지만, 만약 웹사이트의 특정 기능을 얼마나 많은 사람들이 사용하는지 궁금해하는 경우가 있을 수 있습니다. 이 경우 custom tag들이 필요한데, Google Analytics는 방문자가 특정 행동을 완료했을때만 event가 발생됩니다. form 제출이 가장 대표적인 사례죠.

> So what do you do here? Ask the developer to add that form submission tracking tag to a website, right? But what happens when there are tens or hundreds of interactions you are willing to track with Google Analytics?
여기서 우린, 보통 개발자들한테 form 제출을 트래킹해달라고 부탁하곤 하죠. 그런데, Google Analytics로 추적하고 싶은 interaction이 수백개 수천개면 어떻게 하죠?

그래서 필요한 것이 Google Tag Manager라고 합니다.

출처 - https://www.analyticsmania.com/post/google-tag-manager-vs-google-analytics/