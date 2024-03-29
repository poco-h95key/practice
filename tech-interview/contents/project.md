# 1. Project
**:book: Contents**
* [NH은행/상호금융 전자창구 PPR 구축 프로젝트](#NH은행/상호금융-전자창구-PPR-구축-프로젝트)
* [NH선물 차세대 프로젝트](#NH선물-차세대-프로젝트)
---

### NH은행/상호금융 전자창구 PPR 구축 프로젝트
* 기간 : 은행(2020.10-01 - 2021.06.12) , 상호금융(2021.10.01 - 진행중)
* 사용언어 : java, Oracle, javascript
* 프레임워크 : ProObject, Istudio(MCA전문 프레임워크), ezbuilder(농협공통화면개발툴)
* 프로젝트 소개 : 영업점에서 발생하는 종이문서를 전자화하여 고객이 전자서식을 작성하고 각 업무(수신,여신,카드,외환 등)를 진행하기 위한 프로젝트
* 개발내역 : NH은행 전자창구
  * 서비스/화면 : 공통코드관리, 카드 업무 이수관, 컨텐츠관리
  * 배치 : 근태관리배치, 신주소등록배치, 컨텐츠관리배치
  * 인터페이스 : CDD/EDD여부 조회 EAI
* 개발내역 : 상호금융 전자창구
  * 서비스/화면 : 처리내역조회(수신/여신/카드/ODS), 미처리내역조회, 업무취소/업무복구, 내부전표 정정/정정취소/결재, 공통코드관리
    * ODS : 태블릿으로 들어온 서식을 말한다. AS-IS에 해당하는 경우인데 즉시거래가 가능한 서식인 경우 ODS로 들어온 건은 바로 서버에 저장된다.
  * 인터페이스 : 카드 제휴코드 조회 GGW, 카드 고객정보 조회 GGW, 전자창구 서식리스트 조회 EAI
### NH선물 차세대 프로젝트(지원)
* 기간 : 2021.06.14 - 2021.09.30
* 사용언어 : C, Oracle, Python
* 프레임워크 : ProFrame, FormDesigner(화면 툴)
* 프로젝트 소개 : NH선물 HTS 차세대 구축으로 백오피스 화면 및 보고서 개발 담당
* 개발내역
  * 서비스/화면 : 잔고매매원장 조회, 위탁매매계좌 상위 수익률 조회, 실전투자대회
  * 보고서 : 클립소프트 연동 jsp 및 화면 공통함수 개발
