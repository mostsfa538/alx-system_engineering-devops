# Solving Apche returing error code 500

# the problem is that in the file /var/www/html/wp-settings.php
# in line 137: require_once( ABSPATH . WPINC . '/class-wp-locale-switcher.php' );
# the file name "class-wp-locale-switcher.php" was written as "class-wp-locale-switcher.phpp"
# which is the file does not exits.
exec{'fix-syntax':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    =>  ['/bin', '/usr/bin']
}
