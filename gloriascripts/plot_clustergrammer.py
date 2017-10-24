def display(dataframe, normalize=True, filter_rows=True, n_rows=500):
    
        from clustergrammer_widget import *
        net=Network(clustergrammer_widget)

        #Loading the Dataframe

        net.load_df(dataframe)

        #Z-score normalizing the rows
        if normalize:
                net.normalize(axis='row', norm_type='zscore', keep_orig=True)

        #Filtering top 500 genes by variance
        if filter_rows:
                net.filter_N_top('row',n_rows,'var')

        #Clustering the heatmap

        net.cluster()

        #Display

        return net.widget()
