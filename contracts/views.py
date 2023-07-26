# contracts/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contract
from .forms import ContractForm

def contract_list(request):
    contracts = Contract.objects.all()
    return render(request, 'contracts/contract_list.html', {'contracts': contracts})

def contract_create(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contract_list')
    else:
        form = ContractForm()
    return render(request, 'contracts/contract_create_form.html', {'form': form})

def contract_update(request, contract_id):
    contract = get_object_or_404(Contract, id=contract_id)
    if request.method == 'POST':
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('contract_list')
    else:
        form = ContractForm(instance=contract)
    return render(request, 'contracts/contract_update_form.html', {'form': form})

def contract_delete(request, contract_id):
    contract = get_object_or_404(Contract, id=contract_id)
    if request.method == 'POST':
        contract.delete()
        return redirect('contract_list')
    return render(request, 'contracts/contract_confirm_delete.html', {'contract': contract})