from paste.script.templates import BasicPackage, Template, var

class OpenCorePlugin(BasicPackage):
    _template_dir = 'paster-templates/opencore_plugin'
    summary = "A basic OpenCore plugin with ZCML auto-loaded"

