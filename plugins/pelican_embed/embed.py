# -*- coding: utf-8 -*-

# Copyright (c) 2013 Kura
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import unicode_literals

from docutils import nodes
from docutils.parsers.rst import directives, Directive
import urllib2
from urllib import quote_plus
import json

class Embed(Directive):
    """ Embed external content in posts.

    Based on the YouTube directive by Brian Hsu:
    https://gist.github.com/1422773

    VIDEO_ID is required, with / height are optional integer,
    and align could be left / center / right.

    Usage:
    .. embed:: ID
        :type: vimeo (or youtube, slideshare)
        :align: center
    """

    def align(argument):
        """Conversion function for the "align" option."""
        return directives.choice(argument, ('left', 'center', 'right'))


    def embed_type_validator(argument):
        """ Conversion function for the "type" option."""
        return directives.choice(argument, ('vimeo', 'youtube', 'slideshare', 'pdf'))
    
    def get_oembed(self, embed_type, content_id):
        if embed_type == 'vimeo':
            url = 'http://vimeo.com/api/oembed.json?url=http%3A//vimeo.com/{}'.format(content_id)
        elif embed_type == 'youtube':
            url = 'http://www.youtube.com/oembed?url=http%3A//youtube.com/watch%3Fv%3D{}&format=json'.format(content_id)
        elif embed_type == 'slideshare':
            url = 'http://www.slideshare.net/api/oembed/2?url=http%3A//www.slideshare.net/slideshow/embed_code/{}&format=json'.format(content_id)
        elif embed_type == 'pdf':
            return {
                'width': 800,
                'height': 400
            }

        response = urllib2.urlopen(url)
        data = json.loads(response.read())

        width = data['width']
        height = data['height']
        
        if int(width) > 800:
            data['width'] = 800
            data['height'] = 800 * (float(data['height']) / float(data['width']))

        return data

    required_arguments = 1
    optional_arguments = 2
    option_spec = {
        'align': align,
        'type': embed_type_validator,
    }

    final_argument_whitespace = False
    has_content = False

    def run(self):
        content_id = self.arguments[0].strip()
        align = 'left'
        embed_type = 'vimeo'

        if 'type' in self.options:
            embed_type = self.options['type'].lower()

        if 'align' in self.options:
            align = self.options['align']

        oembed_data = self.get_oembed(embed_type, content_id)

        if embed_type == 'vimeo':
            url = '//player.vimeo.com/video/{}'.format(content_id)
            div_block = '<div class="vimeo" align="{}">'.format(align)
            embed_block = '<iframe width="{}" height="{}" src="{}" '\
                          'frameborder="0"></iframe>'.format(oembed_data['width'], oembed_data['height'], url)

        elif embed_type == 'slideshare':
            url = '//www.slideshare.net/slideshow/embed_code/{}?rel=0'.format(content_id)
            div_block = '<div class="slideshare" align="{}">'.format(align)
            
            embed_block = '<iframe width="{}" height="{}" src="{}" scrolling="no" '\
                          'allowfullscreen frameborder="0"></iframe>'.format(oembed_data['width'], oembed_data['height'], url)

        elif embed_type == 'youtube':
            url = 'https://www.youtube.com/embed/{}'.format(content_id)
            div_block = '<div class="youtube" align="{}">'.format(align)
            embed_block = '<iframe width="{}" height="{}" src="{}" '\
                          'frameborder="0"></iframe>'.format(oembed_data['width'], oembed_data['height'], url)

        elif embed_type == 'pdf':
            url = 'http://docs.google.com/viewer?url={}&embedded=true'.format(quote_plus(content_id))
            div_block = '<div class="pdf" align="{}">'.format(align)
            embed_block = '<iframe width="{}" height="{}" src="{}" '\
                          'frameborder="0"></iframe>'.format(oembed_data['width'], oembed_data['height'], url)
        return [
            nodes.raw('', div_block, format='html'),
            nodes.raw('', embed_block, format='html'),
            nodes.raw('', '</div>', format='html')]


def register():
    directives.register_directive('embed', Embed)
