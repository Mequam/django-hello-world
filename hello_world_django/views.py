from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.template import loader

# Create your views here.

"""
********************************************************************
 FUNCTION NAME: scare_responce
********************************************************************
 WRITTEN BY: David Kennamer
 DATE CREATED: January 16, 2024
********************************************************************
 FUNCTION PURPOSE:
 
 generate an http response of an ominous page to scare the user into
 behaving
********************************************************************
 CALLS: 
 (NONE) 
********************************************************************
 PARAMETER LIST (In Parameter Order):
********************************************************************
 RETURNS:
 
 HttpResponse Object containing ominous text
********************************************************************
 SAMPLE INVOCATION:
 
 scare_responce()
********************************************************************
"""
def scare_responce():
    return HttpResponse('''you are here because you sent invalid data,
                            admins have been notified *^*''')

"""
********************************************************************
 FUNCTION NAME: hello_world_basic
********************************************************************
 WRITTEN BY: David Kennamer
 DATE CREATED: January 16, 2024
********************************************************************
 FUNCTION PURPOSE: display a basic hello world view
********************************************************************
 CALLS: 
 (NONE) 
********************************************************************
 PARAMETER LIST (In Parameter Order):
 request - django request object
********************************************************************
 RETURNS:
 
 HttpResponseObject with instructions to render a page that displays
 hello world
********************************************************************
 SAMPLE INVOCATION:
 
 hello_world_basic()
********************************************************************
"""
def hello_world_basic(request):
    if request.method == 'GET':
        return HttpResponse('hello world')
    else:
        return scare_responce()

"""
********************************************************************
 FUNCTION NAME: static_hello_world
********************************************************************
 WRITTEN BY: David Kennamer
 DATE CREATED: January 16, 2024
********************************************************************
 FUNCTION PURPOSE: 
 
 generate a hello world page that includes static resources
 from django
********************************************************************
 CALLS: 
 (NONE) 
********************************************************************
 PARAMETER LIST (In Parameter Order):
 req - django requests object
********************************************************************
 RETURNS:
 HttpResponse that includes a hello world site and links to djangos static objects
********************************************************************
 SAMPLE INVOCATION:

 static_hello_world()
********************************************************************
"""
def static_hello_world(req):
    hello_world_template = loader.get_template('hello_world.html')
    return HttpResponse(hello_world_template.render({},req))

"""
********************************************************************
 FUNCTION NAME: hello_world_paramaters
********************************************************************
 WRITTEN BY: David Kennamer
 DATE CREATED: January 16, 2024
********************************************************************
 FUNCTION PURPOSE:
 
 create a web page that says hello world followed by the name 
 of the user passed through in a GET parameter
********************************************************************
 CALLS: 
 scare_responce
 multi_name_hello_world
********************************************************************
 PARAMETER LIST (In Parameter Order):
 req - django request object
********************************************************************
 RETURNS:
 HttpResponse object containing either the rendered page or the scare_responce 
 if invalid data is detected
********************************************************************
 SAMPLE INVOCATION:
 hello_world_paramaters()
********************************************************************
"""
def hello_world_paramaters(req):
    if req.method != 'GET':
        return scare_responce()
    
    #POST paramaters use the .POST method from the request
    #this can also be done using regex in a configuration file,
    #see hello_world_reg_params for an example
    names = req.GET.get('names',None)
    if names == None:
        return scare_responce()

    return multi_name_hello_world(names.split(','))


"""
********************************************************************
 FUNCTION NAME: multi_name_hello_world
********************************************************************
 WRITTEN BY: David Kennamer
 DATE CREATED: January 16, 2024
********************************************************************
 FUNCTION PURPOSE: general purpos
********************************************************************
 CALLS: 
********************************************************************
 PARAMETER LIST (In Parameter Order):
 names - array of strings containing names to be rendered in the ret val
********************************************************************
 RETURNS:
 HttpResponse object that details a page that says hello world to each
 name inside of the names variable
********************************************************************
 SAMPLE INVOCATION:
 
 multi_name_hello_world(['jhon','steve','sue'])

********************************************************************
 LOCAL VARIABLE LIST (Alphabetically):

 param_template
********************************************************************
"""
def multi_name_hello_world(names : [str]):
    param_template = loader.get_template('hello_world_params.html')
    return HttpResponse(
            param_template.render({'names':names})
            )

"""
********************************************************************
 FUNCTION NAME: hello_world_url_paramaters
********************************************************************
 WRITTEN BY: David Kennamer
 DATE CREATED: January 16, 2024
********************************************************************
 FUNCTION PURPOSE: 
 say hello world to a list of names as specified in a url paramater 
 from django
********************************************************************
 CALLS: 
 multi_name_hello_world
********************************************************************
 PARAMETER LIST (In Parameter Order):
 req - django requests object
 names - comma seperated list of names to render
********************************************************************
 RETURNS:
 HttpResponse object containing the rendered page
********************************************************************
 SAMPLE INVOCATION:

 hello_world_url_paramaters(request,'steve,bob,alice')
********************************************************************
"""
def hello_world_url_paramaters(req,names : str):
    return multi_name_hello_world(names.split(','))

