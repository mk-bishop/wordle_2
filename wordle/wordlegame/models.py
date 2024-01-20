from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#models make the database tables

#user model #followed a tutorial idk why it's called post
#does it have a password? idk
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title


#input field?

#stats
#generate emoji jawns

#possible solutions
#accepted guesses
    
# Game Model:

# Store information about each game session.
# Fields may include: game ID, start time, end time, status (ongoing, completed), and a reference to the player(s) involved.
# Word Model:

# Store words used in the game.
# Fields may include: word ID, word value, and a reference to the game it belongs to.
# Guess Model:

# Store each guess made by a player.
# Fields may include: guess ID, guessed word, correctness (whether the guess is correct or not), and a reference to the game.
# Player Model:

# Store information about players.
# Fields may include: player ID, name, and a reference to the game they are participating in.
# Feedback Model:

# Store feedback for each guess.
# Fields may include: feedback ID, feedback message, and a reference to the corresponding guess.
