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

## 시스템 아키텍처
Tor 크롤러
    ↓
URL 수집 및 확장
    ↓
키워드 분석
    ↓
위험 점수 계산
    ↓
위험도 분류
    ↓
Telegram 알림
    ↓
HTML 리포트 생성

## 프로젝트 구조
darkweb-leak-monitor/
│
├── crawler/              # Tor 크롤러 모듈
├── utils/                # URL 저장 및 관리
├── report/               # HTML 리포트 생성기
├── data/                 # visited 데이터
├── reports/              # 생성된 리포트 저장
├── run_pipeline.py       # 전체 파이프라인 실행 스크립트

## 리포트 결과

- 위험 점수 기준 상위 10개 도메인 정렬
- 위험도 등급 표시
- HTML 대시보드 형태 출력
