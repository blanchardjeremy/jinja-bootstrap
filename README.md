# Jinja Bootstrap
This libray is for using [Twitter Bootstrap][bootstrap] with [Jinja2 python templates][jinja].
It is particularly useful for using Bootstrap with Django and Jinja templates.

Here are some formulas for you:

  * CSS framework + Javascript framework + Twitter awesomeness = [Bootstrap][bootstrap]
  * Python + Templating language = [Jinja2][jinja]
  * Jinja2 + Django = [Jingo][jingo]
  * **Jinja2 + Boostrap + love = [Jinja Bootstrap](http://github.com/auzigog/jinja-bootstrap)**


## Features

  * `base.html` template for easy extending
  * Lots of blocks to make overriding easy
  * Form rendering macros
  * Alert/message rendering macros


## General Usage

`bootstrap/layout

There is a copy of Bootstrap's CSS/Javascript/images in `bootstrap/static/` that you can use to quickly get started.

If you'd like to override those files, simple

### Block names
Blocks are named with the following conventions

  * All Javascript blocks begin with `js_`
  * All CSS blocks begin with `css_`
  * All important tags have a `tag_wrapper` block and a `tag` block. For example:


    {% block container_wrapper %}
        <div class="container container-primary">
            {% block container %}
                ...


## Django
Jinja Bootstrap is designed primarily with Django in mind. Use [Jingo][jingo] to bring Jinja+Django together. (I recommend the Concentric Sky fork of Jingo linked to here).

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


### Django Forms



## Using with other frameworks
I'm not sure where else folks might want to use this, but I'd like to add instructions to make that kind of thing easy.

[Open a ticket](http://github.com/auzigog/jinja-bootstrap), if you'd like to suggest other ways of using Jinja Bootstrap or if you'd like to offer a set of instructions for getting setup with other platforms.


## Suggested Addons
Other bootstrap add-ons you can use:

  * [Font Awesome](http://fortawesome.github.com/Font-Awesome/) - Font-based icon set for Bootstrap
  * [Bootswatch](http://bootswatch.com/) - Color/design pallets for Bootstrap

## Roadmap

  * Add bootstrap support to other frameworks: Flask, Hyde, Google App Engine, others?

This library uses version numbers according to the [SemVer](http://semver.org/) specification.


## Author
Built with love by [Jeremy Blanchard](http://blanchardjeremy.com)


## License
This project is licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)

Bootstrap files included under Apache 2.0 as well. See [Boostrap's license](https://github.com/twitter/bootstrap/blob/master/LICENSE).



[bootstrap]: http://twitter.github.com/bootstrap/
[jingo]: http://github.com/concentricsky/jingo/
[jinja]: http://jinja.pocoo.org/docs/