import matplotlib.pyplot as plt
import numpy as np

# 데이터
num_samples = 6
num_attributes = 12

# X 축 레이블
x_labels = ['R amplitude mean','R amplitude max','RR interval min','QQ interval min','SS interval min','TT interval min']

# 막대 그래프에 사용될 색상
colors = plt.cm.tab20(np.linspace(0, 1, num_attributes))

cumulative = np.zeros(num_samples)

# 누적 막대 그래프 그리기
fig, ax = plt.subplots(figsize=(14, 14), dpi=500) 
Leads = ['I','II','III','aVR','aVL','aVF','V1','V2','V3','V4','V5','V6']
for i,lead in enumerate(Leads):
    ax.bar(x_labels, data_array[:, i], bottom=cumulative, color=colors[i], label=f'{lead}')
    for j, value in enumerate(data_array[:, i]):
        if value > 10:  # 임계값 설정
            ax.text(j, cumulative[j] + value / 2, f'{value:.2f}', ha='center', va='center', fontsize=8, color='white')
    cumulative += data_array[:, i]

# 각 열의 합 계산
column_sum = np.sum(data_array, axis=1)

# 각 열의 합을 막대 그래프 위에 검정색으로 표시
for i, value in enumerate(column_sum):
    ax.text(i, np.sum(column_sum[i]), f'{value:.2f}', ha='center', va='bottom', fontsize=9, color='black')

# 그래프 스타일과 레이아웃 설정
plt.title('Serial ECG Model ANOVA', fontsize=16)
plt.xlabel('Features', fontsize=14)
plt.ylabel('F-Value', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# 범례
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], loc='upper left', fontsize=9)

# 그래프 표시
plt.tight_layout()
plt.savefig('serial_ecg_anova.png')
plt.show()
