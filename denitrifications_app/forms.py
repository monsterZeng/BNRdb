"""
  Django’s role in forms
    numerous items of data of several different types may need to be prepared 
    for display in a form, rendered as HTML, edited using a convenient interface, 
    returned to the server, validated and cleaned up, and then saved or passed on for further processing.
  
  Django handles three distinct parts of the work involved in forms:
  Django处理表单中涉及的三个不同部分
    *preparing and restructuring data to make it ready for rendering
    预处理和重新组织数据，以便于去渲染
    *creating HTML forms for the data
    为数据创建HTML表单
    *receiving and processing submitted forms and data from the client
    接收并且处理从客服端接收过来的数据
  In a similar way that a model class’s fields map to database fields, 
  a form class’s fields map to HTML form <input> elements.
  模型类的字段对应数据库中的字段，表单类的字段映射HTML表单的<input>元素
  
  A form’s fields are themselves classes; they manage form data and perform validation when a form is submitted. 
  表单的字段本身就是一个类，他们管理表单的数据和对提交的表单执行有效性验证(validation).
  
  A form field is represented to a user in the browser as an HTML “widget” - a piece of user interface machinery.
  表单字段一HTML的'widget'的形式展示给浏览器的用户
  Each field type has an appropriate default Widget class, but these can be overridden as required.
  每一个字段类型都右一个合适的默认widget类，这些类还能够被重载
  
  Instantiating, processing, and rendering forms(实例化，处理和渲染表单)
  当我们再Django中渲染表单时，我们通常需要：
    1.能够再视图中找到它
    2.把它传递到模板中
    3.使用模板变量扩展到HTML的标记中
    
  当我们初始化一个表单时，我们选择保留它或者预先填充。例如：
    1.保存模型实例的数据
    2.核对其它地方的数据
    3.获取传递的表单数据
"""
from django import forms

class NameForm(forms.Form):
  """
  max_length是指表单的输入的最大长度，Django接收到表单时，会验证这一数据的长度
  Form实例有一个is_vaild()方法，它会对其所有字段实施验证步骤。当这个方法被调用时，
  如果所有字段都包含有效的数据，它就会：
    return True
    把表单的数据放置在`cleaned_data`属性上
  """
  
  your_name = forms.CharField(label = "Your name", max_length = 100)
  your_age  = forms.IntegerField(label = "Your age", max_value = 100)
  
  
class ProductForm(forms.Form):
  # product视图函数会调用这个类，类里的属性代表着表单name属性所传递过来的值
  opt    = forms.CharField(max_length=50)
  inputText = forms.CharField(max_length=200) 

class EnzymesForm(forms.Form):
  
  opt    = forms.CharField(max_length=50)
  inputText = forms.CharField(max_length=200)
  
class Hmmer_tool(forms.Form):
  sequence = forms.CharField(max_length = 2000000)

class Clusto(forms.Form):
  sequence = forms.CharField(max_length = 2000000)

class UploadFileForm(forms.Form):
  file = forms.FileField()
  
class ID(forms.Form):
  format = forms.CharField(max_length =200)
  id = forms.CharField(max_length = 200)

class System(forms.Form):
  opt       = forms.CharField(max_length = 200)
  inputText = forms.CharField(max_length =200)

class Submit(forms.Form):
  firstName  = forms.CharField(max_length  = 30, required = False)
  lastName   = forms.CharField(max_length  = 30, required = False)
  email   = forms.EmailField(max_length = 200, required = True)
  Pubmed_ID   = forms.CharField(max_length  = 200, required = False)
  Microorganism = forms.CharField(max_length = 200, required = False)
  product     = forms.CharField(max_length = 200, required = False)
  comment     = forms.CharField(max_length = 500, required = False)

class Contact(forms.Form):
  Name = forms.CharField(max_length = 200, required = True)
  Email = forms.EmailField(max_length = 200, required = True)
  Subject = forms.CharField(max_length = 200, required = False)
  Message = forms.CharField(max_length = 500, required = False)