# Jinja Bootstrap
This libray is for using [Twitter Bootstrap][bootstrap] with [Jinja2 python templates][jinja].
It is particularly useful for using Bootstrap with Django and Jinja templates.

Here are some formulas for you:

  * CSS framework + Javascript framework + Twitter awesomeness = [Bootstrap][bootstrap]
  * Python + Templating language = [Jinja2][jinja]
  * Jinja2 + Django = [Jingo][jingo]
  * **Jinja2 + Boostrap + love = [Jinja Bootstrap](http://github.com/auzigog/jinja-bootstrap)**


## Usage with Django
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
    ]


## Usage with Hyde
You can use it with Hyde in a similar way as with Django:

    pip install git+https://github.com/concentricsky/jingo.git
    pip install git+https://github.com/auzigog/jinja-bootstrap.git


## Usage with others
I'm not sure where else folks might want to use this, but I'd like to add instructions to make that kind of thing easy.

[Open a ticket](http://github.com/auzigog/jinja-bootstrap), if you'd like to offer a set of instructions for getting this setup with the platform of your choice


## Roadmap


## Author
Built with love by [Jeremy Blanchard](http://blanchardjeremy.com)

## License
This project is licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)


[bootstrap]: http://twitter.github.com/bootstrap/
[jingo]: http://github.com/concentricsky/jingo/
[jinja]: http://jinja.pocoo.org/docs/