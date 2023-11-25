from django.shortcuts import get_object_or_404, render, redirect
from .models import Fertilisation , Modéle_Variante


from django.shortcuts import render

def about (request): 
    return render(request, 'about.html')
def accordion (request): 
    return render(request, 'accordion.html')
def alerts (request): 
    return render(request, 'alerts.html')
def avatar (request): 
    return render(request, 'avatar.html')
def background (request): 
    return render(request, 'background.html')
def badge (request): 
    return render(request, 'badge.html')
def blog_details (request): 
    return render(request, 'blog-details.html')
def blog_edit (request): 
    return render(request, 'blog-edit.html')
def blog (request): 
    return render(request, 'blog.html')
def border (request): 
    return render(request, 'border.html')
def breadcrumbs (request): 
    return render(request, 'breadcrumbs.html')
def buttons (request): 
    return render(request, 'buttons.html')
def calendar2 (request): 
    return render(request, 'calendar2.html')
def cards (request): 
    return render(request, 'cards.html')
def carousel (request): 
    return render(request, 'carousel.html')
def cart (request): 
    return render(request, 'cart.html')
def chart_chartjs (request): 
    return render(request, 'chart-chartjs.html')
def chart_echart (request): 
    return render(request, 'chart-echart.html')
def chart_flot (request): 
    return render(request, 'chart-flot.html')
def chart_morris (request): 
    return render(request, 'chart-morris.html')
def chart_nvd3 (request): 
    return render(request, 'chart-nvd3.html')
def chat (request): 
    return render(request, 'chat.html')
def checkout (request): 
    return render(request, 'checkout.html')
def client_create (request): 
    return render(request, 'client-create.html')
def clients (request): 
    return render(request, 'clients.html')
def colors (request): 
    return render(request, 'colors.html')
def construction (request): 
    return render(request, 'construction.html')
def counters (request): 
    return render(request, 'counters.html')
def datatable (request): 
    return render(request, 'datatable.html')
def display (request): 
    return render(request, 'display.html')
def dropdown (request): 
    return render(request, 'dropdown.html')
def empty (request): 
    return render(request, 'empty.html')
def error404 (request): 
    return render(request, 'error404.html')
def error500 (request): 
    return render(request, 'error500.html')
def error501 (request): 
    return render(request, 'error501.html')
def faq (request): 
    return render(request, 'faq.html')
def file_attachments (request): 
    return render(request, 'file-attachments.html')
def file_manager_1 (request): 
    return render(request, 'file-manager-1.html')
def file_manager_2 (request): 
    return render(request, 'file-manager-2.html')
def file_manager (request): 
    return render(request, 'file-manager.html')
def flex (request): 
    return render(request, 'flex.html')
def footers (request): 
    return render(request, 'footers.html')
def forgot_password (request): 
    return render(request, 'forgot-password.html')
def form_advanced (request): 
    return render(request, 'form-advanced.html')
def form_editable (request): 
    return render(request, 'form-editable.html')
def form_elements (request): 
    return render(request, 'form-elements.html')
def form_layouts (request): 
    return render(request, 'form-layouts.html')
def form_validation (request): 
    return render(request, 'form-validation.html')
def form_wizard (request): 
    return render(request, 'form-wizard.html')
def gallery (request): 
    return render(request, 'gallery.html')
def height (request): 
    return render(request, 'height.html')
def icons (request): 
    return render(request, 'icons.html')
def icons2 (request): 
    return render(request, 'icons2.html')
def icons3 (request): 
    return render(request, 'icons3.html')
def icons4 (request): 
    return render(request, 'icons4.html')
def icons5 (request): 
    return render(request, 'icons5.html')
def icons6 (request): 
    return render(request, 'icons6.html')
def icons7 (request): 
    return render(request, 'icons7.html')
def icons8 (request): 
    return render(request, 'icons8.html')
def icons9 (request): 
    return render(request, 'icons9.html')
def icons10 (request): 
    return render(request, 'icons10.html')
def index (request): 
    return render(request, 'index.html')
def invoice_create (request): 
    return render(request, 'invoice-create.html')
def invoice_details (request): 
    return render(request, 'invoice-details.html')
def invoice_edit (request): 
    return render(request, 'invoice-edit.html')
def invoice_list (request): 
    return render(request, 'invoice-list.html')
def invoice_timelog (request): 
    return render(request, 'invoice-timelog.html')
def landing (request): 
    return render(request, 'landing.html')
def loaders (request): 
    return render(request, 'loaders.html')
def lockscreen (request): 
    return render(request, 'lockscreen.html')
def login (request): 
    return render(request, 'login.html')
def mail_compose (request): 
    return render(request, 'mail-compose.html')
def mail_inbox (request): 
    return render(request, 'mail-inbox.html')
def mail_read (request): 
    return render(request, 'mail-read.html')
def mail_settings (request): 
    return render(request, 'mail-settings.html')
def maps (request): 
    return render(request, 'maps.html')
def maps1 (request): 
    return render(request, 'maps1.html')
def maps2 (request): 
    return render(request, 'maps2.html')
def margin (request): 
    return render(request, 'margin.html')
def mediaobject (request): 
    return render(request, 'mediaobject.html')
def modal (request): 
    return render(request, 'modal.html')
def navigation (request): 
    return render(request, 'navigation.html')
def notify (request): 
    return render(request, 'notify.html')
def offcanvas (request): 
    return render(request, 'offcanvas.html')
def opacity (request): 
    return render(request, 'opacity.html')
def padding (request): 
    return render(request, 'padding.html')
def pagination (request): 
    return render(request, 'pagination.html')
def panels (request): 
    return render(request, 'panels.html')
def position (request): 
    return render(request, 'position.html')
def pricing (request): 
    return render(request, 'pricing.html')
def product_details (request): 
    return render(request, 'product-details.html')
def products (request): 
    return render(request, 'products.html')
def profile (request): 
    return render(request, 'profile.html')
def progress (request): 
    return render(request, 'progress.html')
def project_details (request): 
    return render(request, 'project-details.html')
def project_edit (request): 
    return render(request, 'project-edit.html')
def project_new (request): 
    return render(request, 'project-new.html')
def projects_list (request): 
    return render(request, 'projects-list.html')
def projects (request): 
    return render(request, 'projects.html')
def rangeslider (request): 
    return render(request, 'rangeslider.html')
def rating (request): 
    return render(request, 'rating.html')
def register (request): 
    return render(request, 'register.html')
def scroll (request): 
    return render(request, 'scroll.html')
def services (request): 
    return render(request, 'services.html')
def settings (request): 
    return render(request, 'settings.html')
def sweetalert (request): 
    return render(request, 'sweetalert.html')
def switcherpage (request): 
    return render(request, 'switcherpage.html')
def table_editable (request): 
    return render(request, 'table-editable.html')
def tables (request): 
    return render(request, 'tables.html')
def tabs (request): 
    return render(request, 'tabs.html')
def tags (request): 
    return render(request, 'tags.html')
def task_create (request): 
    return render(request, 'task-create.html')
def task_edit (request): 
    return render(request, 'task-edit.html')
def tasks_list (request): 
    return render(request, 'tasks-list.html')
def terms (request): 
    return render(request, 'terms.html')
def thumbnails (request): 
    return render(request, 'thumbnails.html')
def ticket_details (request): 
    return render(request, 'ticket-details.html')
def timeline (request): 
    return render(request, 'timeline.html')
def tooltipandpopover (request): 
    return render(request, 'tooltipandpopover.html')
def treeview (request): 
    return render(request, 'treeview.html')
def typography (request): 
    return render(request, 'typography.html')
def users_list (request): 
    return render(request, 'users-list.html')
def width (request): 
    return render(request, 'width.html')
def wishlist (request): 
    return render(request, 'wishlist.html')
def wysiwyag (request): 
    return render(request, 'wysiwyag.html')



###################   CRUD   Fertilisation ###################

def create_fertilisation(request):
    if request.method == 'POST':
        nom_commercial = request.POST.get('Nom_Commercial')
        image = request.FILES.get('image')
        quantite_total = request.POST.get('QuantiteTotal')
        quantite_h = request.POST.get('Quantite_H')
        n = request.POST.get('N')
        k2o = request.POST.get('K2O')
        p2o5 = request.POST.get('P2O5')
        pour_plante = bool(request.POST.get('Pour_Plante'))
        pour_arbre = bool(request.POST.get('Pour_Arbre'))
        pour_semis = bool(request.POST.get('Pour_Semis'))

        fertilisation = Fertilisation(
            Nom_Commercial=nom_commercial,
            image=image,
            QuantiteTotal=quantite_total,
            Quantite_H=quantite_h,
            N=n,
            K2O=k2o,
            P2O5=p2o5,
            Pour_Plante=pour_plante,
            Pour_Arbre=pour_arbre,
            Pour_Semis=pour_semis
        )
        fertilisation.save()
        return redirect('fertilisation_list')

    return render(request, 'Fertilisation/create_fertilisation.html')


def fertilisation_list(request):
    fertilisations = Fertilisation.objects.all()
    return render(request, 'Fertilisation/fertilisation_list.html', {'fertilisations': fertilisations})


def update_fertilisation(request, pk):
    fertilisation = Fertilisation.objects.get(pk=pk)
    
    if request.method == 'POST':
        nom_commercial = request.POST.get('Nom_Commercial')
        image = request.FILES.get('image')
        quantite_total = request.POST.get('QuantiteTotal')
        quantite_h = request.POST.get('Quantite_H')
        n = request.POST.get('N')
        k2o = request.POST.get('K2O')
        p2o5 = request.POST.get('P2O5')
        pour_plante = bool(request.POST.get('Pour_Plante'))
        pour_arbre = bool(request.POST.get('Pour_Arbre'))
        pour_semis = bool(request.POST.get('Pour_Semis'))

        fertilisation.Nom_Commercial = nom_commercial
        if image:
            fertilisation.image = image
        fertilisation.QuantiteTotal = quantite_total
        fertilisation.Quantite_H = quantite_h
        fertilisation.N = n
        fertilisation.K2O = k2o
        fertilisation.P2O5 = p2o5
        fertilisation.Pour_Plante = pour_plante
        fertilisation.Pour_Arbre = pour_arbre
        fertilisation.Pour_Semis = pour_semis
        
        fertilisation.save()
        return redirect('fertilisation_list')
    
    return render(request, 'Fertilisation/update_fertilisation.html', {'fertilisation': fertilisation})



def fertilisation_detail(request, pk):
    fertilisation = Fertilisation.objects.get(pk=pk)
    return render(request, 'Fertilisation/fertilisation_detail.html', {'fertilisation': fertilisation})

def delete_fertilisation(request, pk):
    fertilisation = Fertilisation.objects.get(pk=pk)
    
    if request.method == 'POST':
        fertilisation.delete()
        return redirect('fertilisation_list')
    
    return render(request, 'Fertilisation/delete_fertilisation.html', {'fertilisation': fertilisation})



###################   CRUD   Modéle_Variante #################

def create_ModéleVraiante(request):
    if request.method == 'POST':
        categorie = request.POST.get('categorie')
        sous_categorie = request.POST.get('sous_categorie')
        nom_variante = request.POST.get('nom_variante')
        nombre_etape = int(request.POST.get('nombre_etape'))
        description = request.POST.get('description')
        debut_saison = request.POST.get('debut_saison')
        fin_saison = request.POST.get('fin_saison')

        modéle_variante = Modéle_Variante.objects.create(
            categorie=categorie,
            sous_categorie=sous_categorie,
            nom_variante=nom_variante,
            nombre_etape=nombre_etape,
            description=description,
            debut_saison=debut_saison,
            fin_saison=fin_saison
        )
        modéle_variante.save()
        return redirect('list_M')  # Rediriger vers la liste des produits ou une autre vue

    return render(request, 'Modéle/create_Modéle.html')



def Modéle_list(request):
    modéles = Modéle_Variante.objects.all()
    return render(request, 'Modéle/Modéle_list.html', {'modéles': modéles})



def edit_modéle(request, pk):
    
    modéle = Modéle_Variante.objects.get(pk=pk)
    if request.method == 'POST':
        # Mise à jour des données du formulaire
        modéle.categorie = request.POST['categorie']
        modéle.sous_categorie = request.POST['sous_categorie']
        modéle.nom_variante = request.POST['nom_variante']
        modéle.nombre_etape = int(request.POST['nombre_etape'])
        modéle.description = request.POST['description']
        modéle.debut_saison = request.POST['debut_saison']
        modéle.fin_saison = request.POST['fin_saison']
        
        modéle.save()
        return redirect('list_M')
    return render(request, 'Modéle/edit_modéle.html', {'modéle': modéle})

def delete_modéle(request, pk):
    modéle = Modéle_Variante.objects.get(pk=pk)
    
    if request.method == 'POST':
        modéle.delete()
        return redirect('list_M')
    
    return render(request, 'Modéle/delete_modéle.html', {'modéle': modéle})



def modèle_details(request, pk):
    modéle = Modéle_Variante.objects.get(pk=pk)
    return render(request, 'Modéle/modéle_details.html', {'modéle': modéle})

from django.shortcuts import render, redirect
from .models import Modéle_Variante, Etape
"""""
def saisie_etapes(request, pk):
    variante = Modéle_Variante.objects.get(pk=pk)
    nb_etape= variante.nombre_etape
    fertilisations = Fertilisation.objects.all()  # Récupérer tous les objets de la classe Fertilisation

    
    if request.method == 'POST':
        nom_etape = request.POST['nom_etape']
        periode_min = int(request.POST['periode_min'])
        periode_max = int(request.POST['periode_max'])
        action_sur_terre = request.POST['action_sur_terre']
        irrigation_quantite = float(request.POST['irrigation_quantite']) if request.POST['irrigation_quantite'] else None
        irrigation_periode = request.POST['irrigation_periode']
        type_fertilisation_id = int(request.POST['type_fertilisation']) if request.POST['type_fertilisation'] else None
        type_fertilisation_quantite = float(request.POST['type_fertilisation_quantite']) if request.POST['type_fertilisation_quantite'] else None
        type_fertilisation_periode = request.POST['type_fertilisation_periode']
        
        etape = Etape.objects.create(
            variante=variante,
            nom_etape=nom_etape,
            periode_min=periode_min,
            periode_max=periode_max,
            action_sur_terre=action_sur_terre,
            irrigation_quantite=irrigation_quantite,
            irrigation_periode=irrigation_periode,
            type_fertilisation_id=type_fertilisation_id,
            type_fertilisation_quantite=type_fertilisation_quantite,
            type_fertilisation_periode=type_fertilisation_periode,
            image=request.FILES.get('image'),  # Récupère le fichier image
        )
        etape.save()
        return redirect('list_M')
    
    context = {'variante': variante , 'fertilisations': fertilisations}
    return render(request, 'Modéle/saisieEtape.html', context)
"""""

"""""
from django.shortcuts import render, redirect
from .models import Modéle_Variante, Etape, Fertilisation

def saisie_etapes(request, pk):
    variante = Modéle_Variante.objects.get(pk=pk)
    nb_etape = variante.nombre_etape
    fertilisations = Fertilisation.objects.all()  # Récupérer tous les objets de la classe Fertilisation

    if request.method == 'POST':
        # Traiter le formulaire pour chaque étape
        for i in range(1, nb_etape+1):
            nom_etape = request.POST[f'nom_etape_{i}']
            periode_min = int(request.POST[f'periode_min_{i}'])
            periode_max = int(request.POST[f'periode_max_{i}'])
            action_sur_terre = request.POST[f'action_sur_terre_{i}']
            irrigation_quantite = float(request.POST[f'irrigation_quantite_{i}']) if request.POST[f'irrigation_quantite_{i}'] else None
            irrigation_periode = request.POST[f'irrigation_periode_{i}']
            type_fertilisation_id = int(request.POST[f'type_fertilisation_{i}']) if request.POST[f'type_fertilisation_{i}'] else None
            type_fertilisation_quantite = float(request.POST[f'type_fertilisation_quantite_{i}']) if request.POST[f'type_fertilisation_quantite_{i}'] else None
            type_fertilisation_periode = request.POST[f'type_fertilisation_periode_{i}']

            etape = Etape.objects.create(
                variante=variante,
                nom_etape=nom_etape,
                periode_min=periode_min,
                periode_max=periode_max,
                action_sur_terre=action_sur_terre,
                irrigation_quantite=irrigation_quantite,
                irrigation_periode=irrigation_periode,
                type_fertilisation_id=type_fertilisation_id,
                type_fertilisation_quantite=type_fertilisation_quantite,
                type_fertilisation_periode=type_fertilisation_periode,
                image=request.FILES.get(f'image_{i}'),  # Récupère le fichier image
            )
            etape.save()

        return redirect('list_M')
    
    context = {'variante': variante, 'fertilisations': fertilisations, 'nb_etape': nb_etape}
    return render(request, 'Modéle/saisieEtape.html', context)

"""

"""""

def saisie_etapes(request, pk):
    variante = Modéle_Variante.objects.get(pk=pk)
    nb_etape = variante.nombre_etape
    fertilisations = Fertilisation.objects.all()

    all_steps_entered = False

    if request.method == 'POST':
        for i in range(1, nb_etape + 1):
            nom_etape = request.POST[f'nom_etape_{i}']
            periode_min = int(request.POST[f'periode_min_{i}'])
            periode_max = int(request.POST[f'periode_max_{i}'])
            action_sur_terre = request.POST[f'action_sur_terre_{i}']
            irrigation_quantite = float(request.POST.get(f'irrigation_quantite_{i}', 0))
            irrigation_periode = request.POST[f'irrigation_periode_{i}']
            type_fertilisation_id = int(request.POST.get(f'type_fertilisation_{i}', 0))
            type_fertilisation_quantite = float(request.POST.get(f'type_fertilisation_quantite_{i}', 0))
            type_fertilisation_periode = request.POST[f'type_fertilisation_periode_{i}']
            image = request.FILES.get(f'image_{i}')

            etape = Etape.objects.create(
                variante=variante,
                nom_etape=nom_etape,
                periode_min=periode_min,
                periode_max=periode_max,
                action_sur_terre=action_sur_terre,
                irrigation_quantite=irrigation_quantite,
                irrigation_periode=irrigation_periode,
                type_fertilisation_id=type_fertilisation_id if type_fertilisation_id != 0 else None,
                type_fertilisation_quantite=type_fertilisation_quantite if type_fertilisation_quantite != 0 else None,
                type_fertilisation_periode=type_fertilisation_periode,
                image=image,
            )
            etape.save()

        # Vérification si toutes les étapes ont été saisies
        if Etape.objects.filter(variante=variante).count() >= nb_etape:
            all_steps_entered = True

    context = {'variante': variante, 'fertilisations': fertilisations, 'all_steps_entered': all_steps_entered , 'nb_etape': nb_etape}
    return render(request, 'Modéle/saisieEtape.html', context)
"""""

from django.shortcuts import render, redirect
from .models import Modéle_Variante, Fertilisation, Etape

def saisie_etapes(request, pk):
    variante = Modéle_Variante.objects.get(pk=pk)
    nb_etape = variante.nombre_etape
    fertilisations = Fertilisation.objects.all()

    if request.method == 'POST':
        etapes = []
        for step in range(1, nb_etape + 1):
            nom_etape = request.POST[f'nom_etape_{step}']
            periode_min = int(request.POST[f'periode_min_{step}'])
            periode_max = int(request.POST[f'periode_max_{step}'])
            action_sur_terre = request.POST[f'action_sur_terre_{step}']
            irrigation_quantite = float(request.POST[f'irrigation_quantite_{step}']) if request.POST[f'irrigation_quantite_{step}'] else None
            irrigation_periode = request.POST[f'irrigation_periode_{step}']
            type_fertilisation_id = int(request.POST[f'type_fertilisation_{step}']) if request.POST[f'type_fertilisation_{step}'] else None
            type_fertilisation_quantite = float(request.POST[f'type_fertilisation_quantite_{step}']) if request.POST[f'type_fertilisation_quantite_{step}'] else None
            type_fertilisation_periode = request.POST[f'type_fertilisation_periode_{step}']
            #image=request.FILES.get(f'image_{step}'),  # Récupère le fichier image


            etapes.append({
                'nom_etape': nom_etape,
                'periode_min': periode_min,
                'periode_max': periode_max,
                'action_sur_terre': action_sur_terre,
                'irrigation_quantite': irrigation_quantite,
                'irrigation_periode': irrigation_periode,
                'type_fertilisation_id': type_fertilisation_id,
                'type_fertilisation_quantite': type_fertilisation_quantite,
                'type_fertilisation_periode': type_fertilisation_periode,
                #'image' : image,
            })
        
        # Sauvegardez les étapes dans la base de données
        for etape_data in etapes:
            etape = Etape.objects.create(
                variante=variante,
                nom_etape=etape_data['nom_etape'],
                periode_min=etape_data['periode_min'],
                periode_max=etape_data['periode_max'],
                action_sur_terre=etape_data['action_sur_terre'],
                irrigation_quantite=etape_data['irrigation_quantite'],
                irrigation_periode=etape_data['irrigation_periode'],
                type_fertilisation_id=etape_data['type_fertilisation_id'],
                type_fertilisation_quantite=etape_data['type_fertilisation_quantite'],
                type_fertilisation_periode=etape_data['type_fertilisation_periode'],
                image=request.FILES.get(f'image_{step}'),  # Récupère le fichier image
            )
            etape.save()

        return redirect('list_M')

    context = {'variante': variante, 'nb_etape': nb_etape, 'fertilisations': fertilisations}
    return render(request, 'Modéle/saisieEtape.html', context)


"""""
def saisie_etapes(request, pk):
    variante = Modéle_Variante.objects.get(pk=pk)
    nb_etape = variante.nombre_etape
    fertilisations = Fertilisation.objects.all()

    if request.method == 'POST':
        for i in range(1, nb_etape + 1):
            nom_etape = request.POST.get(f'nom_etape_{i}')
            periode_min = int(request.POST.get(f'periode_min_{i}'))
            periode_max = int(request.POST.get(f'periode_max_{i}'))
            action_sur_terre = request.POST.get(f'action_sur_terre_{i}')
            irrigation_quantite = float(request.POST.get(f'irrigation_quantite_{i}', 0))
            irrigation_periode = request.POST.get(f'irrigation_periode_{i}')
            type_fertilisation_id = int(request.POST.get(f'type_fertilisation_{i}'))
            type_fertilisation_quantite = float(request.POST.get(f'type_fertilisation_quantite_{i}', 0))
            type_fertilisation_periode = request.POST.get(f'type_fertilisation_periode_{i}')
            
            etape = Etape.objects.create(
                variante=variante,
                nom_etape=nom_etape,
                periode_min=periode_min,
                periode_max=periode_max,
                action_sur_terre=action_sur_terre,
                irrigation_quantite=irrigation_quantite,
                irrigation_periode=irrigation_periode,
                type_fertilisation_id=type_fertilisation_id,
                type_fertilisation_quantite=type_fertilisation_quantite,
                type_fertilisation_periode=type_fertilisation_periode,
                image=request.FILES.get(f'image_{i}', None),
            )
            etape.save()
        return redirect('list_M')
    
    context = {'variante': variante, 'fertilisations': fertilisations, 'nb_etape': nb_etape}
    return render(request, 'Modéle/saisieEtape.html', context)
"""

##############################################################





#########################################################################################""""

"""""

def create_fertilisation(request):
    if request.method == 'POST':
        form = FertilisationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fertilisation_list')
    else:
        form = FertilisationForm()
    return render(request, 'create_fertilisation.html', {'form': form})

"""""


"""""
def update_fertilisation(request, pk):
    fertilisation = Fertilisation.objects.get(pk=pk)
    if request.method == 'POST':
        form = FertilisationForm(request.POST, request.FILES, instance=fertilisation)
        if form.is_valid():
            form.save()
            return redirect('fertilisation_list')
    else:
        form = FertilisationForm(instance=fertilisation)
    return render(request, 'Fertilisation/update_fertilisation.html', {'form': form})
"""

"""""
def modèle_details(request, pk):
    modéle = get_object_or_404(Modéle_Variante, pk=pk)
    return render(request, 'modèle_details.html', {'modéle': modéle})
"""


############################################################################################""


