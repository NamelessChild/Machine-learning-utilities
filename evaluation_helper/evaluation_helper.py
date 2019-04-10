from sklearn.model_selection import learning_curve
import numpy as np

def plot_learning_curve(estimator, X, y, axe, cv, train_sizes = np.linspace(.1,1,5), n_jobs=-1):
    train_sizes, train_scores, val_scores = learning_curve(estimator, X, y, cv=cv, n_jobs=n_jobs,
                                                            train_sizes=train_sizes)
    # compute the mean and std in order to plot them
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    val_scores_mean = np.mean(val_scores, axis=1)
    val_scores_std = np.std(val_scores, axis=1)
    
    axe.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1, color='red')
    axe.fill_between(train_sizes, val_scores_mean - val_scores_std,
                     val_scores_mean + val_scores_std, alpha=0.1, color='green')
    axe.plot(train_sizes, train_scores_mean, 'o-', color="black", label="training score")
    axe.plot(train_sizes, val_scores_mean, 'o-', color="blue", label="validation score")
    axe.set_title(estimator.__class__.__name__)
    axe.set_xlabel('Training sizes')
    axe.set_ylabel('Scores')
    axe.grid(True)
    axe.legend(loc='best')
