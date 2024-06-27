# This Pong game offers a more dynamic and challenging experience with features like temporary speed boosts, ball direction changes, and endless play.

## Controls:

### Feautures
- ### Paddle Movement:
``` python
Player 1: W / S
Player 2: Up Arrow / Down Arrow
```
- ### Ball Speed Boost (Temporary):
``` python
Player 1: (Your Turn): E
Player 2: (Your Turn): Page Up
```
- ### Ball Direction Change (Temporary):
``` python
Player 1: (Your Turn): D
Player 2: (Your Turn): Left Arrow
```

- ### Point Manipulation (To adjust how many points it takes to win): Space (Changes both players' points by 1)

-  ### Endless Play (Game will never end): B

- ### Slow Down Ball (Once per Game): A / Right Arrow

- ## Boundary Protection (Once per Game):
```python
Left Wall Bounce: Q
Right Wall Bounce: Page Down
```
- ### Increase Frame Rate (Permanent): P

- ### Quit Game: x



## Gameplay:

The ball will bounce between paddles and change direction on collision.

The ball's speed will dynamically increase over time.

Players can press specific keys (during their turn to act) to gain temporary speed boosts or change the ball's direction.

Scoring points happens when the ball misses a paddle.

The game will end if one player aquires a total of 25 points, declaring them the winner.

Pressing B (once) allows you to play endlessly (ignoring points).

Pressing A or Left Arrow (once) slows down the ball temporarily.

Pressing Page Down or Q (once) allows the ball to bounce back from a wall after hitting it.

Pressing P permanently increases the game's frame rate for faster gameplay.

Pressing X quits the game at any point.
## Notes:

- Temporary speed boosts and ball direction changes deactivate upon point scoring.

- Slowing down the ball and boundary protection can only be used once per game.

- The game is won after 25 points are scored

## Tips:
- Use the speed boosts and direction changes strategically to gain an edge.

- Time your paddle movements carefully to deflect the ball.

- Utilize the slow down and boundary protection options wisely for critical moments.

## Remember, the game becomes progressively faster over time, so practice your reflexes!

### Technical Details
```python
Language: Python
Library: Pygame
```