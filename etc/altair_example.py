# 'Group'과 'Original_Group'을 결합하여 새로운 열 'Group_Original' 생성
month_group['Group_Change'] =  month_group['Original_Group'] + ','  + month_group['Group'] 

# Altair로 시각화
chart = al.Chart(month_group).mark_line().encode(
    x='Year_Month:T',
    y='Average_Frequency:Q',
    color='Group_Original:N',  # 새로운 열을 색상으로 구분
).properties(
    title='Average Frequency by (Original Group, Group) over Time'
)

# 시각화 출력
chart.show()
