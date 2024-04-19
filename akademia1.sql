brew install postgresql
initdb --locale=C -E UTF-8 /opt/homebrew/var/postgresql@14
brew services start postgresql@14
psql -l
createdb academy 
psql -l