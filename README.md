#Команды для командной строки: установка postgres

brew install postgresql
initdb --locale=C -E UTF-8 /opt/homebrew/var/postgresql@14
brew services start postgresql@14

# Выводит список сущуствующих баз

psql -l

# Команды для командной строки для подключения к postgres, подсоединения к существующей базе данных
psql postgres
\connect academy


