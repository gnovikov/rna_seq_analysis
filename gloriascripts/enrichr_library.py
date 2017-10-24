def data(gene_set_library,user_list_id_up,user_list_id_dn):
    import json
    import requests
    import pandas as pd
    ENRICHR_URL = 'http://amp.pharm.mssm.edu/Enrichr/enrich'
    query_string = '?userListId=%s&backgroundType=%s'
    response_up = requests.get(
    ENRICHR_URL + query_string % (user_list_id_up, gene_set_library)
     )
    response_dn = requests.get(
    ENRICHR_URL + query_string % (user_list_id_dn, gene_set_library)
    )
    data_up=pd.DataFrame()
    data_dn=pd.DataFrame()
    if not response_up.ok:
        raise Exception('Error fetching enrichment results')
        
    data_up = json.loads(response_up.text)
    result_dataframe_up=pd.DataFrame(data_up[gene_set_library])
       
    if not response_dn.ok:
        raise Exception('Error fetching enrichment results')
        
    data_dn = json.loads(response_dn.text)
    result_dataframe_dn=pd.DataFrame(data_dn[gene_set_library])
    return result_dataframe_up,result_dataframe_dn
