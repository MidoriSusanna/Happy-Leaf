# Happy Leaf
Happy Leaf is a website dedicated to providing a platform for individuals interested in embracing an eco-friendly lifestyle. It serves as a judgment-free zone where people can freely explore and share insights on sustainable living.

The focus of Happy Leaf is on positive change, personal growth, and collective commitment to building a healthier and happier world in harmony with nature. The website is meant to encourage individuals on the journey towards a greener, more eco-conscious life.

The website targets people interested in learning more about an eco-friendly lifestyle, catering to both those just approaching it and individuals already immersed in it. The focus is also on Ireland, aiming to keep the people of this country informed about initiatives. However, many articles can be a valuable source for everyone. The blog section features three main types of articles: eco-tips, vegan recipes, and information on sustainable practices in Ireland.

The name of the website, Happy Leaf, was chosen to evoke the concept of happiness and harmonious nature. The Japanese kanji for 'leaf' serves as the logo, reflecting the tradition of nature poetry and the ancient production of the Japanese.


# Project Goals and Stories
## Project Goals
- As a user I want to:
  - easily and intuitively navigate the website.
  - browse the website to be able to find the information I am looking for.
  - be able to find information through different devices.
  - be able to interact with the interface and receive feedback.
  - be able to recognise a brand to come back to visit the website again.
  - create an account on the website and join the community.
  - search for blog posts and information I need.
  - get in touch with the admin of the page.


## Epics and User Stories
[Full list of User Stories available here](https://github.com/MidoriSusanna/Happy-Leaf/issues?q=is%3Aissue+is%3Aopen>)

[Full list of Epics available here](https://github.com/MidoriSusanna/Happy-Leaf/milestones)


# Agile Development
I utilized GitHub Issues and Projects for writing and managing user stories and epics. The Kanban board was employed to categorize stories into Todo, In Progress, and Done columns. Additionally, I applied the MoSCoW method to label stories as Must-Have, Could-Have and Should-Have.

[Kanban Board](https://github.com/users/MidoriSusanna/projects/1)


# Design an User Experience
Happy Leaf is a website designed with sustainability in mind. The layout is crafted to be easy on the eyes and welcoming, providing users with a sense of being invited and facilitating a smooth start to their journey. The chosen colors are reminiscent of nature, particularly autumn shades. The font is simple yet playful at times, striking a balance to effectively convey a serious message.


**Fonts:**

- Comfortaa for main titles.
- PT Sans for paragraphs.

**Colour Palette:**

![Colour palette](read.me_pics/palette.jpg)
White was also added, to emphasize and keep some parts and pages of the website clearer. 

**Customize background:**

![Customised background](read.me_pics/background-about-section.jpg)

A customise background with leaves has been made to provide even more the sense of balance and harmony in the layout. This bacjground appears in the index.html page and as a constant in all the pages related to authentication.


## Wireframes

Wirefranes were created by me using Adobe Illustrator for both Dekstop and Phone:

[Wireframes for dekstop and phone](WIREFRAME.md)

# Features 

The website consists of a blog with essentially four main pages and several secondary ones. Users can easily navigate through the navigation bar and clickable links on the homepage (such as the logo, carousel, about us section, preview section, and footer). The homepage offers an initial idea of the main contents and serves as a gateway to all other pages. The website clearly communicates its purpose through text and visual content. Authentication functions are available, allowing users to become part of the community and contribute by signing up to the site and/or contacting the admins.

## Homepage

### Navigation bar

Featured on all three pages, the navigation bar includes the logo, 'About Us' page, personal area dropdown, and 'Contact Us' page, and is identical on each page to allow easy navigation. The navigation bar changes appearance when the user is authenticated. In this case, it shows a welcome message, and the dropdown changes from 'Login' and 'Sign Up' options to a 'Log Out' option. On smaller screens, the nav bar becomes a hamburger icon but retains the dropdown menu. Hovering over the buttons provides a clear indication of interactivity through underlining. Additionally, the logo is clickable and returns the user to the homepage.

- Non authenticated user:
![Navigation bar non authenticated](read.me_pics/features/navbar-notauth.png)

- Authenticated user:
![Navigation bar authenticated](read.me_pics/features/navbar-yesauth.png)

- Smaller screens: 
![Nav bar on smaller screens](read.me_pics/features/navbar-smallscreen.png)

### Carousel

A carousel is displayed right below the navigation bar on the homepage. The pictures slide automatically and represent natural elements. The slideshow is clickable and redirects to the blog page. On smaller screens, the subtitles are not visible.
![Carousel picture with robin](read.me_pics/features/index-slideshow.png)

### Homepage - About us section

The 'About Us' section provides both visual and written insight into the scope and primary goals of the website. It includes a button that links to the dedicated 'About Us' page, where the topic is further expanded.
![About us section in homepage](read.me_pics/features/index-aboutus.png)

### Homepage - Preview section

The preview section is divided into three parts, each linking to different pages:

- Blog page
- Sign-up page (If the user is authenticated, the message on the button changes, and this link also directs to the blog page)
- Contact page

It serves as another reminder to explore the blog posts and join the community.
![Preview section in homepage](read.me_pics/features/index-preview.png)

### Footer

The footer also includes links to all pages and contains a brief explanation of the website's purpose, along with the logo. It summarizes the main possible actions users can take on the website and lists the pages they can visit, along with social media icons. When the user is authenticated, the 'join' link disappears to avoid excessive repetition throughout the website.

![Footer](read.me_pics/features/footer-notauth.png)

## About us page

The 'About Us' page comprises two main sections, delving deeper into the explanation of the blog's mission. These sections are titled 'More about Happy Leaf' and 'Meet the Team'. Consistent with the website's nature-oriented style, administrators are depicted as avatars. These avatars were created by me using Canva.

![More about Happy Leaf section](read.me_pics/features/about-page.png)
![Meet the team section](read.me_pics/features/about-meet-team.png)

## Blog page

The blog page aims to be tidy and clear. At the top of the page, there is a search bar that allows users to quickly find a topic, title, or category. The articles are paginated with six per page. At the bottom, there are 'Next' and 'Previous' buttons to navigate to more articles. Clicking on an article card allows users to read the entire article, even if they are not authenticated. In the bio posts, the following information is displayed: author, date and time of publishing, number of likes, and category.

![Blog page](read.me_pics/features/blog-page.png)
![Blog pagination](read.me_pics/features/blog-pagination.png)

## Post detail page

Clicking on the titles of blog posts on the blog page allows users to view the content of each post. The picture appears on the right, while the title and further information are displayed on the left. The content of the post appears below. At the end of the page, authenticated users can see the comment form and the submit button to leave a comment on the blog post. If the user is not authenticated, they will be able to see the comments and number of likes but will not be able to leave a comment.

![Post detail page](read.me_pics/features/post-detail-page.png)
![Post detail bottom page](read.me_pics/features/post-detail-page-2.png)

## Contact page

The contact page is designed as a lovely and welcoming section with a rainbow background. Its purpose is to create a positive atmosphere for the contact form, encouraging users to get in touch. All fields in the form are required, and users must also tick a privacy box before submitting. The subject of the inquiry is presented through a dropdown menu. The contact form was implemented using emailJs. After submission, a thank you message is displayed.

![Contact page](read.me_pics/features/contact-us-form.png)
![Thank you message](read.me_pics/features/enquiry-sent-form.png)

## Authentication pages

The login, sign up, and logout pages have a similar layout to promote consistency and reinforce the design/branding. Each form displays messages upon submission.

![Sign up page](read.me_pics/features/sign-up-page.png)
![Log in page](read.me_pics/features/login-page.png)
![Log out page](read.me_pics/features/sign-out-page.png)

## Delete and Edit comment pages

The delete and edit pages are designed for users to update or remove comments they have posted. These pages serve as a precautionary step before finalizing changes or deletions. Users can only perform these actions when authenticated and for their own comments. Upon deletion or editing of comments, confirmation messages are displayed.

![Delete comment page](read.me_pics/features/delete-comment-page.png)
![Edit comment page](read.me_pics/features/edit-comment-page.png)

## Messages

Messages are implemented using the message function of Django. Additionally, a JavaScript script is utilized to automatically remove these messages after a few seconds. Users can view these messages immediately after completing an action or submitting a form.

1. Message that appears after the user submits a comment:
![Submitted successfully](read.me_pics/features/comment-succ-approv.png)

2. Message that appears when a user deletes a comment permanently:
![Deleted comment](read.me_pics/features/delete-succ-mess.png)

3. Message that appears when a user edits a comment:
![Edit comment](read.me_pics/features/edited-succ-mess.png)

4. Message that appears when the user signs in:
![User signed in](read.me_pics/features/sign-in-mess.png)

5. Message that appears when the user logs out:
![User log out](read.me_pics/features/sign-out-mess.png)

6. Messages that appear when the user tries to leave an empty or blank comment:
![Empty comment messagge](read.me_pics/features/empty-comment-mess.png)
![Blank comment message](read.me_pics/features/blank-comment-mess.png)

7. The contact form also has some validatin messages: an alert for the privacy checkbox and the thank you message after submission. 

## Admin Panel

Through the admin panel, administrators can manage posts, create drafts and blogs, approve comments, remove comments, and customize the layout of posts.

![Admin panel](read.me_pics/features/admin-panel.png)

The page for creating drafts/posts is built using Summernote, a text editor that offers a "What You See Is What You Get" view of article creation. This simplifies content creation and editing processes. Users can easily add images, and the slug is automatically generated when the title is typed. Additionally, posts can be categorized and saved as either published or drafts
![Create blog](read.me_pics/features/post1-panel.png)

The admin has the authority to approve or not user comments via the comment section within the admin panel.
![Approve comments admin](read.me_pics/features/comment-approve-panel.png)

# Features left to implement

The original idea envisions this website not only as a blog but also as a personal diary to record our own eco-friendly journey. Here are some potential features to implement:
- As a user I can create my profile with a picture and some basic information so that I can create an identity for the blog community and identify other users too. 
- As a user I can see other user's basic profiles and be able to identify them when they comment so that I can have a better idea of the community and recognise people I interact with. 
- As an authenticated user I can create a diary page (which I can only see) so that I can take notes about my eco-friendly journey. 
- As an authenticated user I can check the older 
pages of my diary so that I can keep track of the progresses of my eco-friendly journey. 
- As an authenticated admin I can like comments of other users so that I can express my agreement or disagreement with what another user has written. 

# Database Chart

![Database chart](read.me_pics/database_pic/database-charts.png)

**Relationships**
- **Post-Author:** A many-to-one relationship from Post to Django's built-in User model (author field). Each post is written by one user, and a user can write many posts.
-	**Post-Likes** A many-to-many relationship between Post and User (likes field), allowing many users to like many posts.
- **Post-Category** A many-to-one relationship from Post to Category (category field). Each post belongs to one category, and a category can contain many posts.
- **Comment-Post** A many-to-one relationship from Comment to Post (post field). Each comment is associated with one post, and a post can have many comments.

# Testing

Manual Testing and validation can be found here:

[TESTING](TESTING.md)

# Bugs

- When I changed my model.py file to introduce the category model, I needed to reset my database and migrate the changes again ('python manage.py makemigrations')in order to reset the relationships between models.
- I have encountered several deployment issues, mostly related to the versions of the package dependencies installed in the requirements.txt document.
- I encountered an issue setting up the contact form of the website. I wanted to introduce a dropdown menu to show the topic of the inquiry in the email template. At first, the template was not showing titles but numbers (values added to the option tag). I fixed this by working on the variable inquiryType.
- I set up the site using Bootstrap tags for responsiveness, but in many cases, I had to customize the CSS with media queries to provide a better user experience.
- I was not sure about how to render the HTML templates which do not contain Python/Django functionalities in the deployed site, according to the MVC system. In the end, I simply rendered them as a request with return render.
- I mainly used class-based views to simplify the code and be able to reuse them, refactoring my code sometimes.
- The blog search view was initially only handling title search, but I thought that wouldn’t be good for a sectorial search (according to the topic). I encountered some issues, but then I was able to include the category in the search. I used Q, which is a Django model utility that allows for complex database queries. It stands for "query" and is used to encapsulate a set of keyword arguments. I also used icontains to eliminate case sensitivity.
- While validating HTML, I identified an error due to the absence of the 'alt' attribute in images uploaded via the admin panel using Summernote. To resolve this issue, I utilized the 'title' attribute from the image object and set the 'alt' attribute dynamically using 'alt="{{ post.title }}"'.

# Tools and technologies used

## Languages and Frameworks

**Django** is utilized as the web framework, built on Python for server-side programming.

**Python** acts as the primary backend programming language.

**HTML** is used for both markup and template design.

**CSS** is applied for styling purposes, customised CSS has been added to Bootstrap tags. 

**Bootstrap** is selected as the CSS framework for responsive design.

**JavaScript** is mainly used to implement the contact form through the API emailJs. 

## Django Packages

Django installs a some packages by default and some packages were instead installed manually:

**cloudinary**: Provides an easy-to-use interface for integrating Cloudinary services, allowing for advanced media management.

**dj3-cloudinary-storage**: a Django storage backend for Cloudinary integration.

**dj-database-url**: simplifies database configuration by using a single environment variable.

**django-allauth**: offers comprehensive authentication features and templates, including social login, email verification, etc. to Django projects.

**django-crispy-forms**: enhances Django forms by allowing for easy customization of form layouts.

**django-summernote**: integrates the Summernote WYSIWYG editor with Django, enabling rich text editing capabilities in Django admin panel.

**gunicorn**: python WSGI HTTP Server for better deployment.

**psycopg2-binary**: PostgreSQL database adapter for Python, necessary for connecting the Django project to a PostgreSQL database.

## Others

**Font Awesome**: website used for icons.

**ElephantSQL**: it is the cloud-based PostgreSQL database management service that was used for this project.

**emailJS**: API used for handling the emails through the contact form. By using the EmailJS API, it is possible to integrate email functionalities into the application by making HTTP requests to the EmailJS servers. 

**VS Code**: used as a main coding environment. 

**Git**: used for version control.

**GitHub**: hosting site for the repository of the project.

**Heroku**: cloud-based platform where the website was deployed.

# Credits

- My project is inspired to the Walkthrough Code Institute project "I Think Therefore I blog".
- Bootstrap documentation has been used for different parts of the website, as for example the carousel in the index page.
- For the category model this has been very helpful: https://www.youtube.com/watch?v=_ph8GF84fX4
- The search bar has been implemented with the help of this tutorial:
https://www.youtube.com/watch?v=VL5ZNCjXEbw
- To change the colour of the nav bar toggler icon: https://stackoverflow.com/questions/42586729/how-can-i-change-the-bootstrap-4-navbar-button-icon-color
- Pictures were taken from Pexels.com and Unsplash.com
- Blog posts content was created with the help of ChatGPT
- The About section poem and text was taken from:
https://jti.lib.virginia.edu/japanese/kokinshu/Cook/CookKok.html
http://www.wakapoetry.net/poems/anthologies/kokinshu/
- Messages have been implemented with the help of the message framework Django documentation: https://docs.djangoproject.com/en/3.2/ref/contrib/messages/#using-messages-in-views-and-templates
- Wireframes were made by me using Adobe Illustrator
- The background was created by me using Adobe Illustrator
- "Meet the Team" avatars were created by me using Canva.
- Colour Palette was chosen with the help of: https://colorhunt.co
- For good HTML indentation: https://www.freeformatter.com/html-formatter.html
