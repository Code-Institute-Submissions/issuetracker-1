{"filter":false,"title":"urls.py","tooltip":"/accounts/urls.py","undoManager":{"mark":10,"position":10,"stack":[[{"start":{"row":0,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":["from django.conf.urls import url, include","from accounts.views import logout, login, registration, user_profile","from accounts import url_reset","","urlpatterns = [","    url(r'^logout/', logout, name=\"logout\"),","    url(r'^login/', login, name=\"login\"),","    url(r'^register/', registration, name=\"registration\"),","    url(r'^profile/', user_profile, name=\"profile\"),","    url(r'^password-reset/', include(url_reset))","]"],"id":1}],[{"start":{"row":2,"column":5},"end":{"row":2,"column":13},"action":"remove","lines":["accounts"],"id":2}],[{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"remove","lines":[" "],"id":3},{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"remove","lines":["m"]},{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"remove","lines":["o"]},{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"remove","lines":["r"]},{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"remove","lines":["f"]}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"remove","lines":[" "],"id":4}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["f"],"id":5},{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":["r"]},{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":["o"]},{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":[" "],"id":6},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["a"]},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["c"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["c"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["o"]},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["u"]},{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["n"]},{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"insert","lines":["t"]},{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":[" "],"id":7}],[{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["$"],"id":8}],[{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["$"],"id":9}],[{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"insert","lines":["$"],"id":10}],[{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"insert","lines":["$"],"id":11}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":10,"column":1},"end":{"row":10,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1602663880195,"hash":"d993aafbb8110cb5114cfae2b5fdc1a1219f125f"}