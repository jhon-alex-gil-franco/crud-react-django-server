from django.views import View
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

from api.models import Company


class CompanyView(View):


    # esta funcion permite saltar la autenticacion en las peticiones http del client
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    # metodo que devuelve los resultados ya sea por parametro o el listado completo de las compañias.
    def get(self, request, id=0):
        if (id > 0):
            companies = list(Company.objects.filter(id=id).values())
            if len(companies) > 0:
                company = companies[0]
                data = {'message': "Success", 'company': company}
            else:
                data = {'message': "Company not found..."}
            return JsonResponse(data)
        else:
            companies = list(Company.objects.values())
            if len(companies) > 0:
                data = {'message': "Success", 'companies': companies}
            else:
                data = {'message': "Companies not found..."}
            return JsonResponse(data)

    # metodo para almacer una compañia
    def post(self, request):
        jd = json.loads(request.body)
        Company.objects.create(
            name=jd['name'],
            dir=jd['dir'],
            nit=jd['dir'],
            tel=jd['tel'])
        data = {'message': "Company create"}
        return JsonResponse(data)

    # metodo para editar una compañia
    def put(self, request, id):
        jd = json.loads(request.body)
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            company = Company.objects.get(id=id)
            company.name = jd['name']
            company.dir = jd['dir']
            company.nit = jd['nit']
            company.tel = jd['tel']
            company.save()
            data = {'message': "Company updated"}
        else:
            data = {'message': "Company not found..."}
        return JsonResponse(data)
  
    # metodo para eliminar una compañia
    def delete(self, request, id):
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            Company.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message':"Company not found..."}
        return JsonResponse(data)

  