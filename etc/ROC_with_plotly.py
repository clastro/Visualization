from sklearn.metrics import roc_curve
fpr, tpr, thresholds = roc_curve(y_test, pro[:,1])
import plotly.express as px

# The histogram of scores compared to true labels
fig_hist = px.histogram(
    x=pro[:,1], color=y_test, nbins=2000,
    labels=dict(color='True Labels', x='Score')
)

fig_hist.show()

# Evaluating model performance at various thresholds
df = pd.DataFrame({
    'False Positive Rate': fpr,
    'True Positive Rate': tpr
}, index=thresholds)
df.index.name = "Thresholds"
df.columns.name = "Rate"

fig_thresh = px.line(
    df, title='TPR and FPR at every threshold',
    width=3700, height=3100
)

fig_thresh.update_yaxes(scaleanchor="x", scaleratio=1)
fig_thresh.update_xaxes(range=[0, 1], constrain='domain')
fig_thresh.show()
