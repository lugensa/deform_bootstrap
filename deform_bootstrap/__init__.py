from pkg_resources import resource_filename
from deform import Form

deform_templates = resource_filename('deform', 'templates')
deform_bootstrap_templates = resource_filename('deform_bootstrap', 'templates')
search_path = (deform_bootstrap_templates, deform_templates)

def set_renderer(path):
    translator = None
    try:
        import pyramid.i18n
        import pyramid.threadlocal
        # Set up pyramid i18n
        translator = lambda term: pyramid.i18n.get_localizer(
                pyramid.threadlocal.get_current_request()
                ).translate(term)
    except ImportError:
        pass

    Form.set_zpt_renderer(path, translator=translator)

def includeme(config):
    set_renderer(search_path)
    config.add_static_view('static-deform_boostrap', 'deform_bootstrap:static')

