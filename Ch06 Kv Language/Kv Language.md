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

Key concepts:

load by name matching
load by Builder: file or string
Both the load_file() and the load_string() methods return the root 
widget defined in your kv file/string. They will also add any 
class and template definitions to the Factory for later usage.

Three constructs: rule, root, class. Another construct, template, 
is deprecated by dynamic classes.

#: import name x.y.z
#: set name value


property: expression. All properties used in the expression 
will be observed !!!

Event binding: on_event: callback(args[1]), args is the event arguments.

Kvlang used id -- like a class level variable. 

A sample to demo weak reference. id.__self__

All ids are stored in self.ids attribute.

A template is a dynamic class that can be used by other widgets.
 
Multiple widgets can share styles <w1, w2>: 

[Kvlang Reference](http://kivy.org/docs/api-kivy.lang.html)

The content can contain rule definitions, a root widget, or 
dynamic class definitions.

The content of the file should always start with the Kivy header, 
where version must be replaced with the Kivy language 
version you’re using. For now, use 1.0:

```
#:kivy `1.0`
# content here
```

The content can contain rule definitions, a root widget, and 
dynamic class definitions

```
# Syntax of a rule definition. Note that several Rules can share the same
# definition (as in CSS). Note the braces: they are part of the definition.
<Rule1,Rule2>:
    # .. definitions ..

<Rule3>:
    # .. definitions ..

# Syntax for creating a root widget
RootClassName:
    # .. definitions ..

# Syntax for creating a dynamic class
<NewWidget@BaseClass>:
    # .. definitions ..
```

Regardless of whether it’s a rule, root widget, dynamic class 
or template you’re defining, the definition should look like this:

```
# With the braces it's a rule. Without them, it's a root widget.
<ClassName>:
    prop1: value1
    prop2: value2

    canvas:
        CanvasInstruction1:
            canvasprop1: value1
        CanvasInstruction2:
            canvasprop2: value2

    AnotherClass:
        prop3: value1
```

Here prop1 and prop2 are the properties of ClassName and prop3 
is the property of AnotherClass. If the widget doesn’t have a property 
with the given name, an ObjectProperty will be automatically 
created and added to the widget. AnotherClass will be created and added 
as a child of the ClassName instance.

### Property Values
When you specify a property’s value, the value is evaluated 
as a Python expression. This expression can be static or dynamic, 
which means that the value can use the values of other 
properties using reserved keywords.

Some keywords:

* self: The current widget instance. For example: `self.state`.
* root: the root widget. For example: `root.prop1`.
* app: the Kivy app instance. For example: `app.name`
* args: Used in `on_<action>` callbacks referring to the arguments
passed to the callback: `args[1]`.
* Ids: an id is only used in kvlang for external references. It is a 
weakref to a widget, not the widget itself. The original widget
can be access with `id.__self__`. For example, if a button has 
an id of `btn`, the the button is `btn.__self__` and its state 
is `id.state`. When a kv file is loaded, all defined ids 
are added to the `ids` dictionary
of the root widget. It can be accessed in two methods: 
`root.ids[`btn1`].state`  or `root.ids.btn`.state`. 

An expression as a property value must be in a single line. 
If an expression is used as a `on_<action>` callback, it can
has multiple lines but all lines must have the same indentation level !!!

For example, the following is valid:

```
on_state:
    if self.state == 'normal': \
    print('normal')
```

And the following is invalid

```
on_state:
    if self.state == 'normal':
        print('normal')
```

The Kivy language detects properties in your value expression and 
will create create callbacks to automatically update the property 
via your expression when changes occur. For example,

```
Button:
    text: str(self.state)
```

In this example, the parser detects that self.state is a 
dynamic value (a property). The state property of the button can 
change at any moment (when the user touches it). We now want 
this button to display its own state as text, even as the 
state changes. To do this, we use the state property of the 
Button and use it in the value expression for the button’s 
text property, which controls what text is displayed on the 
button (We also convert the state to a string representation).
Now, whenever the button state changes, the text property 
will be updated automatically.

### Dynamic Classes

Dynamic classes allow you to create new widgets on-the-fly, 
without any python declaration in the first place. 
The syntax of the dynamic classes is similar to the Rules, 
but you need to specify the base classes you want to subclass.

Any new properties, usually added in python code, should be 
declared first. If the property doesn’t exist in the dynamic class,
it will be automatically created as an appropriate typed property.

For example, 

```
<ImageButton@Button>:
    source: None

    Image:
        source: root.source
        pos: root.pos
        size: root.size

# let's use the new classes in another rule:
<MainUI>:
    BoxLayout:
        ImageButton:
            source: 'hello.png'
            on_press: root.do_something()
        ImageButton:
            source: 'world.png'
            on_press: root.do_something_else()
```

In Python, we can create an instance of the dynamic class as follows:

```python
from kivy.factory import Factory
button_inst = Factory.ImageButton()
```

