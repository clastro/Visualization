from sklearn.model_selection import GroupShuffleSplit
from matplotlib.patches import Patch

X = df_train.drop(['label'],1) # ExampleData
y = df_train['label'] # ExampleData


n_folds = 5
fig, ax1 = plt.subplots(figsize = (12, 8))
mean_tpr = 0.0
mean_fpr = np.linspace(0, 1, 100)
gss = GroupShuffleSplit(n_splits=n_folds, test_size=0.2, random_state=0)


cmap_data = plt.cm.Paired
cmap_cv = plt.cm.coolwarm
n_splits = 5

def plot_cv_indices(cv, X, y, group, ax, n_splits, lw=10):
    """Create a sample plot for indices of a cross-validation object."""

    # Generate the training/testing visualizations for each CV split
    for ii, (tr, tt) in enumerate(cv.split(X=X, y=y, groups=group)):
        # Fill in indices with the training/test groups
        indices = np.array([np.nan] * len(X))
        indices[tt] = 1
        indices[tr] = 0

        # Visualize the results
        ax.scatter(
            range(len(indices)),
            [ii + 0.5] * len(indices),
            c=indices,
            marker="_",
            lw=lw,
            cmap=cmap_cv,
            vmin=-0.2,
            vmax=1.2,
        )

    # Plot the data classes and groups at the end
    ax.scatter(
        range(len(X)), [ii + 1.5] * len(X), c=y, marker="_", lw=lw, cmap=cmap_data
    )

    ax.scatter(
        range(len(X)), [ii + 2.5] * len(X), c=group, marker="_", lw=lw, cmap=cmap_data
    )

    # Formatting
    yticklabels = list(range(n_splits)) + ["class", "group"]
    ax.set(
        yticks=np.arange(n_splits + 2) + 0.5,
        yticklabels=yticklabels,
        xlabel="Sample index",
        ylabel="CV iteration",
        #ylim=[n_splits + 2.2, -0.2],
        #xlim=[0, 100],
    )
    ax.legend(
        [Patch(color=cmap_cv(0.8)), Patch(color=cmap_cv(0.02))],
        ["Validation set", "Training set"],
        loc=(1.02, 0.8),
    )
    ax.set_title("{}".format(type(cv).__name__), fontsize=10)
    return ax
    
    
fig, ax = plt.subplots()
cv = GroupShuffleSplit(n_splits=n_folds, test_size=0.2, random_state=0)
plot_cv_indices(cv, X, y, grouped, ax, n_splits)

plt.show()
