---
layout: software
section: software
title: NodeBox 1
authors:
  - [Frederik De Bleser, ../people/frederik-de-bleser]
license:
  - MIT
documentation:
  - http://nodebox.net
images:
  - [nodebox-1/screenshot1.png, NodeBox - recursive type]
  - [nodebox-1/screenshot2.jpg, NodeBox - paths with dropshadows]
---

<h3>Description</h3>

NodeBox 1 is a Mac OS X application that lets you create 2D visuals (static, animated or interactive) using Python programming code and export them as a PDF or a QuickTime movie. It is free and well-documented. Several (free) plug-in libraries have been developed for NodeBox, for example for Core Image filters, SVG import, organic systems such as graphs, boids, L-systems, and an OSC wrapper. For an exponent of generative art made with NodeBox, see <a href="http://www.spamghetto.com" class="tag-project">Spamghetto</a> (Olivero, 2009).

NodeBox 1 is built on Mac OS X's Quartz rendering engine, using PyObjC. Ports exist for other platforms that use the same API, such as <a href="http://shoebot.net" class="tag-software">Shoebot</a>.

NodeBox 1 has been stable for a long time and is now in "maintenace mode": we only release new versions to fix critical issues. 

<h3>Example</h3>

This example demonstrates a simple NodeBox script. It draws a number of ellipses to the canvas, in random shades of transparent red, with random size and position.

<pre class="python">
for i in range(100):
    x = random(WIDTH)
    y = random(HEIGHT)
    r = 50 + random(200)
    fill(random(), 0, 0, random(0.5))
    oval(x-r, y-r, r*2, r*2)
</pre>


<h3>Reference</h3>

<p class="cite"><small>De Bleser F., De Smedt T., Nijs L. (2004). <cite>NodeBox version 1.9.5 for Mac OS X.</cite><br /> 
Retrieved March 2012, from: http://nodebox.net</small></p>