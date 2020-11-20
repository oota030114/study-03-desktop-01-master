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
    sourcejson=json.dumps(source, ensure_ascii=False)
    # print("sourcejson->")
    # print(sourcejson)

    # source_list = list(enumerate(source))
    # adr_dict = dict(source_list)

    # print("source_list->")
    # print(source_list)
    # dic = {key: val for key, val in source_list}

    # print("dic->")
    # print(dic)
    # sourcejson=json.dumps(dic, ensure_ascii=False)
    eel.view_log_js(sourcejson)

#HTML表示
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)



