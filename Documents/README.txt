Instructions to run

1. After cloning, navigate to root directory
2. Create a virtual env by running the following command: python3 -m venv venv
3. Activate the virtual environment: `source venv/bin/activate`
4. Install the dependencies: `pip install -r requirements.txt`, do note that we are using PyQt5 so the file may be large.
5. run main.py: python3 main.py


To navigate via the application

1. The window can/may be maximized
2. the mouse icon (arrow) is selected initially, you may select the line or rectangle to draw them
3. clicking on a shape highlights it, these shapes can be dragged around the canvas. Click anywhere else on the canvas to unhighlight while the mouse is selected.
4. To draw the shapes, click on the icon corresponding to it and drag your mouse across your screen by clicking left button. To highlight the rectangle, click on its edge (and not on center).
5. While the mouse is selected, highlight a shape and press on edit/copy/delete for their respective features.
6. Signal support is also present, you may click ctrl+c , del for copy and delete respectively on highlighted shape (or group)
7. Debug button is solely for development purposes, the terminal prints the heirarchy of the canvas.
8. Import and Export for XML files are also supported, for exporting after drawing on canvas, click on export and enter file name you want to create.


Groups

1. Ensure the mouse icon is selected and (IMPORTANT) make sure you press Ctrl first, before even selecting the first shape. 
2. While pressing ctrl (keep it pressed, dont release) highlight multiple shapes, and click on Group button
3. Click on anywhere else on the canvas to see the border of group, initially the groups are highlighted by default
4. You may move the group , which moves all the shapes, same goes for copying and deleting. Deleting a group first delees the shapes inside, and deleting it again deletes the entire group itself.
5. Click on a group and press Ungroup, to ungroup the last layer of grouping, inner groups if present retain their grouping. (Note if it does not work then make sure you select the group first and then click on ungroup)
6. Signal handling is also supported for groups (ctrl c, del)


Relevant information

We have used PyQt5, since it provides alot of components inbuilt, widgets, toolbar, paint functions, and GUI supports. 

Moreover PyQt5 also allows us to listen to event handlers, such as `Qt_KeyC` which ensures that the control button has been clicked on the  users laptop, regardless of it being windows/mac or linux.

PyQt5 also has great documentation present, some functions in the code have been commented with their respective documentation link which may be reffered to later if needed.