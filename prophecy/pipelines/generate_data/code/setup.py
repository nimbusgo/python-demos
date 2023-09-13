from setuptools import setup, find_packages
setup(
    name = 'generate_data',
    version = '1.0',
    packages = find_packages(include = ('generate_data*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'hvac==1.2.1', 'prophecy-libs==1.6.1'],
    entry_points = {
'console_scripts' : [
'main = generate_data.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
