Experimental Media Research Group
=================================
This is the website for the Experimental Media Research Group (emrg.be)

Installing on Mac
-----------------
Install [Xcode][] first.

    sudo gem update --system
    sudo gem install rake jekyll RedCloth
    sudo easy_install pygments

Installing on Ubuntu
--------------------

    sudo apt-get install ruby rubygems
    sudo gem install rubygems-update
    sudo gem install rake jekyll RedCloth
    sudo easy_install pygments

Running
-------
To build the website:

    rake

To run the built-in server:

    rake server
    
To deploy to the live server:

    rake deploy

Writing Content
---------------
Each page has a header at the top, called the "front matter". It contains page metadata, such as the title and layout. The layout is a file (in the _layouts directory) that contains the "wrapper" around the content.

Content is written in [Markdown][]. If you want to use HTML, you can: just remember that Markdown tags do not work inside of HTML tags.


    ---
    layout: default
    section: default
    title: About
    ---
    Content goes here using [Markdown](http://daringfireball.net/projects/markdown/).


Frameworks
----------
* [Jekyll][] - Transform dynamic content into a static site.
* [Normalize][] - An alternative to CSS reset which keeps sane browser defaults and makes them consistent across browsers.
* [Skeleton][] - A responsive CSS grid that scales nicely on mobile.

License
-------
Text & images on this blog are licensed under the [Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License][cc].

[Jekyll]: http://github.com/mojombo/jekyll
[Normalize]: https://github.com/jonathantneal/normalize.css
[Skeleton]: http://www.getskeleton.com/
[Xcode]: http://itunes.apple.com/us/app/xcode/id422352214
[cc]: http://creativecommons.org/licenses/by-nc-nd/3.0/