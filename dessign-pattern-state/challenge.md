## Description of the challenge

Imagine that you have to implement a cellphone with the following states:

- Locked
- Ready
- Recording
- In a Call

And globally, these are the actions that can be done with this cellphone:

- Make a call (normal or emergency call)
- Record / stop recording a video
- Open facebook
- Lock / unlock

And for each state you can do or cannot do certain actions:

- Locked state:
  - Unlock the phone
  - Make an emergency call
- Ready state:
  - Lock the phone
  - Make a call
  - Record a video
  - Open facebook
- Recording state:
  - Stop recording
- In a Call state:
  - Open facebook

The challenge is to implement (using the dessign patern State) this class, the states, the actions and define the available transitions of the phone. Be free of adding more states or actions.