# Fix the error

exec { 'Fix issue':
  command  => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  provider => shell,
}
