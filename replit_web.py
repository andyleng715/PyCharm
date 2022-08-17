"""
參考Youtube用repl.it做一個簡單的網站，並利用Database
https://www.youtube.com/watch?v=9yU-lj20zd4
"""

from replit import web
import flask

app = flask.Flask(__name__)
users = web.UserStore()


@app.route("/")
@web.authenticated
def index():
    # name_list = ["王凱","Nill","Hello","World"]

    hits = users.current.get("hits", 0) + 1
    users.current["hits"] = hits
    user_name = "BillCash"
    users.current["user_name"] = user_name
    # return str(name_list)+"\n"+

    note = """參考Youtube用repl.it做一個簡單的網站，並利用Database
  <a href ="https://www.youtube.com/watch?v=9yU-lj20zd4">做網站</a>"""
    return "<H1>你到訪過" + str(hits) + "次 </H1><br>" + "<H2>" + str(user_name) + "</H2><br>" + note


web.run(app)
