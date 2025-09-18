import seaborn as sns

tips = sns.load_dataset("tips")

total_lower = tips.total_bill.min()
total_upper = tips.total_bill.max()
time_selected = tips.time.unique().tolist()

idx1 = tips.total_bill.between(
    left=total_lower,
    right=total_upper,
    inclusive="both",
)

idx2 = tips.time.isin(time_selected)

tips_filtered = tips[idx1 & idx2]
tips_filtered.shape
