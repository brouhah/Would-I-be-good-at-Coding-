command = ""
bouncing = False
while True:
  command = input("> ").lower()
  if command == "bounce":
    if bouncing:
      print("Ball is already bouncing!")
    else:
        bouncing = True
        print("The ball has begun bouncing....")
  elif command == "stop":
    if not bouncing:
      print("Ball has already stopped bouncing!")
    else:
      bouncing = False
      print("Bouncing has stopped.")
  elif command == "help":
    print("""
bounce - to bounce the ball
stop - to stop the ball from bouncing
quit - to exit""")
  elif command == "quit":
    print("Thanks for playing! This game was created by Tyler Raniszewski; check him out on GitHub @brouhah!")
    break
else:
  print("Sorry, I don't understand that!")