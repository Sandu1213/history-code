for i in range(5):
    print(i)
siteInfo = [{"name":"1","address":"add"},{"name":"2","address":"cc"}]
for index, infos in enumerate(siteInfo):
    print("NO." +str(index+1) + ":" + infos['name'] + infos['address']);