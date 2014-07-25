# Jinja Bootstrap
This library is for using [Twitter Bootstrap][bootstrap] with [Jinja2 python templates][jinja].
It is particularly useful for using Bootstrap with Django and Jinja templates.

Put simply, Jinja Bootstrap gives you [all of this Boostrap awesomness][demo] with just a [few lines of Jinja templates code][examplesfile].

Here are some formulas for you:

  * [Bootstrap][bootstrap] = CSS framework + Javascript framework + Twitter awesomeness
  * [Jinja2][jinja] = Python + Templating language
  * [Jingo][jingo] = Jinja2 + Django
  * **[Jinja Bootstrap](http://github.com/auzigog/jinja-bootstrap) = Jinja2 + Bootstrap + love**

**NOTE:** This library is under active development. Please [open an issue][issues] if you have problems, questions, or suggestions for improvements to the code or the documentation.

## Features

  * A `base.html` template to use as a base for your bootstrap projects
  * Lots of blocks to make overriding easy
  * Form field rendering macros
  * Alert/message rendering macros

Version numbers:

  * Jinja Bootstrap 0.4.0
  * Bootstrap 3.0.1
  * jQuery 1.10.2


## Installation

The quickest ways to get started are:

To install via pip:

    pip install git+https://github.com/auzigog/jinja-bootstrap.git

Or to download this package as a [zip](https://github.com/auzigog/jinja-bootstrap/zipball/master)


## General Usage


The two most interesting files to take a peek at are:

  * [The `base.html` template layout](http://github.com/auzigog/jinja-bootstrap/blob/master/bootstrap/templates/bootstrap/layouts/base.html)
  * [The example usage of all of the macros][examplesfile]

`bootstrap/layouts/base.html` defines a base HTML layout that your templates can extend.
There is a copy of Bootstrap's CSS/Javascript/images in `bootstrap/static/` that you can use to quickly get started.

Inside `bootstrap/layouts/base.html`, the `STATIC_URL` context variable is used to define the path for your bootstrap folder.
In Django, this works by default. In other apps, you will have to make sure to specify `STATIC_URL` yourself.

In Django, you can specify your own bootstrap files by putting your own static files (`.css`, `.js`) inside an app folder that is higher up on your `INSTALLED_APPS` list or is higher up on your `TEMPLATE_LOADERS` list. (This probably means putting files in `my_app/static/bootstrap/css/bootstrap.js`). This is especially necessary when you want to compile your own CSS from the original LESS files.


### Block names
Blocks are named with the following conventions

  * All Javascript blocks begin with `js_`
  * All CSS blocks begin with `css_`
  * All important tags have a `tag_wrapper` block and a `tag` block. For example:

```
{% block container_wrapper %}
    <div class="container container-primary">
        {% block container %}
            ...
```


## Django
Jinja Bootstrap is designed primarily with Django in mind. Use [Jingo][jingo] to bring Jinja+Django together. (I recommend using the Concentric Sky fork of Jingo linked to here).

Install the following files using pip:

    pip install git+https://github.com/concentricsky/jingo.git
    pip install git+https://github.com/auzigog/jinja-bootstrap.git

Add/update the following lines in your `settings.py` file:

    # Jingo support
    JINGO_EXCLUDE_APPS = ['admin','registration',]
    TEMPLATE_LOADERS = [
    	'jingo.Loader',
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]

    # Jinja Bootstrap support
    INSTALLED_APPS = [
        'bootstrap',
        # ... your other apps
    ]

See the **[example django project](http://github.com/auzigog/jinja-bootstrap/tree/master/example_project_django)** for more examples about how to configure and use Jinja Bootstrap with Django.


## Using with other frameworks
I'd love to know where/how folks might want to use this framework, but I'd like to add instructions to make that kind of thing easy.

[Open an issue][issues], if you'd like to suggest other ways of using Jinja Bootstrap or if you'd like to offer a set of instructions for getting setup with other platforms.


## Suggested Addons
Other bootstrap add-ons you can use:

  * [Font Awesome](http://fortawesome.github.com/Font-Awesome/) - Font-based icon set for Bootstrap
  * [Bootswatch](http://bootswatch.com/) - Color/design pallets for Bootstrap

## TODO
Pull requests and suggestions for these items are very welcome. :)

Major TODO items:

  * Add bootstrap support to other frameworks: Flask, Hyde, Google App Engine, others?
  * Put code samples inside the example django project
  * Macros to help with reponsive design (not sure what this would look like)

Bootstrap features to support:

  * ~~Pagination~~
  * ~~Breadcrumbs~~
  * ~~Navigation other than the top nav~~
  * Helpers to make class="active" easy
  * ~~Labels~~
  * ~~Progress bars~~

Minor TODO items:

  * Inline help text on forms

Documentation TODO items:

  * Body classes and IDs


## Development
The [`develop`](https://github.com/auzigog/jinja-bootstrap/tree/develop) branch is used for active development. The master branch will always contain the latest stable release.

This library uses version numbers according to the [SemVer](http://semver.org/) specification.


## Author
Built with love by [Jeremy Blanchard](http://blanchardjeremy.com).


## License
This project is licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).

Bootstrap  is [licensed](https://github.com/twitter/bootstrap/blob/master/LICENSE) under Apache 2.0.
jQuery is [licensed](http://jquery.org/license/) under MIT/GPL.


[demo]: http://jinjabootstrap.herokuapp.com/
[examplesfile]: http://github.com/auzigog/jinja-bootstrap/blob/master/example_project_django/root/templates/home.html
[issues]: https://github.com/auzigog/hyde-bootstrap/issues
[bootstrap]: http://twitter.github.com/bootstrap/
[jingo]: http://github.com/concentricsky/jingo/
[jinja]: http://jinja.pocoo.org/docs/
