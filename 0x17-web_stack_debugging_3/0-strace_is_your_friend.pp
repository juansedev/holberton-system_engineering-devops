# Fix error in PHP file
exec { 'fix the wp-settings file':
    command  => 'sed -i "s|class-wp-locale.phpp|class-wp-locale.php|g" /var/www/html/wp-settings.php',
    provider => shell,
}

exec { 'restart apache':
  command => 'sudo /etc/init.d/apache2 restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
