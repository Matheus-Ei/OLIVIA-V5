from distutils.core import setup
import py2exe

# Lista de scripts que você deseja incluir no executável (inclua todos os arquivos .py relevantes)
scripts = ['main\classifier.py']

# Lista de módulos ou pacotes que seu script depende
# Certifique-se de incluir todos os módulos e pacotes necessários aqui
packages = ['main.executor', 'main.system.messages', "main.system.config.operations", "main.modules.translator", "main.modules.search", "main.modules.sounds.voice", "main.ia.sumarizer", "main.ia.rewritter", "main.ia.questions", "main.ia.image_gen", "main.ia.emotions"]

setup(
    console=scripts,
    options={
        'py2exe': {
            'packages': packages,
        }
    }
)

# EXECUTE THIS COMMAND: python setup.py py2exe