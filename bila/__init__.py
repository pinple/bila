__author__ = 'Neulana'
__email__ = 'fupinyou@gmail.com'
__version__ = "0.1.0"
__version_info__ = tuple(
    [
        int(num) if num.isdigit() else num
        for num in __version__.replace("-", ".", 1).split(".")
    ]
)

BILA_APPS = [
    # Wagtail apps
    'wagtail.core',
    'wagtail.admin',
    'wagtail.documents',
    'wagtail.snippets',
    'wagtail.users',
    'wagtail.images',
    'wagtail.embeds',
    'wagtail.search',
    'wagtail.sites',
    'wagtail.contrib.redirects',
    'wagtail.contrib.forms',
    'wagtail.contrib.sitemaps',
    'wagtail.contrib.routable_page',

    # Third-party apps
    'taggit',
    'modelcluster',
    'django_social_share',

    # Puput apps
    'bila',
]
