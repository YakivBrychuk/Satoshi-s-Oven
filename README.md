# Satoshi's Oven 👨🏻‍🍳 🍕 ₿

Satoshi's Oven combines classic pizza making with cryptocurrency payments for a modern ordering experience. Users can start new orders, customizing their pizza with various toppings and sizes, or check existing orders. 

The intuitive platform leads through selection, payment, and order review, offering a 'finish' option to process orders. 

On completion, a warm message confirms the order and invites customers to the collection point, ensuring a user-friendly journey from start to delicious finish.

![Home Screen](/readme_images/main_welcome.png)

[Satoshi's Oven](https://satoshisoven-553cf9e9f5ec.herokuapp.com/)
- - -

## Table of Contents
### [How to Order](#how-to-order)
### [Logic Flowchart](#logic-flowchart-1)
### [User Experience (UX)](#user-experience-ux-1)
### [Features](#features-1)
### [Features Left to Implement](#features-left-to-implement-1)
### [Design](#design-1)
### [Technologies Used](#technologies-used-1)
### [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used-1)
### [Testing](#testing-1)
### [Manual Testing](#manual-testing-1)
### [Input validation testing](#input-validation-testing-1)
### [Fixed Bugs](#fixed-bugs-1)
### [Deployment](#deployment-1)
* [Deployment to Heroku](#deployment-to-heroku)
* [Forking the GitHub Repository](#forking-the-github-repository)
* [Local Clone](#local-clone)
### [Credits](#credits-1)
* [Code](#code)
* [Content](#content)
### [Acknowledgements](#acknowledgements-1)
---

## How to Order

At Satoshi's Oven, select your pizza adventure with a choice of toppings, sizes, and payment methods, including cryptocurrency. 

Simply start a new order, customize your pizza, and finalize with 'finish'. Check existing orders anytime. 

---
For the scope of this project, each order is limited to one pizza to maintain simplicity in the project's logic.

## Logic flowchart

![Flowchart](/readme_images/logic_flow_chart.png)

## User Experience (UX)

Satoshi's Oven is an engaging pizza ordering experience that blends the art of pizza customization with the thrill of using modern payment methods, including cryptocurrency. Users embark on a culinary journey by selecting from an array of fresh toppings and sizes to craft their perfect pizza. The process is straightforward: choose your ingredients, confirm your order, and select a payment method. With each step, the anticipation builds until the order is placed. It's not just about ordering pizza; it's about creating an experience that's as unique as the user. Satoshi's Oven offers a delightful balance of creativity, convenience, and innovation, making it more than just a meal—it's an adventure in modern dining. Plus, it's an excellent way to explore the fusion of traditional cuisine with digital age advancements.


### User Stories

* First-time visitor goals:
    * Grasp the ordering process. Clear guidance on how to customize and order a pizza, including an understanding of the unique option to pay with cryptocurrency.
    * Place an order. After getting acquainted with how it works, the user is likely to proceed with crafting and ordering their personalized pizza.
    Enjoy the overall experience. Satoshi's Oven aims to provide an engaging and innovative pizza ordering journey.

* Returning visitor goals:
    * Reorder their favorites. A returning visitor might want to relive the delightful experience by ordering their favorite pizza again.
    * Share with friends. Encourage friends to try out the unique experience of ordering from Satoshi's Oven.
    * Check out new toppings or payment options, exploring any updates to the menu or payment methods.

* Frequent user goals:
    * Perfect their pizza customization, finding the right balance of toppings for the ultimate pizza.
    * Experiment with different sizes and additional options to enhance their meal.
    * Recommend Satoshi's Oven to others, sharing their positive experiences.
    * Stay updated on and try new features, toppings, or special promotions offered.

---

## Features

* Pizza Customization. Users can create their unique pizza by selecting from a variety of fresh toppings.
* Payment Options. Satoshi's Oven accepts traditional and modern payment methods, including cryptocurrency.
* User-friendly Interface. An intuitive design makes it easy for users to navigate and place their orders.
* Order Confirmation. Customers receive a detailed summary of their order for review before finalizing.
* Order Tracking. Users can check the status of their existing orders in real time.
* Feedback Loop. After completing an order, customers are encouraged to share their experience and suggestions.
* Repeat Orders. The platform allows for quick reordering of favorite pizzas with a simple click.

## Features Left to Implement

* Edit current order
* Have multiple pizzas in the same order
* Loyalty Rewards
* Custom Pizza Profiles


## Design

* Flowchart
    * [lucid.app](https://lucid.app/)


---


## Technologies Used

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

---

## Frameworks, Libraries & Programs Used

* [VS Code](https://code.visualstudio.com/)
    * To write the code.
* [Git](https://git-scm.com/)
    * for version control.
* [Github](https://github.com/)
    * Deployment of the website and storing the files online.
* [lucid.app](https://lucid.app/)
    * To create a logic flowchart of the Satoshi's Oven.
* [Heroku](https://www.heroku.com/)
    * To deploy the project.
* [CI Python Linter](https://pep8ci.herokuapp.com/)
    * Check code for any issues.


## Testing 

CI Python Linter was used to test run.py

<details>
<summary> run.py CI Python Linter check
</summary>

![run.py linter check](/readme_images/lintercheck.png)
</details>

## Manual Testing

The prtogram was manually tested extensively using VS code terminal, and when deployed on Heroku it was manually tested again.

| Feature | Expected Result | Steps Taken | Actual Result | Screenshot |
|---------------------------|-------------------------------------------------------------------|----------------------------------------------|---------------|--------------------------------------|
| Welcome Screen            | Display welcome message | Open application                             | As Expected   | ![Welcome Screen](/readme_images/welcome_stage1.png) |
| Menu Options              | Display menu options (New Order, Check Status)                  | Select 1 or 2                        | As Expected   | ![Menu Options](/readme_images/welcome_stage1.png) |
| Start new order           | Show List of available locations for collection   | Input "1" from menu options | As Expected   | ![Start New Order](/readme_images/welcome_option1.png) |
| Input invalid entry in menu of options | Display a message: Invalid input, try again |  Input invalid option                        | As Expected   | ![Choose Pizza](/readme_images/welcone_invalid_option.png) |
| Check the status of existing order          | Display message to input order number           | Input 2 into options menu                    | As Expected   | ![Customize Pizza](/readme_images/test_option2_first_menu.png) |
| Display Order             | Display the order details                                         | Input Order number         | As Expected   | ![Select Payment Method](/readme_images/display_order_option2.png) |
| Input Invalid Order Number| Display: You don't have access to this order or it doesn't exist. | Input random number                         | As Expected   | ![Order Summary](/readme_images/message_invalid_order_nr.png) |
| Selecting Address Option        | Display Address Selected and procede to Pizza Menu          | Input number of address 1 or 2 | As Expected   | ![Final Confirmation](/readme_images/address_selection.png) |
| Invalid Input Address Option | Display invalid entry                            | Input invalid entry           | As Expected   | ![Order Status](/readme_images/invalid_address.png) |
| Display Size menu & make choice| Confirm Size Selection & procede to cheese selection menu                      | Input code number of selected size            | As Expected   | ![Repeat Order](/readme_images/piza_code_selection.png) |
| Input Invalid code selection for size option   | Confirm Invalid Selection & ask to try again | Input Invalid code number for size selection            | As Expected   | ![Repeat Order](/readme_images/invalid_size.png) |
| Input cheese code selection   | Confirm cheese Selection & procede to Payment Method Selection | Input code number of selected cheese            | As Expected   | ![Repeat Order](/readme_images/cheese_selection.png) |
| Display Toppings menu  | Display Selection menu of Toppings | none(its loaded automatically after selecting cheese option)           | As Expected   | ![Repeat Order](/readme_images/toppings_menu.png) |
| Select indefinite nr of toppings until user inputs 'done'  | Display Selection , after typing 'done' procede to Payment Methods selection Menu | Input code number of toppings & 'done'          | As Expected   | ![Repeat Order](/readme_images/select_toppings.png) |
| Display Payment method menu  | Display Selection Payment method menu  | none(its loaded automatically after toppings menu)           | As Expected   | ![Repeat Order](/readme_images/payment_method.png) |
| Display Selected Payment ,Display Order Sumary and finish option  | Display Selected Payment ,Display Order Sumary and finish option | Input Letter C or F       | As Expected   | ![Repeat Order](/readme_images/final_display.png) |
| Display final order summary & goodbye message  | Display final order summary & goodbye message | Input finish     | As Expected   | ![Repeat Order](/readme_images/final_message.png) |

## Fixed Bugs
* Heroku Deployment Error due to pywin32 Dependency

   * Issue: The application failed to deploy on Heroku because pywin32, a package designed for Windows, was listed in requirements.txt, causing a build failure on Heroku's Linux-based environment.
   * Solution: The recommendation was to remove pywin32 from requirements.txt or conditionally include it for Windows environments only, using environment markers in requirements.txt.

* Incorrect IPython Version for Python Runtime

   * Issue: A specific version of IPython required for the project was incompatible with the Python version defined in runtime.txt, leading to deployment issues.
   * Solution: Two potential solutions were proposed: updating the runtime.txt to specify a compatible Python version or adjusting the requirements.txt to use a version of IPython compatible with the current Python runtime.

## Deployment

### Deploying to Heroku

To deploy with Heroku, Code Institute Python Essentials Template was used so the python code can be viewed in a terminal in a browser
1. Log in to Heroku or create a new account
2. On the main page click "New" and select "Create new app"
3. Choose your unique app name and select your region
4. Click "Create app"
5. On the next page find "settings" and locate "Config Vars"
6. Click "Reveal Config Vars" and add "PORT" key and value "8000", click "Add"
7. Scroll down, locate "Buildpack" and click "Add", select "Python"
8. Repeat step 7. only this time add "Node.js", make sure "Python" is first
9. Scroll to the top and select "Deploy" tab
10. Select GitHub as deployment method and search for your repository and link them together
11. Scroll down and select either "Enable Automatic Deploys" or "Manual Deploy"
12. Deployed site [Satoshi-s-Oven](https://satoshisoven-553cf9e9f5ec.herokuapp.com/)

### Forking the GitHub Repository

By forking the repository, we make a copy of the original repository on our GitHub account to view and change without affecting the original repository by using these steps:

1. Log in to GitHub and locate [GitHub Repository Satoshi-s-Oven](https://github.com/YakivBrychuk/Satoshi-s-Oven/tree/main)
2. At the top of the Repository(under the main navigation) locate "Fork" button.
3. Now you should have a copy of the original repository in your GitHub account.

### Local Clone

1. Log in to GitHub and locate [GitHub Repository Satoshi-s-Oven](https://github.com/YakivBrychuk/Satoshi-s-Oven/tree/main)
2. Under the repository name click "Clone or download"
3. Click on the code button, select clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone` and then paste The URL copied in the step 3.
7. Press Enter and your local clone will be created.

## Credits

### Code

* I gained understanding of python through code institute lessons.
* I gained more python concepts through 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu.
* MDN web docs for python [Documentation](https://developer.mozilla.org/en-US/docs/Glossary/Python).

## Acknowledgements

 * My mentor [Mitko Bachvarov](https://www.linkedin.com/in/mitko-bachvarov-40b50776/) who provided helpful feedback.
 * Slack community for encouragement.

