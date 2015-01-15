# Kv Language
## Separation of Concerns
The developers of Kivy framework invented kvlang to create user interface.
The motivation is the so-called [separation of concerns](http://en.wikipedia.org/wiki/Separation_of_concerns).
The ideas behind this concept is pretty simple: 

* Do not mix different things together. A user interface deals with
the look and feel, i.e., the presentation, of an application. 
It is a different concern from the process logic behind it. 
The separation of UI (presentation) from its code (logic) 
not only divides a big application into small parts but also
allows different people solve different concerns. 
* Use the right tools to solve a concern. Specifying the layout, 
colors, fonts, hierarchy etc in Python code is verbose and hard
to understand. Programming languages such as Python are created 
for data processing. It is better to user a specialized language
for creating a user interface. 

As we can tell from the previous samples, using kvlang to specify 
a widget tree is simpler and easy to understand. 




