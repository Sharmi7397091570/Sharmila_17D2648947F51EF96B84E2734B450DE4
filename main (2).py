class Player:
  def play(self):
      print("The player is playing cricket.")


class Batsman(Player):
  def play(self):
      print("The batsman is batting.")


class Bowler(Player):
  def play(self):
      print("The bowler is bowling.")


# Testing the Player, Batsman, and Bowler classes
if _name_ == "_main_":
  player = Player()
  player.play()  # Output: The player is playing cricket.

  batsman = Batsman()
  batsman.play()  # Output: The batsman is batting.

  bowler = Bowler()
  bowler.play()  # Output: The bowler is bowling.