# make-font-face
Python3 script to convert ttf font to woff, woff2 and svg


Requirements
----
* Python 3.x
* Fontforge (in your PATH, see here : https://fontforge.github.io/en-US/)
* woff2_compress (in your PATH, see here: https://github.com/google/woff2)
* sfnt2woff (in your PATH, see here: https://github.com/wget/sfnt2woff)
* convert2svgfont.pe (in your PATH, located under scripts)


Recommendation
----

Don't try to use it on Windows, i had a hard time to get all these
small programs properly compiled on Windows. I recommend a recent and decent 
Linux distribution, like Ubuntu, Centos, etc. There the compilation of the C 
related things is pretty much straight forward

Also provide proper font files ( no osbscure charachter and no spaces in file names). 


Usage
----
```

python3 font-face.py <my-font-directory with *.ttf font files> 

```

Gives you
----

converts *.ttf to woff, woff2, svg and produces a font-face.css file at once


Convert otf to ttf
----

```
fontforge -script convert_otf2ttf.sh FONTNAME.otf
``` 

see: http://www.stuermer.ch/blog/convert-otf-to-ttf-font-on-ubuntu.html













