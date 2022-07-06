weather=[
    {"district": "tvm", "temp":30},
    {"district": "ktm","temp":28 },
    {"district": "apy","temp":27},
    {"district": "idk","temp":18 },
    {"district": "ekm","temp":31 },
    {"district": "pta","temp":21},
    {"district": "tsr","temp":24},
    {"district": "kzd","temp":29},
    {"district": "pkd","temp":34},
    {"district": "mpm","temp":31},
    {"district": "tvm", "temp": 31},
    {"district": "ktm", "temp": 29},
    {"district": "apy", "temp": 26},
    {"district": "idk", "temp": 20},
    {"district": "ekm", "temp": 30},
    {"district": "pta", "temp": 22},
    {"district": "tsr", "temp": 27},
    {"district": "kzd", "temp": 28},
    {"district": "pkd", "temp": 30},
    {"district": "mpm", "temp": 29},

]
 #1  #out={"tvm":31,"ktm":29,}  #output pole dict akkenam

out={}  #oru empty dict create chythu
for data in weather: #data={"district":"tvm","temp":30}   (weather il ah data undo enne check chtythu)
    dict_name=data["district"]  #tvm  (avishyam ulla pole thannirukkunna question il ninne data eduthu,key value veche)
    cur_temp=data["temp"]   #30
    if dict_name in out:  #(out il dict undo enne check chythu)
        old_temp=out[dict_name]  #old temp value store chythekkunnathe dict_name key il ane so athe old_temp il assign chythu
        if cur_temp>old_temp:   #(puthiya temp pazhaya temp inekkal valuthe ano enne check cheyyummu)
            out[dict_name]=cur_temp  #(dist_name value ayi curent temp store chythu
    else:
        out[dict_name]=cur_temp  #dict_name key ayitte edukkummu value temp
print(out)



#2 # sort out based on temparature

srt_out=sorted(out.items(),key=lambda item:item[1],reverse=True)
print(srt_out)


# find max tem district

# find min tem district

# dictionary methods