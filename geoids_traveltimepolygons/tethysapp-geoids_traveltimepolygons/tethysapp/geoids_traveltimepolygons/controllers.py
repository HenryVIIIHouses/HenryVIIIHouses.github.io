from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button
from tethys_sdk.gizmos import RangeSlider
from tethys_sdk.gizmos import TextInput

@login_required()
def home(request):
    """
    Controller for the app home page.
    """


    context = {}

    return render(request, 'geoids_traveltimepolygons/home.html', context)

def map(request):
    slider1 = RangeSlider(display_text='Time of Day',
                          name='slider1',
                          min='6AM',
                          max='9PM',
                          initial='6AM',
                          step=1)
    text_input = TextInput(display_text='Location Search',
                           name='input',
                           placeholder='e.g.: BYU Clyde Building',
                           prepend='')
    map_button = Button(
        display_text='Calculate',
        name='map-button',
        icon='glyphicon glyphicon-globe',
        style='info',
        attributes={
            'data-toggle': 'tooltip',
            'data-placement': 'top',
            'onclick': 'app.bufferPoint()',
            'title': 'Calculate'
        }
    )

    context = {'slider1': slider1,
               'map_button': map_button,
               'text_input': text_input
            }

    return render(request, 'geoids_traveltimepolygons/map.html', context)

def proposal(request):
    context = {
    }

    return render(request, 'geoids_traveltimepolygons/proposal.html', context)

def design(request):
    context = {
    }

    return render(request, 'geoids_traveltimepolygons/design.html', context)
