### HTML

All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/). See results in below table.
| Page                 | Logged Out | Logged In |
|----------------------|------------|-----------|
| Trigger_detail.html  | No errors  | No errors |
| base.html            | No errors  | No errors |
| sharetriggers.html   | N/A        | No errors |
| index.html           | No errors  | No errors |
| favorites.html       | N/A        | No errors |
| login.html           | No errors  | N/A       |
| logout.html          | N/A        | No errors |
| signup.html          | No errors  | N/A       |

#### Fixed Errors 
Had a problem with dubble id. I had to move the id to a div. 

### CSS
No errors were found when passing my CSS file through the official [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

 <details>

 <summary>CSS</summary>

![CSS Validation](docs/readme_images/CSS.png)
 </details>

### Javascript
No errors were found when passing my javascript through [Jshint](https://jshint.com/) 

<details>

<summary>Jshint</summary>

![Jshint](docs/readme_images/jshint.png)
</details>

### Python
All Python files were run through [Pep8](https://pep8ci.herokuapp.com/#) with no errors found. 

### Site Navigation
| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| NavBar                |            |                                                                    |           |
| Site Name (logo area) | Click      | Redirect to home                                                   | Pass      |
| Home Link             | Click      | Redirect to home                                                   | Pass      |
| Triggerlist           | Click      | Scolls down to trigger section                                     | Pass      |
| Favourites            | Click      | Opens the favouites page                                           | Pass      |
| Favourites            | Display    | Only visible if user in session                                    | Pass      |
| Logout Link           | Click      | Open logout confirm page                                           | Pass      |
| Logout Link           | Display    | Only visible if user in session                                    | Pass      |
| Sharetrigger          | Click      | Opens the shretigger page                                          | Pass      |
| Sharetrigger          | Display    | Only visible if user in session                                    | Pass      |
| Sign Up Link          | Click      | Open Sign up page                                                  | Pass      |
| Sign Up Link          | Display    | Not visible if user in session                                     | Pass      |
| Log In Link           | Click      | Open Login page                                                    | Pass      |
| Log In Link           | Display    | Not visible if user in session                                     | Pass      |
| All Nav Links         | Hover      | Makes links yellow                                                 | Pass      |
|                       |            |                                                                    |           |
| Mobile View           |            |                                                                    |           |
| Hamburger Menu        | Responsive | Display when screen size reduces to medium size                    | Pass      |
| Site Name (logo area) | Click      | Redirect to home                                                   | Pass      |
| Home Link             | Click      | Redirect to home                                                   | Pass      |
| Triggerlist           | Click      | Scolls down to trigger section                                     | Pass      |
| Favourites            | Click      | Opens the favouites page                                           | Pass      |
| Favourites            | Display    | Only visible if user in session                                    | Pass      |
| Logout Link           | Click      | Open logout confirm page                                           | Pass      |
| Logout Link           | Display    | Only visible if user in session                                    | Pass      |
| Sharetrigger          | Click      | Opens the shretigger page                                          | Pass      |
| Sharetrigger          | Display    | Only visible if user in session                                    | Pass      |
| Sign Up Link          | Click      | Open Sign up page                                                  | Pass      |
| Sign Up Link          | Display    | Not visible if user in session                                     | Pass      |
| Log In Link           | Click      | Open Login page                                                    | Pass      |
| Log In Link           | Display    | Not visible if user in session                                     | Pass      |
|                       |            |                                                                    |           |
| Footer                |            |                                                                    |           |
| All links             | Click      | Open in new tab and to correct location                            | Pass      |

### Home Page
| Element               | Action  | Expected Result                 | Pass/Fail |
|-----------------------|---------|---------------------------------|-----------|
| Explore trigger Button| Click   | Scolls down to trigger section  | Pass      |

### Triggerlist
| Element              | Action            | Expected Result                                                                         | Pass/Fail |
|----------------------|-------------------|-----------------------------------------------------------------------------------------|-----------|
| Collapsible-header   | Click             | Infogrid opens up                                                                       | Pass      |
| Comment button       | Click             | Opens the trigger_detail.html page                                                      | Pass      |
| E-trading button     | Click             | Opens the webiste for E-Trade                                                           | Pass      |
| Robin Hood button    | Click             | Opens the webiste for Robin Hood                                                        | Pass      |
| To The Source button | Click             | Opens the webiste to the source                                                         | Pass      |
| To The Company button| Click             | Opens the webiste to the company                                                        | Pass      |

### Recipe Detail Page

| Element                        | Action              | ExpectedResult                                                  | Pass/Fail |
|--------------------------------|---------------------|-----------------------------------------------------------------|-----------|
