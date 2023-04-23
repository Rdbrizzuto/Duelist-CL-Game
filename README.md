# Duelist-clGame
A command line game called "Duelist" in which you engage in a rock-paper-scissors like duel with your opponent. 

To run the game you just need to type "Python3 Duelist.py" into your command line
(While in the directory that the script is stored in)

In the game you fight another player in a deadly duel.
In the duel you and your opponent will attempt to either strike the other or block the other's strike.
Whether your strike or block is successful will depend on what your opponent does.

- If you both strike in the same direction then your swords will clang together, causing no damage.
(Note: an example of the "same direction" would be player 1 choosing to strike left, and player 2 choosing to strike right. As the duelists are facing towards each other, that would mean both strike in the same direction)

- If you both strike opposite sides then both parties will take 5 damage.

- If you strike your opponent and they block on the opposite side, then they will take 5 damage.

- If you strike your opponent and they block on the same side, then they will strike back at you and deal 10 damage while you are staggered. 

- If both parties block then no damage is done

You both start at 20 health, and whoever drops to 0 first loses.
