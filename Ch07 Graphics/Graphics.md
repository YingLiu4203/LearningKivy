# Graphics
## Introduction
Like most graphic framework, Kivy uses canvas to draw graphics. 
Kivy graphics are based on the cross-language, platform-independent 
OpenGL API to render graphics. Kivy builds a set of instructions 
based on OpenGL API that can draw graphics in different systems. 

Kivy defines three types of instructions: context instructions, 
vertex instructions and manipulating instructions. 
Instructions can be executed before, during and after canvas rendering. 

**Note**: This section uses a lot `with` statements to 
draw graphics. When a resource has a setup procedure before its use and 
a cleanup procedure after its use, the `with` statement is 
handy in this situation. The [Understanding Python's "with" statement](http://effbot.org/zone/python-with-statement.htm)
is a good introduction to this concept. The following is 
a customized simple example from the article. 
 
```python
class controlled_execution(object):
        def __enter__(self):
            print "set things up"
            return 8
        def __exit__(self, type, value, traceback):
            print "tear things down"

with controlled_execution() as thing:
         print thing
```

## Context Instructions
[Context instructions](http://kivy.org/docs/api-kivy.graphics.context_instructions.html#)
are non-graphics instructions that change canvas context. 
Some context instructions are matrix manipulation instructions used 
to rotate, translate, and scale context. Other instructions include 
color manipulations and texture binding instructions. 

### Texture Instructions
A texture is an image that can be applied to a canvas. A common usage 
is to apply a set of 2D images to a 3D object. A texture has attributes
such as size, format, and color ect. 

### Color Instructions
A color instruction affects the color state for vertex instructions
following it. If a vertex instruction has a texture, a color instruction
is applied as a multiplier to the texture. If there is no texture, 
the color instruction is directly used. 

    For instance, if a Rectangle has a texture with uniform color 
    (0.5, 0.5, 0.5, 1.0) and the preceding Color has rgba=(1, 0.5, 2, 1), 
    the actual visible color will be (0.5, 0.25, 1.0, 1.0) since the 
    Color instruction is applied as a multiplier to every rgba component. 
    In this case, a Color component outside the 0-1 range gives a 
    visible result as the intensity of the blue component is doubled.

A color value can use one of two modes: `rgb` (the default mode) or 
`hsv`. Following are two examples: 

```python
c1 = Color(1, 0, 0, .2)
c2 = Color(r=1)
c3 = Color(1, 0, 0, .2, mode='hsv')
c4 = Color(h=1, a=.2)
```

In kv lang, mode is explicitly declared:

```
<Rule>:
    canvas:
        # red color
        Color:
            rgb: 1, 0, 0
        # blue color
        Color:
            rgb: 0, 1, 0
        # blue color with 50% alpha
        Color:
            rgba: 0, 1, 0, .5

        # using hsv mode
        Color:
            hsv: 0, 1, 1
        # using hsv mode + alpha
        Color:
            hsv: 0, 1, 1
            a: .5
```

For example, the following code changes canvas color: 

```
with self.canvas.before:
    Color(1, 0, .4, mode='rgb')
```


## Vertex Instructions
[Vertex Instructions](http://kivy.org/docs/api-kivy.graphics.vertex_instructions.html#)
are instructions that draw simple vertex objects. According 
to this [Wikipedia Defintion](http://en.wikipedia.org/wiki/Vertex_\(computer_graphics\)): 

    A vertex (plural vertices) in computer graphics is an object, that 
    has certain attributes, one of which is its position. A vertex is a 
    data structure, that describes certain attributes, among which, 
    the position of a point in 2D or 3D space. Display objects are composed 
    of arrays of flat surfaces (typically triangles) and vertices 
    define the location and other attributes of the corners of the surfaces. 

Because OpenGL uses vertices to describe its graphic objects, 
vertex instructions are instructions that draw graphics. 
Common vertex instructions include `Point`, `Line`, `Triangle`, `Rectangle`,
`Ellipse`, `Mesh`, `Bezier`, etc. 

The following is a simple example drawing a line and a rectangle: 

```python
with self.canvas:
   # draw a line using the default color
   Line(points=(x1, y1, x2, y2, x3, y3))

   # lets draw a semi-transparent red square
   Color(1, 0, 0, .5, mode='rgba')
   Rectangle(pos=self.pos, size=self.size)
```

## Manipulating Instructions
Manipulating instructions are instructions that update or remove
other instructions. 

You can keep a reference to your instructions and update them:

```python
from kivy.app import App
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics import Color
from kivy.uix.widget import Widget


class MyWidget(Widget):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        with self.canvas:
            Color(1, 0, 0, .5, mode='rgba')
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.update_rect)
        self.bind(size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = (self.size[0] / 2, self.size[1] / 2)


class MyApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MyApp().run()
```

Or you can clean your canvas and start fresh:

```python
from kivy.app import App
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics import Color
from kivy.uix.widget import Widget


class MyWidget(Widget):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        with self.canvas:
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.update_rect)
        self.bind(size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = (self.size[0] / 2, self.size[1] / 2)
        self.canvas.clear()
        with self.canvas:
            Color(1, 0, 0, .5, mode='rgba')
            rect_size = (self.size[0] / 2, self.size[1] / 2)
            self.rect = Rectangle(pos=self.pos, size=rect_size)


class MyApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MyApp().run()
```

Note that updating the instructions is considered the best practice 
as it involves less overhead and avoids creating new instructions.

## Examples

[rotation button](https://github.com/kivy/kivy/blob/master/examples/canvas/rotation.py)

[draw shapes](https://github.com/kivy/kivy/blob/master/examples/canvas/lines_extended.py)

[repeat texture](https://github.com/kivy/kivy/blob/master/examples/canvas/repeat_texture.py)

[canvas stress](https://github.com/kivy/kivy/blob/master/examples/canvas/canvas_stress.py)

[control circle](https://github.com/kivy/kivy/blob/master/examples/canvas/circle.py)

[animation](https://github.com/kivy/kivy/blob/master/examples/animation/animate.py)
