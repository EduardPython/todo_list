#Vytvoření Django projektu
- virtualni prostredi "mkvirtualenv todo_list"
- instalace Django do toho prostředí
- vytvoření requirements.txt (echo "Django~=4.0.4 > requirements.txt" (vytvoří soubor requirements.txt a uloží do něj závislost Django)
- vytvorit projekt "django-admin startproject todo_list"
- migrace internich Django modelů "python manage.py migrate"
- vytvoreni appky python "manage.py startapp base"
- v settings.py pridat nazev appky do INSTALLED_APPS
- pridani urls.py do slozky base
- do base/urls.py pridano:
    from django.urls import path
    from nazev_appky import views

    urlpatterns = [] (sem pak prijdou vsechny url)
- vytvoreni slozky templates a v ní slozku base a v ní homepage.html #sem prijdou vsechny html sablony
- v todo_list/urls.py pridano:
    path("", include("base.urls"))
- - vytvoreni superusera pro pristup do 127.0.0.1:8000/admin. "python manage.py createsuperuser"
- tvorba modelu Task v models.py #základ appky, z tohoto se berou data pro views
- registrace modelu Task v admin.py     #aby jsme mohly v 127.0.0.1:8000/admin zkouknout jak vypadá náš model Task a můžeme přidat na zkoušku nějaké ukoly
- ve views.py vytvořen TaskListView pro zobrazovani vytvorenych ukolu pomoci nejake sablony
- base/urls.py > pridáno nase nove >view< a >name< pro odkazy na tuto stranku: path("", TaskListView.as_view(), name="tasks"),
- vytvoreni base.html jako základu pro ostatní podstránky. tady bude hlavička se všemi "must have" html věcmi
- v homepage.html uprava na {% extends %}, odteď všechny html "rozšiřují" základní base.html

# VIRTUALENVWRAPPER
- create VE:
>mkvirtualenv name_of_new_ve (location: user/Envs)
- activate VE:
>workon name_of_existing_ve
- deactivate: 
>deactivate
- list of ve:
>lsvirtualenv

# CSS
- vytvořen soubor base.css ve složce static/css/
- import a pridani urlpatterns do urls.py
- v settings.py pridany cesty ke statics files
- do base.html pridan {% load static %} a link.... pro načtení css
- proveden prikaz "python manage.py collectstatic"

#LOGIN 
- aby se nepřihlášenéému uživateli nezobrazil obsah, stačí importovat LoginRequiredMixin a přidat je k dědění do views
které chceme nepřihlášeným zablokovat

- když někdo nepřihlášený příjde na stránku používající "loginrequiredmixin" můžeme v settings.py nastavit
  LOGIN_URL = "login" (zkratka v urlpaterns v urls.py), k přesměrování na přihlašovací formulář. Jinak django zahlásí prosté "page not found error 404"

# GIT BRANCHES
##vytvoření větve:
>git branch name_of_branch      (pouze vytvoří větev)\
>git checkout -b name_of_branch     (vytvoří větev a přepne se na ni)
##smazání větve:
>git branch -d name_of_branch       (smaže lokální větev)\
> git push origin -delete name_of_branch        (smaže větev na remotu)

##stáhnutí změn:
(musím být přepnutý na větvi kterou chci aktualizovat)
 >git pull
##přepínání mezi větvemi:
 >git checkout name_of_branch\
 >git switch name_of_branch 
##zobrazení aktivní větve:
 >git status
##seznam větví:
 >git branch\
> git beanch -a
##výpis commitů:
>git log
