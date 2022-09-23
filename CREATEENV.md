# install pyenv
curl https://pyenv.run
vim ~/.zshrc

# put this lines in .zshrc
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"

# reiniciar shell
exec zsh

# instalar python 3.10.7
pyenv install 3.10.7

# activate env
pyenv global 3.10.7

# restart shell
exec zsh

# install pyenv-virtualenv
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv

# put this lines in .zshrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

# verify installation
pyenv virtualenv --version

# creating virtualenv
pyenv virtualenv 3.10.1 venv-name-3.10.1

# verify versions
pyenv versions

# activate virtualenv
pyenv activate venv-name

# deactivate virtualenv
pyenv deactivate

# activate virtualenv when you enter in a folder (run inside the folder)
pyenv local venv-name
