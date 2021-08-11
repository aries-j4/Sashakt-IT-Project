from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt, client, sms
from flaskblog.forms import RegistrationForm, LoginForm, ContactForm, PostForm, SendSMS
from flaskblog.models import User, Contacts, Post
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template("login.html", form=form)

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    contacts = Contacts.query.all()
    posts = Post.query.all()
    return render_template('account.html',contacts=contacts, posts=posts)

@app.route("/contacts", methods=['GET', 'POST'])
@login_required
def contacts():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contacts(name=form.name.data, phone=form.phone.data, relation=form.relation.data, client=current_user)
        db.session.add(contact)
        db.session.commit()
        flash('Your contact has been successfully added!', 'success')
        return redirect(url_for('account'))
    return render_template('contacts.html', form=form)    

@app.route("/send_sos")
@login_required
def send_sos():
    flash('Your emergency sos has been successfully sent to your contact!', 'success')
    return redirect(url_for('account'))

@app.route('/blogs/')
def blogs():
    return render_template("blogs.html")

@app.route("/stories")
def stories():
    posts = Post.query.all()
    return render_template('stories.html', posts=posts)

@app.route("/create_post", methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('stories'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')

@app.route("/send_sms", methods=['GET', 'POST'])
def send_sms():
    form = SendSMS()
    if form.validate_on_submit():
        sms1 = SendSMS(name=form.name.data, number=form.number.data, address=form.address.data, complaint=form.complaint.data )
        message = "Name: " + request.form['name'] + " Mobile: " + request.form['number'] + " living in " + request.form['address'] + " has a complaint saying: " + request.form['complaint']
        #sms_text = "Name: "+str(form.name)+" Mobile: " + str(form.number) + " living in " + str(form.address) + " has a complaint saying: " + str(form.complaint)
        print(message)
        responseData = sms.send_message(
        {
            "from": "Vonage APIs",
            "to": "917042685209",
            "text": message,
        }
        )
        if responseData["messages"][0]["status"] == "0":
            flash('Your sms has been sent!', 'success')
            return redirect(url_for('send_sms_successful'))
        else:
            flash(f"Message failed with error: {responseData['messages'][0]['error-text']}")
    return render_template('send_sms.html', form=form)

@app.route('/send_sms_successful/')
def send_sms_successful():
    return render_template('send_sms_successful.html')


@app.route('/tweet_analysis')
def tweet_analysis():
    return render_template('tweet_analysis.html')