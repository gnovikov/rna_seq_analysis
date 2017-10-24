import sys
sys.path.append('/Users/maayanlab/Desktop/projects/rna_seq_analysis/scripts')
sys.path.append('/Users/maayanlab/Desktop/projects/rna_seq_analysis/gloriascripts')
import pandas as pd
import archs4
import numpy as np
import nbformat
import textwrap

nb=nbformat.v4.new_notebook()




rawcount_dataframe,sample_title_dict = archs4.fetch_dataset('GSE86956_GPL16791')

group_dataframe=pd.DataFrame()

group_dataframe_list=sample_title_dict.values()

group_dataframe['treatment']=pd.Series(sample_title_dict.get(v) for v in rawcount_dataframe.columns)
group_dataframe['treatment']=pd.Series(v.split('_')[2] for v in group_dataframe['treatment'])

group_dataframe.index=pd.Series(sample_title_dict.get(v) for v in rawcount_dataframe.columns)
group_dataframe.index=pd.Series(v.split('(GSM')[0] for v in group_dataframe.index)
group_dataframe.index=pd.Series(v.split('_')[2:4] for v in group_dataframe.index)
group_dataframe.index =pd.Series(' '.join(x) for x in group_dataframe.index.tolist())

rawcount_dataframe.columns=group_dataframe.index
indices=rawcount_dataframe[(rawcount_dataframe.mean(axis=1)<=1)].index
rawcount_dataframe=rawcount_dataframe.drop(rawcount_dataframe.index[rawcount_dataframe.mean(axis=1)<=1])

norm_dataframe=pd.DataFrame()
norm_dataframe=rawcount_dataframe

#cpm normalizing the columns

cpm_factors=rawcount_dataframe.sum(axis=0)/1000000
for i in range(0,rawcount_dataframe.shape[1]):
    norm_dataframe.iloc[:,i]=rawcount_dataframe.iloc[:,i]/cpm_factors[i]

#z score normalize the rows

from scipy import stats
for rows in range(0,rawcount_dataframe.shape[0]):
    norm_dataframe.iloc[rows,:] = stats.zscore(rawcount_dataframe.iloc[rows,:])

from sklearn.decomposition import PCA
pca_3=PCA(n_components=3)
pca_3.fit_transform(norm_dataframe)

import customplot

customplot.plot_3d_scatter(pca_3.components_[0],pca_3.components_[1],pca_3.components_[2], size=5, color_by=group_dataframe['treatment'].tolist(),
                xlab= 'PC1 ({:.2%} of variance explained)'.format(pca_3.explained_variance_ratio_[0]),
                ylab= 'PC2 ({:.2%} of variance explained)'.format(pca_3.explained_variance_ratio_[1]),
                zlab= 'PC3 ({:.2%}of variance explained)'.format(pca_3.explained_variance_ratio_[2])
                          )
