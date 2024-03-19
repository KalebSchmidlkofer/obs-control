from django.views import generic, View
from django.shortcuts import render, redirect
from .obs_integration import obs
from .models import scene
from django.http import JsonResponse
import logging
from threading import Thread
from time import sleep


logging.basicConfig(level=logging.DEBUG)

class ObsList(generic.ListView):
    queryset = scene.objects.all().order_by('id')  # Replace scene with your actual model
    
    def get_queryset(self):
        return scene.objects.all().order_by('id')  # Replace scene with your actual model

    context_object_name = 'obs_list'
    template_name = 'control_panel/panel.html'

def execute_command_view(request):
    if request.method == 'POST' and request.is_ajax():
        scene_id = request.POST.get('scene_id')

        # Perform the desired command execution based on the scene_id

        # Return a JSON response indicating the success or failure
        return JsonResponse({'status': 'success'})

    # Return a JSON response with an error if the request method is not valid
    return JsonResponse({'status': 'error'})


def recreate_entries(request):
  # Delete all existing entries
  scene.objects.all().delete()
  
  # List of items to recreate
  item_list = obs.requests.list_scenes()

  # Recreate entries from the item list
  for item in item_list:
      scene.objects.create(name=item, active=False)

  # Redirect to a success page or the desired URL
  return redirect('panel')  # Replace 'success-page' with the appropriate URL name
  
def change_scene(request, scene_name):
    # Set all active scenes to inactive
    scene.objects.filter(active=True).update(active=False)
    obs.requests.change_scene(scene_name)
    for item in scene.objects.all():
      if item.name == scene_name:
        item.active = True
        item.save()
      else:
        item.active = False
        item.save()
  
    # scene.objects.filter(active=True)
    return redirect('panel')

def active_scene():
  scene = obs.active_scene()
  return scene

def index(request):
  return render(request, 'control_panel/panel.html')
  
  

class events(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.observer = obs.Observer()

    def get(self, request):
        return render(request, 'your_template.html')

    def dispatch(self, request, *args, **kwargs):
        thread = Thread(target=self.start_observer)
        thread.start()
        return super().dispatch(request, *args, **kwargs)

    def start_observer(self):
        while self.observer.running:
            sleep(0.1)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add necessary context variables
        return context