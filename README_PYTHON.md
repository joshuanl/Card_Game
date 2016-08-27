#Card game used to teach Sidney Chan basics of Python and PyGames

----------------------------
###Crash Course of the Card Game (currently does not have title)
##There are three types of cards
	```Core```, ```Basic```, and ```Special```

Core and Basic cards have ```One Action``` where Special cards may have ```Two Actions```
There are three types of actions, ```Attack```, ```Block```, and ```Heal```.  An attack can only be stopped by a Block card.  Meaning, if an Attack card is played against another Attack card, both players take damage.  If two Block cards are played, nothing will happen.  Heal cards will restore 1 life but is only effective if it's not against an Attack Card.  Thus, if two Heal cards are played, both players will recover 1 life.

#Special Cases
When a Special card is played, it may have two actions.  For the first action, follow the rules above.  For example, the Special card ```Mighty Swing``` works as a single action Basic Attack card but will hit for 3 damage if played against a Heal card.  The ```Double Attack``` card has two actions.  Both actions work as a Basic Attack card.  If played against a card that does not have a second action, the attack will go through.  Resolve each action separately unless the text on the card says otherwise.  This means, if a Double Attack is played against a Basic Block card, the blocking player will only take 1 damage from the second action.


Note that some cards in this Python project do not exist in the physical version (```Overkill``` is unbalanced).

Copyright © 2016 Joshua Lum 
Downloading and playing the game is allowed but the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software/Card Game Concept, and to permit persons to whom the Software/Card Game Concept is furnished to do so, must notify and receive consent from myself and Sidney Chan.  

You may contact us at:
Joshua Lum: jnlcross@gmail.com
Sidney Chan: sidneychan23@yahoo.com