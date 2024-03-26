# TriggerStocks

TriggerStocks is a web application designed to simplify the process of staying informed about significant events affecting the stock market. Tailored for users who are passionate about investing and staying updated on market dynamics, this platform streamlines the task of monitoring stock triggers while saving valuable time and effort.

The live link can be found here - [TriggerStocks](https://stocktriggers-dffa3b7c370b.herokuapp.com/)

picture


## Site Owner Goals

- To provide users with the best stock trigger tips and to easily navigate through them.
- To provide users with easy access to additional information and to facilitate seamless access to trading sites.
- To offer users a comment section where they can share their thoughts about the triggers.
- User-friendly design to provide users with an easy way to follow the triggers conveniently.

## User Stories

- ### First-time User
  - As a first-time user, I want to understand the main purpose of the site and learn about the benefits of staying informed about stock triggers.
  - As a first-time user, I want to navigate the website intuitively, ensuring a positive and enjoyable experience.
  - As a first-time user, I want to be able to browse stock triggers without having to sign up or register.

- ### Returning User
  - As a returning user, I want to effortlessly navigate to the latest stock triggers, ensuring I stay updated on market events.
  - As a returning user, I want to find comprehensive information about each trigger, including company details and related press releases, to make informed decisions.
  - As a returning user, I want to easily access the comment section to share my thoughts and insights about specific triggers.

- ### Frequent User
  - As a frequent user, I want to quickly bookmark my favorite triggers for easy access later, ensuring I can track them effectively.
  - As a frequent user, I want to explore additional resources such as educational content and trading platform links, enhancing my understanding and trading experience.
  - As a frequent user, I want to receive personalized notifications about important trigger updates, ensuring I never miss critical market events.


## Design

### Video
The captivating video at the top of the Stock Trigger website features a bustling cityscape with skyscrapers and a majestic bridge. This dynamic imagery sets the tone for the site, evoking energy and excitement while mirroring the fast-paced nature of the stock market.

### Image
In the "Suggest" section, users encounter an impactful image of a bull, symbolizing strength and bullish market sentiment. This visual reinforces the website's focus on identifying opportunities for success in the stock market.

### Colors
The color palette of the Stock Trigger site is carefully chosen to evoke a sense of professionalism, trustworthiness, and clarity. Utilizing a combination of deep blues, sleek grays, and vibrant accents, the site's colors exude a sense of reliability and sophistication. The primary color scheme consists of shades of navy blue and charcoal gray, complemented by pops of vibrant yellow to draw attention to key elements and calls to action.

### Fonts
The Stock Trigger website uses **Quicksand** as its primary font, lending a modern and professional feel to the content. **Raleway** is reserved for headers and larger text, adding emphasis and style to key sections. These fonts work together to create a visually appealing and easily readable experience for users, enhancing the overall design and usability of the site. This font was imported via [Google Fonts](https://fonts.google.com/)

### Wireframes

![ADD HERE]()
![ADD HERE]()

## Agile Methodology

Github projects was used to manage the development process using an agile approach. Please see link to project board [here](add link here)

## Data Model

Add text and pictures here from the other pc

### User Authentication

- Django's LoginRequiredMixin is used to make sure that any requests to access secure pages by non-authenticated users are redirected to the login page. 

### Form Validation
If incorrect or empty data is added to a form, the form won't submit and a warning will appear to the user informing them what field raised the error. 

### Database Security
The database url and secret key are stored in the env.py file to prevent unwanted connections to the database and this was set up before the first push to Github.

Cross-Site Request Forgery (CSRF) tokens were used on all forms throughout this site.

## Features

### Header

![header](ADD pic)


**Logo**
- It features a white logo elegantly crafted with the Raleway font.
- This logo is positioned in the top left of the navigation bar. The logo is linked to the home page for ease of navigation for the user.

**Navigation Bar**

- The navigation bar is present at the top of every page and includes all links to the various other pages.
- "When users log in, they'll see the 'Favorites' link and the 'Suggest' button."
- The options to Sign up or Log in will change to the option to log out once a user has logged in.
- The navigation bar is fully responsive, collapsing into a hamburger menu when the screen size becomes too small.
- Hovering over the links will make the links yellow.
- The navbar is sticky so it will be on the top of the page when you scroll.

![header](Add pic)

### Footer 

![header](Add pic)

- The footer section includes links to Facebook, Instagram and X. It also includes a 'contact us' and a short explination about the site
- Clicking the links in the footer opens a separate browser tab to avoid pulling the user away from the site.


