import pandas as pd
from chembl_webresource_client.new_client import new_client

target = new_client.target
target_query = target.search("coronavirus")
targets = pd.DataFrame.from_dict(target_query)
#print(targets)

selected_target = targets.target_chembl_id[4]
#print(selected_target)

activity = new_client.activity
res = activity.filter(target_chembl_id=selected_target).filter(standard_type="IC50")
res_df = pd.DataFrame.from_dict(res)
#print(res_df)

#res_df.to_csv('bioactivity_data.csv', index=False)

csvfile = pd.read_csv('bioactivity_data.csv')

print (csvfile.head)

data = res_df[res_df.standard_value.notna()]

#####

bioactivity_class = []
for i in data.standard_value:
    if float(i) >= 10000:
        bioactivity_class.append("inactive")
    elif float(i) <= 1000:
        bioactivity_class.append("active")
    else:
        bioactivity_class.append("intermediate")

mol_cid = []
for i in data.molecule_chembl_id:
    mol_cid.append(i)