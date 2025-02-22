{
    "name": "Language Selector",
    "category": "Productivity",
    "summary": "To select the languages easily.",
    "author": "White Star Myanmar education center",
    "company": "White Star Myanmar education center",
    "maintainer": "White Star Myanmar education center",
    "website": "https://www.facebook.com/odooerpdevelopment",
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": False,
    "depends": ["base"],

    'assets': {
        'web.assets_qweb': [
            'language_selector_v15/static/src/xml/language.xml',
        ],
        'web.assets_backend': [
            'language_selector_v15/static/src/js/language.js',
            'language_selector_v15/static/src/css/language.css',
        ],
    },
}
