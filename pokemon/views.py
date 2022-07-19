from django.http import HttpResponse
from .models import Pokemon


def get_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    pokemon_data_list = "\n".join(
        f"{pokemon.id} - {pokemon.name}")
    return HttpResponse(f"<b>{pokemon_data_list}</b>")


def get_pokemon_list(request):
    pokemon_list = Pokemon.objects.all()
    pokemon_list = "\n".join(
        f"<p>{pokemon.id} - {pokemon.name} - {pokemon.type} - {pokemon.hp} - {pokemon.active} <p>" for pokemon in pokemon_list)
    return HttpResponse(f"<b>{pokemon_list}</b>")
