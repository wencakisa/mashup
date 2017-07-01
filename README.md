![Logo](https://raw.githubusercontent.com/wencakisa/mashup/master/static/images/mashup_logo.jpg)

# mashup

**mashup** is a social network for events. You can plan upcoming events easily with this platform.


## Tech

* [Django](https://github.com/django/django) - A really nice high-level Python web framework
* [materialize-css](https://github.com/Dogfalo/materialize) - CSS Framework based on Material design.
* [Cloudinary](https://github.com/cloudinary/pycloudinary) - Cloud service used for delivering images via CDN


## Getting started

How to copy this project to your local machine and run it:

1. Download a copy from GitHub:

    ```
    $ git clone https://github.com/wencakisa/mashup.git
    $ cd mashup/
    ```

2. Setup Django requirements:

    ```
    $ pip3 install -r requirements.txt
    $ python3 manage.py makemigrations
    $ python3 manage.py migrate
    ```

3. Create a superuser:

    ```
    $ python3 manage.py createsuperuser
    ```

4. Run the tests:

    ```
    $ python3 manage.py test
    ```

5. Run the server:

    ```
    $ python3 manage.py runserver
    ```


### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.