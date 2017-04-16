# Website for markzz.com

This is the code for my personal website, features (or future features) include:

* Basic pages
* Simple blog with comment system
* Arch Linux/pacman repository browser

## Installing for testing

1. First, install php however your system does it.
2. Install [php-alpm](https://github.com/markzz/php-alpm) (the php extension needed for the repo browser)
3. Initialize db (instructions soon)
4. Customize `config/config.php`
5. Run the PHP Built-in Server
   * `$ php -S localhost:8080 -t /path/to/website/web/root`