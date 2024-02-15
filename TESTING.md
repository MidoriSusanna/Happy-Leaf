# Manual Testing

![Manual Testing 1](read.me_pics/testing_pics/manual-testing-1.png)
![Manual Testing 2](read.me_pics/testing_pics/manual-testing-2.png)
![Manual Testing 3](read.me_pics/testing_pics/manual-testing3.png)
![Manual Testing 4](read.me_pics/testing_pics/manual-testing-4.png)
![Manual Testing 5](read.me_pics/testing_pics/manual-testing-5.png)
![Manual Testing 6](read.me_pics/testing_pics/manual-testing-6.png)

# Validation

## HTML

Each page has been validated with [W3 Validator](https://validator.w3.org/), only warnings about the h1 tag have been found, but no errors.Info pop ups have also been found about the hr tag.

- Index.html:
![Index html check](read.me_pics/testing_pics/indexpage-html-check.png)

- About.html:
![About html check](read.me_pics/testing_pics/aboutpage-html-check.png)

- Blog.html:
![Blog html check](read.me_pics/testing_pics/blogpage-html-check.png)

- Contact.html:
![Contact html check](read.me_pics/testing_pics/contact-html-check.png)
The type warning is related to the script added to use emailJs. 

- Log-in, Log-out, Sign-up:
![Log-in html check](read.me_pics/testing_pics/login-html-check.png)
![Log-out html check](read.me_pics/testing_pics/logout-html-check.png)
![Sign-up html check](read.me_pics/testing_pics/signup-html-check.png)

- Delete and edit comment pages:
![Comment delete html check](read.me_pics/testing_pics/deletecomment-html-check.png)
![Comment edit html check](read.me_pics/testing_pics/editcomment-html-check.png)

- Post_detail.html:
![Post detail html check](read.me_pics/testing_pics/postdetail-html-check.png)
In the post_detail.html page 42 errors and warnings have been found. Those errors are related to the installation of SummerNote. 

# CSS

The custom css page has been validated with [W3C Validator](https://jigsaw.w3.org/css-validator/) and no errors have been found.

![CSS check](read.me_pics/testing_pics/custom-css-check.png)

# JS

The emailJs file has been validated with [JShint](https://jshint.com/) and no errors were found. Some warnings related to the use of let as a variable were found.

![Email js check](read.me_pics/testing_pics/emailjs-check.png)

# Python

The project follows the PEP8 style guidelines and passes the [CI Phyton Linter](https://pep8ci.herokuapp.com) with no errors. 
The files settings.py and env.py have not undergone validation against the PP8 standards to prevent any potential disruptions to the application's functionality. These files are critical to the app's operation, and I opted to not modify them to ensure stability.

- Manage.py:
![Manage py check](read.me_pics/testing_pics/managepy-check.png)

- Admin.py:
![Admin py check](read.me_pics/testing_pics/adminpy-check.png)

- Apps.py:
![Apps py check](read.me_pics/testing_pics/appspy-check.png)

- Forms.py
![Forms py check](read.me_pics/testing_pics/formspy-check.png)

- Models.py
![Models py check](read.me_pics/testing_pics/modelspy-check.png)

- Url.py (Blog):
![Urls py check](read.me_pics/testing_pics/urlpy-check.png)

- Views.py:
![Views py check](read.me_pics/testing_pics/viewspy-check.png)

- Asgi.py:
![Asgi py check](read.me_pics/testing_pics/agsipy-check.png)

- Urls.py (Happy Leaf):
![Asgi py check](read.me_pics/testing_pics/happyleaf-urlpy-check.png)

- Wsgi.py:
![Wsgi py check](read.me_pics/testing_pics/wsgipy-check.png)

# Lighthouse report

- Index.html:
![Index light check](read.me_pics/testing_pics/index-lighthouse.png)

- About.html:
![About light check](read.me_pics/testing_pics/about-lighthouse.png)

- Blog.html:
![Blog light check](read.me_pics/testing_pics/blogpage-lighthouse.png)

- Contact.html:
![Contact light check](read.me_pics/testing_pics/contact-lighthouse.png)

- Log-in, Log-out, Sign-up:
![Log-in light check](read.me_pics/testing_pics/login-lighthouse.png)
![Log-out light check](read.me_pics/testing_pics/log-out-lighthouse.png)
![Sign-up light check](read.me_pics/testing_pics/signup-lighthouse.png)

- Delete and edit comment pages:
![Comment delete light check](read.me_pics/testing_pics/deletecomment-lighthouse.png)
![Comment edit light check](read.me_pics/testing_pics/editcomment-lighthouse.png)

- Post_detail.html:
![Post detail light check](read.me_pics/testing_pics/post-detail-lighthouse.png)

# Responsiveness

The website is fully responsive across various screen sizes including desktops, tablets, and phones. Several modifications have been implemented to enhance user experience. Examples include the addition of a hamburger menu for the navigation bar, removal of one section in the footer, elimination of subtitles in the carousel for smaller screens, and exclusion of pictures in the post detail section.

# Colour contrast

The website was tested for colour contrasts with [WAVE](https://wave.webaim.org) to improve accessibility, no low contrast areas were found. 