import eel
import desktop
import search
import json
from io import StringIO

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
def kimetsu_search(word):
    source = search.kimetsu_search(word)
    print("source->")
    print(source)
    sourcejson=json.dumps(source)
    print("sourcejson->")
    print(sourcejson)
    eel.view_log_js(sourcejson)


#HTML表示
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)



