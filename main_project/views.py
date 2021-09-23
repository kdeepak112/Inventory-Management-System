from django.shortcuts import render
from .models import product,location,ProductMovement
# Create your views here.


def home(request):
    return render(request, 'home.html')

def main(request,function):
    db = {
        'product' : product.objects.all(),
        'location' : location.objects.all(),
        'product_movement' : ProductMovement.objects.all()
    }

    info = {'fun_name' : function , 'info_data' : db[function]}
    
    return render(request,'main.html',info)

def operation(request,oper,section):
    print(oper,section)
    print(type(section),type('product'))
    if section == 'product':
        print('inside product')
        if oper == 'add':
            print('inside add')
            p_name = request.GET.get('add_product')
            print(p_name)
            new_data = product(product_name = p_name)
            new_data.save()
        elif oper == 'edit':
            p_id = request.GET.get('p_id')
            p_name = request.GET.get('add_product')
            product.objects.filter(id=p_id).update(product_name = p_name)
        else:
            print('Wrong Operation Entered')
    
    elif section == 'location':
        if oper == 'add':
            l_name = request.GET.get('add_location')
            new_data = location(location=l_name)
            new_data.save()
        elif oper == 'edit':
            l_id = request.GET.get('l_id')
            l_name = request.GET.get('add_location')
            location.objects.filter(id=l_id).update(location=l_name)
        else:
            print('Wrong Operation Entered')
    
    elif section == 'product_movement':
        if oper == 'add':
            fromL = request.GET.get('from_location')
            toL = request.GET.get('to_location')
            p_name = request.GET.get('add_product')
            qty = request.GET.get('qty')
            floc = location.objects.get(location = fromL)
            tloc = location.objects.get(location = toL)
            pName = product.objects.get(product_name = p_name)
            new_data = ProductMovement(from_location=floc,to_location = tloc,product_id = pName,qty = qty )
            new_data.save()
        elif oper == 'edit':
            print('in location edit')
            m_id = request.GET.get('m_id')
            fromL = request.GET.get('from_location')
            toL = request.GET.get('to_location')
            p_name = request.GET.get('add_product')
            qty = request.GET.get('qty')
            floc = location.objects.get(location=fromL)
            tloc = location.objects.get(location=toL)
            pName = product.objects.get(product_name=p_name)
            print('updating')
            print(ProductMovement.objects.filter(id=m_id).update(
                from_location=floc, to_location=tloc, product_id=pName, qty=qty))
        else:
            print('Wrong Operation Entered')
        pass
    else:
        print('nothing matched')
    return render(request, 'home.html')

def balance(request):
    info = {'locations':location.objects.all()}
    return render(request,'location.html',info)

def locBalance(request,loc_id):
    print(loc_id,type(loc_id))
    loc_name = location.objects.get(id=loc_id)
    print('loc_name',loc_name.location)
    moving_in = ProductMovement.objects.filter(to_location = loc_name).filter(from_location = None)
    moving_out = ProductMovement.objects.filter(from_location=loc_name).filter(to_location= None)
    intransit = ProductMovement.objects.filter(from_location = loc_name)

    info = {"l_name":loc_name.location,'m_in':moving_in,'m_out':moving_out,'intransit':intransit}

    return render(request,'final.html',info)
    
