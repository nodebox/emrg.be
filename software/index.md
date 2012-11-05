---
layout: default
section: software
title: Software
images:
  - [software/nodebox3.jpg, NodeBox 3]
  - [software/nogl.jpg, NodeBox for OpenGL]
  - [software/nodebox1.jpg, NodeBox 1]
---

<h2><a href="nodebox-3.html">NodeBox 3</a></h2>

NodeBox 3 (2012) is a free, cross-platform software application for creating generative graphics using an easy-to-use node-based UI. Next to writing Python code, users can creatively connect visual building blocks (or <em>nodes</em>) together into networks, creating visually rich compositions. 
<span class="tag-feature">free</span> <span class="tag-feature">cross-platform</span> <span class="tag-feature">GUI</span>
[Read more &raquo;][nodebox3]
<p><a class="homepage" href="http://nodebox.net/node/">http://nodebox.net/node/</a></p><br>

<h2>NodeBox 2</h2>

NodeBox 2 (2008) started the conversion from code to a node-based UI. Experience through workshops and user feedback led to a new approach and NodeBox 3. **No active development.** 
<p><a class="homepage" href="http://beta.nodebox.net">http://beta.nodebox.net</a></p><br>

<h2><a href="nodebox-1.html">NodeBox 1</a></h2>

NodeBox 1 (2004, the "classic") is a free software application for Mac OS X that generates 2D graphics (static, animated or interactive) using Python programming code. It was originally based on <a href="http://www.drawbot.com" class="tag-software">DrawBot</a>, and has since become a serious playground for research in design automation and AI, with many libraries. NodeBox 1 is in "maintenace mode": we only release new versions to fix critical issues. 
<span class="tag-feature">free</span>
[Read more &raquo;][nodebox1]
<p><a class="homepage" href="http://nodebox.net/code/">http://nodebox.net/code/</a></p><br>

<h2><a href="nodebox-opengl.html">NodeBox for OpenGL</a></h2>

NOGL (2011) is a free, cross-platform, hardware-accelerated library for creating 2D animations using Python programming code. It is based on <a href="http://www.pyglet.org" class="tag-software">Pyglet</a> and uses the NodeBox 1 API, minus the graphical user interface. It was initiated as part of a computer game project (<a href="../projects/city-in-a-bottle.html" class="tag-project">City in a bottle</a>). 
<span class="tag-feature">free</span> <span class="tag-feature">cross-platform</span> <span class="tag-feature">GPU</span>
[Read more &raquo;][nogl]
<p><a class="homepage" href="http://www.cityinabottle.org">http://www.cityinabottle.org</a></p><br>

<br>
<hr>

<h3>Design philosophy</h3>
In 2003 we created NodeBox (now cited as "NodeBox 1" or the "classic" version) to overcome limitations in existing computer graphics software. We didn't just want to apply pre-build effects, we wanted to create our own. We wanted to connect the visual output to different input channels, such as databases, corpora and information from the WWW. This is possible in a programming language (<a href="http://www.python.org" class="tag-software">Python</a>), where plug-in libraries can be freely combined. This work was inspired by <a href="http://www.processing.org" class="tag-software">Processing</a> and <a href="http://www.drawbot.com" class="tag-software">DrawBot</a>. 

However, not everyone is a programmer. Since NodeBox 1, different spin-off versions are in development. NodeBox 3 focuses on a flexible GUI instead of Python code. NOGL focuses on performance. The idea is to converge on one version: one that is free, cross-platform, with a node-based GUI, hardware accelerated, parallel, working on mobile devices, with both scientific and artistic functionality for robust data visualization.

<h3>Feature comparison</h3>
<table style="margin-bottom:0;">
	<tr>
		<th>Version</th>
		<th>Since</th>
		<th>Platform</th>
		<th>Language</th>
		<th>Engine</th>
		<th>GUI</th>
		<th>GPU</th>
		<th>PDF</th>
		<th>PNG</th>
		<th>MOV</th>
	</tr>
	<tr>
		<td data-title="Version">NodeBox 3</td>
		<td data-title="Since">2012</td>
		<td data-title="Platform">Windows, Mac, Linux</td>
		<td data-title="Language">Python</td>
		<td data-title="Engine">Java2D</td>
		<td data-title="GUI">✓</td>
		<td data-title="GPU"></td>
		<td data-title="PDF">✓</td>
		<td data-title="PNG">✓</td>
		<td data-title="MOV">✓</td>
	</tr>
	<tr>
		<td data-title="Version">NodeBox 2<sup>1</sup></td>
		<td data-title="Since">2008</td>
		<td data-title="Platform">Windows, Mac, Linux</td>
		<td data-title="Language">Python</td>
		<td data-title="Engine">Java2D</td>
		<td data-title="GUI">✓</td>
		<td data-title="GPU"></td>
		<td data-title="PDF">✓</td>
		<td data-title="PNG">✓</td>
		<td data-title="MOV">✓</td>
	</tr>
	<tr>
		<td data-title="Version">NodeBox 1</td>
		<td data-title="Since">2004</td>
		<td data-title="Platform" data-title="Platform">Mac OS X</td>
		<td data-title="Language">Python</td>
		<td data-title="Engine">Quartz2D</td>
		<td data-title="GUI">✓</td>
		<td data-title="GPU"></td>
		<td data-title="PDF">✓</td>
		<td data-title="PNG">✓</td>
		<td data-title="MOV">✓</td>
	</tr>
	<tr>
		<td data-title="Version">NOGL</td>
		<td data-title="Since">2011</td>
		<td data-title="Platform">Windows, Mac, Linux</td>
		<td data-title="Language">Python</td>
		<td data-title="Engine">OpenGL</td>
		<td data-title="GUI"></td>
		<td data-title="GPU">✓</td>
		<td data-title="PDF"></td>
		<td data-title="PNG">✓</td>
		<td data-title="MOV"></td>
	</tr>
</table>
<small><sup>1</sup> No longer actively developed.</small>

<h3>Developers</h3>

All versions of NodeBox are free software and source code is available on [GitHub](https://github.com/nodebox).

[nodebox1]: /software/nodebox-1.html
[nodebox3]: /software/nodebox-3.html
[nogl]: /software/nodebox-opengl.html
