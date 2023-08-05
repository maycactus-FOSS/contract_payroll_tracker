from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Contract
from .forms import ContractForm

def contract_list(request):
    clicked_column = request.GET.get('sort_column')

    sort_column = request.session.get('sort_column', 'date')
    sort_order = request.session.get('sort_order', 'desc')

    if clicked_column:
        if sort_column != clicked_column:
            sort_column = clicked_column
            sort_order = 'asc' if sort_column == 'place' else 'desc'
        else:
            sort_order = 'asc' if sort_order == 'desc' else 'desc'

    request.session['sort_column'] = sort_column
    request.session['sort_order'] = sort_order

    if sort_order == 'asc':
        contracts = Contract.objects.order_by(sort_column)
    else:
        contracts = Contract.objects.order_by('-' + sort_column)
    items_per_page = int(request.GET.get('items_per_page', 10))
    
    paginator = Paginator(contracts, items_per_page)
    page = request.GET.get('page')

    try:
        contracts_page = paginator.page(page)
    except PageNotAnInteger:
        contracts_page = paginator.page(1)
    except EmptyPage:
        contracts_page = paginator.page(paginator.num_pages)
    
    context = {
        'contracts': contracts_page,
        'items_per_page': items_per_page,
    }
    return render(request, 'contracts/contract_list.html', context=context)

def contract_create(request):
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contract_list')
    else:
        form = ContractForm()
    return render(request, 'contracts/contract_create_form.html', {'form': form})

def contract_update(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('contract_list')
    else:
        form = ContractForm(instance=contract)
    return render(request, 'contracts/contract_update_form.html', {'form': form})

def contract_delete(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        contract.delete()
        return redirect('contract_list')
    return render(request, 'contracts/contract_confirm_delete.html', {'contract': contract})

def contract_detail(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    return render(request, 'contracts/contract_detail.html', {'contract': contract})