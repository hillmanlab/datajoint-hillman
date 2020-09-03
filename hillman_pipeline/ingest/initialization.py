import datajoint as dj
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lab, microscopy, organism, setup, experiment

# lab.Lab
data = [
  {'lab': 'Hillmanlab', 'lab_description': ''},
]
lab.Lab.insert(data,skip_duplicates=True)

# lab.LabMember
data = [
    {'user':'Boss','lab':'Hillmanlab'},
    {'user':'Sam_Benezra','lab':'Hillmanlab'},
    {'user':'Wenze_Li','lab':'Hillmanlab'},
    {'user':'Wenxuan_Liang','lab':'Hillmanlab'},
    {'user':'Malte_Casper','lab':'Hillmanlab'},
    {'user':'Grace_Lee','lab':'Hillmanlab'},
    {'user':'Elizabeth_Malan','lab':'Hillmanlab'},
    {'user':'Kripa_Patel','lab':'Hillmanlab'},
    {'user':'Nic_Thibodeaux','lab':'Hillmanlab'},
    {'user':'Weihao_Xu','lab':'Hillmanlab'},
    {'user':'Richard_Yan','lab':'Hillmanlab'},
    {'user':'Hang_Yu','lab':'Hillmanlab'},
    {'user':'Teresa_Zhao','lab':'Hillmanlab'},
    {'user':'Chinwendu_Nwokeabia','lab':'Hillmanlab'},
    {'user':'Citlali_Campos','lab':'Hillmanlab'},
    {'user':'Alexis_Yagielski','lab':'Hillmanlab'},
]
lab.LabMember.insert(data,skip_duplicates=True)

# lab.project
data = [
    {'project':'NeuroPal','user':'Richard_Yan'},
    {'project':'Kimara Heart','user':'Richard_Yan'},
]
lab.Project.insert(data,skip_duplicates=True)

# microscopy.ScapeSystem
data = [
    {'scape_name','Super SCAPE','person_in_charge','Wenze_Li'},
    {'scape_name','Yan SCAPE','person_in_charge','Richard_Yan'},
    {'scape_name','Meso SCAPE','person_in_charge','Grace_Lee'},
    {'scape_name','2P SCAPE','person_in_charge','Hang_Yu'},
]
microscopy.ScapeSystem.insert(data,skip_duplicates=True)

# microscopy.Laser
data = [
    {}
]
