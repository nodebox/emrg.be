---
layout: software
section: software
title: NodeBox for OpenGL
authors:
  - [Tom De Smedt, ../people/tom-de-smedt.html]
  - [Frederik De Bleser, ../people/frederik-de-bleser.html]
license:
  - BSD
documentation:
  - http://www.cityinabottle.org/nodebox
images:
  - [nodebox-opengl/nogl1.jpg, NOGL + GLSL mirror shader]
  - [nodebox-opengl/nogl2.jpg, NOGL + Twitter graph visualization]
---

<h3>Description</h3>
NodeBox for OpenGL (NOGL) is a free, cross-platform library for generating 2D animations with Python programming code. It is based on <a href="http://www.pyglet.org" class="tag-software">Pyglet</a> (Python OpenGL toolkit) and augmented with a simple API of drawing commands, near-identical to NodeBox for Mac OS X. Unlike NodeBox for Mac OS X, it does not have an extensive repository of plug-in libraries. However, motion tweening, layers, hardware-accelerated pixel effects (GLSL shaders on-the-fly), geometry &amp; Bézier path interpolation, tesselation and simple physics algorithms have been bundled into the core. Its implementation for graph networks is identical to that in <a href="http://www.clips.ua.ac.be/pages/pattern" class="tag-software">Pattern</a>, so users proficient in both packages can easily switch between graph analysis and graph visualization.

NodeBox for OpenGL handles 3D (for example, in <a href="../projects/city-in-a-bottle.html" class="tag-project">City In A Bottle</a>) if one is willing to call OpenGL functions directly. Using VertexArrays it is possible to achieve a decent 3D performance. 

NodeBox for OpenGL does not have a GUI. Users can work with an external editor of their own choice (we use TextMate).

<h3>Example</h3>
This example demonstrates a simple NOGL script. It assumes NOGL, Pyglet and Python are installed on your system. It imports the <code>nodebox.graphics</code> module with the standard set of drawing commands. It defines a <code>draw()</code> function and attaches it to the canvas, so that it will be drawn each animation frame. It opens the main application window with <code>canvas.run()</code>.

<pre class="brush:python;">
from nodebox.graphics import *

def draw(canvas):
    canvas.clear()
    translate(250, 250)
    rotate(canvas.frame)
    rect(-200, -200, 400, 400, fill=(1,0,0,1))

canvas.size = 500, 500
canvas.draw = draw
canvas.run()
</pre>

<h3>Reference</h3>

<p class="cite"><small>De Smedt T., De Bleser F. (2011). <cite>NodeBox for OpenGL version 1.7.</cite> Retrieved May 2012, from: http://cityinabottle.org/nodebox</small></p>
