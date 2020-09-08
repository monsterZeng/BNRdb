

# Create your views here.
from . import views
import urllib.parse
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
# Create your views here.

from .models import Product as products
# 把模型换成小写，防止模型与函数名相同造成引用错误
from .models import Narg, Napa, NirS as Nirs, Nirk as Nirk, cNorB as cNorb, qNorB as qNorb, NosZ as Nosz
from .models import WaterTreatmentPlant, FreshwaterSystem, MarineSystem, GoundwaterSystem, WetlandRiparianZones, SulphurRemoval
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, FileResponse
from .forms import NameForm, ProductForm, EnzymesForm, Hmmer_tool, UploadFileForm, ID, System, Submit, Contact, Clusto
import os

def home(request):
    return render(request, "home.html")

def NarG(request, opt = None, inputText = None, page = 1):
    Enzymes = []
    if page < 1:
        page = 1
    
    From_brosower = False
    
    # ------------------------------------------表单而来-------------------------------------
    if request.method == "GET":
        enzymesForm = EnzymesForm(request.GET)
        print("GET")
        if enzymesForm.is_valid():
            print("is_valid")
            opt = enzymesForm.cleaned_data["opt"]
            inputText = enzymesForm.cleaned_data["inputText"]
            print("is_valid")
            if opt == "Enzyme_Name":
                Enzymes = Narg.objects.filter(Enzyme_Name = inputText)
            elif opt == "Nuc_GenBank ID":
                Enzymes = Narg.objects.filter(GenBank_ID = inputText)
            inputText = urllib.parse.quote(inputText)
            From_brosower = True
        elif opt is not None:
            From_brosower = True
            # 由于inputText有空格等其它符号，并且已经是URL编码过的，所以需要解码
            inputText = urllib.parse.unquote(inputText)
            if opt == "Enzyme_Name":
                Enzymes = Narg.objects.filter(Enzyme_Name = inputText)
            elif opt == "Nuc_GenBank ID":
                Enzymes = Narg.objects.filter(GenBank_ID = inputText)
            print("-----in broswer-------")
            # 使用完inputText之后，需要再传递到浏览器中，所以需要编码
            inputText = urllib.parse.quote(inputText)
    # ----------------------------------------------------------------------------------
    
    if len(Enzymes) == 0:
        Enzymes = Narg.objects.all()    
    total_num = len(Enzymes)
    max_pages = (total_num) // 10 + 1  # 判断是否超出最大页
    if  page > max_pages:
        page = max_pages
    Enzymes = Enzymes[(page - 1) * 10: (page) * 10]
    length = pagination_args(page, total_num)
    return render(request, "Enzymes/NarG.html",
                    {"title":"NarG",
                     "page":page,
                     "length":length,
                     "total_num":total_num,
                     "From_brosower":From_brosower,
                     "opt":opt,
                     "inputText":inputText,
                     "Enzymes":Enzymes})

def NapA(request, opt = None, inputText = None, page = 1):
    Enzymes = []
    From_brosower = False
    if page < 1:
        page = 1
    # ----------------------------从表单获取来的数据-------------------------------    
    if request.method == "GET":
        enzymesForm = EnzymesForm(request.GET)
        print("GET")
        if enzymesForm.is_valid():
            opt = enzymesForm.cleaned_data["opt"]
            inputText = enzymesForm.cleaned_data["inputText"]
            if opt == "Enzyme_Name":
                Enzymes = Napa.objects.filter(Enzyme_Name = inputText)
            elif opt == "Nuc_GenBank ID":
                Enzymes = Napa.objects.filter(GenBank_ID = inputText)
            inputText = urllib.parse.quote(inputText)
            From_brosower = True
        elif opt is not None:
            From_brosower = True
            # 由于inputText有空格等其它符号，并且已经是URL编码过的，所以需要解码
            inputText = urllib.parse.unquote(inputText)
            if opt == "Enzyme_Name":
                Enzymes = Napa.objects.filter(Enzyme_Name = inputText)
            elif opt == "Nuc_GenBank ID":
                Enzymes = Napa.objects.filter(GenBank_ID = inputText)
            print("-----in broswer-------")
            # 使用完inputText之后，需要再传递到浏览器中，所以需要编码
            inputText = urllib.parse.quote(inputText)
    # ---------------------------------------------------------------------------

    if len(Enzymes) == 0:
        Enzymes = Napa.objects.all()    
    total_num = len(Enzymes)
    max_pages = (total_num) // 10 + 1  # 判断是否超出最大页
    if  page > max_pages:
        page = max_pages
    Enzymes = Enzymes[(page - 1) * 10: (page) * 10]
    length = pagination_args(page, total_num)
    return render(request, "Enzymes/NapA.html",
                    {"title":"NapA",
                     "page":page,
                     "length":length,
                     "total_num":total_num,
                     "From_brosower":From_brosower,
                     "opt":opt,
                     "inputText":inputText,
                     "Enzymes":Enzymes})
    
def NirK(request, opt = None, inputText = None, page = 1):
    Enzymes = []
    From_brosower = False
    if page < 1:
        page = 1
    # ----------------------------从表单获取来的数据-------------------------------    
    if request.method == "GET":
        enzymesForm = EnzymesForm(request.GET)
        print("GET")
        if enzymesForm.is_valid():
            opt = enzymesForm.cleaned_data["opt"]
            inputText = enzymesForm.cleaned_data["inputText"]
            if opt == "Enzyme_Name":
                Enzymes = Nirk.objects.filter(Enzyme_Name = inputText)
            elif opt == "Nuc_GenBank ID":
                Enzymes = Nirk.objects.filter(GenBank_ID = inputText)
            inputText = urllib.parse.quote(inputText)
            From_brosower = True
        elif opt is not None:
            From_brosower = True
            # 由于inputText有空格等其它符号，并且已经是URL编码过的，所以需要解码
            inputText = urllib.parse.unquote(inputText)
            if opt == "Enzyme_Name":
                Enzymes = Nirk.objects.filter(Enzyme_Name = inputText)
            elif opt == "Nuc_GenBank ID":
                Enzymes = Nirk.objects.filter(GenBank_ID = inputText)
            print("-----in broswer-------")
            # 使用完inputText之后，需要再传递到浏览器中，所以需要编码
            inputText = urllib.parse.quote(inputText)
    # ---------------------------------------------------------------------------

    if len(Enzymes) == 0:
        Enzymes = Nirk.objects.all()    
    total_num = len(Enzymes)
    max_pages = (total_num) // 10 + 1  # 判断是否超出最大页
    if  page > max_pages:
        page = max_pages
    Enzymes = Enzymes[(page - 1) * 10: (page) * 10]
    length = pagination_args(page, total_num)
    return render(request, "Enzymes/Nirk.html",
                    {"title":"NirK",
                     "page":page,
                     "length":length,
                     "total_num":total_num,
                     "From_brosower":From_brosower,
                     "opt":opt,
                     "inputText":inputText,
                     "Enzymes":Enzymes})

def NirS(request, page = 1, opt = None, inputText = None):
    Enzymes = []
    if page < 1:
        page = 1
    From_brosower = False
    if request.method == "GET":
        enzymesForm = EnzymesForm(request.GET)
        print("GET")
        if enzymesForm.is_valid():
            print("is_valid")
            opt = enzymesForm.cleaned_data["opt"]
            inputText = enzymesForm.cleaned_data["inputText"]
            print("is_valid")
            if opt == "Enzyme_Name":
                Enzymes = Nirs.objects.filter(Enzyme_Name = inputText)
            elif opt == "Nuc_GenBank ID":
                Enzymes = Nirs.objects.filter(GenBank_ID = inputText)
            inputText = urllib.parse.quote(inputText)
            From_brosower = True
        elif opt is not None:
            From_brosower = True
            # 由于inputText有空格等其它符号，并且已经是URL编码过的，所以需要解码
            inputText = urllib.parse.unquote(inputText)
            if opt == "Enzyme_Name":
                Enzymes = Nirs.objects.filter(Enzyme_Name = inputText)
            elif opt == "Nuc_GenBank ID":
                Enzymes = Nirs.objects.filter(GenBank_ID = inputText)
            print("-----in broswer-------")
            # 使用完inputText之后，需要再传递到浏览器中，所以需要编码
            inputText = urllib.parse.quote(inputText)
                
    if len(Enzymes) == 0:
        Enzymes = Nirs.objects.all()    
    total_num = len(Enzymes)
    max_pages = (total_num) // 10 + 1  # 判断是否超出最大页
    if  page > max_pages:
        page = max_pages
    Enzymes = Enzymes[(page - 1) * 10: (page) * 10]
    length = pagination_args(page, total_num)
    return render(request, "Enzymes/NirS.html",
                    {"title":"NirS",
                     "page":page,
                     "length":length,
                     "total_num":total_num,
                     "From_brosower":From_brosower,
                     "opt":opt,
                     "inputText":inputText,
                     "Enzymes":Enzymes})    

def qNorB(request, opt = None, inputText = None, page = 1):
    Enzymes = []
    if page < 1:
        page = 1
    From_brosower = False
    
    if request.method == "GET":
        enzymesForm = EnzymesForm(request.GET)
        if enzymesForm.is_valid():
            print("is_valid")
            opt = enzymesForm.cleaned_data["opt"]
            inputText = enzymesForm.cleaned_data["inputText"]
            print("is_valid")
            if opt == "Enzyme_Name":
                Enzymes = qNorb.objects.filter(Enzyme_Name = inputText)
            elif opt == "Nuc_GenBank ID":
                Enzymes = qNorb.objects.filter(GenBank_ID = inputText)
            inputText = urllib.parse.quote(inputText) # 之后要将inputText放到URL，所以需要编码
            From_brosower = True
        elif opt is not None:
            From_brosower = True
            # 由于inputText有空格等其它符号，并且已经是URL编码过的，所以需要解码
            inputText = urllib.parse.unquote(inputText)
            if opt == "Enzyme_Name":
                Enzymes = qNorb.objects.filter(Enzyme_Name = inputText)
            elif opt == "Nuc_GenBank ID":
                Enzymes = qNorb.objects.filter(GenBank_ID = inputText)
            print("-----in broswer-------")
            # 使用完inputText之后，需要再传递到浏览器中，所以需要编码
            inputText = urllib.parse.quote(inputText)
    if len(Enzymes) == 0:
        Enzymes = qNorb.objects.all()    
    total_num = len(Enzymes)
    max_pages = (total_num) // 10 + 1  # 判断是否超出最大页
    if  page > max_pages:
        page = max_pages
    Enzymes = Enzymes[(page - 1) * 10: (page) * 10]
    length = pagination_args(page, total_num)
    return render(request, "Enzymes/qNorB.html",
                    {"title":"qNorB",
                     "page":page,
                     "length":length,
                     "total_num":total_num,
                     "From_brosower":From_brosower,
                     "opt":opt,
                     "inputText":inputText,
                     "Enzymes":Enzymes})     
    
def cNorB(request, opt = None, inputText = None, page = 1):
    Enzymes = []
    From_brosower = False
    if page < 1:
        page = 1
    # ----------------------------从表单获取来的数据-------------------------------    
    if request.method == "GET":
        enzymesForm = EnzymesForm(request.GET)
        print("GET")
        if enzymesForm.is_valid():
            opt = enzymesForm.cleaned_data["opt"]
            inputText = enzymesForm.cleaned_data["inputText"]
            if opt == "Enzyme_Name":
                Enzymes = cNorb.objects.filter(Enzyme_Name = inputText)
            elif opt == "Nuc_GenBank ID":
                Enzymes = cNorb.objects.filter(GenBank_ID = inputText)
            inputText = urllib.parse.quote(inputText)
            From_brosower = True
        elif opt is not None:
            From_brosower = True
            # 由于inputText有空格等其它符号，并且已经是URL编码过的，所以需要解码
            inputText = urllib.parse.unquote(inputText)
            if opt == "Enzyme_Name":
                Enzymes = cNorb.objects.filter(Enzyme_Name = inputText)
            elif opt == "Nuc_GenBank ID":
                Enzymes = cNorb.objects.filter(GenBank_ID = inputText)
            print("-----in broswer-------")
            # 使用完inputText之后，需要再传递到浏览器中，所以需要编码
            inputText = urllib.parse.quote(inputText)
    # ---------------------------------------------------------------------------

    if len(Enzymes) == 0:
        Enzymes = cNorb.objects.all()    
    total_num = len(Enzymes)
    max_pages = (total_num) // 10 + 1  # 判断是否超出最大页
    if  page > max_pages:
        page = max_pages
    Enzymes = Enzymes[(page - 1) * 10: (page) * 10]
    length = pagination_args(page, total_num)
    return render(request, "Enzymes/cNorB.html",
                    {"title":"cNorB",
                     "page":page,
                     "length":length,
                     "total_num":total_num,
                     "From_brosower":From_brosower,
                     "opt":opt,
                     "inputText":inputText,
                     "Enzymes":Enzymes})
    
def NosZ(request, opt = None, inputText = None, page = 1):
    Enzymes = []
    if page < 1:
        page = 1
    From_brosower = False
    
    if  opt is not None:
            From_brosower = True
            # 由于inputText有空格等其它符号，并且已经是URL编码过的，所以需要解码
            inputText = urllib.parse.unquote(inputText)
            if opt == "Enzyme_Name":
                Enzymes = Nosz.objects.filter(Enzyme_Name = inputText)
            elif opt == "Nuc_GenBank ID":
                Enzymes = Nosz.objects.filter(GenBank_ID = inputText)
            print("-----in broswer-------")
            # 使用完inputText之后，需要再传递到浏览器中，所以需要编码
            inputText = urllib.parse.quote(inputText)
    elif  request.method == "GET":
            enzymesForm = EnzymesForm(request.GET)
            if enzymesForm.is_valid():
                print("is_valid")
                opt = enzymesForm.cleaned_data["opt"]
                inputText = enzymesForm.cleaned_data["inputText"]
                print("is_valid")
                if opt == "Enzyme_Name":
                    Enzymes = Nosz.objects.filter(Enzyme_Name = inputText)
                elif opt == "Nuc_GenBank ID":
                    Enzymes = Nosz.objects.filter(GenBank_ID = inputText)
                inputText = urllib.parse.quote(inputText) # 之后要将inputText放到URL，所以需要编码
                From_brosower = True
        
    if len(Enzymes) == 0:
        Enzymes = Nosz.objects.all()    
    total_num = len(Enzymes)
    Enzymes = Enzymes[(page - 1) * 10: (page) * 10]
    length = pagination_args(page, total_num)
    return render(request, "Enzymes/NosZ.html",
                    {"title":"NosZ",
                     "page":page,
                     "length":length,
                     "total_num":total_num,
                     "From_brosower":From_brosower,
                     "opt":opt,
                     "inputText":inputText,
                     "Enzymes":Enzymes})     


def EnzymesDetail(request, EnzymeName, GenBank_ID):
    print(EnzymeName, " and ", GenBank_ID)
    Enzyme = ""
    if EnzymeName == "NapA":
        Enzyme = Napa.objects.get(GenBank_ID = GenBank_ID)
    elif EnzymeName == "NarG":
        Enzyme = Narg.objects.get(GenBank_ID = GenBank_ID)
    elif EnzymeName == "cNorB":
        Enzyme = cNorb.objects.get(GenBank_ID = GenBank_ID)
    elif EnzymeName == "NirK":
        Enzyme = Nirk.objects.get(GenBank_ID = GenBank_ID)
    elif EnzymeName == "NirS":
        Enzyme = Nirs.objects.get(GenBank_ID = GenBank_ID)
    elif EnzymeName == "NosZ":
        Enzyme = Nosz.objects.get(GenBank_ID = GenBank_ID)
    elif EnzymeName == "qNorB":
        Enzyme = qNorb.objects.get(GenBank_ID = GenBank_ID)
    return render(request,"Enzymes/detail.html",
                {
                    "title":GenBank_ID,
                    "Enzyme": Enzyme,
                })


# ----------------------------------------------------------------
def Product(request, page = 1):
    productList = products.objects.all()
    total_num = len(productList)        
    productList = productList[(page - 1) * 10 : page * 10]
    
    div = int(total_num / 10) + 1
    if page <= 0:
        page = 1
    elif page > div:
        page = div
    if page + 10 > div:
        length = list(range(page, div))
    else:
        length = list(range(page, page + 10))
    
    
    return render(request,"products/product.html",
                {"title":"product",
                "products":productList,
                "page" : page,
                "length":length,
                "total_num": total_num,
                })    

def productMicro(request, opt = None, inputText = None, page = 1):
    if page < 1:
        page = 1
    flag = [False, False]#用来控制哪个进度条有效
    productList = []
    if request.method == "POST":
        form = ProductForm(request.POST )
        print("GET")
        
        if form.is_valid():
            print("is_valid")
            opt = form.cleaned_data["opt"]
            inputText = form.cleaned_data['inputText']
            if opt == "Microorganism":
                productList = products.objects.filter(Microorganism = inputText)
                flag[0] = True
            elif opt == "Accession Number":
                productList = products.objects.filter(Accesion_Number = inputText)
                flag[1] = True
    # 如果是从进度条进来的，就需要重新获取数据
    else:
        if opt == "Microorganism":
            productList = products.objects.filter(Microorganism = inputText)
            flag[0] = True
        elif opt == "Accession Number":
            productList = products.objects.filter(Accesion_Number = inputText)
            flag[1] = True
    total_num = len(productList)        
    productList = productList[(page - 1) * 10 : page * 10]
    length = pagination_args(page, total_num)
    print("len = ", len(productList))
    # 如果点击的进度条超越了当前数据,就返回第一页
    #if len(productList) == 0 :
    #    return redirect('/denitrifications_app/Product/')
    
    length = pagination_args(page = page, total_num = total_num)
        
    return render(request,"products/product.html",
                    {"title":inputText,
                "products":productList,
                "page" : page,
                "length":length,
                "total_num": total_num,
                "Microorganism":flag[0],
                "Accesion_Number":flag[1],
                "opt":opt,
                "inputText":inputText,   
                })

"""
    objects.filter(field = given_args) 返回一个字段包含此参数的索引集(Query Set).
        可以通过下标索引object
    
    object.get(field = given_args) 返回一个字段包含此参数的实体
"""
def product_detail(request, Accession_num):
    pro = products.objects.get(Accesion_Number = Accession_num)
    print(pro.Title)
    return render(request,"products/detail.html", 
                {"title":Accession_num,
                 "product": pro})
# ----------------------------------------------------------------


def pagination_args(page, total_num):
    length = []
    div = int(total_num / 10) + 1
    if page <= 0:
        page = 1
    elif page > div:
        page = div
    if page + 10 > div:
        length = list(range(page, div + 1))
    else:
        length = list(range(page, page + 10))
    if len(length) is None:
        length = [1]
    return length

def add(request):
    flag = False
    your_name = ""
    your_age = ""
    """ if request.method == "GET":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            flag = True
            print("is_valid")
            your_name = form.cleaned_data["your_name"]
            your_age  = form.cleaned_data["your_age"]
             """
    if request.is_ajax():
        print("is_ajax")
        your_name = request.GET('name')
        your_age  = request.GET('age')
        return JsonResponse(str(your_name+str(your_age)))
    else:
        print("no_vaild")
        your_name = "..."
        your_age  = "..."   
    return render(request,"add.html",
                  {'your_name':your_name,'your_age':your_age})


def path_svg(request):
    print("pathway_svg")
    return render(request, "pathway/path.html") 

# -----------------------------prediction---------------------
def prediction(request):
    return render(request, "Predictions/Prediction.html")

def hmmer(request):
    return render(request, "Predictions/hmmer.html")

def blast(rquest):
    return render(rquest, "Predictions/blast.html")

def clusto(request):
    seq = ""
    download = ""
    if request.method == "GET":
        hmmer_tool = Hmmer_tool(request.GET)
        if hmmer_tool.is_valid():
            seq = hmmer_tool.cleaned_data['sequence']
            
            """
                写入到多序列比对文件中
            """    

            with open('/root/peiji/denitrifications/templates/Predictions/multiAligmnt.fasta', mode = "w+", encoding="utf-8") as fp:
                
                fp.write(seq)
            cmd = ".././clustalo -i /root/peiji/denitrifications/templates/Predictions/multiAligmnt.fasta -o /root/peiji/denitrifications/dataset/genes/protein_result/output.tbout --outfmt clu --force" # --force就是强制重写
            os.system(cmd)
            seq = ""
            with open("/root/peiji/denitrifications/dataset/genes/protein_result/output.tbout", mode="r", encoding="utf-8") as fp:
                for line in fp.readlines():
                    seq+=line
            return render(request, "Predictions/paste.html",{                                                                                                                      
        "sequence": seq,
    }) 
    elif request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)  # 从表单中获取文件
        if form.is_valid():
            file = request.FILES['file'] # 获取文件名为 'file'的文件
            with open('/root/peiji/denitrifications/templates/Predictions/multiAligmnt.fasta', 'wb+') as fp:
                for chunk in file.chunks(): # 打开另外一个文件，将从表单获取到的文件内容以二进制的形式写入
                    fp.write(chunk) 
            cmd = ".././clustalo -i /root/peiji/denitrifications/templates/Predictions/multiAligmnt.fasta -o /root/peiji/denitrifications/dataset/genes/protein_result/output.tbout --outfmt clu --force" # --force就是强制重写
            os.system(cmd)
            seq = ""
            with open("/root/peiji/denitrifications/dataset/genes/protein_result/output.tbout", mode="r", encoding="utf-8") as fp:
                for line in fp.readlines():
                    seq+=line
            return render(request, "Predictions/paste.html",{                                                                                                                      
        "sequence": seq,
    })
    return render(request, "Predictions/clustaO.html")

def phylotree(request):
    if request.method == "GET":
        hmmer_tool = Hmmer_tool(request.GET)
        if hmmer_tool.is_valid():
            seq = hmmer_tool.cleaned_data['sequence']
            
            # 获得数据之后，就把数据写到文件中
            with open('physeq.fasta', mode = "w") as fp:
                fp.write(seq)
            
            # 数据写完之后，就需要使用clustalo把多序列比对的文件变成phy格式的输出
            cmd = ".././clustalo -i physeq.fasta -o infile --outfmt phy --force"           
            os.system(cmd)
            # 这里，多序列比对文件infile就制作好了，接下来，要使用命令制作进化树
            cmd = "proml <input> screenout &" # 已经将proml程序放到/usr/bin/,可以直接使用
            os.system(cmd)
            # 需要注意的是制作这个进化树需要很长时间，需要必须要保证输出文件有内容时才可以返回
            data = ""
            while len(data) == 0:
                if os.path.exists("outtree"):   
                    with open("outtree", mode = "r") as fp:
                        data = fp.read()
            # 写完之后，要把之前生成的文件删除，防止再次出现
            cmd = "rm -rf outtree outfile "
            os.system(cmd)
            data = data[:-1]
            return render(request, "Predictions/phylotree_result.html",{'data':data})
    elif request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)  # 从表单中获取文件
        if form.is_valid():
            file = request.FILES['file'] # 获取文件名为 'file'的文件
            with open('physeq.fasta', 'wb+') as fp:
                for chunk in file.chunks(): # 打开另外一个文件，将从表单获取到的文件内容以二进制的形式写入
                    fp.write(chunk)
            # 数据写完之后，就需要使用clustalo把多序列比对的文件变成phy格式的输出
            cmd = ".././clustalo -i physeq.fasta -o infile --outfmt phy --force"           
            os.system(cmd)
            # 这里，多序列比对文件infile就制作好了，接下来，要使用命令制作进化树
            cmd = "proml <input> screenout &" # 已经将proml程序放到/usr/bin/,可以直接使用
            os.system(cmd)
            # 需要注意的是制作这个进化树需要很长时间，需要必须要保证输出文件有内容时才可以返回
            data = ""
            while len(data) == 0:
                if os.path.exists("outtree"):   
                    with open("outtree", mode = "r") as fp:
                        data = fp.read()
            # 写完之后，要把之前生成的文件删除，防止再次出现
            cmd = "rm -rf outtree outfile "
            os.system(cmd)
            data = data[:-1]
            return render(request, "Predictions/phylotree_result.html",{'data':data})
            

            
    return render(request, "Predictions/phylotree.html",)


def paste(request):
    sequence = ""
    if request.method == "GET":
        hmmer_tool = Hmmer_tool(request.GET)
        if hmmer_tool.is_valid():
            sequence = hmmer_tool.cleaned_data["sequence"] #获得sequence
            """
                写入得到的sequence文件，用phmmer比对，最后返回结果
            """
            
            with open("/root/peiji/denitrifications/dataset/genes/protein_result/input.fasta", mode="w+", encoding="utf-8") as fp:
                fp.write(str(sequence))
                download = "/dataset/genes/protein_result/output.tbout"
            
            cmd = "phmmer -o /root/peiji/denitrifications/dataset/genes/protein_result/output.tbout /root/peiji/denitrifications/dataset/genes/protein_result/input.fasta /root/peiji/denitrifications/dataset/genes/proteins.fasta"
            os.system(cmd)
            with open("/root/peiji/denitrifications/dataset/genes/protein_result/output.tbout", mode="r", encoding="utf-8") as fp:
                for line in fp.readlines():
                    sequence+=line
    return render(request, "Predictions/paste.html",{                                                                                                                      
        "sequence": sequence,
    })
    
def upload(request):  
    sequence = ""
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)  # 从表单中获取文件
        if form.is_valid():
            file = request.FILES['file'] # 获取文件名为 'file'的文件
            with open('/root/peiji/denitrifications/dataset/genes/protein_result/input.fasta', 'wb+') as fp:
                for chunk in file.chunks(): # 打开另外一个文件，将从表单获取到的文件内容以二进制的形式写入
                    fp.write(chunk) 
            # 写入之后就执行phmmer的命令
            cmd = "phmmer -o /root/peiji/denitrifications/dataset/genes/protein_result/output.tbout /root/peiji/denitrifications/dataset/genes/protein_result/input.fasta /root/peiji/denitrifications/dataset/genes/proteins.fasta"
            os.system(cmd)
            
            # 将比对的结果传入sequence中，用以在页面中显示
            with open("/root/peiji/denitrifications/dataset/genes/protein_result/output.tbout", mode="r", encoding="utf-8") as fp:
                for line in fp.readlines():
                    sequence+=line
    return render(request, "Predictions/paste.html",{                                                                                                                      
        "sequence": sequence,
    })


def idsearch(request):
    sequence = "No sequence was selected"
    path = ["/root/peiji/denitrifications/dataset/genes/Nuc.fasta", "/root/peiji/denitrifications/dataset/genes/proteins.fasta"]
    #path = ["E:\\program_project\\Python\\Enzyme_fasta\\Nuc.fasta", "E:\\program_project\\Python\\protein_seq\\proteins.fasta"]
    if request.method == "GET":
        id = ID(request.GET)
        if id.is_valid():
            _format = id.cleaned_data["format"]
            _id = id.cleaned_data["id"]
            if _format == "nucleic acid sequence":
                sequence = search_Id(path = path[0], ID = _id)
            else:
                sequence = search_Id(path = path[1], ID = _id)
    
            with open("/root/peiji/denitrifications/dataset/seq.fasta", "w") as fp:
                fp.write(sequence)
        
    return render(request, "Predictions/downloadSeq.html",{                                                                                                                      
        "sequence": sequence,
    })

def search_Id(path, ID):
    flag = False
    sequence = ""
    with open(path, mode="r") as fp:
        for line in fp.readlines():
            if line[0] == ">":
                if line.split(" ")[0][1:] == ID:
                    flag = True
                elif flag == True: # 说明此时已经写入了(flag=True)，但是遇见新的sequence，那么就不用遍历了  
                    flag = False
                    break
            if flag:
                sequence +=line
    #with open("/root/peiji/denitrifications/dataset/genes/protein_result/output.tbout", mode='w') as fp:
    #    fp.write(sequence)
    return sequence


# --------------------------------------提供下载链接---------------------
def download(request):
    file=open('/root/peiji/denitrifications/dataset/genes/protein_result/output.tbout','rb')
    response =FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="out.tbout"'
    return response

def downloadSeq(request):
    file=open('/root/peiji/denitrifications/dataset/seq.fasta','rb')
    response =FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="seq.fasta"'
    return response

def downloadGenes(request):
    """
        下载Genes文件
    """
    file=open('/root/peiji/denitrifications/dataset/Genes_excel/Enzymes_new_layout.xlsx','rb')
    response =FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="Genes.xlsx"'
    return response
    
def downloadStrains(request):
    """
        下载Strains文件
    """
    file=open('/root/peiji/denitrifications/dataset/Strains_excel/Products_new_layout.xlsx','rb')
    response =FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="Strains.xlsx"'
    return response

def downloadSequence(request):
    """
        下载Sequence文件
    """
    file=open('/root/peiji/denitrifications/dataset/seqDownload/sequence.zip','rb')
    response =FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="sequence.zip"'
    return response

def downloadDenitriSystem(request):
    """
        下载dentrification System文件
    """
    file=open('/root/peiji/denitrifications/dataset/microbialdenitrification_systems_table.xlsx','rb')
    response =FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="microbialdenitrification_systems_table.xlsx"'
    return response

def downloadBioreactor(request):
    """
        下载dentrification System文件
    """
    file=open('/root/peiji/denitrifications/dataset/Bioreactors_for_wastewater_treatment.xlsx','rb')
    response =FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="Bioreactors_for_wastewater_treatment.xlsx"'
    return response



# ------------------------blast----------------------------------
def blastpaste(request):
    sequence = ""
    download = ""
    if request.method == "GET":
        hmmer_tool = Hmmer_tool(request.GET)
        if hmmer_tool.is_valid():
            sequence = hmmer_tool.cleaned_data["sequence"] #获得sequence
            """
                写入得到的sequence文件，用phmmer比对，最后返回结果
            """
            
            with open("/root/peiji/denitrifications/dataset/genes/protein_result/input.fasta", mode="w+", encoding="utf-8") as fp:
                fp.write(sequence)
                download = "/dataset/genes/protein_result/output.tbout"
            cmd = "blastn -db /root/peiji/denitrifications/dataset/genes/Nuc.fasta -query /root/peiji/denitrifications/dataset/genes/protein_result/input.fasta  -out /root/peiji/denitrifications/dataset/genes/protein_result/output.tbout -index_name /root/peiji/denitrifications/dataset/genes/NucDataBase/Nuc_all.asnb"
            os.system(cmd)
            with open("/root/peiji/denitrifications/dataset/genes/protein_result/output.tbout", mode="r", encoding="utf-8") as fp:
                for line in fp.readlines():
                    sequence+=line
    return render(request, "Predictions/paste.html",{                                                                                                                      
        "sequence": sequence,
    })

def blastupload(request):
    sequence = ""
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)  # 从表单中获取文件
        if form.is_valid():
            file = request.FILES['file'] # 获取文件名为 'file'的文件
            with open('/root/peiji/denitrifications/dataset/genes/protein_result/input.fasta', 'wb+') as fp:
                for chunk in file.chunks(): # 打开另外一个文件，将从表单获取到的文件内容以二进制的形式写入
                    fp.write(chunk) 
            # 写入之后就执行phmmer的命令
            cmd = "blastn -db /root/peiji/denitrifications/dataset/genes/Nuc.fasta -query /root/peiji/denitrifications/dataset/genes/protein_result/input.fasta  -out /root/peiji/denitrifications/dataset/genes/protein_result/output.tbout -index_name /root/peiji/denitrifications/dataset/genes/NucDataBase/Nuc_all.asnb"
            os.system(cmd)
            
            # 将比对的结果传入sequence中，用以在页面中显示
            with open("/root/peiji/denitrifications/dataset/genes/protein_result/output.tbout", mode="r", encoding="utf-8") as fp:
                for line in fp.readlines():
                    sequence+=line
    return render(request, "Predictions/paste.html",{                                                                                                                      
        "sequence": sequence,
    })
# --------------------------------------------------------------

def enzyme(request):
    print("enzyme")
    return render(request, "Reaction/Enzyme.html")

def enzyme_narg(request):
    print(enzyme_narg)
    return render(request, "Reaction/Enzyme_Narg.html")

def enzyme_napa(request):
    print("enzyme_napa")
    return render(request, "Reaction/Enzyme_Napa.html")

def enzyme_nirk(request):
    print("enzyme_napa")
    return render(request, "Reaction/Enzyme_Nirk.html")

def enzyme_nirs(request):
    print("enzyme_napa")
    return render(request, "Reaction/Enzyme_Nirs.html") 

def enzyme_norc(request):
    print("enzyme_napa")
    return render(request, "Reaction/Enzyme_Norc.html")

def enzyme_norb(request):
    print("enzyme_napa")
    return render(request, "Reaction/Enzyme_Norb.html")

def enzyme_nosz(request):
    print("enzyme_napa")
    return render(request, "Reaction/Enzyme_Nosz.html")          

def mechanism(request):

    return render(request, "Reaction/Mechanisms.html")


def nitrate_reduction(request, num):
    
    return render(request, "Reaction/NitrateReduction.html",{"num":num})

# ----------------------------------denitrifications System------------------------
def WastewaterTreat(request, page = 1):
    Datas = ""
    if request.method == "GET":
        system = System(request.GET)
        if system.is_valid():
            print("is_valid")
            opt = system.cleaned_data["opt"]
            inputText = system.cleaned_data["inputText"]
            print("is_valid")
            if opt == "Influent":
                Datas = WaterTreatmentPlant.objects.filter(Influent_Source_Type = inputText)
            elif opt == "Denitrifying_reactor":
                Datas = WaterTreatmentPlant.objects.filter(Denitrifying_Reactor = inputText)
            inputText = urllib.parse.quote(inputText) # 之后要将inputText放到URL，所以需要编码
            From_brosower = True
            
    if len(Datas) == 0:
        Datas = WaterTreatmentPlant.objects.all() 
    total_num = len(Datas)
    if page > int(total_num / 10) + 1:
        page = int(total_num / 10) + 1 # max_pages
    length = pagination_args(page, total_num)
    Datas = Datas[(page - 1) * 10: page * 10]
    return render(request, "DenitrificationSystem/WasteWaterTreat.html",
                  {
                      "Datas": Datas,
                      "page":page,
                  })

def FreshwaterSystems(request, page = 1):
    Datas = ""
    if request.method == "GET":
        system = System(request.GET)
        if system.is_valid():
            print("is_valid")
            opt = system.cleaned_data["opt"]
            inputText = system.cleaned_data["inputText"]
            print("is_valid")
            if opt == "Influent":
                Datas = FreshwaterSystem.objects.filter(Influent_Source_Type = inputText)
            elif opt == "Denitrifying_reactor":
                Datas = FreshwaterSystem.objects.filter(Denitrifying_Reactor = inputText)
            inputText = urllib.parse.quote(inputText) # 之后要将inputText放到URL，所以需要编码
            From_brosower = True
    if len(Datas) == 0:
        Datas = FreshwaterSystem.objects.all() 
    total_num = len(Datas)
    if page > int(total_num / 10) + 1:
        page = int(total_num / 10) + 1 # max_pages
    length = pagination_args(page, total_num)
    Datas = Datas[(page - 1) * 10: page * 10]
    return render(request, "DenitrificationSystem/FreshwaterSystems.html",
                  {
                      "Datas": Datas,
                      "page":page,
                  })

def MarineSystems(request, page = 1):
    Datas = ""
    
    if request.method == "GET":
        system = System(request.GET)
        if system.is_valid():
            print("is_valid")
            opt = system.cleaned_data["opt"]
            inputText = system.cleaned_data["inputText"]
            print("is_valid")
            if opt == "Influent":
                Datas = MarineSystem.objects.filter(Influent_Source_Type = inputText)
            elif opt == "Denitrifying_reactor":
                Datas = MarineSystem.objects.filter(Denitrifying_Reactor = inputText)
            inputText = urllib.parse.quote(inputText) # 之后要将inputText放到URL，所以需要编码
            From_brosower = True
            
    if len(Datas) == 0:
        Datas = MarineSystem.objects.all() 
    total_num = len(Datas)
    if page > int(total_num / 10) + 1:
        page = int(total_num / 10) + 1 # max_pages
    length = pagination_args(page, total_num)
    Datas = Datas[(page - 1) * 10: page * 10]
    return render(request, "DenitrificationSystem/MarineSystems.html",
                  {
                      "Datas": Datas,
                      "page":page,
                  })

def GroundwaterSystems(request, page = 1):
    Datas = ""
    
    if request.method == "GET":
        system = System(request.GET)
        if system.is_valid():
            print("is_valid")
            opt = system.cleaned_data["opt"]
            inputText = system.cleaned_data["inputText"]
            print("is_valid")
            if opt == "Influent":
                Datas = GoundwaterSystem.objects.filter(Influent_Source_Type = inputText)
            elif opt == "Denitrifying_reactor":
                Datas = GoundwaterSystem.objects.filter(Denitrifying_Reactor = inputText)
            inputText = urllib.parse.quote(inputText) # 之后要将inputText放到URL，所以需要编码
            From_brosower = True
            
    if len(Datas) == 0:
        Datas = GoundwaterSystem.objects.all() 
    total_num = len(Datas)
    if page > int(total_num / 10) + 1:
        page = int(total_num / 10) + 1 # max_pages
    length = pagination_args(page, total_num)
    Datas = Datas[(page - 1) * 10: page * 10]
    return render(request, "DenitrificationSystem/GroundwaterSystems.html",
                  {"Datas": Datas,
                   "page":page,
                  }
                  )

def WetlandsRiparinZone(request, page = 1):
    Datas = ""
    
    if request.method == "GET":
        system = System(request.GET)
        if system.is_valid():
            print("is_valid")
            opt = system.cleaned_data["opt"]
            inputText = system.cleaned_data["inputText"]
            print("is_valid")
            if opt == "Influent":
                Datas = WetlandRiparianZones.objects.filter(Influent_Source_Type = inputText)
            elif opt == "Denitrifying_reactor":
                Datas = WetlandRiparianZones.objects.filter(Denitrifying_Reactor = inputText)
            inputText = urllib.parse.quote(inputText) # 之后要将inputText放到URL，所以需要编码
            From_brosower = True
            
    if len(Datas) == 0:
        Datas = WetlandRiparianZones.objects.all() 
    total_num = len(Datas)
    if page > int(total_num / 10) + 1:
        page = int(total_num / 10) + 1 # max_pages
    length = pagination_args(page, total_num)
    Datas = Datas[(page - 1) * 10: page * 10]
    return render(request, "DenitrificationSystem/WetlandsRiparinZones.html",
                  {
                      "Datas": Datas,
                      "page":page,
                  })

def sulphurRemoval(request, page = 1):
    Datas = ""
    
    if request.method == "GET":
        system = System(request.GET)
        if system.is_valid():
            print("is_valid")
            opt = system.cleaned_data["opt"]
            inputText = system.cleaned_data["inputText"]
            print("is_valid")
            if opt == "Influent":
                Datas = SulphurRemoval.objects.filter(Influent_Source_Type = inputText)
            elif opt == "Denitrifying_reactor":
                Datas = SulphurRemoval.objects.filter(Denitrifying_Reactor = inputText)
            inputText = urllib.parse.quote(inputText) # 之后要将inputText放到URL，所以需要编码
            From_brosower = True
            
    if len(Datas) == 0:
        Datas = SulphurRemoval.objects.all() 
    total_num = len(Datas)
    if page > int(total_num / 10) + 1:
        page = int(total_num / 10) + 1 # max_pages
    length = pagination_args(page, total_num)
    Datas = Datas[(page - 1) * 10: page * 10]
    return render(request, "DenitrificationSystem/SulphurRemoval.html",
                  {
                      "Datas": Datas,
                      "page":page,
                  })
def  download(request):
    return render(request, "Download.html")


def about(request):
    return render(request, "about.html")

def submit(request):
    print("submit")
    if request.method == "GET":
        print("submit get")
        submit = Submit(request.GET)
        
        if submit.is_valid():
            print("is valid")
    
    return render(request, "submit.html")

def contact(request):
    print("contact")
    if request.method == "GET":
        print("contact get")
        submit = Contact(request.GET)
        if submit.is_valid():
            print("contact is valid")
    return render(request, "contact.html")

def FluidizedBedReactors(request):
    return render(request, "Bioreactor/FluidizedBedReactors.html")
def ContinuousStirredTankReactor(request):
    return render(request, "Bioreactor/ContinuousStirredTankReactor.html")

def MovingBedBiofilmReactor(request):
    return render(request, "Bioreactor/MovingBedBiofilmReactor.html")

def PackedBedReactor(request):
    return render(request, "Bioreactor/PackedBedReactor.html")

def MembraneBioreactor(request):
    return render(request, "Bioreactor/MembraneBioreactor.html")

def SequencingBatchBioreactor(request):
    return render(request, "Bioreactor/SequencingBatchBioreactor.html")