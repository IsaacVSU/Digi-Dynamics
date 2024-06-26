from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse


from .forms import Games, Demo, DLC, Music, userform
# from .models import select
# from .ReadGames.database.Connect_DB import connect, close_connection


from .Django_handlers import searchHander, searchHander_demo, login_Handler, liked_games, insert_into_LikedGames, likedHistory, dislike_game

# Create your views here.
# Syntax: for rendering, so inside of these template html files will be a {{}} that uses a dictionary. 
# render(response, htmlFile, dict)
# dictionary will have variable tokens so that way you can put them into the application.
# NOTE: Use this aspect of django to render informationf from the database

def signOut(response):
    print(response.POST)
    if response.POST.get("logout"):
        response.session["session_id"] = None
        return True
    return False

def base(response):
    userLoggedIn = False
    if response.session.get("session_id"):
        userLoggedIn = True
        if signOut(response):
            userLoggedIn = False

    return_dict = {
        "loggedIn" : userLoggedIn,
    }
    return render(response, "main/base.html", return_dict)


def home(response):
    userLoggedIn = False
    if response.session.get("session_id"):
        userLoggedIn = True
    
    return render(response, "main/home.html", {"loggedIn" : userLoggedIn,})


def games(response):
    form = Games()
    games = []
    userLoggedIn = False

    # This if statement will never run bc the response.method will be "GET"
    if response.session.get("session_id"):
        userLoggedIn = True

    if response.method == "POST":
        game_id = response.POST.get("liked")
        print(game_id)
        if userLoggedIn:
            insert_into_LikedGames(response.session.get("session_id"), game_id)

        return JsonResponse({"status": "success"})
            
    elif userLoggedIn and response.method == "GET":
        Already_liked_games = liked_games(response.session.get("session_id"))
        print(Already_liked_games)

        searchBy = response.GET.get("SearchBy", None)

        searchHander(response, "Games", searchBy, games)

        for game in games:
            if Already_liked_games.get(game["id"]):
                game["liked"] = True
            else:
                game["liked"] = False
            
        
    elif response.method == "GET":
        print("GET REQUEST")
        print(response.GET)

        searchBy = response.GET.get("SearchBy", None)
        searchHander(response,"Games", searchBy, games)
        for game in games:
            game["liked"] = False 

    return_dict = {
        "form": form,
        "games" : games,
        "display": "none" if len(games) == 0 else "block",
        "displayLike" : "block" if userLoggedIn else "none",
        "loggedIn" : userLoggedIn,
    }

    
    return render(response, "main/games.html", return_dict)


def music(response):
    form = Music()
    Music_list = []
    userLoggedIn = False

    if response.session.get("session_id"):
        userLoggedIn = True

    if response.method == "GET":
        searchBy = response.GET.get("SearchBy", None)
        searchHander(response, "Music", searchBy, Music_list)
    return_dict = {
        'form' : form,
        "musics" : Music_list,
        "display": "none" if len(Music_list) == 0 else "block",
        "loggedIn" : userLoggedIn,
        "displayLike" : "block" if userLoggedIn else "none",
    }
    return render(response, "main/music.html", return_dict)


def dlc_view(response):
    form = DLC()
    DLC_list = []
    userLoggedIn = False

    if response.session.get("session_id"):
        userLoggedIn = True
    
    if response.method == "GET":
        searchBy = response.GET.get("SearchBy", None)

        # print(searchBy)
        searchHander(response, "DLC", searchBy, DLC_list)
    
    return_dict = {
        'form' : form,
        'DLC' : DLC_list,
        "display": "none" if len(DLC_list) == 0 else "block",
        "loggedIn" : userLoggedIn,
        "displayLike" : "block" if userLoggedIn else "none",
    }

    return render(response, "main/DLC.html", return_dict)


def demo(response):
    form = Demo()
    games = []
    userLoggedIn = False

    if response.session.get("session_id"):
        userLoggedIn = True


    print(response.session.get("session_id"))
    if response.method == "GET":
        print("GET REQUEST")
        print(response.GET)

        searchBy = response.GET.get("SearchBy", None)
        searchHander_demo(response,"Demo", searchBy, games)
        for game in games:
            game["liked"] = False 

    return_dict = {
        "form" : form,
        "loggedIn" : userLoggedIn,
        "displayLike" : "block" if userLoggedIn else "none",
        "display" : "block" if len(games) > 0 else 'none',
        "Demo" : games,
    }
    return render(response, "main/demo.html", return_dict)


def user(response):
    # TODO: Implement liked history here
    games = []
    userLogIN = False
    username = response.session.get("session_id")

    if response.POST and username:
        # disliking_game
        # Do this for all the others
        dislike_id = response.POST.get('game')
        dislike_game(username, dislike_id, "LikedGames")
        

    if username:
        userLogIN = True
        likedGames = likedHistory(response, "LikedGames")
        for game in likedGames:
            games.append(game)
    # print(games)

    return_dict = {
        "loggedIn" : userLogIN,
        "games" : games,
        "display" : "block" if len(games) != 0 else 'None',
        
    }
    return render(response, "main/history.html", return_dict)

def login(response):

    userLoggedIn = False

    if response.session.get("session_id"):
        userLoggedIn = True


    log_out_display = None
    form = userform(response.POST or None)
    login_msg = None


    # print(response.POST)
    # print(response.POST.get("logout"))
    # print(response.session.get("session_id"))

    if response.POST.get("logout"):
        response.session["session_id"] = None
        return redirect("home")

    if response.session.get("session_id"):
        log_out_display = 'block'

    elif response.method == "POST" and form.is_valid():
        uname = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        if login_Handler(uname, password):
            response.session["session_id"] = uname
            login_msg = "Login successful"
            log_out_display = 'block'
            return redirect("home")
        else:
            login_msg = "Login error"
        
    

    return_dict = {
        "form" : form,
        "alert_msg": login_msg,
        "log_out" : log_out_display,
        "loggedIn" : userLoggedIn,
    }
    return render(response, "main/login.html", return_dict)
