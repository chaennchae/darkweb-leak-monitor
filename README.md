# darkweb-leak-monitor

Tor 네트워크 기반으로 .onion 도메인을 수집하고, 유출 관련 키워드를 분석하여 위험도를 산정한 뒤
실시간 알림 및 HTML 리포트를 생성하는 자동화 모니터링 시스템

## Stack
- Python
- Tor Network
- MongoDB
- Telegram Bot

## 프로젝트 목적
- 다크웹 내 데이터 유출 정황 탐지
- 자동화된 위험도 분석
- 실시간 알림 제공
- 시각화된 리포트 생성
- 주기적 자동 실행 시스템 구축

## 주요 기능
- Tor 기반 .onion 크롤링
- URL 자동 확장 (Frontier 시스템)
- 키워드 기반 유출 탐지
- Risk Score 계산
- Severity 등급 분류 (Low / Medium / High)
- Telegram 실시간 알림
- Top 10 위험 도메인 HTML 리포트 생성
- Windows 작업 스케줄러 자동화

## 리포트 결과

- 위험 점수 기준 상위 10개 도메인 정렬
- 위험도 등급 표시
- HTML 대시보드 형태 출력

## Sample Report Output

아래는 테스트 환경에서 실행한 리포트 예시입니다.
<img width="2493" height="948" alt="image" src="https://github.com/user-attachments/assets/c8c9e434-a3b0-4b7e-8fa2-fdafa5f852c1" />


