import math
import folium
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium

# 앱 제목 설정
st.title("🚇 부산 지하철 역별 이용객 수 지도 분석")

# 1. CSV 파일 업로드
uploaded_file = st.file_uploader("busan_subway.csv 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    # 데이터 불러오기
    df = pd.read_csv(uploaded_file)

    # ----------------------------------------------------
    # 호선별 색상 지정 함수 (1호선: 주황, 2호선: 초록, 3호선: 갈색, 4호선: 파랑)
    # ----------------------------------------------------
    def get_line_color(line_name):
        line_str = str(line_name)  # 숫자로 들어올 경우를 대비해 문자열로 변환
        if "1" in line_str:
            return "#F26A36"  # 주황색
        elif "2" in line_str:
            return "#3CB44A"  # 초록색
        elif "3" in line_str:
            return "#BB8C40"  # 갈색
        elif "4" in line_str:
            return "#2A72B5"  # 파랑색
        else:
            return "#808080"  # 기타 호선은 회색

    # ----------------------------------------------------
    # 호선 필터 (multiselect)
    # ----------------------------------------------------
    # 데이터에 존재하는 호선 목록 추출
    available_lines = sorted(df["호선"].unique().tolist())

    # 사용자로부터 보여줄 호선 선택받기 (기본값: 전체 선택)
    selected_lines = st.multiselect(
        "조회할 호선을 선택하세요:", options=available_lines, default=available_lines
    )

    # 선택한 호선에 해당하는 데이터만 필터링
    filtered_df = df[df["호선"].isin(selected_lines)]

    # ① 전체 데이터 표로 보여주기
    st.subheader("📊 전체 데이터")
    st.dataframe(df)

    # ----------------------------------------------------
    # 이용객 상위 5개 역 표 표시 (필터링된 데이터 기준)
    # ----------------------------------------------------
    st.subheader("🏆 이용객 상위 5개 역")
    top5_df = filtered_df.sort_values(by="이용객수", ascending=False).head(5)
    # 필요한 열만 보기 좋게 출력
    st.dataframe(
        top5_df[["호선", "역명", "이용객수"]].reset_index(drop=True)
    )

    # ----------------------------------------------------
    # ②, ③ Folium 지도 생성 및 마커 추가
    # ----------------------------------------------------
    # 지도 중심을 부산 시청 근처(35.1796, 129.0756)로 설정
    m = folium.Map(location=[35.1796, 129.0756], zoom_start=11)

    # 선택된 호선의 역들만 지도에 원형 마커(CircleMarker)로 표시
    for index, row in filtered_df.iterrows():
        # 이용객 수의 제곱근에 비례하도록 반지름 계산
        radius_size = math.sqrt(row["이용객수"]) * 0.15

        # 호선별 색상 가져오기
        line_color = get_line_color(row["호선"])

        # 지도에 원형 마커 그리기
        folium.CircleMarker(
            location=[row["위도"], row["경도"]],  # 역 위도, 경도
            radius=radius_size,  # 계산된 반지름 크기
            tooltip=f"[{row['호선']}] {row['역명']}",  # 마우스 올렸을 때: [호선] 역명
            popup=f"<b>{row['역명']}</b><br>이용객 수: {row['이용객수']:,}명",  # 클릭했을 때: 이용객 수
            color=line_color,  # 테두리 색상
            fill=True,  # 채우기
            fill_color=line_color,  # 내부 채우기 색상
            fill_opacity=0.6,  # 투명도
        ).add_to(m)

    # Streamlit 화면에 folium 지도 표시하기
    st.subheader("🗺️ 역별 이용객 수 지도")
    st_folium(m, width=700, height=500)

else:
    st.info("💡 CSV 파일을 업로드하면 지도가 표시됩니다.")