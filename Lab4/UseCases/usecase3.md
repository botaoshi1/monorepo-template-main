**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 3

<hr>

**Use Case**: Canvas Clear

**Primary Actor**: User

**Goal in Context**: To clear all materials on the canvas by pressing the space key.

**Preconditions**: The program must be running and in a responsive state.

**Trigger**: Pressing the space key.
  
**Scenario**: If the previous drawing color is red and after the user presses the space key, the entire canvas is filled with color red.
 
**Exceptions**: The user pressed the space key but nothing happened. In this case, the user should first check if the keyboard is working and connecting to the computer and fix correspondingly. Then the user should make sure the function of screen clear through keyboard is turned on in the program setup. If all these methods are not working, the user should be allowed to clear the canvas by clicking on the sidebar.

**Priority**: High-priority.

**When available**: First release

**Channel to actor**: The primary actor communicates through I/O devices. This includes the keyboard and the mouse. The system is responsible for maintaining focus of the window when the user clicks, and should respond within 1 second of any keyboard event. The user is responsible for all other input.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: We may need to implement 'undo' functionality in the future, so that users won't delete everything in accident by mis-touching the space key.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
