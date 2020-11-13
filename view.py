import eel
import desktop
import search

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
def kimetsu_search(word):
    search.kimetsu_search(word)

@ eel.expose
def view_log_js(word):
    eel.viewlogjs(word)

#HTML表示    
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)



