import eel
import desktop
import search
import json
from io import StringIO

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
def kimetsu_search(word, saveFolder):
    if saveFolder[-1]=='/':
        saveFile=saveFolder + "source.csv"
    else:
        saveFile=saveFolder + "/source.csv"
    
    source = search.kimetsu_search(word, saveFile)
    str = ','.join(source)
    sourcejson=json.dumps(str, ensure_ascii=False)
    eel.view_log_js(sourcejson)

#HTML表示
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)



