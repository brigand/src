#!/usr/bin/env python
import argparse
import sys, os
import urllib2, json
import re

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
SOURCE_FILE = SCRIPT_DIR + '/cdnjs.list'
allow_exts = ['js', 'css']


def get_sources():
    with open(SOURCE_FILE) as fin:
        return fin.read().splitlines()

def get_url(search, all_containing=False):
    """
    Takes a search string and attempts to find a matching library
    Returns a tuple: (url, file, name, ext)

    If all_containing is true: return a list of the aforementioned tuples where they start with the search string.
    """
    matches = []

    for source in sources:
        # Take the last chunk of the the url (e.g. jquery.min.js)
        _, package, version, file = source.rsplit('/', 3)

        # jquery.min.js to jquery.js, etc.
        file_no_min = file.replace('.min', '')

        name, ext = file_no_min.rsplit('.', 1)

        # name and search should be one word, so simple to compare
        if package.lower() == search.lower() and ext in allow_exts:
            return (source, file, name, ext)
        elif all_containing and package.lower().startswith(search.lower()) and package not in skipped:
            matches.append((source, file, name, ext))

    if not matches:
        raise IOError("Couldn't find library specified.")

    return matches

def build_index(into):
    package_json = urllib2.urlopen('https://github.com/cdnjs/website/raw/gh-pages/packages.json').read()
    packages = json.loads(package_json)['packages']
    with open(SOURCE_FILE, 'w') as fout:
        for package in packages:
            url = "//cdnjs.cloudflare.com/ajax/libs/{name}/{version}/{filename}".format(
                name = package['name'],
                version = package['version'],
                filename = package['filename']
            )
            fout.write(url + "\n")


# Attempt to read the sources; but otherwise download them
try:
    sources = get_sources()
except IOError:
    print "Can't find cdnjs.list.  Now updating from repo..."
    build_index(SOURCE_FILE)
    sources = get_sources()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="web development asset url and download tool")

    parser.add_argument('action', help='The action to take (get, url, or code)')
    parser.add_argument('name', nargs='?',
                        help='The name or partial name of the library.  Examples include underscore and jquery.mobile')
    parser.add_argument('--js', help='JavaScript files only', action="store_true")
    parser.add_argument('--css', help='CSS files only', action="store_true")

    args = parser.parse_args()

    if args.js: allow_exts = 'js'
    if args.css: allow_exts = 'css'

    if args.name and args.action:
        url, file, name, ext = get_url(args.name)

    if args.action == "get":
        # Browsers like the //site.tld format some sites use, but urllib2 expects http://site.tld
        url = re.sub(r'^//', 'http://', url)
        data = urllib2.urlopen(url).read()
        with open(file, 'w') as fout:
            fout.write(data)
        print 'We found {} and put it in {}'.format(name.title(), file)

    elif args.action == "url":
        print url

    elif args.action == "code":
        if ext == 'js':
            print '<script src="{}" type="text/javascript"></script>'.format(url)
        else:
            print "We don't recognize the extension of {}, what is a {} file?".format(file, ext.upper())

    elif args.action == "update":
        print 'Now updating from repository...'
        build_index(SOURCE_FILE)

    else:
        print "Sorry, I don't know how to do that.  I know how to 'get', 'url', and 'code'.  " + \
              "Perhaps one of those would be good?"

