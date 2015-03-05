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

## Loading KV Files
There are two methods to load a KV file to a Kivy applicatoin. 

1. By Name Matching
During application start, Kivy looks for a KV file that matches the 
application class name. Matching means the same name that is lower case, 
doesn't have the ending 'App' and has a postfix of `.kv`.  
For example, if the app class name is `HelloWorldApp`, the kv file
name should be `helloworld.kv`. 
2. Loading by Kivy Builder class: 
Both the load_file() and the load_string() methods return the root 
widget defined in a kv file or a string. They will also add any 
class defined in the kv file or string. 

The following is an example from [GitHub Kivy examples]( https://github.com/kivy/kivy/blob/master/examples/widgets/label_with_markup.py)

```python
from kivy.app import App
from kivy.lang import Builder

root = Builder.load_string('''
Label:
    text:
        ('[b]Hello[/b] [color=ff0099]World[/color]\\n'
        '[color=ff0099]Hello[/color] [b]World[/b]\\n'
        '[b]Hello[/b] [color=ff0099]World[/color]')
    markup: True
    font_size: '64pt'
''')


class LabelWithMarkup(App):
    def build(self):
        return root

if __name__ == '__main__':
    LabelWithMarkup().run()
```


## Kv Constructors and Syntax

The content of a Kv file should always start with the Kivy header, 
where version must be replaced with the Kivy language 
version you’re using. For now, use 1.0:

```
#:kivy `1.0`
# content here
```

The content of a kv file has a set of rules that describe one root widget and 
a set of dynamic classes. A root widget is a widget
appears in the left most position. All child widgets are indented. 
A dynamic class is defined between the `<>` and followed by `:`. 
It defines the appearance and properties of an instance of the widget class.
Additionally, it allows name importing and variable declaration using 
the following syntax: 

```
#: import name x.y.z
#: set name value
```


### Kv Syntax

The following are syntax definitions defined in 
[Kvlang Reference](http://kivy.org/docs/api-kivy.lang.html). 

```
# Syntax of a rule definition. Note that several Rules can share the same
# definition (as in CSS). Note the braces: they are part of the definition.
<W1, W2>:
    # .. definitions ..

<W3>:
    # .. definitions ..

# Syntax for creating a root widget
RootClassName:
    # .. definitions ..

# Syntax for creating a dynamic class
<NewWidget@BaseClass>:
    # .. definitions ..
```

 
Multiple widgets can share styles using a syntax `<w1, w2>:`. 
Regardless of whether it’s a root widget or a dynamic class, 
the definition should look like this:

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
is the property of AnotherClass. If the widget doesn't have a property 
with the given name, a property will be automatically 
created and added to the widget. In the above example, an
instance of the `AnotherClass` will be created and added 
as a child of the ClassName instance.

### Expression in Property Values or Event Callbacks

When you specify a property’s value or an event callback, 
the value is evaluated as a Python expression. This expression 
can be static or dynamic, which means that the value can 
use the values of other properties using reserved keywords.

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

## Kv Properties and Events
The Kivy language detects properties in your value expression and 
will create callbacks to automatically update the property 
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

## Dynamic Classes

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

## Accessing Widgets Defined in Kv File
A sample application: 

```
<MyFirstWidget>:
    # both these variables can be the same name and this doesn't lead to
    # an issue with uniqueness as the id is only accessible in kv.
    txt_inpt: txt_inpt
    Button:
        id: f_but
    TextInput:
        id: txt_inpt
        text: f_but.state
        on_text: root.check_status(f_but)
```

```python
from kivy.app import App
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class MyFirstWidget(BoxLayout):

    txt_inpt = ObjectProperty(None)

    def check_status(self, btn):
        print('button state is: {state}'.format(state=btn.state))
        print('text input text is: {txt}'.format(txt=self.txt_inpt))


class KvDemoApp(App):
    def build(self):
        return MyFirstWidget()


if __name__ == '__main__':
    KvDemoApp().run()
```

## Kivy `weakref` id

The example demonstrates the `weakref` type of widget id. 

```
<MyWidget@BoxLayout>:
    label_widget: label_widget
    Button:
        text: 'Add Button'
        on_press: root.add_widget(label_widget)
    Button:
        text: 'Remove Button'
        on_press: root.remove_widget(label_widget)
    Label:
        id: label_widget
        text: 'widget'
```

The Python code: 

```python
from kivy.app import App
from kivy.factory import Factory


class KvDemoApp(App):
    def build(self):
        my_widget = Factory.MyWidget()
        return my_widget


if __name__ == '__main__':
    KvDemoApp().run()
```

To see the demo, run the code, click the remove button, resize
the screen, then click the add button. 