**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 4

<hr>

**Use Case**: Drawing

**Primary Actor**: User

**Goal in Context**: To draw on canvas through mouse.

**Preconditions**: The program must be running and in a responsive state.

**Trigger**: Left-clicking the mouse to change the pixel color and draging the mouse to draw like a pencil.
  
**Scenario 1**: If the previous selected color is yellow and after a user left-clicks the mouse, the color of the pixel where the mouse is located is changed to yellow.

**Scenario 2**: If the previous selected color is green and after a user presses the mouse and drags it on canvas, a green line should be displayed. The line should end when the mouse is released.
 
**Exceptions**:  
1. The user pressed the mouse but nothing happened. In this case, the user should first check whether the mouse is connected to the computer and it could be clicked successfully. Then the user should make sure the mouse is left-clicked not right-clicked.

2. The user pressed the mouse and draged it but no line was displayed. In this case, the user should first make sure if the mouse is dragged while pressed but not released. If this is not working, the user should be able to create a line by selecting from the sidebar.

**Priority**: High-priority.

**When available**: First release

**Channel to actor**: The primary actor communicates through I/O devices. This includes the keyboard and the mouse. The system is responsible for maintaining focus of the window when the user clicks, and should respond within 1 second of any keyboard event. The user is responsible for all other input.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: We may need to implement 'undo' functionality in the future, so that users won't draw something in accident by mis-pressing the mouse on canvas.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
