init:
    $ c = Character("Claudia", color=(250, 203, 252))

init:
    $ s = Character("Sienna", color=(203, 252, 211))

init:
    $ a = Character("Ashlynn", color=(180, 216, 255))

init:
    $ n = Character("Nila", color=(198, 180, 255))

init:
    $ cr = Character("Christine", color=(126, 9, 36, 255))



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg hallway

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show christine sprite

    # These display lines of dialogue.

    cr "This is a work in progress."

    cr "So fuck off shithead"

    # This ends the game.
    # I super hope this works

    return

    # blahblahblah