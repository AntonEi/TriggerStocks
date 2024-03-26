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

### Home Page

**Call to Action Section**

![header](add)

- The home page features a captivating video showcasing dynamic stock market scenes, setting the stage for an engaging exploration of TriggerStocks.
- Upon arrival, users are greeted with the bold message "TriggerStocks: Your key to smart investments" overlaid on the video background, emphasizing the site's mission to provide valuable investment insights.
- A compelling call-to-action encourages users to dive into the world of triggers by exploring the Trigger List, guiding them towards informed investment decisions.
- With a seamless experience, users are invited to embark on their investment journey with TriggerStocks, where smart investments are just a click away.


**What Is A Trigger**

![header](docs/readme_images/features/what_we_do.png)

- The "What is a trigger?" section offers a comprehensive explanation of the concept, breaking it down into four key components.
- Firstly, triggers involve the disclosure of information through official channels, such as company reports or press releases, providing insights into future events or outcomes.
- Each trigger is associated with a trigger date, indicating the timing of the event and its potential impact on the market.
- Identifying triggers presents investment opportunities, allowing investors to analyze companies and make informed decisions.
- Finally, investor actions in response to triggers influence stock prices, reflecting market sentiments and expectations.


**Our Purpose**

This section on the TriggerStocks website articulates our mission and goals. It's aimed at providing investors with insights and information to make informed decisions in the stock market. The objectives are:

- Seize the opportunity and invest in tomorrow's companies today: Identifying upcoming triggers to anticipate market movements.
- Sharing of Information: Guiding investors with valuable insights for successful investments.
- Remember: Emphasizing personal responsibility in decisions; TriggerStocks does not offer investment advice.

### User Account Pages

**Sign Up**

![header](docs/readme_images/features/signup.png)

**Log In**

![header](docs/readme_images/features/login.png)

**Log Out**

![header](docs/readme_images/features/logout.png)

- Django allauth was installed and used to create the Sign up, Log in and Log out functionality. 
- Success messages inform the user if they have logged in/ logged out successfully.


