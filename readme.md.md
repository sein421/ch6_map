# 🚇 부산 지하철 역별 이용객 수 지도 분석 앱 (Busan Subway Map App)

Streamlit과 Folium을 활용하여 부산 지하철 역별 이용객 수 데이터를 시각화하고 분석하는 웹 애플리케이션입니다. 

---

## 📌 주요 기능 (Features)

1. **데이터 업로드 및 확인**: `busan_subway.csv` 파일을 업로드하여 전체 지하철 역 데이터 표 확인
2. **호선별 필터링**: `multiselect`를 통해 원하는 호선(1~4호선)만 선택하여 지도에 표시
3. **호선별 색상 구분**: 
   - 🟠 **1호선**: 주황색 (`#F26A36`)
   - 🟢 **2호선**: 초록색 (`#3CB44A`)
   - 🟤 **3호선**: 갈색 (`#BB8C40`)
   - 🔵 **4호선**: 파랑색 (`#2A72B5`)
4. **인터랙티브 지도 시각화**:
   - 이용객 수의 제곱근에 비례하는 크기의 원형 마커(CircleMarker) 표시
   - 마우스 호버 시 역명 확인 (Tooltip)
   - 마커 클릭 시 이용객 수 확인 (Popup)
5. **이용객 상위 5개 역 표기**: 선택한 호선 기준 이용객 수가 가장 많은 상위 5개 역 데이터 표시

---

## 🛠️ 기술 스택 (Tech Stack)

- **Language**: Python 3.x
- **Web Framework**: Streamlit
- **Data Processing**: Pandas
- **Map Visualization**: Folium, streamlit-folium

---

## 📁 프로젝트 구조 (Project Structure)

```text
.
├── app.py              # 메인 Streamlit 애플리케이션 코드
├── busan_subway.csv    # 지하철 역 데이터 (호선, 역명, 위도, 경도, 이용객수)
├── requirements.txt    # 의존성 라이브러리 목록
└── README.md           # 프로젝트 안내 문서
```

---

## 🚀 실행 방법 (How to Run)

### 1. 저장소 복제 (Clone)
```bash
git clone https://github.com/사용자이름/저장소이름.git
cd 저장소이름
```

### 2. 필요한 라이브러리 설치
```bash
pip install -r requirements.txt
```

### 3. Streamlit 앱 실행
```bash
streamlit run app.py
```

---

## 📊 CSV 데이터 형식 예시 (`busan_subway.csv`)

| 호선 | 역명 | 위도 | 경도 | 이용객수 |
| :--- | :--- | :--- | :--- | :--- |
| 1호선 | 서면 | 35.1578 | 129.0592 | 85000 |
| 2호선 | 해운대 | 35.1637 | 129.1585 | 42000 |
