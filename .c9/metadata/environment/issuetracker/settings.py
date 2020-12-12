{"filter":false,"title":"settings.py","tooltip":"/issuetracker/settings.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":13,"column":7},"end":{"row":13,"column":10},"action":"remove","lines":["dj_"],"id":218},{"start":{"row":13,"column":7},"end":{"row":13,"column":22},"action":"insert","lines":["dj_database_url"]}],[{"start":{"row":13,"column":22},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":219}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":22},"action":"insert","lines":["import dj_database_url"],"id":220}],[{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"remove","lines":["import dj_database_url",""],"id":221}],[{"start":{"row":26,"column":41},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":222}],[{"start":{"row":27,"column":0},"end":{"row":27,"column":41},"action":"insert","lines":["SECRET_KEY = os.environ.get(\"SECRET_KEY\")"],"id":223}],[{"start":{"row":26,"column":0},"end":{"row":27,"column":0},"action":"remove","lines":["SECRET_KEY = os.environ.get('SECRET_KEY')",""],"id":224}],[{"start":{"row":91,"column":1},"end":{"row":92,"column":0},"action":"insert","lines":["",""],"id":225},{"start":{"row":92,"column":0},"end":{"row":93,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":93,"column":0},"end":{"row":104,"column":5},"action":"insert","lines":["if \"DATABASE_URL\" in os.environ:","    DATABASES = {","        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))","    }","else:","    print(\"Postgres URL not found, using sqlite instead\")","    DATABASES = {","        'default': {","            'ENGINE': 'django.db.backends.sqlite3',","            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","        }","    }"],"id":226}],[{"start":{"row":89,"column":0},"end":{"row":89,"column":2},"action":"insert","lines":["# "],"id":227},{"start":{"row":90,"column":0},"end":{"row":90,"column":2},"action":"insert","lines":["# "]},{"start":{"row":91,"column":0},"end":{"row":91,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":55,"column":61},"end":{"row":56,"column":0},"action":"insert","lines":["",""],"id":228},{"start":{"row":56,"column":0},"end":{"row":56,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":56,"column":4},"end":{"row":56,"column":6},"action":"insert","lines":["''"],"id":229}],[{"start":{"row":56,"column":5},"end":{"row":56,"column":6},"action":"insert","lines":["w"],"id":230},{"start":{"row":56,"column":6},"end":{"row":56,"column":7},"action":"insert","lines":["h"]},{"start":{"row":56,"column":7},"end":{"row":56,"column":8},"action":"insert","lines":["i"]},{"start":{"row":56,"column":8},"end":{"row":56,"column":9},"action":"insert","lines":["t"]},{"start":{"row":56,"column":9},"end":{"row":56,"column":10},"action":"insert","lines":["e"]},{"start":{"row":56,"column":10},"end":{"row":56,"column":11},"action":"insert","lines":["n"]},{"start":{"row":56,"column":11},"end":{"row":56,"column":12},"action":"insert","lines":["o"]},{"start":{"row":56,"column":12},"end":{"row":56,"column":13},"action":"insert","lines":["i"]},{"start":{"row":56,"column":13},"end":{"row":56,"column":14},"action":"insert","lines":["s"]},{"start":{"row":56,"column":14},"end":{"row":56,"column":15},"action":"insert","lines":["e"]},{"start":{"row":56,"column":15},"end":{"row":56,"column":16},"action":"insert","lines":["."]}],[{"start":{"row":56,"column":16},"end":{"row":56,"column":17},"action":"insert","lines":["m"],"id":231},{"start":{"row":56,"column":17},"end":{"row":56,"column":18},"action":"insert","lines":["i"]},{"start":{"row":56,"column":18},"end":{"row":56,"column":19},"action":"insert","lines":["d"]},{"start":{"row":56,"column":19},"end":{"row":56,"column":20},"action":"insert","lines":["d"]},{"start":{"row":56,"column":20},"end":{"row":56,"column":21},"action":"insert","lines":["l"]},{"start":{"row":56,"column":21},"end":{"row":56,"column":22},"action":"insert","lines":["e"]}],[{"start":{"row":56,"column":22},"end":{"row":56,"column":23},"action":"insert","lines":["w"],"id":232},{"start":{"row":56,"column":23},"end":{"row":56,"column":24},"action":"insert","lines":["a"]},{"start":{"row":56,"column":24},"end":{"row":56,"column":25},"action":"insert","lines":["r"]},{"start":{"row":56,"column":25},"end":{"row":56,"column":26},"action":"insert","lines":["e"]},{"start":{"row":56,"column":26},"end":{"row":56,"column":27},"action":"insert","lines":["."]},{"start":{"row":56,"column":27},"end":{"row":56,"column":28},"action":"insert","lines":["W"]},{"start":{"row":56,"column":28},"end":{"row":56,"column":29},"action":"insert","lines":["h"]},{"start":{"row":56,"column":29},"end":{"row":56,"column":30},"action":"insert","lines":["i"]},{"start":{"row":56,"column":30},"end":{"row":56,"column":31},"action":"insert","lines":["t"]},{"start":{"row":56,"column":31},"end":{"row":56,"column":32},"action":"insert","lines":["e"]}],[{"start":{"row":56,"column":32},"end":{"row":56,"column":33},"action":"insert","lines":["H"],"id":233}],[{"start":{"row":56,"column":32},"end":{"row":56,"column":33},"action":"remove","lines":["H"],"id":234}],[{"start":{"row":56,"column":32},"end":{"row":56,"column":33},"action":"insert","lines":["B"],"id":235}],[{"start":{"row":56,"column":32},"end":{"row":56,"column":33},"action":"remove","lines":["B"],"id":236}],[{"start":{"row":56,"column":32},"end":{"row":56,"column":33},"action":"insert","lines":["N"],"id":237},{"start":{"row":56,"column":33},"end":{"row":56,"column":34},"action":"insert","lines":["o"]},{"start":{"row":56,"column":34},"end":{"row":56,"column":35},"action":"insert","lines":["i"]},{"start":{"row":56,"column":35},"end":{"row":56,"column":36},"action":"insert","lines":["s"]},{"start":{"row":56,"column":36},"end":{"row":56,"column":37},"action":"insert","lines":["e"]}],[{"start":{"row":56,"column":37},"end":{"row":56,"column":38},"action":"insert","lines":["M"],"id":238},{"start":{"row":56,"column":38},"end":{"row":56,"column":39},"action":"insert","lines":["i"]},{"start":{"row":56,"column":39},"end":{"row":56,"column":40},"action":"insert","lines":["d"]},{"start":{"row":56,"column":40},"end":{"row":56,"column":41},"action":"insert","lines":["d"]},{"start":{"row":56,"column":41},"end":{"row":56,"column":42},"action":"insert","lines":["l"]},{"start":{"row":56,"column":42},"end":{"row":56,"column":43},"action":"insert","lines":["e"]},{"start":{"row":56,"column":43},"end":{"row":56,"column":44},"action":"insert","lines":["w"]}],[{"start":{"row":56,"column":44},"end":{"row":56,"column":45},"action":"insert","lines":["a"],"id":239},{"start":{"row":56,"column":45},"end":{"row":56,"column":46},"action":"insert","lines":["r"]},{"start":{"row":56,"column":46},"end":{"row":56,"column":47},"action":"insert","lines":["e"]}],[{"start":{"row":56,"column":48},"end":{"row":56,"column":49},"action":"insert","lines":[","],"id":240}],[{"start":{"row":156,"column":1},"end":{"row":157,"column":0},"action":"insert","lines":["",""],"id":241}],[{"start":{"row":157,"column":0},"end":{"row":157,"column":1},"action":"insert","lines":["S"],"id":242},{"start":{"row":157,"column":1},"end":{"row":157,"column":2},"action":"insert","lines":["T"]},{"start":{"row":157,"column":2},"end":{"row":157,"column":3},"action":"insert","lines":["A"]},{"start":{"row":157,"column":3},"end":{"row":157,"column":4},"action":"insert","lines":["T"]},{"start":{"row":157,"column":4},"end":{"row":157,"column":5},"action":"insert","lines":["I"]},{"start":{"row":157,"column":5},"end":{"row":157,"column":6},"action":"insert","lines":["C"]}],[{"start":{"row":157,"column":6},"end":{"row":157,"column":7},"action":"insert","lines":["_"],"id":243},{"start":{"row":157,"column":7},"end":{"row":157,"column":8},"action":"insert","lines":["R"]},{"start":{"row":157,"column":8},"end":{"row":157,"column":9},"action":"insert","lines":["O"]},{"start":{"row":157,"column":9},"end":{"row":157,"column":10},"action":"insert","lines":["O"]},{"start":{"row":157,"column":10},"end":{"row":157,"column":11},"action":"insert","lines":["T"]}],[{"start":{"row":157,"column":11},"end":{"row":157,"column":12},"action":"insert","lines":[" "],"id":244},{"start":{"row":157,"column":12},"end":{"row":157,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":157,"column":13},"end":{"row":157,"column":14},"action":"insert","lines":[" "],"id":245},{"start":{"row":157,"column":14},"end":{"row":157,"column":15},"action":"insert","lines":["o"]},{"start":{"row":157,"column":15},"end":{"row":157,"column":16},"action":"insert","lines":["x"]},{"start":{"row":157,"column":16},"end":{"row":157,"column":17},"action":"insert","lines":["."]},{"start":{"row":157,"column":17},"end":{"row":157,"column":18},"action":"insert","lines":["p"]},{"start":{"row":157,"column":18},"end":{"row":157,"column":19},"action":"insert","lines":["a"]}],[{"start":{"row":157,"column":19},"end":{"row":157,"column":20},"action":"insert","lines":["t"],"id":246},{"start":{"row":157,"column":20},"end":{"row":157,"column":21},"action":"insert","lines":["h"]},{"start":{"row":157,"column":21},"end":{"row":157,"column":22},"action":"insert","lines":["."]},{"start":{"row":157,"column":22},"end":{"row":157,"column":23},"action":"insert","lines":["j"]},{"start":{"row":157,"column":23},"end":{"row":157,"column":24},"action":"insert","lines":["o"]},{"start":{"row":157,"column":24},"end":{"row":157,"column":25},"action":"insert","lines":["i"]},{"start":{"row":157,"column":25},"end":{"row":157,"column":26},"action":"insert","lines":["n"]}],[{"start":{"row":157,"column":26},"end":{"row":157,"column":28},"action":"insert","lines":["()"],"id":247}],[{"start":{"row":157,"column":27},"end":{"row":157,"column":28},"action":"insert","lines":["B"],"id":248},{"start":{"row":157,"column":28},"end":{"row":157,"column":29},"action":"insert","lines":["A"]},{"start":{"row":157,"column":29},"end":{"row":157,"column":30},"action":"insert","lines":["S"]},{"start":{"row":157,"column":30},"end":{"row":157,"column":31},"action":"insert","lines":["E"]},{"start":{"row":157,"column":31},"end":{"row":157,"column":32},"action":"insert","lines":["_"]}],[{"start":{"row":157,"column":32},"end":{"row":157,"column":33},"action":"insert","lines":["D"],"id":249},{"start":{"row":157,"column":33},"end":{"row":157,"column":34},"action":"insert","lines":["I"]},{"start":{"row":157,"column":34},"end":{"row":157,"column":35},"action":"insert","lines":["R"]},{"start":{"row":157,"column":35},"end":{"row":157,"column":36},"action":"insert","lines":["E"]}],[{"start":{"row":157,"column":35},"end":{"row":157,"column":36},"action":"remove","lines":["E"],"id":250}],[{"start":{"row":157,"column":35},"end":{"row":157,"column":36},"action":"insert","lines":[","],"id":251}],[{"start":{"row":157,"column":36},"end":{"row":157,"column":37},"action":"insert","lines":[" "],"id":252}],[{"start":{"row":157,"column":37},"end":{"row":157,"column":39},"action":"insert","lines":["''"],"id":253}],[{"start":{"row":157,"column":38},"end":{"row":157,"column":39},"action":"insert","lines":["s"],"id":254},{"start":{"row":157,"column":39},"end":{"row":157,"column":40},"action":"insert","lines":["t"]},{"start":{"row":157,"column":40},"end":{"row":157,"column":41},"action":"insert","lines":["a"]},{"start":{"row":157,"column":41},"end":{"row":157,"column":42},"action":"insert","lines":["t"]},{"start":{"row":157,"column":42},"end":{"row":157,"column":43},"action":"insert","lines":["u"]}],[{"start":{"row":157,"column":42},"end":{"row":157,"column":43},"action":"remove","lines":["u"],"id":255}],[{"start":{"row":157,"column":42},"end":{"row":157,"column":43},"action":"insert","lines":["i"],"id":256},{"start":{"row":157,"column":43},"end":{"row":157,"column":44},"action":"insert","lines":["c"]},{"start":{"row":157,"column":44},"end":{"row":157,"column":45},"action":"insert","lines":["f"]},{"start":{"row":157,"column":45},"end":{"row":157,"column":46},"action":"insert","lines":["i"]},{"start":{"row":157,"column":46},"end":{"row":157,"column":47},"action":"insert","lines":["l"]},{"start":{"row":157,"column":47},"end":{"row":157,"column":48},"action":"insert","lines":["e"]},{"start":{"row":157,"column":48},"end":{"row":157,"column":49},"action":"insert","lines":["s"]}],[{"start":{"row":157,"column":15},"end":{"row":157,"column":16},"action":"remove","lines":["x"],"id":257}],[{"start":{"row":157,"column":15},"end":{"row":157,"column":16},"action":"insert","lines":["s"],"id":258}],[{"start":{"row":31,"column":116},"end":{"row":31,"column":117},"action":"insert","lines":[","],"id":259}],[{"start":{"row":31,"column":117},"end":{"row":32,"column":0},"action":"insert","lines":["",""],"id":260}],[{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"insert","lines":["    "],"id":261}],[{"start":{"row":32,"column":4},"end":{"row":32,"column":8},"action":"insert","lines":["    "],"id":262}],[{"start":{"row":32,"column":8},"end":{"row":32,"column":12},"action":"insert","lines":["    "],"id":263}],[{"start":{"row":32,"column":12},"end":{"row":32,"column":16},"action":"insert","lines":["    "],"id":264}],[{"start":{"row":32,"column":12},"end":{"row":32,"column":16},"action":"remove","lines":["    "],"id":265},{"start":{"row":32,"column":8},"end":{"row":32,"column":12},"action":"remove","lines":["    "]},{"start":{"row":32,"column":4},"end":{"row":32,"column":8},"action":"remove","lines":["    "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"remove","lines":["    "]},{"start":{"row":31,"column":117},"end":{"row":32,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":31,"column":117},"end":{"row":31,"column":118},"action":"insert","lines":[" "],"id":266}],[{"start":{"row":31,"column":118},"end":{"row":31,"column":120},"action":"insert","lines":["''"],"id":267}],[{"start":{"row":31,"column":119},"end":{"row":31,"column":120},"action":"insert","lines":["d"],"id":268},{"start":{"row":31,"column":120},"end":{"row":31,"column":121},"action":"insert","lines":["m"]},{"start":{"row":31,"column":121},"end":{"row":31,"column":122},"action":"insert","lines":["-"]}],[{"start":{"row":31,"column":122},"end":{"row":31,"column":123},"action":"insert","lines":["s"],"id":269}],[{"start":{"row":31,"column":122},"end":{"row":31,"column":123},"action":"remove","lines":["s"],"id":270}],[{"start":{"row":31,"column":122},"end":{"row":31,"column":123},"action":"insert","lines":["i"],"id":271},{"start":{"row":31,"column":123},"end":{"row":31,"column":124},"action":"insert","lines":["s"]},{"start":{"row":31,"column":124},"end":{"row":31,"column":125},"action":"insert","lines":["s"]},{"start":{"row":31,"column":125},"end":{"row":31,"column":126},"action":"insert","lines":["u"]},{"start":{"row":31,"column":126},"end":{"row":31,"column":127},"action":"insert","lines":["e"]},{"start":{"row":31,"column":127},"end":{"row":31,"column":128},"action":"insert","lines":["t"]}],[{"start":{"row":31,"column":128},"end":{"row":31,"column":129},"action":"insert","lines":["r"],"id":272}],[{"start":{"row":31,"column":122},"end":{"row":31,"column":129},"action":"remove","lines":["issuetr"],"id":273},{"start":{"row":31,"column":122},"end":{"row":31,"column":134},"action":"insert","lines":["issuetracker"]}],[{"start":{"row":31,"column":134},"end":{"row":31,"column":135},"action":"insert","lines":["."],"id":274},{"start":{"row":31,"column":135},"end":{"row":31,"column":136},"action":"insert","lines":["h"]},{"start":{"row":31,"column":136},"end":{"row":31,"column":137},"action":"insert","lines":["e"]}],[{"start":{"row":31,"column":137},"end":{"row":31,"column":138},"action":"insert","lines":["o"],"id":275},{"start":{"row":31,"column":138},"end":{"row":31,"column":139},"action":"insert","lines":["k"]},{"start":{"row":31,"column":139},"end":{"row":31,"column":140},"action":"insert","lines":["u"]}],[{"start":{"row":31,"column":139},"end":{"row":31,"column":140},"action":"remove","lines":["u"],"id":276},{"start":{"row":31,"column":138},"end":{"row":31,"column":139},"action":"remove","lines":["k"]},{"start":{"row":31,"column":137},"end":{"row":31,"column":138},"action":"remove","lines":["o"]}],[{"start":{"row":31,"column":137},"end":{"row":31,"column":138},"action":"insert","lines":["r"],"id":277},{"start":{"row":31,"column":138},"end":{"row":31,"column":139},"action":"insert","lines":["o"]},{"start":{"row":31,"column":139},"end":{"row":31,"column":140},"action":"insert","lines":["k"]},{"start":{"row":31,"column":140},"end":{"row":31,"column":141},"action":"insert","lines":["u"]}],[{"start":{"row":31,"column":141},"end":{"row":31,"column":142},"action":"insert","lines":["a"],"id":278},{"start":{"row":31,"column":142},"end":{"row":31,"column":143},"action":"insert","lines":["p"]},{"start":{"row":31,"column":143},"end":{"row":31,"column":144},"action":"insert","lines":["p"]}],[{"start":{"row":31,"column":144},"end":{"row":31,"column":145},"action":"insert","lines":["."],"id":279},{"start":{"row":31,"column":145},"end":{"row":31,"column":146},"action":"insert","lines":["c"]},{"start":{"row":31,"column":146},"end":{"row":31,"column":147},"action":"insert","lines":["o"]},{"start":{"row":31,"column":147},"end":{"row":31,"column":148},"action":"insert","lines":["m"]}],[{"start":{"row":31,"column":119},"end":{"row":31,"column":148},"action":"remove","lines":["dm-issuetracker.herokuapp.com"],"id":280},{"start":{"row":31,"column":119},"end":{"row":31,"column":157},"action":"insert","lines":["https://dm-issuetracker.herokuapp.com/"]}],[{"start":{"row":31,"column":126},"end":{"row":31,"column":127},"action":"remove","lines":["/"],"id":281},{"start":{"row":31,"column":125},"end":{"row":31,"column":126},"action":"remove","lines":["/"]},{"start":{"row":31,"column":124},"end":{"row":31,"column":125},"action":"remove","lines":[":"]},{"start":{"row":31,"column":123},"end":{"row":31,"column":124},"action":"remove","lines":["s"]},{"start":{"row":31,"column":122},"end":{"row":31,"column":123},"action":"remove","lines":["p"]},{"start":{"row":31,"column":121},"end":{"row":31,"column":122},"action":"remove","lines":["t"]},{"start":{"row":31,"column":120},"end":{"row":31,"column":121},"action":"remove","lines":["t"]},{"start":{"row":31,"column":119},"end":{"row":31,"column":120},"action":"remove","lines":["h"]}],[{"start":{"row":31,"column":148},"end":{"row":31,"column":149},"action":"remove","lines":["/"],"id":282}],[{"start":{"row":152,"column":44},"end":{"row":153,"column":0},"action":"insert","lines":["",""],"id":283}],[{"start":{"row":153,"column":0},"end":{"row":154,"column":0},"action":"insert","lines":["",""],"id":284},{"start":{"row":154,"column":0},"end":{"row":154,"column":1},"action":"insert","lines":["S"]},{"start":{"row":154,"column":1},"end":{"row":154,"column":2},"action":"insert","lines":["T"]},{"start":{"row":154,"column":2},"end":{"row":154,"column":3},"action":"insert","lines":["R"]}],[{"start":{"row":154,"column":3},"end":{"row":154,"column":4},"action":"insert","lines":["I"],"id":285},{"start":{"row":154,"column":4},"end":{"row":154,"column":5},"action":"insert","lines":["P"]},{"start":{"row":154,"column":5},"end":{"row":154,"column":6},"action":"insert","lines":["E"]},{"start":{"row":154,"column":6},"end":{"row":154,"column":7},"action":"insert","lines":["_"]}],[{"start":{"row":154,"column":7},"end":{"row":154,"column":8},"action":"insert","lines":["P"],"id":286},{"start":{"row":154,"column":8},"end":{"row":154,"column":9},"action":"insert","lines":["U"]},{"start":{"row":154,"column":9},"end":{"row":154,"column":10},"action":"insert","lines":["B"]},{"start":{"row":154,"column":10},"end":{"row":154,"column":11},"action":"insert","lines":["L"]},{"start":{"row":154,"column":11},"end":{"row":154,"column":12},"action":"insert","lines":["I"]},{"start":{"row":154,"column":12},"end":{"row":154,"column":13},"action":"insert","lines":["S"]}],[{"start":{"row":154,"column":13},"end":{"row":154,"column":14},"action":"insert","lines":["H"],"id":287},{"start":{"row":154,"column":14},"end":{"row":154,"column":15},"action":"insert","lines":["A"]},{"start":{"row":154,"column":15},"end":{"row":154,"column":16},"action":"insert","lines":["B"]},{"start":{"row":154,"column":16},"end":{"row":154,"column":17},"action":"insert","lines":["L"]},{"start":{"row":154,"column":17},"end":{"row":154,"column":18},"action":"insert","lines":["E"]}],[{"start":{"row":154,"column":18},"end":{"row":154,"column":19},"action":"insert","lines":[" "],"id":288},{"start":{"row":154,"column":19},"end":{"row":154,"column":20},"action":"insert","lines":["="]}],[{"start":{"row":154,"column":20},"end":{"row":154,"column":21},"action":"insert","lines":[" "],"id":289},{"start":{"row":154,"column":21},"end":{"row":154,"column":22},"action":"insert","lines":["o"]},{"start":{"row":154,"column":22},"end":{"row":154,"column":23},"action":"insert","lines":["s"]}],[{"start":{"row":154,"column":23},"end":{"row":154,"column":24},"action":"insert","lines":["."],"id":290},{"start":{"row":154,"column":24},"end":{"row":154,"column":25},"action":"insert","lines":["g"]},{"start":{"row":154,"column":25},"end":{"row":154,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":154,"column":26},"end":{"row":154,"column":27},"action":"insert","lines":["t"],"id":291},{"start":{"row":154,"column":27},"end":{"row":154,"column":28},"action":"insert","lines":["e"]}],[{"start":{"row":154,"column":24},"end":{"row":154,"column":28},"action":"remove","lines":["gete"],"id":292},{"start":{"row":154,"column":24},"end":{"row":154,"column":32},"action":"insert","lines":["getenv()"]}],[{"start":{"row":154,"column":31},"end":{"row":154,"column":33},"action":"insert","lines":["''"],"id":293}],[{"start":{"row":154,"column":32},"end":{"row":154,"column":33},"action":"insert","lines":["S"],"id":294},{"start":{"row":154,"column":33},"end":{"row":154,"column":34},"action":"insert","lines":["T"]}],[{"start":{"row":154,"column":32},"end":{"row":154,"column":34},"action":"remove","lines":["ST"],"id":295},{"start":{"row":154,"column":32},"end":{"row":154,"column":50},"action":"insert","lines":["STRIPE_PUBLISHABLE"]}],[{"start":{"row":154,"column":52},"end":{"row":155,"column":0},"action":"insert","lines":["",""],"id":296},{"start":{"row":155,"column":0},"end":{"row":155,"column":1},"action":"insert","lines":["S"]},{"start":{"row":155,"column":1},"end":{"row":155,"column":2},"action":"insert","lines":["T"]}],[{"start":{"row":155,"column":2},"end":{"row":155,"column":3},"action":"insert","lines":["I"],"id":297},{"start":{"row":155,"column":3},"end":{"row":155,"column":4},"action":"insert","lines":["P"]},{"start":{"row":155,"column":4},"end":{"row":155,"column":5},"action":"insert","lines":["E"]}],[{"start":{"row":155,"column":4},"end":{"row":155,"column":5},"action":"remove","lines":["E"],"id":298},{"start":{"row":155,"column":3},"end":{"row":155,"column":4},"action":"remove","lines":["P"]},{"start":{"row":155,"column":2},"end":{"row":155,"column":3},"action":"remove","lines":["I"]},{"start":{"row":155,"column":1},"end":{"row":155,"column":2},"action":"remove","lines":["T"]}],[{"start":{"row":155,"column":1},"end":{"row":155,"column":2},"action":"insert","lines":["T"],"id":299},{"start":{"row":155,"column":2},"end":{"row":155,"column":3},"action":"insert","lines":["R"]},{"start":{"row":155,"column":3},"end":{"row":155,"column":4},"action":"insert","lines":["I"]},{"start":{"row":155,"column":4},"end":{"row":155,"column":5},"action":"insert","lines":["P"]},{"start":{"row":155,"column":5},"end":{"row":155,"column":6},"action":"insert","lines":["E"]},{"start":{"row":155,"column":6},"end":{"row":155,"column":7},"action":"insert","lines":["_"]}],[{"start":{"row":155,"column":7},"end":{"row":155,"column":8},"action":"insert","lines":["S"],"id":300},{"start":{"row":155,"column":8},"end":{"row":155,"column":9},"action":"insert","lines":["E"]},{"start":{"row":155,"column":9},"end":{"row":155,"column":10},"action":"insert","lines":["C"]},{"start":{"row":155,"column":10},"end":{"row":155,"column":11},"action":"insert","lines":["T"]},{"start":{"row":155,"column":11},"end":{"row":155,"column":12},"action":"insert","lines":["R"]},{"start":{"row":155,"column":12},"end":{"row":155,"column":13},"action":"insert","lines":["E"]}],[{"start":{"row":155,"column":12},"end":{"row":155,"column":13},"action":"remove","lines":["E"],"id":301},{"start":{"row":155,"column":11},"end":{"row":155,"column":12},"action":"remove","lines":["R"]},{"start":{"row":155,"column":10},"end":{"row":155,"column":11},"action":"remove","lines":["T"]}],[{"start":{"row":155,"column":10},"end":{"row":155,"column":11},"action":"insert","lines":["R"],"id":302},{"start":{"row":155,"column":11},"end":{"row":155,"column":12},"action":"insert","lines":["E"]},{"start":{"row":155,"column":12},"end":{"row":155,"column":13},"action":"insert","lines":["T"]}],[{"start":{"row":155,"column":13},"end":{"row":155,"column":14},"action":"insert","lines":[" "],"id":303},{"start":{"row":155,"column":14},"end":{"row":155,"column":15},"action":"insert","lines":["="]}],[{"start":{"row":155,"column":15},"end":{"row":155,"column":16},"action":"insert","lines":[" "],"id":304},{"start":{"row":155,"column":16},"end":{"row":155,"column":17},"action":"insert","lines":["o"]},{"start":{"row":155,"column":17},"end":{"row":155,"column":18},"action":"insert","lines":["s"]},{"start":{"row":155,"column":18},"end":{"row":155,"column":19},"action":"insert","lines":["."]}],[{"start":{"row":155,"column":19},"end":{"row":155,"column":20},"action":"insert","lines":["g"],"id":305},{"start":{"row":155,"column":20},"end":{"row":155,"column":21},"action":"insert","lines":["e"]},{"start":{"row":155,"column":21},"end":{"row":155,"column":22},"action":"insert","lines":["t"]}],[{"start":{"row":155,"column":22},"end":{"row":155,"column":23},"action":"insert","lines":["e"],"id":306},{"start":{"row":155,"column":23},"end":{"row":155,"column":24},"action":"insert","lines":["n"]}],[{"start":{"row":155,"column":19},"end":{"row":155,"column":24},"action":"remove","lines":["geten"],"id":307},{"start":{"row":155,"column":19},"end":{"row":155,"column":27},"action":"insert","lines":["getenv()"]}],[{"start":{"row":155,"column":26},"end":{"row":155,"column":28},"action":"insert","lines":["()"],"id":308}],[{"start":{"row":155,"column":27},"end":{"row":155,"column":29},"action":"insert","lines":["''"],"id":309}],[{"start":{"row":155,"column":28},"end":{"row":155,"column":29},"action":"insert","lines":["S"],"id":310},{"start":{"row":155,"column":29},"end":{"row":155,"column":30},"action":"insert","lines":["T"]},{"start":{"row":155,"column":30},"end":{"row":155,"column":31},"action":"insert","lines":["R"]},{"start":{"row":155,"column":31},"end":{"row":155,"column":32},"action":"insert","lines":["U"]}],[{"start":{"row":155,"column":31},"end":{"row":155,"column":32},"action":"remove","lines":["U"],"id":311}],[{"start":{"row":155,"column":31},"end":{"row":155,"column":32},"action":"insert","lines":["I"],"id":312},{"start":{"row":155,"column":32},"end":{"row":155,"column":33},"action":"insert","lines":["P"]},{"start":{"row":155,"column":33},"end":{"row":155,"column":34},"action":"insert","lines":["E"]},{"start":{"row":155,"column":34},"end":{"row":155,"column":35},"action":"insert","lines":["_"]}],[{"start":{"row":155,"column":35},"end":{"row":155,"column":36},"action":"insert","lines":["S"],"id":313},{"start":{"row":155,"column":36},"end":{"row":155,"column":37},"action":"insert","lines":["E"]}],[{"start":{"row":155,"column":28},"end":{"row":155,"column":37},"action":"remove","lines":["STRIPE_SE"],"id":314},{"start":{"row":155,"column":28},"end":{"row":155,"column":41},"action":"insert","lines":["STRIPE_SECRET"]}],[{"start":{"row":45,"column":14},"end":{"row":46,"column":0},"action":"insert","lines":["",""],"id":315},{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":46,"column":4},"end":{"row":46,"column":6},"action":"insert","lines":["''"],"id":316}],[{"start":{"row":46,"column":5},"end":{"row":46,"column":6},"action":"insert","lines":["c"],"id":317},{"start":{"row":46,"column":6},"end":{"row":46,"column":7},"action":"insert","lines":["h"]},{"start":{"row":46,"column":7},"end":{"row":46,"column":8},"action":"insert","lines":["e"]},{"start":{"row":46,"column":8},"end":{"row":46,"column":9},"action":"insert","lines":["c"]},{"start":{"row":46,"column":9},"end":{"row":46,"column":10},"action":"insert","lines":["k"]},{"start":{"row":46,"column":10},"end":{"row":46,"column":11},"action":"insert","lines":["o"]},{"start":{"row":46,"column":11},"end":{"row":46,"column":12},"action":"insert","lines":["u"]},{"start":{"row":46,"column":12},"end":{"row":46,"column":13},"action":"insert","lines":["t"]}],[{"start":{"row":46,"column":14},"end":{"row":46,"column":15},"action":"insert","lines":[","],"id":318}]]},"ace":{"folds":[],"scrolltop":300,"scrollleft":0,"selection":{"start":{"row":43,"column":29},"end":{"row":43,"column":29},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1606342887644,"hash":"864334994aa48bd214a9b26e8eea0861633f5206"}