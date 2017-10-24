def upperGenes(genes):
    return [gene.upper() for gene in genes]
def small_molecule_query(upgenes,dngenes,mimic):
    import requests
    import json
    url = 'http://amp.pharm.mssm.edu/L1000CDS2/query'
    
    data = {"upGenes":upgenes,
    "dnGenes":dngenes}
    data['upGenes'] = upperGenes(data['upGenes'])
    data['dnGenes'] = upperGenes(data['dnGenes'])
    config = {"aggravate":mimic,"searchMethod":"geneSet","share":True,"combination":True,"db-version":"latest"}
    metadata = [{"key":"Tag","value":"gene-set python example"},{"key":"Cell","value":"MCF7"}]
    payload = {"data":data,"config":config,"meta":metadata}
    headers = {'content-type':'application/json'}
    r = requests.post(url,data=json.dumps(payload),headers=headers)
    resGeneSet = r.json()
    result_url = 'http://amp.pharm.mssm.edu/L1000CDS2/#/result/{shareId}'.format(**resGeneSet)
    
    return result_url,resGeneSet                
