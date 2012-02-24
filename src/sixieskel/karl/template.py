import copy
from templer.core.base import BaseTemplate
from templer.core.vars import StringVar
from templer.core.vars import IntVar
from sixieskel.buildout.template import run_cmd


class KarlBuildout(BaseTemplate):
    _template_dir = 'templates/buildout'
    summary = "A KARL buildout"
    category = "Six Feet Up"
    default_required_structures = ['sixie_fabfile', 'bootstrap']
    required_templates = []
    use_cheetah = True
    vars = copy.deepcopy(BaseTemplate.vars)
    vars.extend([
        StringVar(
            'instance_name',
            'KARL instance name',
            help="""
The KARL instance name will be what shows as the url of this site.
for example:

http://localhost:6543/instance_name
""",
        ),
        StringVar(
            'project_name',
            'Project name (used for dist and fabric setup)',
        ),
        StringVar(
            'customization_package',
            'The name of the customization package',
            help="""
This is the package that will contain the overrides of the KARL
code.
""",
        ),
        IntVar(
            'paster_port',
            'HTTP port (51000 range)',
            default=51000,
        ),
    ])

    def check_vars(self, vars, cmd):
        result = BaseTemplate.check_vars(self, vars, cmd)
        # Add a db password for the project user
        passwd = run_cmd('pwgen -acn 9 1')
        if not passwd:
            passwd = 'admin'
        result['db_password'] = passwd
        # XXX: var.structures can't handle this case yet
        if vars['project_name']:
            self.required_structures.append('buildouthttp')
        return result
