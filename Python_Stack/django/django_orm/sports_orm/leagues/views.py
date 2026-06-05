from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q

from . import team_maker

def index(request):

	context = {
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		# query 1: All baseball leagues
		'baseball_leagues' : League.objects.filter(sport="Baseball"),
		# all women's leagues
		'womens_leagues' : League.objects.filter(name__icontains="women"),
		# all leagues where sport is any hockey
		"hockey_leagues": League.objects.filter(sport__icontains="hockey"),
		# all leagues where sport is something OTHER THAN football
		"not_football": League.objects.exclude(sport="Football"),
		# all leagues that call themselves "conferences."
        "conferences": League.objects.filter(name__icontains="conference"),
		# all leagues in the Atlantic region
        "atlantic_leagues": League.objects.filter(name__icontains="Atlantic"),
		# all teams based in Dallas
		"dallas_teams" :Team.objects.filter(location = 'Dallas'),
		# all teams named the Raptors
		"raptors": Team.objects.filter(team_name="Raptors"),
		# all teams whose location includes "City."
        "city_teams": Team.objects.filter(location__icontains="City"),
		# all teams whose names begin with "T."
        "t_teams": Team.objects.filter(team_name__startswith="T"),
		# all teams, ordered alphabetically by location
        "ordered_teams_loc": Team.objects.all().order_by("location"),
		# all teams, ordered by team name in reverse alphabetical order
        "ordered_teams_name_rev": Team.objects.all().order_by("-team_name"),
		# every player with the last name "Cooper."
        "cooper_players": Player.objects.filter(last_name="Cooper"),
		# every player with the first name "Joshua."
        "joshua_players": Player.objects.filter(first_name="Joshua"),
		# every player with the previous name "Cooper" EXCEPT those with "Joshua" as the first name
        "cooper_not_joshua": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		# all players with the first name "Alexander" OR first name "Wyatt
        "alex_or_wyatt": Player.objects.filter(Q(first_name="Alexander") | Q(first_name="Wyatt")),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
	
	