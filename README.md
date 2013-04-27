# src

the simple command line tool for web developers

## Why src?

src works with [CDNJS](http://cdnjs.com).  It has a collection of JavaScript and CSS code used by web developers every day.

## Install

On MacOS or Linux you can install it simply on the commandline.

    curl https://raw.github.com/brigand/src/master/update.sh | /bin/bash

## Usage

Let's say we're interested in jQuery.  We can get it in a few different ways.

The first is to just grab the **url** from CDNJS.

    $ src url jquery
    //cdnjs.cloudflare.com/ajax/libs/jquery/2.0.0/jquery.min.js

Pretty simple, right?  Now let's have src do some more of the work for us, by writing our **code**.

    $ src code jquery
    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.0.0/jquery.min.js" type="text/javascript"></script>

Content Delivery Networks are great, but maybe we want a local copy.

    $ src get jquery
    We found Jquery and put it in jquery.min.js

Thanks **src***!

## Future

Some more features would be cool.  Have an idea?  Please share it on the issues page.  Have time?  Help is always appreciated!

## License


Copyright (c) 2013 Frankie Bagnardi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.