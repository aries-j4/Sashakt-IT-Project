# Sashakt - Be Aware, Be Secure
Sashakt - Be Aware, Be Secure is a project aimed at providing assistance to people who need it through our various features. It includes providing assistance through filing-complaint(via sms), reading and composing blogs, resource pages ( self-defense, quiz pages) and twitter tweet analysis to make them fully aware and equipped in this present world of technology. 


### 📌 Table of Contents
* [Toolchain](#toolchain)
* [Features](#features)
* [Application Overview](#overview)
* [Future Scope](#scope)
* [Conclusion](#conclusion)
* [Resources](#resources)
* [Authors](#authors)


<a id="toolchain"></a>
## 💻 Toolchain

<img alt="HTML" src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"/><img alt="CSS" src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white"/><img alt="Javascript" src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/><img alt="Bootstrap" src="https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white"/><img alt="Flask" src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"/><img alt="Pandas" src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" /><img alt="Numpy" src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" /><img alt="Matplotlib" src="https://img.shields.io/badge/matplotlib-%23013243.svg?style=for-the-badge&logo=matplotlib&logoColor=white" /><img alt="SQLite" src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white" /><img alt="Visual Studio Code" src="https://img.shields.io/badge/VisualStudioCode-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"/><img alt="Git" src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"/>

***Frontend*** : HTML, CSS, JS, Bootstrap

***Backend*** : Flask, Jinja

***Dtabase*** : SQLite

***Libraries*** : Pandas, Numpy, Matplotlib, TextBlob

***API*** : Vonage API, Tweepy

***Other*** : Git - Version Control, Visual Studio Code


<a id="features"></a>
## 🚀 Features
1.	Read & Compose Blogs-: Anything can be found provided one looks at the right place. With this idea in mind, we designed the feature of writing small blogs where different people can tell how they managed to cope with their difficulties and stress for others to read and get inspired. 
2.	Send SMS Seeking Help-: This is basically a system where a user can send an sms to our team (after entering their credentials) and file a complaint without letting anyone know. This has been done using sms sending APIs of Vonage (using free credits).
3.	Twitter Tweet Analysis-: The user can enter any trending hashtag and the website offers an analysis in the form of wordcloud and pie charts. This involves the use of Machine Learning.
4.	Resource Pages-: We have added resource pages in our project that includes information/videos on self-defense and a small quiz on women safety. 


<a id="overview"></a>
## 📖 Application Overview
### Home Page
![Website Image](flaskblog/static/images/home.png?raw=true "Title")
### About Page 
![Website Image](flaskblog/static/images/about.png?raw=true "Title")
### Resources Page 
![Website Image](flaskblog/static/images/resources.png?raw=true "Title")
### Login Page
![Website Image](flaskblog/static/images/login.png?raw=true "Title")
### Profile Page 
![Website Image](flaskblog/static/images/account.png?raw=true "Title")
### Blogs Page 
![Website Image](flaskblog/static/images/blog.png?raw=true "Title")
### Read Top Posts
![Website Image](flaskblog/static/images/readtopblogs.png?raw=true "Title")
### SMS Complaint Filing Page
![Website Image](flaskblog/static/images/smssend.png?raw=true "Title")
### SMS Received on Phone
![Website Image](flaskblog/static/images/sms.jpeg?raw=true "Title")
### SMS Successfully Sent
![Website Image](flaskblog/static/images/smssuccess.png?raw=true "Title")
### Tweet Analysis Page
![Website Image](flaskblog/static/images/tweetanalysis.png?raw=true "Title")
### WordCloud
![Website Image](flaskblog/static/images/wordcloud.png?raw=true "Title")
### Tweet Analysis Result
![Website Image](flaskblog/static/images/resulttweet.png?raw=true "Title")


<a id="scope"></a>
## 🚧 Future Scope

Although the project greatly covers our targets, there are still further alterations that we would like to do to make the website even better.
- [ ] Adding the feature of having a profile-picture, bio, updating account and editing blogs.
- [ ] Adding blog recommendations based on likes and topics.
- [ ] Segregation of the SMS messages received based on complaint-category.
- [ ] Adding an emergency SOS feature to all the contacts entered by the user.
- [ ] Sentiment Analysis of text entered by users along with tweet analysis.


<a id="conclusion"></a>
## 💡 Conclusion
With the project Sashakt, we aimed to create a website that serves as an assistant and offers features of filing complaints, reading blogs and becoming aware of social media atrocities. 

Towards the end of the project, we were able to write working code for all the above mentioned features. The user can login or register, add contacts, write their own blogs, send sms to a number filing any complaint and see the analysis of twitter tweets by entering any trending hashtag. 

We were able to learn various aspects of coding through this project. We worked with python, flask, html, css, bootstrap, Javascript, sqlite, Machine Learning, APIs etc using Visual Studio Code, git and gitHub.


<a id="resources"></a>
## 📚 Resources
- https://flask-doc.readthedocs.io/en/latest/
- https://docs.python.org/3/
- https://devdocs.io/css/
- https://getbootstrap.com/docs/5.0/getting-started/introduction/
- https://developer.mozilla.org/en-US/docs/Web/JavaScript
- https://www.sqlite.org/docs.html
- https://developer.twitter.com/en
- https://developer.nexmo.com/
- https://www.chartjs.org/docs/latest/
- https://textblob.readthedocs.io/en/dev/
- https://git-scm.com/doc
- https://matplotlib.org/
- https://amueller.github.io/word_cloud/
- https://pandas.pydata.org/docs/
- https://docs.python.org/3/library/collections.html
- https://pip.pypa.io/en/stable/
- Apoorv Agarwal, Boyi Xie, Ilia Vovsha, Owen Rambow, Rebecca Passonneau, “Sentiment Analysis of Twitter Data”, Department of Computer Science, Columbia University, New York
- Akshi Kumar and Teeja Mary Sebastian “Sentiment Analysis on Twitter”, Department of Computer Engineering, Delhi Technical University, Delhi, India
- https://help.twitter.com/en/managing-your-account/accessing-your-twitter-data
- William McKinney: Python for Data Analysis, 2nd Edition


<a id="authors"></a>
## 💻 Authors

Samya Jain<br>
[@Linkedin](https://www.linkedin.com/in/samya-jain-a68443204)
<br>
[@Github](https://github.com/samya02)
<br>

Kashika Akhouri<br>
[@Linkedin](https://in.linkedin.com/in/kashika-akhouri-050b4a202)
<br>
[@Github](https://github.com/kashika0112)
<br>

Bhumika Joshi<br>
[@Linkedin](https://www.linkedin.com/in/joshi-bhumika/)
<br>
[@Github](https://github.com/aries-j4)
<br>




