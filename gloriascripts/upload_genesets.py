def enrichr(gene_list):
    import json
    import requests
    ENRICHR_URL = 'http://amp.pharm.mssm.edu/Enrichr/addList'
    gene_str = '\n'.join(gene_list)
    description= 'Example gene list'

    payload = {
        'list': (None, gene_str),
        'description': (None, description)
    }

    response = requests.post(ENRICHR_URL, files=payload)
    if not response.ok:
        raise Exception('Error analyzing gene list')

    data = json.loads(response.text)
    enrichr_url = 'http://amp.pharm.mssm.edu/Enrichr/enrich?dataset={shortId}'.format(**data)
    return enrichr_url,data
