# Widgets and Layouts
## Introduction
A user interface usually has many elements such as input textbox, 
labels, drop down lists, button, radio buttons, etc. These elements
are called widgets in Kivy. Actually everything in the user
interface is a widget. Widgets are the building blocks of 
a Kivy graphic interface. Some widgets are not obvious or invisible.
A special group of widgets are layouts. A layout widget can contain 
other widgets and is used to arrange widgets inside it. 
Developers use layout widgets to control the sizes and 
locations of its child widgets. Kivy provides many widgets 
out of the box. It also let developers to define brand 
new widgets or extend/compose existing widgets
into new widgets. As shown in the previous chapter, a widget can be 
created either by Python code or by a Kv file. Kv files are 
preferred because of its independence, simplicity, and clear syntax.

A widget is represented by a subclass of the `kivy.uix.widget.Widget`
class. A widget has properties such as id, color, text, font size, etc. 
A widget may trigger some events such as touch down, touch move, 
and touch up.   

## Widget Tree
A user interface usually has many widgets. A widget can have 
multiple child widgets. A child widget can have only one parent widget. 
All widgets in a user interface form a tree structure. 
There is only a single widget call `root` widget that doesn't have
a parent widget. Usually it is a layout widget that has one or more
child widgets. In a Kv file, the parent-child relationship are 
declared using indentation. For example, the following kvlang code
describes a `Label` element whose `text` property is "Hello World".
 
    ```
    Label:
        text: "Hello World"
    ```
In Python convention, the class name uses so-called Pascal casing 
that the first letter of a word is an uppercase letter. Widget 
properties such as `text` are 
This `Label` element is the only widget in the user interface 
and it is also the `root` widget because it is leftmost widget 
in this Kv file. The following kvlang code describes a 
`GridLayout` widget that has two `Label` elements as its child
widgets. 

    ```
    GridLayout:
        Label:
            text: "Hello World"
        Label:
            text: "Best Regards"
    ```
In this Kivy file, the `GridLayout` is one of many Kivy layout widgets 
that can have multiple child widgets. It is the leftmost widget 
in the Kv file thus it is a root widget. Running the `main.py` 
and `helloworld.kv` in the folder [./source/0301](./source/0301) 
will display the following window: 

![Two-Leable Window](./images/0301.jpg)





