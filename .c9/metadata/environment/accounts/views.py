{"filter":false,"title":"views.py","tooltip":"/accounts/views.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":8,"column":3},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":167},{"start":{"row":9,"column":0},"end":{"row":9,"column":3},"action":"insert","lines":["   "]}],[{"start":{"row":9,"column":2},"end":{"row":9,"column":3},"action":"remove","lines":[" "],"id":168},{"start":{"row":9,"column":1},"end":{"row":9,"column":2},"action":"remove","lines":[" "]},{"start":{"row":9,"column":0},"end":{"row":9,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":15},"action":"insert","lines":["@login_required"],"id":169}],[{"start":{"row":34,"column":68},"end":{"row":35,"column":0},"action":"insert","lines":["",""],"id":170},{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"insert","lines":["    "]},{"start":{"row":35,"column":4},"end":{"row":36,"column":0},"action":"insert","lines":["",""]},{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":36,"column":4},"end":{"row":57,"column":48},"action":"insert","lines":["def registration(request):","    \"\"\"Render the registration page\"\"\"","    if request.user.is_authenticated:","        return redirect(reverse('index'))","","    if request.method == \"POST\":","        registration_form = UserRegistrationForm(request.POST)","","        if registration_form.is_valid():","            registration_form.save()","","            user = auth.authenticate(username=request.POST['username'],","                                     password=request.POST['password1'])","            if user:","                auth.login(user=user, request=request)","                messages.success(request, \"You have successfully registered\")","            else:","                messages.error(request, \"Unable to register your account at this time\")","    else:","        registration_form = UserRegistrationForm()","    return render(request, 'registration.html', {","        \"registration_form\": registration_form})"],"id":171}],[{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"remove","lines":["    "],"id":172}],[{"start":{"row":35,"column":4},"end":{"row":36,"column":0},"action":"remove","lines":["",""],"id":173}],[{"start":{"row":35,"column":4},"end":{"row":36,"column":0},"action":"insert","lines":["",""],"id":174},{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"remove","lines":["    "],"id":175}],[{"start":{"row":41,"column":4},"end":{"row":57,"column":48},"action":"remove","lines":["if request.method == \"POST\":","        registration_form = UserRegistrationForm(request.POST)","","        if registration_form.is_valid():","            registration_form.save()","","            user = auth.authenticate(username=request.POST['username'],","                                     password=request.POST['password1'])","            if user:","                auth.login(user=user, request=request)","                messages.success(request, \"You have successfully registered\")","            else:","                messages.error(request, \"Unable to register your account at this time\")","    else:","        registration_form = UserRegistrationForm()","    return render(request, 'registration.html', {","        \"registration_form\": registration_form})"],"id":176}],[{"start":{"row":38,"column":4},"end":{"row":38,"column":37},"action":"remove","lines":["if request.user.is_authenticated:"],"id":177},{"start":{"row":38,"column":4},"end":{"row":39,"column":0},"action":"remove","lines":["",""]},{"start":{"row":38,"column":4},"end":{"row":38,"column":8},"action":"remove","lines":["    "]},{"start":{"row":38,"column":4},"end":{"row":38,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":38,"column":4},"end":{"row":38,"column":5},"action":"insert","lines":["r"],"id":178},{"start":{"row":38,"column":5},"end":{"row":38,"column":6},"action":"insert","lines":["e"]},{"start":{"row":38,"column":6},"end":{"row":38,"column":7},"action":"insert","lines":["t"]},{"start":{"row":38,"column":7},"end":{"row":38,"column":8},"action":"insert","lines":["u"]},{"start":{"row":38,"column":8},"end":{"row":38,"column":9},"action":"insert","lines":["r"]},{"start":{"row":38,"column":9},"end":{"row":38,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":38,"column":10},"end":{"row":38,"column":11},"action":"insert","lines":[" "],"id":179},{"start":{"row":38,"column":11},"end":{"row":38,"column":12},"action":"insert","lines":["r"]},{"start":{"row":38,"column":12},"end":{"row":38,"column":13},"action":"insert","lines":["e"]},{"start":{"row":38,"column":13},"end":{"row":38,"column":14},"action":"insert","lines":["n"]},{"start":{"row":38,"column":14},"end":{"row":38,"column":15},"action":"insert","lines":["d"]},{"start":{"row":38,"column":15},"end":{"row":38,"column":16},"action":"insert","lines":["e"]},{"start":{"row":38,"column":16},"end":{"row":38,"column":17},"action":"insert","lines":["r"]}],[{"start":{"row":38,"column":17},"end":{"row":38,"column":18},"action":"insert","lines":[" "],"id":180},{"start":{"row":38,"column":18},"end":{"row":38,"column":19},"action":"insert","lines":["("]},{"start":{"row":38,"column":19},"end":{"row":38,"column":20},"action":"insert","lines":[")"]}],[{"start":{"row":38,"column":19},"end":{"row":38,"column":20},"action":"insert","lines":["r"],"id":181},{"start":{"row":38,"column":20},"end":{"row":38,"column":21},"action":"insert","lines":["e"]},{"start":{"row":38,"column":21},"end":{"row":38,"column":22},"action":"insert","lines":["q"]},{"start":{"row":38,"column":22},"end":{"row":38,"column":23},"action":"insert","lines":["u"]},{"start":{"row":38,"column":23},"end":{"row":38,"column":24},"action":"insert","lines":["e"]},{"start":{"row":38,"column":24},"end":{"row":38,"column":25},"action":"insert","lines":["s"]},{"start":{"row":38,"column":25},"end":{"row":38,"column":26},"action":"insert","lines":["t"]}],[{"start":{"row":38,"column":26},"end":{"row":38,"column":27},"action":"insert","lines":[","],"id":182}],[{"start":{"row":38,"column":27},"end":{"row":38,"column":28},"action":"insert","lines":[" "],"id":183}],[{"start":{"row":38,"column":27},"end":{"row":38,"column":28},"action":"remove","lines":[" "],"id":184}],[{"start":{"row":38,"column":27},"end":{"row":38,"column":29},"action":"insert","lines":["''"],"id":185}],[{"start":{"row":38,"column":28},"end":{"row":38,"column":29},"action":"insert","lines":["r"],"id":186},{"start":{"row":38,"column":29},"end":{"row":38,"column":30},"action":"insert","lines":["e"]},{"start":{"row":38,"column":30},"end":{"row":38,"column":31},"action":"insert","lines":["g"]},{"start":{"row":38,"column":31},"end":{"row":38,"column":32},"action":"insert","lines":["i"]},{"start":{"row":38,"column":32},"end":{"row":38,"column":33},"action":"insert","lines":["s"]},{"start":{"row":38,"column":33},"end":{"row":38,"column":34},"action":"insert","lines":["t"]},{"start":{"row":38,"column":34},"end":{"row":38,"column":35},"action":"insert","lines":["r"]},{"start":{"row":38,"column":35},"end":{"row":38,"column":36},"action":"insert","lines":["a"]},{"start":{"row":38,"column":36},"end":{"row":38,"column":37},"action":"insert","lines":["t"]},{"start":{"row":38,"column":37},"end":{"row":38,"column":38},"action":"insert","lines":["i"]},{"start":{"row":38,"column":38},"end":{"row":38,"column":39},"action":"insert","lines":["o"]},{"start":{"row":38,"column":39},"end":{"row":38,"column":40},"action":"insert","lines":["n"]}],[{"start":{"row":38,"column":40},"end":{"row":38,"column":41},"action":"insert","lines":["."],"id":187},{"start":{"row":38,"column":41},"end":{"row":38,"column":42},"action":"insert","lines":["t"]}],[{"start":{"row":38,"column":41},"end":{"row":38,"column":42},"action":"remove","lines":["t"],"id":188}],[{"start":{"row":38,"column":41},"end":{"row":38,"column":42},"action":"insert","lines":["h"],"id":189},{"start":{"row":38,"column":42},"end":{"row":38,"column":43},"action":"insert","lines":["t"]},{"start":{"row":38,"column":43},"end":{"row":38,"column":44},"action":"insert","lines":["m"]},{"start":{"row":38,"column":44},"end":{"row":38,"column":45},"action":"insert","lines":["l"]}],[{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["r"],"id":190},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["e"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["t"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["u"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["r"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["n"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":[" "]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["r"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["e"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["d"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["i"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["r"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["e"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["c"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["t"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["("]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["r"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["e"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["v"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["e"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["r"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["s"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["e"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["("]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["'"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["i"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["n"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["d"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["e"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["x"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":["'"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":[")"]},{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":[")"]},{"start":{"row":38,"column":47},"end":{"row":39,"column":0},"action":"remove","lines":["",""]},{"start":{"row":38,"column":47},"end":{"row":39,"column":4},"action":"remove","lines":["","    "]}],[{"start":{"row":3,"column":40},"end":{"row":3,"column":41},"action":"insert","lines":[","],"id":191}],[{"start":{"row":3,"column":41},"end":{"row":3,"column":61},"action":"insert","lines":["UserRegistrationForm"],"id":192}],[{"start":{"row":3,"column":41},"end":{"row":3,"column":42},"action":"remove","lines":["U"],"id":193},{"start":{"row":3,"column":41},"end":{"row":3,"column":42},"action":"insert","lines":[" "]}],[{"start":{"row":3,"column":42},"end":{"row":3,"column":43},"action":"remove","lines":["s"],"id":194},{"start":{"row":3,"column":42},"end":{"row":3,"column":43},"action":"insert","lines":["U"]}],[{"start":{"row":3,"column":42},"end":{"row":3,"column":61},"action":"remove","lines":["UerRegistrationForm"],"id":195},{"start":{"row":3,"column":42},"end":{"row":3,"column":62},"action":"insert","lines":["UserRegistrationForm"]}],[{"start":{"row":38,"column":47},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":199},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":39,"column":4},"end":{"row":41,"column":48},"action":"insert","lines":[" registration_form = UserRegistrationForm()","    return render(request, 'registration.html', {","        \"registration_form\": registration_form})"],"id":200}],[{"start":{"row":38,"column":0},"end":{"row":39,"column":47},"action":"remove","lines":["    return render (request,'registration.html')","     registration_form = UserRegistrationForm()"],"id":214},{"start":{"row":38,"column":0},"end":{"row":39,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":3,"column":42},"end":{"row":3,"column":62},"action":"remove","lines":["UserRegistrationForm"],"id":215},{"start":{"row":3,"column":42},"end":{"row":3,"column":62},"action":"insert","lines":["UserRegistrationForm"]}],[{"start":{"row":38,"column":46},"end":{"row":39,"column":48},"action":"remove","lines":[", {","        \"registration_form\": registration_form})"],"id":216}],[{"start":{"row":38,"column":46},"end":{"row":38,"column":47},"action":"insert","lines":[")"],"id":217}],[{"start":{"row":37,"column":38},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":218},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "]},{"start":{"row":38,"column":4},"end":{"row":38,"column":5},"action":"insert","lines":["r"]},{"start":{"row":38,"column":5},"end":{"row":38,"column":6},"action":"insert","lines":["e"]},{"start":{"row":38,"column":6},"end":{"row":38,"column":7},"action":"insert","lines":["g"]},{"start":{"row":38,"column":7},"end":{"row":38,"column":8},"action":"insert","lines":["i"]},{"start":{"row":38,"column":8},"end":{"row":38,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":38,"column":9},"end":{"row":38,"column":10},"action":"insert","lines":["t"],"id":219},{"start":{"row":38,"column":10},"end":{"row":38,"column":11},"action":"insert","lines":["r"]},{"start":{"row":38,"column":11},"end":{"row":38,"column":12},"action":"insert","lines":["a"]},{"start":{"row":38,"column":12},"end":{"row":38,"column":13},"action":"insert","lines":["t"]},{"start":{"row":38,"column":13},"end":{"row":38,"column":14},"action":"insert","lines":["i"]},{"start":{"row":38,"column":14},"end":{"row":38,"column":15},"action":"insert","lines":["o"]},{"start":{"row":38,"column":15},"end":{"row":38,"column":16},"action":"insert","lines":["n"]}],[{"start":{"row":38,"column":16},"end":{"row":38,"column":17},"action":"insert","lines":["_"],"id":220},{"start":{"row":38,"column":17},"end":{"row":38,"column":18},"action":"insert","lines":["f"]},{"start":{"row":38,"column":18},"end":{"row":38,"column":19},"action":"insert","lines":["o"]},{"start":{"row":38,"column":19},"end":{"row":38,"column":20},"action":"insert","lines":["r"]},{"start":{"row":38,"column":20},"end":{"row":38,"column":21},"action":"insert","lines":["m"]}],[{"start":{"row":38,"column":21},"end":{"row":38,"column":22},"action":"insert","lines":[" "],"id":221},{"start":{"row":38,"column":22},"end":{"row":38,"column":23},"action":"insert","lines":["="]}],[{"start":{"row":38,"column":23},"end":{"row":38,"column":24},"action":"insert","lines":[" "],"id":222}],[{"start":{"row":38,"column":24},"end":{"row":38,"column":28},"action":"insert","lines":["    "],"id":223}],[{"start":{"row":38,"column":24},"end":{"row":38,"column":28},"action":"remove","lines":["    "],"id":224}],[{"start":{"row":38,"column":24},"end":{"row":38,"column":25},"action":"insert","lines":["U"],"id":225},{"start":{"row":38,"column":25},"end":{"row":38,"column":26},"action":"insert","lines":["s"]},{"start":{"row":38,"column":26},"end":{"row":38,"column":27},"action":"insert","lines":["e"]},{"start":{"row":38,"column":27},"end":{"row":38,"column":28},"action":"insert","lines":["r"]}],[{"start":{"row":38,"column":24},"end":{"row":38,"column":28},"action":"remove","lines":["User"],"id":226},{"start":{"row":38,"column":24},"end":{"row":38,"column":44},"action":"insert","lines":["UserRegistrationForm"]}],[{"start":{"row":38,"column":44},"end":{"row":38,"column":46},"action":"insert","lines":["()"],"id":228}],[{"start":{"row":39,"column":45},"end":{"row":39,"column":46},"action":"remove","lines":["'"],"id":230},{"start":{"row":39,"column":45},"end":{"row":39,"column":46},"action":"insert","lines":[","]}],[{"start":{"row":39,"column":46},"end":{"row":39,"column":47},"action":"remove","lines":[")"],"id":231},{"start":{"row":39,"column":46},"end":{"row":39,"column":47},"action":"insert","lines":[" "]}],[{"start":{"row":39,"column":47},"end":{"row":39,"column":48},"action":"insert","lines":["{"],"id":232},{"start":{"row":39,"column":48},"end":{"row":39,"column":49},"action":"insert","lines":["}"]}],[{"start":{"row":39,"column":48},"end":{"row":39,"column":49},"action":"remove","lines":["}"],"id":233},{"start":{"row":39,"column":48},"end":{"row":39,"column":49},"action":"insert","lines":["\""]},{"start":{"row":39,"column":49},"end":{"row":39,"column":50},"action":"insert","lines":["\""]}],[{"start":{"row":39,"column":49},"end":{"row":39,"column":50},"action":"remove","lines":["\""],"id":234}],[{"start":{"row":39,"column":49},"end":{"row":39,"column":50},"action":"insert","lines":["r"],"id":235},{"start":{"row":39,"column":50},"end":{"row":39,"column":51},"action":"insert","lines":["e"]},{"start":{"row":39,"column":51},"end":{"row":39,"column":52},"action":"insert","lines":["g"]},{"start":{"row":39,"column":52},"end":{"row":39,"column":53},"action":"insert","lines":["i"]},{"start":{"row":39,"column":53},"end":{"row":39,"column":54},"action":"insert","lines":["s"]},{"start":{"row":39,"column":54},"end":{"row":39,"column":55},"action":"insert","lines":["t"]}],[{"start":{"row":39,"column":49},"end":{"row":39,"column":55},"action":"remove","lines":["regist"],"id":236},{"start":{"row":39,"column":49},"end":{"row":39,"column":66},"action":"insert","lines":["registration_form"]}],[{"start":{"row":39,"column":66},"end":{"row":39,"column":67},"action":"insert","lines":[":"],"id":237}],[{"start":{"row":39,"column":67},"end":{"row":39,"column":68},"action":"insert","lines":[" "],"id":238}],[{"start":{"row":39,"column":67},"end":{"row":39,"column":68},"action":"remove","lines":[" "],"id":239},{"start":{"row":39,"column":66},"end":{"row":39,"column":67},"action":"remove","lines":[":"]}],[{"start":{"row":39,"column":66},"end":{"row":39,"column":67},"action":"insert","lines":["\""],"id":240},{"start":{"row":39,"column":67},"end":{"row":39,"column":68},"action":"insert","lines":[":"]}],[{"start":{"row":39,"column":68},"end":{"row":39,"column":69},"action":"insert","lines":[" "],"id":241},{"start":{"row":39,"column":69},"end":{"row":39,"column":70},"action":"insert","lines":["r"]},{"start":{"row":39,"column":70},"end":{"row":39,"column":71},"action":"insert","lines":["e"]},{"start":{"row":39,"column":71},"end":{"row":39,"column":72},"action":"insert","lines":["g"]},{"start":{"row":39,"column":72},"end":{"row":39,"column":73},"action":"insert","lines":["i"]},{"start":{"row":39,"column":73},"end":{"row":39,"column":74},"action":"insert","lines":["s"]},{"start":{"row":39,"column":74},"end":{"row":39,"column":75},"action":"insert","lines":["t"]},{"start":{"row":39,"column":75},"end":{"row":39,"column":76},"action":"insert","lines":["r"]}],[{"start":{"row":39,"column":76},"end":{"row":39,"column":77},"action":"insert","lines":["a"],"id":242},{"start":{"row":39,"column":77},"end":{"row":39,"column":78},"action":"insert","lines":["t"]},{"start":{"row":39,"column":78},"end":{"row":39,"column":79},"action":"insert","lines":["i"]},{"start":{"row":39,"column":79},"end":{"row":39,"column":80},"action":"insert","lines":["o"]},{"start":{"row":39,"column":80},"end":{"row":39,"column":81},"action":"insert","lines":["n"]},{"start":{"row":39,"column":81},"end":{"row":39,"column":82},"action":"insert","lines":["_"]},{"start":{"row":39,"column":82},"end":{"row":39,"column":83},"action":"insert","lines":["f"]},{"start":{"row":39,"column":83},"end":{"row":39,"column":84},"action":"insert","lines":["o"]}],[{"start":{"row":39,"column":84},"end":{"row":39,"column":85},"action":"insert","lines":["r"],"id":243},{"start":{"row":39,"column":85},"end":{"row":39,"column":86},"action":"insert","lines":["m"]}],[{"start":{"row":39,"column":86},"end":{"row":39,"column":87},"action":"insert","lines":["}"],"id":244},{"start":{"row":39,"column":87},"end":{"row":39,"column":88},"action":"insert","lines":[")"]}],[{"start":{"row":39,"column":45},"end":{"row":39,"column":46},"action":"remove","lines":[","],"id":245},{"start":{"row":39,"column":45},"end":{"row":39,"column":46},"action":"insert","lines":["'"]}],[{"start":{"row":39,"column":46},"end":{"row":39,"column":47},"action":"insert","lines":[","],"id":246}],[{"start":{"row":39,"column":49},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":247},{"start":{"row":40,"column":0},"end":{"row":40,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":37,"column":38},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":248},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":38,"column":4},"end":{"row":39,"column":41},"action":"insert","lines":["if request.user.is_authenticated:","        return redirect(reverse('index'))"],"id":249}],[{"start":{"row":39,"column":41},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":250},{"start":{"row":40,"column":0},"end":{"row":40,"column":8},"action":"insert","lines":["        "]},{"start":{"row":40,"column":8},"end":{"row":41,"column":0},"action":"insert","lines":["",""]},{"start":{"row":41,"column":0},"end":{"row":41,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":41,"column":4},"end":{"row":41,"column":8},"action":"remove","lines":["    "],"id":251}],[{"start":{"row":41,"column":4},"end":{"row":58,"column":0},"action":"insert","lines":["if request.method == \"POST\":","        registration_form = UserRegistrationForm(request.POST)","","        if registration_form.is_valid():","            registration_form.save()","","            user = auth.authenticate(username=request.POST['username'],","                                     password=request.POST['password1'])","            if user:","                auth.login(user=user, request=request)","                messages.success(request, \"You have successfully registered\")","            else:","                messages.error(request, \"Unable to register your account at this time\")","    else:","        registration_form = UserRegistrationForm()","    return render(request, 'registration.html', {","        \"registration_form\": registration_form})",""],"id":252}],[{"start":{"row":51,"column":77},"end":{"row":52,"column":0},"action":"insert","lines":["",""],"id":253},{"start":{"row":52,"column":0},"end":{"row":52,"column":16},"action":"insert","lines":["                "]},{"start":{"row":52,"column":16},"end":{"row":52,"column":17},"action":"insert","lines":["r"]},{"start":{"row":52,"column":17},"end":{"row":52,"column":18},"action":"insert","lines":["e"]},{"start":{"row":52,"column":18},"end":{"row":52,"column":19},"action":"insert","lines":["t"]},{"start":{"row":52,"column":19},"end":{"row":52,"column":20},"action":"insert","lines":["u"]},{"start":{"row":52,"column":20},"end":{"row":52,"column":21},"action":"insert","lines":["r"]},{"start":{"row":52,"column":21},"end":{"row":52,"column":22},"action":"insert","lines":["n"]}],[{"start":{"row":52,"column":22},"end":{"row":52,"column":23},"action":"insert","lines":[" "],"id":254}],[{"start":{"row":52,"column":22},"end":{"row":52,"column":23},"action":"remove","lines":[" "],"id":255}],[{"start":{"row":52,"column":22},"end":{"row":52,"column":23},"action":"insert","lines":[" "],"id":256},{"start":{"row":52,"column":23},"end":{"row":52,"column":24},"action":"insert","lines":["r"]},{"start":{"row":52,"column":24},"end":{"row":52,"column":25},"action":"insert","lines":["e"]},{"start":{"row":52,"column":25},"end":{"row":52,"column":26},"action":"insert","lines":["d"]},{"start":{"row":52,"column":26},"end":{"row":52,"column":27},"action":"insert","lines":["i"]},{"start":{"row":52,"column":27},"end":{"row":52,"column":28},"action":"insert","lines":["r"]},{"start":{"row":52,"column":28},"end":{"row":52,"column":29},"action":"insert","lines":["e"]}],[{"start":{"row":52,"column":23},"end":{"row":52,"column":29},"action":"remove","lines":["redire"],"id":257},{"start":{"row":52,"column":23},"end":{"row":52,"column":33},"action":"insert","lines":["redirect()"]}],[{"start":{"row":52,"column":32},"end":{"row":52,"column":33},"action":"insert","lines":["r"],"id":258},{"start":{"row":52,"column":33},"end":{"row":52,"column":34},"action":"insert","lines":["e"]},{"start":{"row":52,"column":34},"end":{"row":52,"column":35},"action":"insert","lines":["v"]},{"start":{"row":52,"column":35},"end":{"row":52,"column":36},"action":"insert","lines":["e"]},{"start":{"row":52,"column":36},"end":{"row":52,"column":37},"action":"insert","lines":["r"]},{"start":{"row":52,"column":37},"end":{"row":52,"column":38},"action":"insert","lines":["s"]}],[{"start":{"row":52,"column":38},"end":{"row":52,"column":39},"action":"insert","lines":["e"],"id":259}],[{"start":{"row":52,"column":39},"end":{"row":52,"column":41},"action":"insert","lines":["()"],"id":260}],[{"start":{"row":52,"column":40},"end":{"row":52,"column":42},"action":"insert","lines":["''"],"id":261}],[{"start":{"row":52,"column":41},"end":{"row":52,"column":42},"action":"insert","lines":["i"],"id":262},{"start":{"row":52,"column":42},"end":{"row":52,"column":43},"action":"insert","lines":["n"]},{"start":{"row":52,"column":43},"end":{"row":52,"column":44},"action":"insert","lines":["d"]},{"start":{"row":52,"column":44},"end":{"row":52,"column":45},"action":"insert","lines":["e"]},{"start":{"row":52,"column":45},"end":{"row":52,"column":46},"action":"insert","lines":["x"]}],[{"start":{"row":60,"column":4},"end":{"row":62,"column":48},"action":"remove","lines":["registration_form = UserRegistrationForm()","    return render(request, 'registration.html', {","        \"registration_form\": registration_form})"],"id":263}],[{"start":{"row":58,"column":48},"end":{"row":59,"column":0},"action":"insert","lines":["",""],"id":264},{"start":{"row":59,"column":0},"end":{"row":59,"column":8},"action":"insert","lines":["        "]},{"start":{"row":59,"column":8},"end":{"row":60,"column":0},"action":"insert","lines":["",""]},{"start":{"row":60,"column":0},"end":{"row":60,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":60,"column":4},"end":{"row":60,"column":8},"action":"remove","lines":["    "],"id":265},{"start":{"row":60,"column":0},"end":{"row":60,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":60,"column":0},"end":{"row":63,"column":61},"action":"insert","lines":["def user_profile(request):","    \"\"\"The user's profile page\"\"\"","    user = User.objects.get(email=request.user.email)","    return render(request, 'profile.html', {\"profile\": user})"],"id":266}],[{"start":{"row":2,"column":57},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":267},{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["f"]},{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"insert","lines":["r"]},{"start":{"row":3,"column":2},"end":{"row":3,"column":3},"action":"insert","lines":["o"]},{"start":{"row":3,"column":3},"end":{"row":3,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":[" "],"id":268},{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["d"]},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["j"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["a"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["n"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["g"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["o"]}],[{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["."],"id":269},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["c"]},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["o"]}],[{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["n"],"id":270},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":12},"end":{"row":3,"column":16},"action":"remove","lines":["cont"],"id":271},{"start":{"row":3,"column":12},"end":{"row":3,"column":19},"action":"insert","lines":["contrib"]}],[{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"insert","lines":["."],"id":272},{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":["a"]},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["u"]}],[{"start":{"row":3,"column":20},"end":{"row":3,"column":22},"action":"remove","lines":["au"],"id":273},{"start":{"row":3,"column":20},"end":{"row":3,"column":24},"action":"insert","lines":["auth"]}],[{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":["."],"id":274},{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":["d"]},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"insert","lines":["e"]}],[{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"remove","lines":["e"],"id":275},{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"remove","lines":["d"]}],[{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":["m"],"id":276},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"insert","lines":["o"]}],[{"start":{"row":3,"column":25},"end":{"row":3,"column":27},"action":"remove","lines":["mo"],"id":277},{"start":{"row":3,"column":25},"end":{"row":3,"column":31},"action":"insert","lines":["models"]}],[{"start":{"row":3,"column":31},"end":{"row":3,"column":32},"action":"insert","lines":[" "],"id":278},{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"insert","lines":["i"]},{"start":{"row":3,"column":33},"end":{"row":3,"column":34},"action":"insert","lines":["p"]}],[{"start":{"row":3,"column":33},"end":{"row":3,"column":34},"action":"remove","lines":["p"],"id":279}],[{"start":{"row":3,"column":33},"end":{"row":3,"column":34},"action":"insert","lines":["m"],"id":280},{"start":{"row":3,"column":34},"end":{"row":3,"column":35},"action":"insert","lines":["p"]},{"start":{"row":3,"column":35},"end":{"row":3,"column":36},"action":"insert","lines":["r"]},{"start":{"row":3,"column":36},"end":{"row":3,"column":37},"action":"insert","lines":["o"]},{"start":{"row":3,"column":37},"end":{"row":3,"column":38},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":37},"end":{"row":3,"column":38},"action":"remove","lines":["t"],"id":281},{"start":{"row":3,"column":36},"end":{"row":3,"column":37},"action":"remove","lines":["o"]},{"start":{"row":3,"column":35},"end":{"row":3,"column":36},"action":"remove","lines":["r"]}],[{"start":{"row":3,"column":35},"end":{"row":3,"column":36},"action":"insert","lines":["o"],"id":282},{"start":{"row":3,"column":36},"end":{"row":3,"column":37},"action":"insert","lines":["r"]},{"start":{"row":3,"column":37},"end":{"row":3,"column":38},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":38},"end":{"row":3,"column":39},"action":"insert","lines":[" "],"id":283}],[{"start":{"row":3,"column":39},"end":{"row":3,"column":40},"action":"insert","lines":["U"],"id":284},{"start":{"row":3,"column":40},"end":{"row":3,"column":41},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":39},"end":{"row":3,"column":41},"action":"remove","lines":["Us"],"id":285},{"start":{"row":3,"column":39},"end":{"row":3,"column":43},"action":"insert","lines":["User"]}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":33},"action":"insert","lines":["from django.utils import timezone"],"id":302}],[{"start":{"row":4,"column":62},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":302}],[{"start":{"row":33,"column":16},"end":{"row":33,"column":18},"action":"insert","lines":["# "],"id":303}],[{"start":{"row":33,"column":17},"end":{"row":33,"column":18},"action":"remove","lines":["/"],"id":304},{"start":{"row":33,"column":16},"end":{"row":33,"column":17},"action":"remove","lines":["/"]}],[{"start":{"row":33,"column":16},"end":{"row":33,"column":17},"action":"insert","lines":["/"],"id":305},{"start":{"row":33,"column":17},"end":{"row":33,"column":18},"action":"insert","lines":["/"]}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":26},"action":"insert","lines":["from .models import Ticket"],"id":306}],[{"start":{"row":4,"column":62},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":307}],[{"start":{"row":30,"column":80},"end":{"row":31,"column":0},"action":"remove","lines":["",""],"id":308},{"start":{"row":30,"column":80},"end":{"row":30,"column":84},"action":"remove","lines":["    "]},{"start":{"row":30,"column":80},"end":{"row":30,"column":84},"action":"remove","lines":["    "]},{"start":{"row":30,"column":80},"end":{"row":30,"column":84},"action":"remove","lines":["    "]},{"start":{"row":30,"column":80},"end":{"row":30,"column":84},"action":"remove","lines":["    "]}],[{"start":{"row":31,"column":12},"end":{"row":31,"column":16},"action":"insert","lines":["    "],"id":309}],[{"start":{"row":31,"column":8},"end":{"row":31,"column":12},"action":"insert","lines":["    "],"id":310}],[{"start":{"row":31,"column":4},"end":{"row":31,"column":8},"action":"insert","lines":["    "],"id":311}],[{"start":{"row":32,"column":12},"end":{"row":32,"column":16},"action":"insert","lines":["    "],"id":312}],[{"start":{"row":32,"column":8},"end":{"row":32,"column":12},"action":"insert","lines":["    "],"id":313}],[{"start":{"row":32,"column":4},"end":{"row":32,"column":8},"action":"insert","lines":["    "],"id":314}],[{"start":{"row":30,"column":16},"end":{"row":32,"column":75},"action":"insert","lines":["tickets = Ticket.objects.filter(published_date__lte=timezone.now","    ())","    return render(request, \"issuetrackertickets.html\", {'tickets':tickets})"],"id":315}],[{"start":{"row":29,"column":54},"end":{"row":30,"column":0},"action":"insert","lines":["",""],"id":316},{"start":{"row":30,"column":0},"end":{"row":30,"column":16},"action":"insert","lines":["                "]}]]},"ace":{"folds":[],"scrolltop":383,"scrollleft":0,"selection":{"start":{"row":42,"column":21},"end":{"row":42,"column":26},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1605088091601,"hash":"ac931cfd61e26cdc7c18213eba0066a30fa5f334"}