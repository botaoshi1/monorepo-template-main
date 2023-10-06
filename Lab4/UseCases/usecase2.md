**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 2

<hr>

**Use Case**: Color Change

**Primary Actor**: User

**Goal in Context**: To change drawing colors by pressing number keys

**Preconditions**: The program must be running and in a responsive state. The number keys can be pressed. The number-color relationship is set up correctly.

**Trigger**: Pressing the number keys.
  
**Scenario**: The user presses number 2 on the keyboard and now the drawing color is white.
 
**Exceptions**:
1. The user pressed a number key but nothing happened. In this case, the user should first check if the keyboard is working and connecting to the computer and fix correspondingly. Then the user should make sure the function of color switch through keyboard is turned on in the program setup. If all these methods are not working, the user should be allowed to change color by clicking on the sidebar.

2. The user pressed a number key and the color is not displyed as expected. In this case, the user should check the program setup to make sure the number-color relationship is correct.

**Priority**: High-priority.

**When available**: First release

**Channel to actor**: The primary actor communicates through I/O devices. This includes the keyboard and the mouse. The system is responsible for maintaining focus of the window when the user clicks, and should respond within 1 second of any keyboard event. The user is responsible for all other input.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: We may need to implement 'undo' functionality in the future, so that users won't draw something in an unwanted color by mis-touching a number key.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
