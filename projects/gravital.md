---
layout: default
section: projects
title: Gravital
images:
  - gravital/gravital.jpg
  - gravital/gravital2.jpg
  - gravital/gravital3.jpg
  - gravital/gravital4.jpg
---
Gravital was funded by  <a href="http://www.iwt.be"><img src="/media/gravital/iwt.jpg" height = "15" width = "20"></a> <a href="http://www.iwt.be">IWT</a>, the Institute for the Promotion of Innovation by Science and Technology in Flanders, and a consortium of 11 Belgian companies active in the creative industry. The project was a collaborative effort by the Experimental Media Research Group at the Sint Lucas School of Arts (Antwerp, Belgium) and the CNTS Language Technology Group at the University of Antwerp (Antwerp, Belgium) now called <a href="http://www.clips.ua.ac">CLiPS</a> (Computational Linguistics & Psycholinguistics Research Center). The project ran from January 2007 till March 2009. It resulted in the node-based approach that is still used in the latest NodeBox version.

**Budget:** IWT/TETRA 247.541 euro + 20.071 euro <br>
**Project initiator:** Karel de Grote-Hogeschool, department Sint Lucas Antwerpen <br>
**Project leader:** Lucas Nijs <br>
**Project researchers:** Frederik De Bleser, Tom De Smedt <br>
**University partner:** UA, department Linguistics, prof. Walter Daelemans, Vincent Van Asch<br>


**Participating companies:**<br>
<a href="http://www.kandesign.com/">KAN Creative Consultants NV</a>, Antwerpen.<br>
<a href="http://www.netlash-bseen.be/">Netlash BVBA</a>, Gent.<br>
<a href="http://www.antilope.com/nl/bedrijfsgegevens.html">Pre Press Satelit / Antilope NV</a>, Lier, (RvO)<br>
<a href="http://www.k15.be/">K15 BVBA</a>, Antwerpen<br>
<a href="http://www.vigc.be/">VIGC VZW</a>, Turnhout (RvO)<br>
<a href="http://www.visionandfactory.com/index.php/Home">visionandfactory / integrated design</a>, Brussel (RvO)<br>
<a href="http://www.achilles.be/">Achilles Associates BVBA</a>, Mechelen, (RvO)<br>
<a href="http://www.cronos.be/">Cronos NV</a>, Kontich, (RvO)<br>
<a href="http://www.luon.com/">LUON</a>, Overijse, (RvO)<br>
<a href="http://www.addictlab.com/">Lab.001 / Ad!dict Creative Labb</a>, Brussel<br>
<a href="http://www.dehaes.be/welkom/index.html">Drukkerij De Haes</a>, Mechelen (RvO)<br>

Gravital is a <a href="http://nodebox.net">NodeBox</a> spin-off that links language to AI and to design. Like NodeBox, you will be able to create visuals using simple Python programming code, but also using natural language (i.e. plain English) or with a node-based interface in which you can reconnect blocks like playing with Lego.

Translating language to visual output involves two important steps: Graphical Language Processing and a Smart Default Hierarchy. An interesting bit can be said about smart defaults without going into the technical details and challenges of language parsing. 

How do we decide what a visual shape will look like based on the textual content?
Assume we have translated a set of visual elements from a textual assignment. At the moment a visual element is created its visual properties need to be resolved: is it big or small, dark or light, round or edgy? Even when no restrictive statement has been made ("it is red") the system should be able to choose an appropriate solution. Several AI-modules are invoked when this type of under-specification occurs. The goal of the AI-modules is to pick default visual properties (position, size, color, shape, texture, feel) specific to the design context.

All the AI-modules share a characteristic in that they resolve ambiguity with the use of so-called "perceptonyms" (in analogy to "hyponyms" and "hypernyms" in WordNet). Perceptonyms are words that describe an unambiguous visual, auditive or tangible property. They are grouped into pairs of opposites such as sharp-soft, dark-bright and heavy-light. When concepts are described in terms of scores along perceptonym pairs we have a way of translating them visually. The word "ball" would score well on softness, brightness and lightness, therefore the system can interpret a ball visually as being a more round object having light and colorful hues.

Each perceptonym maps to a range of display options. For example, the "dark" range applies to the color of an object, defined in the Hue/Saturation/Brightness color model, with saturation constrained between 70% and 100% and brightness constrained between 15% and 40%. The darker an object scores, the lower its saturation and brightness will be when visualized.

Perceptonym scores are aggregated automatically with the use of internet search engines. More data results will be retrieved for a "soft ball" than for a "sharp ball" - a ball therefore scores better on softness. The system has a cached network of hierarchical data with specific concepts such as "beach ball" and "free jazz" at the top and "toy" and "music" at the bottom. Using lexical hypernym ("is-a") relations in WordNet the system will collapse through the database until a solution is found, e.g. even when no perceptonym information has been aggregated for "beach ball" it can still identify a ball as being a toy and use that information. At the bottom level a random solution is proposed.