#!/bin/bash
read -p "Check that in dist/ there is only one .tar.gz package. Press enter to continue"
## if you have ~/.pypirc:
twine upload -r pypi dist/skeleton*.tar.gz
## you can also use pypirc file located somewhere else:
# twine upload -r pypi --config-file $HOME/maybe_some_encrypted_directory/pypirc dist/skeleton*.tar.gz
