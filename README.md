# tldr
TL;DR: Cut Lines, Cut Time. 

Winner of Calhacks 2022 (Usage of Microsoft Cloud). 

See our [devpost](https://devpost.com/software/tldr-658ih1)!

![medium](https://user-images.githubusercontent.com/68176295/196329132-20d583a9-7218-40ad-8eaa-ad8b5a2e9254.png)
![small](https://user-images.githubusercontent.com/68176295/196329080-e3336469-3294-4c8f-b4c6-19a1e3ede675.png)

## Inspiration

TL;DR: Cut Lines, Cut Time.

With the overflowing amount of information and the limited time that we have, it is important to efficiently distribute the time and get the most out of it. 
With people scrolling short videos endlessly on the most popular apps such as Tiktok, Instagram, and Youtube, we thought, why not provide a similar service but for texts that can not only be fun but also productive?
As a group of college students occupied with not only school but also hobbies and goals, we envisioned an app that can summarize any kind of long text effectively so that while we can get the essence of the text, we can also spend more time on other important things.
Without having to ask someone to provide a TL;DR for us, we wanted to generate it ourselves in a matter of few seconds, which will help us get the big picture of the text. 
TL;DR is applicable anywhere, from social media such as Reddit and Messenger to Wikipedia and academic journals, that are able to pick out the most essentials in just one click. 

Ever on a crunch for time to read a 10-page research paper?
Want to stay updated on the news but are too lazy to actually read the whole article? 
Got sent a box of texts from a friend and just want to know the gist of it. 

TL;DR: this is the app for you!

## What it does
TL;DR helps summarize passages and articles into more short forms of writing, making it easier (and faster) to read on the go. 

## How we built it
We started by prototyping the project on Figma and discussing our vision for TL;DR. From there, we separated our unique roles within the team into NLP, frontend, and backend. We utilized a plethora of services provided by the sponsors for CalHacks, using Azure to host much of our API and CockRoachDB Serverless to seamlessly integrate persistent data on the cloud. We also utilized Vercel’s Edge network to allow our application to quickly be visited by all people across the globe.

## Web/Extension
The minimalistic user interface portraying our goal of simplification provides a web interface and a handy extension accessible by a simple right click. Simply select the text, and it will instantly be shortened and stored for future use!

## Backend and connections
The backend was built with Flask via Python and hosted on Microsoft Azure as an App Service. GitHub Actions were also used in this process to deploy our code from GitHub itself to Microsoft Azure. Cockroach Lab’s DB to store our user data (email, phone number, and password) and cached summaries of past TL;DR. Twilio is also used for user authentication as well as exporting a TL;DR from your laptop to your phone.

We utilized Co:here’s APIs extensively, making use of the text summarization and sentiment classifier endpoints. Leveraging Beautiful Soup’s capability to extract information, these pair together to generate the output needed by our app. In addition, we went above and beyond to better the NLP landscape by allowing our users to make modifications to Co:here’s generations, which we can send to Co:here. Through this, we are empowering a community of users that help support the development of accessible ML and get their work done as well - win/win!

## Challenges we ran into
Every successful project comes with its own challenges, and we sure had to overcome some bugs and obstacles along the way! First, we took our time settling on the perfect idea, as we all wanted to create something that really impacts the lives of fellow students and the general population. Although our project is “quick”, we were slow to make sure that everything was thoroughly thought through.
In addition, we spent some time debugging our database connection, where a combination of user error and inexperience stumped our progress. However, with a bit of digging around and pair programming, we managed to solve all these problems and learned so much along the way! 

## Accomplishments that we're proud of
The integration of different APIs into one platform was a major accomplishment since the numerous code bases that were brought into play and exchanged data had to be done carefully. It did take a while but felt amazing when it all worked out.

## What we learned
From this experience, we learned a lot about using new technologies, especially the APIs and servers provided by the sponsors, which helped us be creative in how we implement them in each part of our backend and analysis. We have also learned the power of collaboration and creating a better product through team synergy and combining our creativity and knowledge together.

## What's next for TL;DR
We have so much in store for TL;DR! Specifically, we were looking to support generating TL;DR for youtube videos (using the captions API or GCP’s speech-to-text service). In addition, we are always striving for the best user experience possible and will find new ways to make the app more enjoyable. This includes allowing users to make more editions and moving to more platforms! 
